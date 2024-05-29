import os # Used to setup environment variable.
from dotenv import load_dotenv
load_dotenv()

os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY') # Pull in the required env vars

# Libraries needed to run program
from llama_index.core import VectorStoreIndex,SimpleDirectoryReader
from llama_index.core.response.pprint_utils import pprint_response

documents = SimpleDirectoryReader("data").load_data() # Load the data in the data folder to a var called "documents"

index = VectorStoreIndex.from_documents(documents) # Converts the documents into indexes

query_engine = index.as_query_engine() # Retrieve the information from the indices

response = query_engine.query("What did the artist sketch in their scene?") # Sends the query to ChatGPT
pprint_response(response,show_source=True) # Compiles the response
print(response) # Prints the response