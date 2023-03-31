import json

import botocore
import botocore.session
from aws_secretsmanager_caching import SecretCache, SecretCacheConfig
from botocore.exceptions import ClientError


class SecretManagerClient:
  """SecretManagerClient is a wrapper around the boto3 client for secretsmanager."""

  def __init__(self):
    client = botocore.session.get_session().create_client('secretsmanager')
    cache_config = SecretCacheConfig()
    self.secret_cache = SecretCache(config=cache_config, client=client)

  def get_secret_string(self, secret_name: str) -> dict:
    # todo: figure out how cache vs client works
    """
    Get the secret string from the secret manager.
    :param secret_name: secret name
    :return: dict
    """
    try:
      secret = self.secret_cache.get_secret_string(secret_name)
      return json.loads(secret)
    except ClientError as e:
      raise Exception("boto3 client error in get_secret_string: " + e.__str__())
    except Exception as e:
      raise Exception("Unexpected error in get_secret_string: " + e.__str__())
