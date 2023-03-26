'''
depency module of the project
'''
import openai
import os
from dotenv import load_dotenv

# Load the environment variables from the .env file
load_dotenv()

def openai_dependency():
  openai.organization = os.getenv("OPENAI_API_ORG")
  openai.api_key = os.getenv("OPENAI_API_KEY")
  return openai
