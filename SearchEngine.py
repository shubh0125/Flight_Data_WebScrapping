import open_browser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class SearchEngine:
    

    
    def using_google(search_query):
        try:
            browser = open_browser.initialize_chrome_driver()
            # browser = webdriver.Chrome()
            browser.get("https://www.google.com")
            # Wait for the search box to be present and then interact with it
            search_box = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.NAME, "q"))
            )

            search_box.send_keys(f"{search_query}" + Keys.RETURN)


            # Wait for the search results to load and display the first link
            first_link = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div.yuRUbf a"))
            )

            # Extract the URL of the first search result
            # first_link_url = first_link.get_attribute("href")
            # print("First link:", first_link_url)

            # Click on the first link
            first_link.click()

            # Wait for the new page to load completely (you can adjust the condition based on the target page's content)
            WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )

        except Exception as e:
            print("An error occurred:", e)



    def using_bing(search_query):
        # Initialize the Chrome driver
        browser = open_browser.initialize_chrome_driver()
        try:
            # Navigate to Bing
            browser.get("https://www.bing.com/")

            # Wait for the search box to be present and enter the search query
            search_box = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.ID, "sb_form_q"))
            )
            search_box.send_keys(search_query + Keys.RETURN)

            # Wait for the first search result to be present
            first_link = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "ol#b_results li.b_algo h2 a"))
            )

            # Click the first search result
            first_link.click()

            # Wait for the page to load by waiting for the body tag to be present
            WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
            return browser

        except TimeoutException:
            print("Timeout occurred while waiting for an element.")
        except NoSuchElementException:
            print("An element was not found.")
        # finally: