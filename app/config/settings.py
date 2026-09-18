from dataclasses import dataclass
from pathlib import Path
import os

from dotenv import load_dotenv

load_dotenv()

PROJECT_ROOT = Path(__file__).resolve().parents[2]


def _bool(name: str, default: bool) -> bool:
    raw = os.getenv(name)
    if raw is None:
        return default
    return raw.strip().lower() in {"1", "true", "yes", "y", "si", "sí"}


@dataclass(frozen=True)
class Settings:
    ebanca_url: str = os.getenv("EBANCA_URL", "https://www.ebanca.com/login")
    wait_timeout: int = int(os.getenv("WAIT_TIMEOUT", "20"))
    keep_browser_open: bool = _bool("KEEP_BROWSER_OPEN", True)
    headless: bool = _bool("HEADLESS", False)

    @property
    def chrome_profile_dir(self) -> Path:
        configured = os.getenv("CHROME_PROFILE_DIR", "runtime/chrome_profile")
        path = Path(configured)
        if not path.is_absolute():
            path = PROJECT_ROOT / path
        path.mkdir(parents=True, exist_ok=True)
        return path


settings = Settings()
