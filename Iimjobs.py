#!/usr/bin/env python
# coding: utf-8

# In[486]:


# import selenium


# In[8]:


from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# In[49]:


from selenium.webdriver.common.by import By


# In[435]:


from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.window import WindowTypes
import time


# In[500]:


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# In[10]:


# --- Basic launch ---
# driver = webdriver.Chrome() 


# In[11]:


# --- Launch with options (e.g., incognito, headless) ---
# options = Options()
# options.add_argument("--incognito")  # Example: launch in incognito mode
# options.add_argument("--headless") # Example: launch in headless mode (no visible browser UI)


# In[487]:


# driver = webdriver.Chrome(options=options)


# In[501]:


driver = webdriver.Chrome()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[502]:


driver.get("https://www.iimjobs.com")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[503]:


driver.maximize_window() 
time.sleep(2)


# In[ ]:





# In[504]:


element_by_id = driver.find_element(By.ID, "email-input")


# In[505]:


element_by_id.click()


# In[506]:


element_by_id.send_keys("Your_Email")


# In[ ]:





# In[507]:


element_by_id_password = driver.find_element(By.ID, "password-input")


# In[508]:


element_by_id_password.send_keys("Your_Password")


# In[509]:


element_by_id_password.submit()    


# In[510]:


# time.sleep(2)


# In[511]:


driver.get("https://www.iimjobs.com/recommended-jobs")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[47]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[498]:


# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager

# ----------------- 1. Setup and Navigation -----------------
# Ensure you have the Chrome driver installed or use webdriver_manager
# to handle it automatically.

# Use ChromeDriverManager to automatically handle driver installation
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# driver.get("https://www.iimjobs.com/")
# driver.maximize_window() 
# time.sleep(3) # Initial wait for the page to load completely

# ----------------- 2. Scrolling Loop Function -----------------

def scroll_to_end_and_load(driver, scroll_pause_time=2, max_loads=100):
    """Scrolls to the bottom of the page repeatedly until no new content loads."""

    print("Starting infinite scroll to load all job listings...")

    # Get initial scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")
    counter = 0
    while True:
        # Scroll down to the bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait for new page content/jobs to load (crucial step)
        time.sleep(scroll_pause_time)

        # Calculate new scroll height and compare with the last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:
            # If heights are the same, we've reached the true bottom
            print("Scroll complete. No new content loaded.")
            break

        if counter == max_loads:
            print("Max scroll complete. Stopping load.")
            break

        counter += 1

        last_height = new_height

# ----------------- 3. Scraping Function -----------------

def scrape_jobs(driver):
    """Scrapes the content from the fully loaded page."""

    job_data = []

    try:
        # Find all individual job listing elements
        # *** REPLACE '.job-listing-container' with the actual selector for one job block ***
        # page_html = driver.page_source
        # return page_html
        # job_listings = driver.find_elements(By.CSS_SELECTOR, '.job-listing-container') 
        # job_listings = driver.find_elements(By.CLASS_NAME, 'joblist-card-v2')
        job_links = driver.find_elements(By.XPATH, './/a[contains(@href, "/j/")]')
        # print(job_links)
        # test = job_links

        for job in job_links:
            try:
                # *** REPLACE these selectors with the actual ones for title and company ***
                title = job.text
                url = job.get_attribute('href')

                job_data.append({
                    "title": title,
                    # "company": company,
                    "url": url
                })
            except Exception as e:
                # Handle cases where a specific element might be missing in a job card
                print(f"Error scraping a job card: {e}")
                continue # Skip this card and move to the next one

        print(f"Scraping complete. Found {len(job_data)} job listings.")
        return job_data

    except Exception as e:
        print(f"An error occurred during scraping: {e}")
        return []

# ----------------- 4. Main Execution -----------------



# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[512]:


if __name__ == "__main__":

    # 1. Scroll to the end, wait, and load all content
    scroll_to_end_and_load(driver, scroll_pause_time=2.5) # Use 1.5s pause for faster loading

    # 2. Scrape the fully loaded page
    final_data = scrape_jobs(driver)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


for job in final_data:
    try:
        print(job['title'])
        driver.get(job['url'])
        # time.sleep(10)
        try:
            # Wait until the element is visible and clickable
            button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[text()='Apply']"))
            )
            # button = driver.find_element(By.CLASS_NAME, "MuiButtonBase-root") (By.XPATH, "//button[text()='Submit']")
            # <selenium.webdriver.remote.webelement.WebElement (session="7ea56abd1a50c7cc5dfa8262ac9d8c67", element="f.EB2B570E52AA10B1D576789214937DC2.d.0234C8F8A37F37513F6327ADFF1D6D5A.e.1344")>
            time.sleep(1)
            # print(button)
            # driver.execute_script("arguments[0].scrollIntoView(true);",button)
            # time.sleep(1)
            try:
                button.click()
                print("Apply clicked")
                time.sleep(3)
                try:
                    rev_sub = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[text()='Review & Submit']"))
            )
                    # time.sleep(3)
                    try:
                        rev_sub.click()
                        print("rev_sub clicked")
                        time.sleep(3)
                    except Exception as error:
                        print('rev_sub click error', error)

                except Exception as errr:
                    # open new tab, & switch focus
                    print("rev_sub_find_exception", errr)

                    try:
                        # Open a new tab and switch to it
                        driver.switch_to.new_window(WindowTypes.TAB)
                        # driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + 't')
                        # Get all window handles
                        # window_handles = driver.window_handles
                        # Get the window handle of the current window
                        # current_window_handle = driver.current_window_handle
                        # print("current_window_handle: ", current_window_handle)
                        # Switch to the new tab (usually the last one in the list)
                        # driver.switch_to.window(int(current_window_handle)-1)
                    except Exception as window_handle_error:
                        print("window_handle_error: ",window_handle_error)
                    # Now you can interact with the elements in the new tab
                    # print("New tab title:", driver.title)
            except Exception as err:
                print("error-apply click", err)
        except Exception as er:
            print("Apply find Exception", er)
        # break
    except Exception as e:
        print(job["url"],"error", e)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[392]:


driver.quit()


# In[ ]:





# In[ ]:





# In[ ]:




