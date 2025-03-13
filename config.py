import os
from dotenv import load_dotenv

load_dotenv()

SA_COOKIE = {
    "bbuserid": os.getenv("SA_BBUSERID"),
    "bbpassword": os.getenv("SA_BBPASSWORD"),
}
