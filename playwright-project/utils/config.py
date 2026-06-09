from dotenv import load_dotenv
import os

load_dotenv()

QA_USERNAME = os.getenv("QA_USERNAME")
QA_PASSWORD = os.getenv("QA_PASSWORD")
BASE_URL = os.getenv("BASE_URL")

print(QA_USERNAME)
print(QA_PASSWORD)
print(BASE_URL)