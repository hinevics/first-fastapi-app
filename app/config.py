import os

from dotenv import load_dotenv

load_dotenv()

DATABASE_NAME = os.getenv('DATABASE_NAME')
DATABASE_PATH = os.getenv('DATABASE_PATH')
DATABASE_URL = r'sqlite:///{dir_path}\{name}'.format(name=DATABASE_NAME, dir_path=DATABASE_PATH)
