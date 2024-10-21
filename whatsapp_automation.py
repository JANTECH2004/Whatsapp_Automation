import time
import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

# Load Excel file using openpyxl
workbook = openpyxl.load_workbook('contacts.xlsx')
sheet = workbook.active  # Assuming data is in the active sheet

# Initialize WebDriver
driver = webdriver.Chrome()  # or webdriver.Firefox() for Firefox
driver.get('https://web.whatsapp.com/')

# Wait for QR code scan
input("Scan QR code and press Enter...")

# Explicit wait setup
wait = WebDriverWait(driver, 10)

# Loop through each contact
for row in sheet.iter_rows(min_row=2, values_only=True):  # Skip header row
    contact_number = row[0]  # First column contains the phone numbers

    try:
        # Search for the contact
        search_box = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"]')))
        search_box.clear()
        search_box.send_keys(contact_number)
        search_box.send_keys(Keys.ENTER)
        time.sleep(2)  # Wait for contact to load

        # Send message
        message = "Hello! This is an automated message."
        message_box = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true" and @data-tab="10"]')))
        message_box.clear()
        message_box.send_keys(message)
        message_box.send_keys(Keys.ENTER)

        time.sleep(1)  # Wait before sending the next message

    except (NoSuchElementException, TimeoutException) as e:
        print(f"Error: Could not send message to {contact_number}")
        continue

# Close the WebDriver
driver.quit()
