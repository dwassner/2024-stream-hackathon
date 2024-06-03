import os
import dotenv

dotenv.load_dotenv()

user = os.getenv("rds_username", "root")
pw = os.getenv("rds_password", "my-db-password")
host = os.getenv("rds_host", "127.0.0.1")
port = 3306
db = "stream-hackathon"
