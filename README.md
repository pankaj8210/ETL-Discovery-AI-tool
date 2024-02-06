# ETL-Discovery-AI-tool
The Open-Source Generic ETL Tool serves as the core engine for Extract, Transform, and Load (ETL) operations. It is designed to handle data extraction, transformation, and loading tasks efficiently. It will be used for training the OpenAI model on the ETL Discovery tools.

## Step 1. File Description
### assistant_creator.py
### Provided Python script uses the OpenAI API to create an OpenAI assistant. The OpenAI assistant is trained on various ETL-related files, such as Jupyter notebooks and Python scripts, which are uploaded using the OpenAI API to create an OpenAI Assistant ID. The files are associated with the assistant to enhance its understanding of ETL concepts and workflows.
•	Import Libraries:
o	In this step we are importing necessary libraries, including OpenAI for interacting with the OpenAI.
o	 In this step API and dotenv are for loading environment variables from a file.
•	Load API Key:
o	In this step loading the OpenAI API key from the environment variables.
o	In this step Defining the client from OpenAI
•	Assistant Creation Function
o	In this step the assistant_creator function is defined to create an OpenAI assistant.

•	File Uploads:
o	In this step inside the assistant_creator function uploads multiple ETL Pipelines files, including Jupyter notebooks and Python scripts, using the OpenAI API's files. These files are associated with the assistant to train it on various aspects of ETL workflows.
•	Assistant Creation:
o	In this step the assistant_creator function then creates an OpenAI assistant using the uploaded files. -The assistant is given a name, and description, and associated with a specific GPT model. It    is configured to use a retrieval tool.
•	Return Assistant ID:
o	In this step the function returns the ID of the created assistant.
•	Print Assistant ID:
o	In this step the function prints the ID of the created OpenAI Assistant in the Terminal.
o	In this step save the printed Assistant ID in a .env file. We will use the Assistant ID in the Flask API
### app1.py
This Python script creates a Flask API that serves as an interface for interacting with an OpenAI model assistant. The OpenAI assistant is designed to respond to user input and provide relevant information based on ETL pipeline workflows.
Here's a step-by-step description of app1.py:
•	Import Libraries:
•	Load Environment Variables:
o	In this step load the OpenAI API key and existing OpenAI assistant ID from environment variables.
•	File Operations Functions:
o	In this step we define two functions (copy_text and remove_references) for file operations and text manipulation.
•	In this step copy_text reads the content of a file.
•	In this step remove_references uses regular expressions to remove specific patterns from text.
•	OpenAI Client Initialization:
o	In this step initializes the OpenAI client using the API key.
•	OpenAI Assistant Setup:
o	In this step use the existing assistant ID from the assistant id that we have already gotten from environment variable.
•	In this step create an empty dictionary to keep track of user conversations.
•	In this step using the copy_text function we are passing our instruction file and store into a variable.
•	Flask App Initialization:
o	In this step the Flask API is initialized and is enabled to handle requests and responses.
•	Chat Endpoint function:
o	In this step the chat endpoint function is defined to handle POST requests. It receives user input and user tokens from the request in JSON format.
•	Thread and Message Handling:
o	In this step in this step this python file manages user threads using the OpenAI API's threads and messages functionality. It creates a new thread if the user token is not present, and then adds the user's message to the thread.
•	Assistant Interaction:
o	In this step it uses the OpenAI API to create a new run, associating it with the existing assistant ID. The conversation history and instructions are updated based on the user input.
•	Return Response:
o	In this step the response from the OpenAI Assistant model is extracted. The final response is sent back as a JSON object.
•	Run the Flask app's main function



### Main.py
##This Python script integrated the Streamlit front-end to create a user interface for an ETL Discovery Tool and integrating OpenAI for conversational interactions. 
Here's a concise step-by-step description:
•	Import Libraries:
•	Environment Initialization:
o	In this step Check for the existence of the OpenAI API key in the environment variables.
•	Page configuration:
o	sets the page title and icon
•	Backend Communication Function:
o	this step defines a function to communicate with a custom backend API, sending user input and receiving responses.
•	Streamlit UI Setup:
o	In this step it sets up the Streamlit UI, including the page header and a chat input box for users to interact.
•	User Input Handling:
o	In this step we are handling the user input and appends it to the message history.
•	Interaction with OpenAI Assistant:
o	In this step sending user input to the OpenAI Assistant model for processing and appends the model's response to the message history.
•	Display Message History:
o	In this step the message history, containing both user and OpenAI messages, is displayed in the Streamlit app.
•	Run main function

## Step 2. How to set up and run
•	Clone the Repository/ download the file
o	UNZIP the sources or clone the private repository. After getting the code, open the file in the vs code, take new terminal and navigate to the working directory.
•	Setup Environment
virtualenv modules installation (Windows-based systems)
o	Python –m venv  .venv-  Name your venv according to you
o	.venv\Scripts\activate- for activating the env
•	Install the Required Application 
o	pip install -r requirements.txt
•	Create a .env file for storing the OpenAI API key 
Run
	-Run assistant_creator.py file
o	Python assistant_creator.py
	- Run app1.py file
o	Python app1.py
	- Run main.py file
o	Streamlit run main.py

