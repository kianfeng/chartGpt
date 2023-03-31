'''
dependency module of the project
'''
import openai
from fastapi import Depends

from src.aws.secret_manager import SecretManagerClient


def get_secret_manager_client() -> SecretManagerClient:
  ''' Dependency for the SecretManagerClient'''
  return SecretManagerClient()

def get_openai_secret_manager(
  openapi_secret_manager: SecretManagerClient = Depends(get_secret_manager_client)
) -> dict:
  ''' Dependency for the OpenAI API'''
  return openapi_secret_manager.get_secret_string("openAPI")


def openai_dependency(
    openai_client_secret_manager: dict = Depends(get_openai_secret_manager)
) -> openai:
  """ Dependency for the OpenAI API """
  openai.organization = openai_client_secret_manager['OPENAI_API_ORG']
  openai.api_key = openai_client_secret_manager['OPENAI_API_KEY']
  return openai
