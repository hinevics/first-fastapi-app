import os

from dotenv import load_dotenv

load_dotenv()

dir_path = os.path.dirname(os.path.realpath(__file__))


DATABASE_URL = 'sqlite:///{dir_path}{name}'.format(name=os.getenv('DATABASE_URL'),
                                                   dir_path=dir_path)
