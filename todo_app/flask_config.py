import os


class Config:
    def __init__(self):
        """Base configuration variables."""
        self.SECRET_KEY = os.getenv('SECRET_KEY')
        self.LOG_LEVEL = os.getenv('LOG_LEVEL') if os.getenv('LOG_LEVEL') is not None else 'DEBUG'
        self.LOGGLY_TOKEN = os.getenv('LOGGLY_TOKEN')
        if not self.SECRET_KEY:
            raise ValueError("No SECRET_KEY set for Flask application. Did you follow the setup instructions?")
