import time
from selenium import webdriver

if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get("https://www.python.org")
    time.sleep(5)
    print(driver.title)