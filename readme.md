
## Create virtual environment using below 
python3.10 -m venv env
## Activate virtual Environment using below 
source env/bin/activate
## to deactivate virtual Envirnment use below
deactivate
## Install required packages then use below to save dependencies
pip freeze > requirements.txt
## create an API key on the Anthropic console and add it to the environment variable for the secure access
export my_key_gen='your_api_key'

