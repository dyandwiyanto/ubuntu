from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# Konfigurasi Chrome
options = Options()

# WAJIB: jangan headless kalau mau terlihat di VNC
# options.add_argument("--headless=new")  # jangan dipakai

options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")

# Sambung ke Selenium server di container
driver = webdriver.Remote(
    command_executor="http://127.0.0.1:4444/wd/hub",
    options=options
)

try:
    # Buka halaman awal
    driver.get("https://www.google.com")

    print("=" * 60)
    print("Browser sudah dibuka di container.")
    print("Sekarang buka noVNC di browser kamu:")
    print("http://IP-VPS:7900")
    print("Password biasanya: secret")
    print("=" * 60)
    print("Kamu bisa kontrol browser dari sana.")
    print("Script ini akan menahan browser tetap hidup selama 30 menit.")
    print("Tekan Ctrl+C di terminal kalau mau berhenti lebih cepat.")
    print("=" * 60)

    # Tahan browser tetap hidup
    for i in range(1800):
        time.sleep(1)
        if i % 30 == 0:
            try:
                title = driver.title
                current_url = driver.current_url
                print(f"[{i:>4}s] TITLE: {title} | URL: {current_url}")
            except Exception as e:
                print(f"Gagal baca status browser: {e}")

except KeyboardInterrupt:
    print("\nDihentikan manual oleh user.")
except Exception as e:
    print(f"Terjadi error: {e}")
finally:
    try:
        driver.quit()
    except Exception:
        pass
    print("Browser ditutup.")
