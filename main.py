import os # Used to setup environment variable.
from dotenv import load_dotenv
load_dotenv()

os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')

from llama_index.core.response.pprint_utils import pprint_response
from llama_index.core import VectorStoreIndex,SimpleDirectoryReader

documents=SimpleDirectoryReader("data").load_data()

index = VectorStoreIndex.from_documents(documents) # Converts the documents into index

query_engine = index.as_query_engine() # Responsible for retrieving the information from the indices

response = query_engine.query("What did the artist sketch in their scene?") # Sends the query to ChatGPT
pprint_response(response,show_source=True)
print(response)