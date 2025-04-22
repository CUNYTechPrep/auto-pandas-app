# titanic_qa_streamlit.py
# A simple Streamlit app to ask questions about the Titanic dataset.
# Updated to use OpenAI Python SDK >=1.0.0 (OpenAI client)

import os
import pandas as pd
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()
# Initialize OpenAI client with your API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@st.cache_data
def load_data(path="data/titanic.csv"):
    """
    Load the Titanic CSV from the data folder into a pandas DataFrame and cache the result.
    """
    return pd.read_csv(path)

@st.cache_data
def generate_pandas_code(df, columns, question):
    """
    Use OpenAI client to generate a pandas code snippet (the part after 'result =')
    that answers the user's question using the DataFrame columns.
    
    Parameters:
    df - The pandas DataFrame with the data
    columns - List of column names in the DataFrame
    question - The user's natural language question
    """
    # Get first 5 rows to provide as context
    first_5_rows = df.head().to_string()
    
    # System and user messages for the chat
    system_msg = (
        "You are a helpful assistant that writes pandas code snippets.\n"
        "When given DataFrame column names, sample data, and a question, respond with only the Python expression after 'result ='."
    )
    user_msg = f"DataFrame columns: {columns}\n\nFirst 5 rows of data:\n{first_5_rows}\n\nQuestion: {question}\n"
    
    # Call the chat completion endpoint on the client
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_msg},
            {"role": "user", "content": user_msg}
        ],
        max_tokens=150,
        temperature=0,
    )
    # Extract the code snippet from the response
    code_snippet = response.choices[0].message.content.strip()
    return code_snippet, system_msg, user_msg


def run_query(df, code_snippet):
    """
    Safely execute the pandas code snippet and return the result.
    """
    local_vars = {"df": df}
    # Execute the snippet in a restricted local scope
    exec(f"result = {code_snippet}", {}, local_vars)
    return local_vars.get("result")

# Streamlit app layout
st.title("Titanic Data Q&A")
st.write("Ask questions about the Titanic dataset, like 'how many men died'.")

# Load data once
df = load_data()

# Optional: show DataFrame preview and columns
with st.expander("Show dataset preview and columns"):
    st.dataframe(df.head())
    st.write("Columns:", list(df.columns))

# User input with default question
question = st.text_input(
    "Enter your question:", 
    value="How many men and women survived the titanic?"
)

if st.button("Ask"):
    if not question:
        st.error("Please enter a question.")
    else:
        try:
            # Generate the pandas expression using the OpenAI client
            code_snippet, system_msg, user_msg = generate_pandas_code(df, list(df.columns), question)
            
            # Show the full prompt sent to the LLM with nice formatting
            with st.expander("Show prompt sent to LLM"):
                st.markdown("### System Message (Instructions to AI)")
                st.markdown(f"```\n{system_msg}\n```")
                
                st.markdown("### User Message (Your Question & Data)")
                st.markdown(f"```\n{user_msg}\n```")
                
            st.code(f"result = {code_snippet}", language="python")

            # Run the generated code and get the answer
            result = run_query(df, code_snippet)

            # Display result
            if isinstance(result, pd.DataFrame):
                st.dataframe(result)
            else:
                st.write(result)
        except Exception as e:
            st.error(f"Error: {e}")
