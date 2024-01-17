#!/usr/bin/env python
# coding: utf-8

# In[5]:


from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
import time
chrome_service = ChromeService(r"C:\Users\shais\OneDrive\Desktop\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_service)
driver.maximize_window()
driver.get("https://jqueryui.com/droppable/")
time.sleep(5)
from selenium.webdriver.common.by import By
driver.switch_to.frame(0)
s1=driver.find_element(By.ID,"draggable")
d1=driver.find_element(By.ID,"droppable")
time.sleep(3)
from selenium.webdriver.common.action_chains import ActionChains
actions = ActionChains(driver)
time.sleep(5)
actions. drag_and_drop(s1,d1)
actions. perform()
time. sleep(5)


# In[ ]:




