from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=key)

def assistant_creator():

    file = client.files.create(
        file=open("Working_ETL/2csv_ETL.ipynb", "rb"),
        purpose='assistants'
    )

    file2 = client.files.create(
        file=open("Working_ETL/apitomysql_ETL.ipynb", "rb"),
        purpose='assistants'
    )

    file3 = client.files.create(
        file=open("Working_ETL/app.py", "rb"),
        purpose='assistants'
    )
    
    file4 = client.files.create(
        file=open("Working_ETL/assignment_ETL.ipynb", "rb"),
        purpose='assistants'
    )

    file5 = client.files.create(
        file=open("Working_ETL/clan_ETL.ipynb", "rb"),
        purpose='assistants'
    )

    file6 = client.files.create(
        file=open("Working_ETL/DataFrame_ETL.ipynb", "rb"),
        purpose='assistants'
    )

    file7 = client.files.create(
        file=open("Working_ETL/etl_1.py", "rb"),
        purpose='assistants'
    )

    file8 = client.files.create(
        file=open("Working_ETL/ETL_crowdfunding.ipynb", "rb"),
        purpose='assistants'
    )
    

    file9 = client.files.create(
        file=open("Working_ETL/etl_googlesheet.py", "rb"),
        purpose='assistants'
    )

    file10 = client.files.create(
        file=open("Working_ETL/ETL_imdb.ipynb", "rb"),
        purpose='assistants'
    )

    file11 = client.files.create(
        file=open("Working_ETL/etl_latest.ipynb", "rb"),
        purpose='assistants'
    )

    file12 = client.files.create(
        file=open("Working_ETL/etl_runtime_analysis.ipynb", "rb"),
        purpose='assistants'
    )

    file13 = client.files.create(
        file=open("Working_ETL/ETL_telecom.ipynb", "rb"),
        purpose='assistants'
    )


    file14 = client.files.create(
        file=open("Working_ETL/PySpark_ETL.py", "rb"),
        purpose='assistants'
    )

    file15 = client.files.create(
        file=open("Working_ETL/spark_etl.py", "rb"),
        purpose='assistants'
    )
    
    assistant = client.beta.assistants.create(
        name="ETL Discovery Assistant OpenAI",
        description="You are ETL Discovery Assistant at Rob Sandberg who responds to the users effectively with a precise response regarding the ETL Workflows, and other relevant information the user requires and their attributes/properties e.g. configuration, workflows, etc. if and when available. You look into the files attached and come up with an appropriate response that suits the best for the user's question.",
        model="gpt-3.5-turbo-1106",
        tools=[{"type": "retrieval"}],
        file_ids=[file.id, file2.id, file3.id, file4.id,file5.id, file6.id, file7.id, file8.id,file9.id, file10.id, file11.id, file12.id,file13.id, file14.id, file15.id]
        # file_ids=[file15.id]
    )
    return assistant.id

x = assistant_creator()
print(x)