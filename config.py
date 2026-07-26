import os
from dotenv import load_dotenv

# Load variables from .env file into the environment
load_dotenv()

class Config:
    """Base configuration class."""
    # Used for securely signing session cookies
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'fallback_default_secret_key'