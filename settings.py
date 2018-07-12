from dotenv import load_dotenv
load_dotenv()

# OR, the same with increased verbosity:
load_dotenv(verbose=True)

# OR, explicitly providing path to '.env'
from pathlib import Path  # python3 only
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

import os
COOKIE = os.getenv("COOKIE")
MEDIUM_CLIENT_SECRET = os.getenv("MEDIUM_CLIENT_SECRET")
MEDIUM_CLIENT_ID = os.getenv("MEDIUM_CLIENT_ID")