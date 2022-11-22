from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
import requests
  
import time
# instance of Options class allows
# us to configure Headless Chrome
options = Options()
  
# this parameter tells Chrome that
# it should be run without UI (Headless)
options.headless = True




chrome = webdriver.Chrome(executable_path = "C:/Users/Amar kumar/Downloads/chromedriver_win32/chromedriver.exe",options=options)

chrome.get('https://www.google.com/')
page_content = requests.get("http://127.0.0.1:8000/scrap/amazon").content
simple_soup = BeautifulSoup(page_content,'html.parser')

record_id = simple_soup.find(id="record_id").string
image_path = simple_soup.find(id="image_data")

image_path = image_path['src']

delay = 3 # seconds
try:
    # myElem = WebDriverWait(chrome, delay).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'img[alt="Camera search"]')))
    # camera_search = chrome.find_element(By.CSS_SELECTOR,'img[alt="Camera search"]')
    # myElem.click()
    chrome.execute_script("arguments[0].click();", WebDriverWait(chrome, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'img[alt="Camera search"]'))))

    time.sleep(2)

    box = chrome.find_element(By.CSS_SELECTOR,'input[placeholder="Paste image link"]')
    attribute_check = box.send_keys(image_path)

    box.send_keys(u'\ue007')
    elems =	WebDriverWait(chrome, delay).until(EC.presence_of_element_located((By.XPATH,'//a[@href]')))
    all_anchors = chrome.find_elements(By.XPATH,'//a[@href]')

    final_links = []
    for anchor in all_anchors:
    	link = anchor.get_attribute('href')
    	amazon_link = "https://www.amazon."
    	if amazon_link in link:
    		final_links.append(link)
    	

    if(len(final_links) > 0):
        if(len(final_links) > 3):
            amazon_link_final_text = ','.join(final_links[:3])
        else:
            amazon_link_final_text = ','.join(final_links)
    else:
        amazon_link_final_text = 'no data found'

    # data to be sent to api
    API_ENDPOINT = 'http://127.0.0.1:8000/update/amazon'
    data = {'record_id':record_id,
            'amazon_link':amazon_link_final_text}
      
    # sending post request and saving response as response object
    response = requests.post(url = API_ENDPOINT, data = data)
    print(response.text)
    print("pass the test")

except TimeoutException:
    print("Loading took too much time!")

