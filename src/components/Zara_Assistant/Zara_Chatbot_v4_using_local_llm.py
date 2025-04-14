import pandas as pd
from dash import Dash, html, Input, Output, ctx, State, dcc, dash_table
import dash_mantine_components as dmc
from dash_iconify import DashIconify

from ...data.source import DataSource
from ...components import ids, cns
from ...components.Zara_Assistant import openai_api_key
from ..Zara_Assistant import prompt

import pandas as pd
import time
# import prompt

# from langchain_community.llms import OpenAI
# from langchain_experimental.agents import create_pandas_dataframe_agent
from openai import OpenAI

import plotly.express as px

import re

from io import StringIO
import io
import contextlib
import os

import requests

def call_custom_llm(question, df=None, plotting_enabled=False, query_enabled=False):
    if df is not None:
        prompt_content = generate_prompt(df, question)
    else:
        prompt_content = question

    messages = [
        {"role": "system", "content": "You are an expert in petroleum engineering."},
        {"role": "user", "content": prompt_content}
    ]

    payload = {
        "model": "llama3.1:8b",
        "options": {
            "temperature": 0.0
        },
        "stream": False,
        "messages": messages
    }

    try:
        response = requests.post("http://117.54.250.177:5162/api/chat", json=payload)
        response.raise_for_status()
        response_data = response.json()
        return response_data['message']['content']
    except Exception as e:
        return f"Error calling LLM API: {str(e)}"

openai_api_key_ = openai_api_key.KEY
os.environ["OPENAI_API_KEY"] = openai_api_key_

client = OpenAI(api_key=openai_api_key_)

conv_hist = []

def contains_word(text, word_list):
    for word in word_list:
        if text.find(word) != -1:
            return True
    return False

word_list = ['table', 'summary', 'summarize', 'rangkum', 'rangkuman']
plot_list = ['plot', 'graph']

def create_table(df):
    columns, values = df.columns, df.values
    header = [html.Tr([html.Th(col) for col in columns])]
    rows = [html.Tr([html.Td(cell) for cell in row]) for row in values]
    table = [html.Thead(header), html.Tbody(rows)]
    return table

def generate_prompt(df, question):
    # Generate insights
    insights = []

    # Basic DataFrame Information
    insights.append(
        f"The DataFrame contains {len(df)} rows and {len(df.columns)} columns."
    )
    insights.append("Here are the first 5 rows of the DataFrame:\n")
    insights.append(df.head().to_string(index=False))

    # Summary Statistics
    insights.append("\nSummary Statistics:")
    insights.append(df.describe().to_string())

    # Column Information
    insights.append("\nColumn Information:")
    for col in df.columns:
        insights.append(f"- Column '{col}' has {df[col].nunique()} unique values.")

    # Missing Values
    missing_values = df.isnull().sum()
    insights.append("\nMissing Values:")
    for col, count in missing_values.items():
        if count > 0:
            insights.append(f"- Column '{col}' has {count} missing values.")

    # Most Common Values in Categorical Columns
    categorical_columns = df.select_dtypes(include=["object"]).columns
    for col in categorical_columns:
        top_value = df[col].mode().iloc[0]
        insights.append(f"\nMost common value in '{col}' column: {top_value}")

    insights_text = "\n".join(insights)

    # Compliment and Prompt
    prompt = (
        """You are Zara, a skilled project manager, data analyst, and petroleum engineer in the oil and gas industry.
        Provide clear, concise answers (1-3 sentences) for project management or data research questions, considering dataset context. 
        If a question is unclear, respond with wit. Use Markdown formatting and introduce yourself as Zara if asked.
        """
    )

    prompt = f"{prompt}\n\nContext:\n\n{insights_text}\n\nUser's Question: {question}"

    return prompt

# filtering code of python
def extract_python_code(text):
    pattern = r'```python\s(.*?)```'
    matches = re.findall(pattern, text, re.DOTALL)
    if not matches:
        return None
    else:
        return matches[0]
    
def safe_exec(code, globals=None, locals=None):
    # Create a StringIO buffer to capture the print output
    output_buffer = io.StringIO()
    exec_globals = globals if globals else {}
    exec_locals = locals if locals else {}

    # Redirect standard output to the buffer
    with contextlib.redirect_stdout(output_buffer):
        exec(code, exec_globals, exec_locals)
    
    # Get the output from the buffer
    exec_output = output_buffer.getvalue()
    output_buffer.close()

    return exec_locals, exec_output

# rendering code

