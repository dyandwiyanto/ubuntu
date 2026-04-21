from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless=new")
options.add_argument("--window-size=1366,768")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Remote(
    command_executor="http://127.0.0.1:4444/wd/hub",
    options=options
)

try:
    driver.get("https://google.com")
    driver.save_screenshot("hasil.png")
    print("Screenshot disimpan: hasil.png")
finally:
    driver.quit()
