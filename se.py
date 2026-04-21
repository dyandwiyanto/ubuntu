import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()

options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--window-size=1920,1080")

# Pakai profile permanen agar sesi login tetap tersimpan.
# Bisa dioverride lewat env CHROME_USER_DATA_DIR jika perlu.
chrome_profile_dir = os.environ.get("CHROME_USER_DATA_DIR", "/tmp/chrome-profile")
options.add_argument(f"--user-data-dir={chrome_profile_dir}")

driver = webdriver.Remote(
    command_executor="http://127.0.0.1:4444",
    options=options
)

try:
    driver.get("https://www.google.com")
    print("Browser kebuka. Login dulu kalau perlu, lalu tekan Enter di terminal buat tutup.")
    input()
finally:
    driver.quit()
