from pathlib import Path
import os

ENV = os.getenv("ENV", "LOCAL")

PROJECT_ROOT = Path(__file__).resolve().parents[2]

BASE_URLS = {
    "LOCAL": (PROJECT_ROOT / "test site" / "app" / "index.html").as_uri(),
}

BASE_URL = BASE_URLS[ENV]

print(ENV)
print(BASE_URL)
