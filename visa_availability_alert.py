# !/usr/bin/python3
import getpass
import smtplib
import time
import os
import threading
from selenium import webdriver
from dotenv import load_dotenv, dotenv_values
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options

gmailMsg = "*** APPOINTMENT IS AVAILABLE ***"

print(""" 

                    ██╗   ██╗██╗███████╗ █████╗ ██╗  ██╗███████╗███████╗██████╗ ███████╗██████╗ 
                    ██║   ██║██║██╔════╝██╔══██╗██║ ██╔╝██╔════╝██╔════╝██╔══██╗██╔════╝██╔══██╗
                    ██║   ██║██║███████╗███████║█████╔╝ █████╗  █████╗  ██████╔╝█████╗  ██████╔╝
                    ╚██╗ ██╔╝██║╚════██║██╔══██║██╔═██╗ ██╔══╝  ██╔══╝  ██╔═══╝ ██╔══╝  ██╔══██╗
                     ╚████╔╝ ██║███████║██║  ██║██║  ██╗███████╗███████╗██║     ███████╗██║  ██║
                      ╚═══╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝     ╚══════╝╚═╝  ╚═╝
                                                                                                
                                                ██████╗ ██╗   ██╗                                                           
                                                ██╔══██╗╚██╗ ██╔╝                                                           
                                                ██████╔╝ ╚████╔╝                                                            
                                                ██╔══██╗  ╚██╔╝                                                             
                                                ██████╔╝   ██║                                                              
                                                ╚═════╝    ╚═╝                                                              
                                                                                                
                         ██╗ █████╗ ██╗   ██╗██╗  ██╗██╗   ██╗███╗   ███╗ █████╗ ██████╗        
                         ██║██╔══██╗╚██╗ ██╔╝██║ ██╔╝██║   ██║████╗ ████║██╔══██╗██╔══██╗       
                         ██║███████║ ╚████╔╝ █████╔╝ ██║   ██║██╔████╔██║███████║██████╔╝       
                    ██   ██║██╔══██║  ╚██╔╝  ██╔═██╗ ██║   ██║██║╚██╔╝██║██╔══██║██╔══██╗       
                    ╚█████╔╝██║  ██║   ██║   ██║  ██╗╚██████╔╝██║ ╚═╝ ██║██║  ██║██║  ██║       
                     ╚════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝       
                                                                                                                                                                                                                    

                                    
DISCLAIMER: Please use this tool reasonably and within the law.
""")

print("Please insert your Gmail credentials")


class Browser:
    browser, service = None, None

    def __init__(self, driver: str):
        self.wait = None
        self.available_date = None
        self.service = Service(driver)
        self.browser = webdriver.Chrome(service=self.service)

    def open_page(self, url: str):
        self.browser.get(url)

    # Add the following lines to fill out the form and submit
    def fill_form(self, email: str, password: str):

        # Fill email
        email_elem = self.browser.find_element(By.ID, "user_email")
        email_elem.clear()
        email_elem.send_keys(email)

        # Fill password
        password_elem = self.browser.find_element(By.ID, "user_password")
        password_elem.clear()
        password_elem.send_keys(password)

        # Click on checkbox
        checkbox_elem = self.browser.find_element(By.ID, "policy_confirmed")
        # checkbox_elem.click()

        self.browser.execute_script("arguments[0].click();", checkbox_elem)

        # Submit form
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.NAME, 'commit'))).click()

        # New action to click on "continue" button
        WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "Continue")]'))).click()

        # Reschedule Appointment button
        WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, 'Reschedule Appointment'))).click()

        # Reschedule Appointment button
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "Reschedule '
                                                                                    'Appointment")]'))).click()

        # Reschedule Appointment "Continue" button
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.NAME, 'commit'))).click()

        # # Select the Location
        # location_dropdown = Select(self.browser.find_element(By.ID, "appointments_consulate_appointment_facility_id"))
        # locations = location_dropdown.options
        # print(locations)
        #
        # for location_index in range(5, len(locations)):
        #     # select location
        #     location_dropdown.select_by_index(location_index)
        #     time.sleep(2)

        self.select_location()

    def select_location(self):
        # 1. Select first location from "Consular Section Location"
        location_dropdown = Select(self.browser.find_element(By.ID, "appointments_consulate_appointment_facility_id"))
        locations = location_dropdown.options
        print(locations)

        for location_index in range(5, len(locations)):
            # select location
            location_dropdown.select_by_index(location_index)
            time.sleep(2)

            # 2.  Go to "Date of Appointment"...
            if self.is_date_available:
                current_location = location_dropdown.first_selected_option.text
                print(current_location)
                print(f"Appointment available at {current_location} on {self.available_date}")
                break

    def is_date_available(self):
        # Get the date of appointment input field
        date_element = self.wait.until(EC.element_to_be_clickable((By.ID, 'appointments_consulate_appointment_date')))

        # Open the date picker by clicking on the date field
        date_element.click()

        # Check for the presence of 'href' attribute in date elements. If it exists, date is available.
        date_cells = self.browser.find_elements(By.XPATH, "//td[contains(@class, 'ui-datepicker-day')]")
        for cell in date_cells:
            if cell.get_attribute('href'):
                self.available_date = cell.text
                return True

        return False

    def close_browser(self):
        self.browser.close()


if __name__ == '__main__':
    browser = Browser("./chromedriver.exe")
    browser.open_page("https://ais.usvisa-info.com/en-ca/niv/users/sign_in")
    time.sleep(2)

    load_dotenv()
    email = os.getenv('EMAIL_ENV_VAR')
    password = os.getenv('PASSWORD_ENV_VAR')

    # Assuming we have the correct username and password for login
    email, password = email, password
    browser.fill_form(email, password)
    time.sleep(2)

    # You can add some sort of verification here to check if login was successful
    assert "No results found." not in browser.browser.page_source

    browser.close_browser()
