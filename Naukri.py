#!/usr/bin/env python
# coding: utf-8

# In[71]:


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC


# In[72]:


# --- Launch with options (e.g., incognito, headless) ---
options = Options()
# options.add_argument("--incognito")  # Example: launch in incognito mode
# options.add_argument("--headless") # Example: launch in headless mode (no visible browser UI)


# In[138]:


driver = webdriver.Chrome(options=options)


# In[ ]:





# In[ ]:





# In[ ]:





# In[139]:


driver.get("https://www.naukri.com/nlogin/login")
driver.maximize_window() 
time.sleep(60)


# In[140]:


# usernameField = driver.find_element(By.ID, "d78918361@gmail.com")
# passwordField = driver.find_element(By.ID, "passwordField")


# In[141]:


# LOGIN
# usernameField.send_keys("Your_Email")
# passwordField.send_keys('Your_Password')
# passwordField.submit()


# In[142]:


driver.get("https://www.naukri.com/mnjuser/recommendedjobs")


# In[144]:


Profile = driver.find_element(By.ID, "profile")


# In[145]:





# In[146]:


job_links = driver.find_elements(By.XPATH, './/article[contains(@class, "jobTuple")]')
for job in range(int(Profile.text[Profile.text.find('(')+1:Profile.text.find(')')])):
    # open new tab
    # driver.switch_to.new_window(WindowTypes.TAB)
    print(driver.title)
    all_tabs = driver.window_handles
    job_links[job].click()
    for e in driver.window_handles:
        if e not in all_tabs:
            driver.switch_to.window(e)
            break
    # driver.switch_to.window(driver.window_handles[1])
    print(driver.title)
    time.sleep(2)
    try:
        # find button by id 'Apply'
        apply = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[text()='Apply']"))
        )
        time.sleep(2)
        # click()
    except Exception as apply_find_error:
        print("apply_find_error", apply_find_error)
    # if  form opens, 'continue'
    try:
        apply.click()
        time.sleep(2)
        try:
            driver.find_element(By.CLASS_NAME, "chatbot_DrawerContentWrapper") # Or By.NAME, By.CLASS_NAME, By.XPATH, etc.
            print("Form is present on the page.")
        except NoSuchElementException:            
            # print("Form is not present on the page.")
            print(driver.title)
            driver.close()
    except Exception as apply_click_error:
        print("apply_click_error", apply_click_error)
        # switch back to original tab

    driver.switch_to.window(driver.window_handles[0])
    print(driver.title)
    # if form not opens, close tab



# In[ ]:





# In[ ]:





# In[ ]:





# In[116]:


driver.quit()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




