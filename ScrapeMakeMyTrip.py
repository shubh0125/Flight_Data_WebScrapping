
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

class ScrapeMakeMyTrip():

    def input_from_destination_box(from_destination, browser):
        travelling_from_input_box = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.ID, "fromCity"))
            )
        travelling_from_input_box.send_keys(f"{from_destination}")
        sleep(2)
        select_travelling_from_airpot = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.ID, "react-autowhatever-1-section-0-item-0"))
            )
        select_travelling_from_airpot.click()


    def input_to_destination_box(to_destination, browser):
        travelling_to_input_box = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.ID, "toCity"))
            )
        travelling_to_input_box.send_keys(f"{to_destination}")
        sleep(2)
        select_travelling_to_airpot = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.ID, "react-autowhatever-1-section-0-item-0"))
            )
        select_travelling_to_airpot.click()

    
    def click_at_position(x, y, browser):
        # Wait for the body element to ensure the page is fully loaded
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

        # Use ActionChains to move to the specified coordinates and click
        actions = ActionChains(browser)
        actions.move_by_offset(x, y).click().perform()

        print(f"Clicked at position ({x}, {y}) on the screen.")


    def click_search(browser, element):
        try:
            # Wait for the button to be present and click it
            button = WebDriverWait(browser, 10).until(
                
                EC.presence_of_element_located((By.CSS_SELECTOR, element))
            )
            button.click()
        except Exception as e:
            print(f"An error occurred: {e}")


        
    def extract_flight_details(driver):
        try:

            # Wait for the flight listings to be present
            flights = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "listingCard"))
            )

            flight_details = []
            aa=0
            for flight in flights:
                try:
                    aa=aa+1
                    airline_name = flight.find_element(By.CSS_SELECTOR, ".airlineName").text
                    flight_code = flight.find_element(By.CSS_SELECTOR, ".fliCode").text

                    # Extract departure and arrival details
                    departure_time = flight.find_element(By.CSS_SELECTOR, ".timeInfoLeft .flightTimeInfo span").text
                    departure_airport = flight.find_element(By.CSS_SELECTOR, ".timeInfoLeft font").text
                    arrival_time = flight.find_element(By.CSS_SELECTOR, ".timeInfoRight .flightTimeInfo span").text
                    arrival_airport = flight.find_element(By.CSS_SELECTOR, ".timeInfoRight font").text

                    # Extract price
                    price = flight.find_element(By.CSS_SELECTOR, ".clusterViewPrice").text

                    flight_details.append({
                        "airline_name": airline_name,
                        "flight_code": flight_code,
                        "departure_time": departure_time,
                        "departure_airport": departure_airport,
                        "arrival_time": arrival_time,
                        "arrival_airport": arrival_airport,
                        "price": price
                    })
                    print(aa)
                except Exception as e:
                    print(f"An error occurred while extracting flight details: {e}")

            return flight_details

        except Exception as e:
            print(f"An error occurred: {e}")
            return []
