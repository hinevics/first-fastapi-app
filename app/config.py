import os

from dotenv import load_dotenv

load_dotenv()

dir_path = r'D:\Dev\Coding\first-fastapi-app\first-fastapi-app\db'

DATABASE_URL = r'sqlite:///{dir_path}\{name}'.format(name=os.getenv('DATABASE_URL'),
                                                    dir_path=dir_path)
