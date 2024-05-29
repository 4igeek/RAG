## Installing the project on your own machine
1) Navigate to where you want to install the project files on your computer and then run the following to clone the project to that folder.

``git clone https://github.com/4igeek/RAG.git .`` 

2) Setup a virtual environment using the following command: 

``conda create -n venv python=3.10 anaconda``.

3) Activate the environment using the following: 

``conda activate venv``.

4) Install all the dependencies (ensuring venv is activated - see step 3) using the following: 

``pip install -r requirements.txt``.

5) Create a file in the root of the project called `.env`

6) Add a new line to .env which contains your OpenAI key information i.e. `OPENAI_API_KEY=sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX` (replacing the X's with your actual key).

7) Replace the PDFs in the `data` folder with your own content (this is the data that will be used in RAG).

Once all that is done you should be able to run the project locally.