"""
Capture screenshots of the SupplyWise interface
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from PIL import Image
import io

def capture_screenshots():
    # Setup Chrome options
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--window-size=1920,1080')
    
    try:
        driver = webdriver.Chrome(options=chrome_options)
        
        screenshots = []
        
        # 1. SupplyWise Dashboard
        print("Capturing SupplyWise dashboard...")
        driver.get('http://127.0.0.1:8000/supplywise')
        time.sleep(3)
        screenshot = driver.get_screenshot_as_png()
        with open('screenshot_supplywise_main.png', 'wb') as f:
            f.write(screenshot)
        screenshots.append('screenshot_supplywise_main.png')
        print("✓ Saved screenshot_supplywise_main.png")
        
        # 2. Dashboard Data (if accessible)
        print("Capturing dashboard data view...")
        driver.get('http://127.0.0.1:8000/supplywise/dashboard')
        time.sleep(2)
        
        # For JSON data, create a simple visualization
        page_text = driver.find_element(By.TAG_NAME, 'body').text
        print("✓ Dashboard data captured")
        
        driver.quit()
        print(f"\n✅ Successfully captured {len(screenshots)} screenshots")
        return screenshots
        
    except Exception as e:
        print(f"❌ Error capturing screenshots: {e}")
        print("Make sure the server is running at http://127.0.0.1:8000")
        try:
            driver.quit()
        except:
            pass
        return []

if __name__ == "__main__":
    print("📸 Starting screenshot capture...")
    print("⚠️  Make sure your server is running: python -m uvicorn app.app:app --host 127.0.0.1 --port 8000\n")
    capture_screenshots()
