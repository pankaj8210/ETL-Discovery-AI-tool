import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
from dotenv import load_dotenv
import uuid
import re

app = Flask(__name__)
CORS(app)

load_dotenv()
key = os.getenv("OPENAI_API_KEY")
assistant_id = os.getenv("ASSISTANT_ID")

# -------------------------
def copy_text(source_file):
    try:
        with open(source_file, 'r') as source:
            text_content = source.read()
            return text_content
    except FileNotFoundError:
        print(f"Error: One of the files not found.")
    except Exception as e:
        print(f"Error: {e}")
# -------------------------
def remove_references(input_string):
    pattern = r'【\d+†\w+】'

    result_string = re.sub(pattern, '. ', input_string)
    return result_string
#--------------------------
client = OpenAI(api_key=key)

existing_assistant_id = assistant_id

user_threads = {}

ins = copy_text('ins.txt')

@app.route('/chat', methods=['POST'])
def chat_endpoint():

    user_input = request.json.get('user_input')
    user_token = request.json.get('user_token')

    if not user_input or not user_token:
        return jsonify({"error": "Both 'user_input' and 'user_token' are required."}), 400

    if user_token not in user_threads:
    
        thread = client.beta.threads.create()
        user_threads[user_token] = {'thread': thread}
    else:
    
        thread = user_threads[user_token]['thread']

    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=user_input,
    )

    new_run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=existing_assistant_id,  # Use the existing assistant ID
        instructions=ins,  # Update with actual instructions
    )
    c=0

    status = None
    while status != "completed":
        run_list = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=new_run.id
        )
        status = run_list.status
        c+=1
    messages = client.beta.threads.messages.list(
        thread_id=thread.id
    )
    # word_list1=['appointment', 'session', 'booking', 'book',  'bookings']
    response = remove_references(messages.data[0].content[0].text.value)
    
    # values = [message.content[0].text.value for message in messages if message.content and message.content[0].type == 'text']
    # v = values[-1]
    print(len(messages.data))
    # contains_word = any(word in user_input.lower() for word in word_list1)

    # if contains_word:
    #     s='''\n\nThe appointments can also be set manually through external links-\nFor appointment in Davenport- click 1,\nLakeland- click 2,\nAuburndale- click 3.\nIf you are unsure of the branch- click 0.'''
    #     return {'response':response + remove_references(s),
    #             'links':[
    #                 {'label':'here', 'link': 'https://msgsndr.com/widget/booking? calendar=h2JxMrxMfp2CKeWEEukm'},
    #                 {'label':'here', 'link': 'https://api.leadconnectorhq.com/widget/bookings/lakeland-slim'},
    #                 {'label':'here', 'link': 'https://api.leadconnectorhq.com/widget/bookings/cryoskinbxktx9'},
    #                 {'label':'here', 'link': 'https://api.leadconnectorhq.com/widget/bookings/cryoskin'}                
    #             ]}
    # elif len(messages.data) % 20 == 0:
    #     s=''' Also explore our latest products by following this external link 0.\nYour feedback is valuable to us, so don't forget to rate our services at 1!'''
    #     return {'response':response+remove_references(s),
    #             'links':[
    #                 {'label':'form', 'link': 'https://form.jotform.com/221244281690149'},
    #                 {'label':'form', 'link': 'https://search.google.com/local/writereview?placeid=ChlJY2gEHLxr3YgRt6dmJ0wf-5k'}      
    #             ]}
    # else: 
    return {'response':response}

if __name__ == "__main__":
    app.run(debug=True)

