from dotenv import load_dotenv
import os

load_dotenv()

DB_CONFIG = {
    'host': os.environ.get("host"),
    'database': os.environ.get("database"),
    'user': os.environ.get("user"),
    'password': os.environ.get("password")
}
