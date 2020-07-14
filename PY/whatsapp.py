# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 16:48:23 2020

@author: Sahil Shaikh
"""


from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
#driver=webdriver.Chrome(r"C:\Users\Sahil Shaikh\Desktop\PY\chromedriver_win32\chromedriver")
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://web.whatsapp.com")
wait=WebDriverWait(driver, 10000000)
target='"Shikha"'
string="."
x_arg='//span[contains(@title, ' + target + ')]'
target=wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
if(wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))):
    print("found")
    target.click()
    input_box=driver.find_element_by_class_name('_1Plpp')
    for i in range(1):
        input_box.send_keys(string+Keys.ENTER)