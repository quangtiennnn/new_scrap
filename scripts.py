import pandas as pd
import time
import os
import csv
import pandas as pd
from tqdm import tqdm
from urllib.parse import urlparse, urlunparse


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Set Chrome options:
chrome_options = Options()
# chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox') 
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-application-cache")
chrome_options.add_argument("--disable-cache")
chrome_options.add_argument("--disk-cache-size=0")


def url_edited(url):
    try:
        parsed_url = urlparse(url)
        new_path = "/vi-vn" + parsed_url.path
        return urlunparse(parsed_url._replace(path=new_path, query=""))
    except Exception as e:
        print(f"Error editing URL: {url}")
        return ""

def get_url(url):
    try:
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(url)
        time.sleep(2)  # Ensure the page loads
        elem = driver.find_element(By.CSS_SELECTOR, "a[data-element-name='property-card-content']")
        href = elem.get_attribute('href')
        driver.close()
        return url_edited(href)
    except Exception as e:
        print(f"Error fetching URL: {url}")
        return ""