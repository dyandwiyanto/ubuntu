from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Remote(
    command_executor="http://127.0.0.1:4444/wd/hub",
    options=options
)

try:
    driver.get("https://example.com")
    print("Title:", driver.title)
    h1 = driver.find_element(By.TAG_NAME, "h1").text
    print("H1:", h1)
finally:
    driver.quit()
