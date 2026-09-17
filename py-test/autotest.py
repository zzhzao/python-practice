import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

ChromeIns = ChromeDriverManager().install()
driver = webdriver.Chrome(service=Service(ChromeIns))

driver.get("http://www.baidu.com")
time.sleep(3)

driver.find_element(By.CSS_SELECTOR,"#chat-textarea").send_keys("天气")

driver.find_element(By.CSS_SELECTOR,"#chat-submit-button").click()

time.sleep(3)

driver.quit()