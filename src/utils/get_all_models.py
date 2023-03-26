import os
import openai
from dotenv import load_dotenv

# Load the environment variables from the .env file
load_dotenv()


def get_all_models() -> list:
  # List the available models
  openai.organization = os.getenv("OPENAI_API_ORG")
  openai.api_key = os.getenv("OPENAI_API_KEY")
  return openai.Model.list()

if __name__ == "__main__":
  print(get_all_models())
