from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from config.settings import settings


class BrowserManager:
    def __init__(self):
        self.driver = None

    def start(self):
        options = Options()

        options.add_argument("--start-maximized")
        options.add_argument(f"--user-data-dir={settings.chrome_profile_dir}")

        if settings.keep_browser_open:
            options.add_experimental_option("detach", True)

        if settings.headless:
            options.add_argument("--headless=new")

        # Selenium Manager resuelve ChromeDriver automáticamente.
        self.driver = webdriver.Chrome(options=options)
        return self.driver

    def close(self):
        if self.driver and not settings.keep_browser_open:
            self.driver.quit()
