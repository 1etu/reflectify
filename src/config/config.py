import os
from dotenv import load_dotenv

load_dotenv()

GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
GITHUB_USERNAME = os.getenv('GITHUB_USERNAME')
DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')

__all__ = ['GITHUB_TOKEN', 'GITHUB_USERNAME', 'DATA_DIR']