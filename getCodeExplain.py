import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.organization = ''
openai.api_key = os.getenv("OPENAI_API_KEY")

# Use o método `list_models` em vez de `Model.list()`
models = openai.Model.list()
print(models)