def render(app: Dash, source: DataSource) -> html.Div:
    
    @app.callback(
        Output(ids.RESPONSE_CHAT, 'children'),
        Output(ids.ZARA_CHAT_AREA, "value"),
        Input(ids.ZARA_SUBMIT_BUTTON, 'n_clicks'),
        Input(ids.MEMORY_OUTPUT, 'data'),
        State(ids.ZARA_CHAT_AREA, "value"),
        State(ids.RESPONSE_CHAT, 'children'),
        State("checkbox-plotting", "checked"),
        State("checkbox-pandasai", "checked"),
    )
    
    def update_convo(n, data, question, cur, plotting_enabled, query_enabled):
        if question:
            df = pd.DataFrame(data)
            prompt_content = prompt.generate_prompt(df, question)

            messages = [
                {"role": "system", "content": """You are Zara, an expert project manager and data analyst in the oil and gas industry.
                                                Answer questions about datasets accurately using provided context.
                                                Use Markdown for formatting and limit responses to 1-3 sentences unless generating code.
                                                Use only pandas for data analysis or tables and Plotly for charts.
                                                End pandas code with print() and only print(), and format code as: ```python <code>```
                                                 """},
                {"role": "user", "content": prompt_content}
            ]

            if query_enabled:
                messages.append({"role": "assistant", "content": """
                    Generate Python code using pandas to create a DataFrame from a dataset stored in <df>.
                    The result must be stored in <df_result>. Provide the code in the format:
                    ```python <code>```.
                    Use only pandas.
                """})

            if plotting_enabled:
                messages.append({"role": "assistant", "content": """
                    Generate Python code using Plotly to plot data from <df>. The plot must be stored in <fig>.
                    Provide the code in the format:
                    ```python <code>```.
                    Use only Plotly.
                """})

            # completion = client.chat.completions.create(
            #     model="gpt-3.5-turbo",
            #     messages=messages,
            #     temperature=0.0,
            #     max_tokens=4000,
            #     top_p=0.5
            # )
            
            # response_result = completion.choices[0].message.content
            
            response_result = call_custom_llm(question, df, plotting_enabled, query_enabled)
            
            print(f"\n --- \n {response_result} \n")
            code = extract_python_code(response_result)
            print(f"\n --- \n {code} \n")
            if code is None:
                question = [
                    dcc.Markdown(question, className="chat-item question"),
                    dcc.Markdown(response_result, className="chat-item answer")
                ]
                return (question + cur if cur else question), None
            else:
                import_statement = "import pandas as pd\nimport plotly.express as px\n"
                code_with_import = import_statement + code
                
                # Execute the generated code safely
                exec_globals = {"df": df, "px": px}
                exec_locals, exec_output = safe_exec(code_with_import, globals=exec_globals)
                
                print(f"\n --- \n {exec_globals} \n")
                print(f"\n --- \n {exec_locals} \n")
                
                # Initialize the outputs to default values
                graph_output = None
                data_output = None

                # Determine the type of output and render appropriately
                if "fig" in exec_locals:
                    fig = exec_locals["fig"]
                    graph_output = dcc.Graph(figure=fig)
                    # data_output = ""
                elif "df_result" in exec_locals:
                    result_df_series = exec_locals["df_result"]
                    
                    # Check if the DataFrame has a non-default index
                    if result_df_series.index.name or result_df_series.index.names:
                        result_df_series = result_df_series.reset_index()
                        
                    result_df = pd.DataFrame(result_df_series)
                    # graph_output = ""
                    data_output = dash_table.DataTable(
                        columns=[{"name": i, "id": i} for i in result_df.columns],
                        data=result_df.to_dict('records'),
                        style_cell={'padding': '5px'},
                        style_header={
                            'backgroundColor': '#C0C0C0',
                            'fontWeight': 'bold'
                        },
                        export_format='xlsx',
                    )
                
                elif exec_output:
                    data_output = html.Div(children=[exec_output], className="chat-item answer")
                    
                else:
                    graph_output = html.Div("No valid output generated.")
                    data_output = html.Div("No valid output generated.")

                question = [
                    dcc.Markdown(question, className="chat-item question"),
                    # dcc.Markdown(completion.choices[0].message.content, className="chat-item answer"),
                ]
                # Conditionally add graph_output and data_output to question
                if graph_output is not None:
                    question.append(html.Div(children=[graph_output], className="chat-item answer"))
                if data_output is not None:
                    question.append(html.Div(children=[data_output], className="chat-item answer"))
                    
                
                return (question + cur if cur else question), None
        else:
            return [], None

    return html.Div(
        className=cns.ZARA_CHAT_INPUT,
        children=[
            dmc.Textarea(
                className=cns.ZARA_CHAT_AREA,
                id=ids.ZARA_CHAT_AREA,
                placeholder='Write your question here...',
                autosize=False,
                minRows=2,
                maxRows=2,
                variant='default',
                radius='lg',
                debounce=True
            ),
            dmc.Checkbox(id="checkbox-plotting", label="Enable plotting"),
            dmc.Checkbox(id="checkbox-pandasai", label="Enable query"),
            html.Div(className=cns.ZARA_SUBMIT_BUTTON,
                     children=[
                         dmc.ActionIcon(
                             DashIconify(icon='formkit:submit', width=25),
                             id=ids.ZARA_SUBMIT_BUTTON,
                             radius='md',
                             size=60,
                             variant='subtle',
                             color='gray',
                             n_clicks=0
                         )
                     ])
        ]
    )
