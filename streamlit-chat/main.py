import streamlit as stream
from streamlit_chat import message
from dotenv import load_dotenv
import os
import requests
import secrets


from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    SystemMessage,
    HumanMessage,
    AIMessage
)


def init():

        # Load the OpenAI API key from the environment variable
    load_dotenv()
    
    # test that the API key exists
    if os.getenv("OPENAI_API_KEY") is None or os.getenv("OPENAI_API_KEY") == "":
        print("OPENAI_API_KEY is not set")
        exit(1)
    else:
        print("OPENAI_API_KEY is set")




    stream.set_page_config(
        page_title="ETL Discovery Tool",
        page_icon="🤖"
        )





def main():
    
    init()

    chat = ChatOpenAI(model_name="gpt-4",temperature=0)

    def fetch_data_from_backend(user_input, user_token):
    # Replace this with your actual API endpoint
        api_url = "http://127.0.0.1:5000/chat"
        payload = {"user_input": user_input,"user_token": user_token}

        try:
            # print("Request Payload:", payload)
            response = requests.post(api_url, json=payload)

            if response.status_code == 200:
                return response.json()
            elif response.status_code == 201:
                # return {"info": f"Success: {response.status_code} - {response.text}"}
                return response.json()
            else:
                return {"error": f"Error: {response.status_code} - {response.text}"}
        except Exception as e:
            return {"error": f"Error: {str(e)}"}


    # initialize message history
    if "messages" not in stream.session_state:
        stream.session_state.messages = [
            SystemMessage(content="You are a helpful assistant.")
        ]



    stream.header("ETL Discovery Tool🤖")

    # with stream.sidebar:
    user_input = stream.chat_input("Message ETL Discovery: ", key ="user_input")

# handle user input
    if user_input:
        stream.session_state.messages.append(HumanMessage(content=user_input))
        user_token = stream.session_state.get("user_token", "jklm")

        # Generate a random user_token
        # user_token = secrets.token_urlsafe(16)
        # print("Generated user_token:", user_token)
        # stream.session_state.user_token = user_token
        
        with stream.spinner("Thinking..."):
            # response = chat(stream.session_state.messages)
            # print("OpenAI GPT Response:", response.content)
            # Fetch data from the custom API endpoint based on user input
            endpoint_response = fetch_data_from_backend(user_input, user_token)
            
            if "error" not in endpoint_response:
            # Assuming the API response contains relevant data
                # stream.session_state.messages.append(AIMessage(content=endpoint_response.content))
                output_content = endpoint_response.get("response", "")
                # print("Output Content:", output_content)
                stream.session_state.messages.append(AIMessage(content=str(output_content)))
                # print("Streamlit Session State:", stream.session_state)
            else:
                stream.warning(endpoint_response["error"])

    # display message history
    messages = stream.session_state.get('messages', [])
    for i, msg in enumerate(messages[1:]):
        if i % 2 == 0:
            message(msg.content, is_user=True, key=str(i) + '_user')
        else:
            message(msg.content, is_user=False, key=str(i) + '_ai')


if __name__ == "__main__":
    main()