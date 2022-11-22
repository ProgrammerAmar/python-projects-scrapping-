from selenium import webdriver
from selenium.webdriver.common.by import By
import requests


from pages.quotes_page import QuotesPage

from selenium.webdriver.chrome.options import Options
  
# instance of Options class allows
# us to configure Headless Chrome
options = Options()
  
# this parameter tells Chrome that
# it should be run without UI (Headless)
options.headless = False



chrome = webdriver.Chrome(executable_path = "C:/Users/Amar kumar/Downloads/chromedriver_win32/chromedriver.exe",options=options)

chrome.get('http://quotes.toscrape.com')

page_content = requests.get("https://quotes.toscrape.com/").content

page = QuotesPage(chrome)

for quote in page.quotes:
	print(quote)
