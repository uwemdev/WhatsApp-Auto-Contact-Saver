from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time

# Set up WebDriver and log in to WhatsApp Web
driver = webdriver.Chrome(executable_path='path/to/chromedriver')
driver.get('https://web.whatsapp.com')

# Wait for manual QR code scan
input("Please scan the QR code on WhatsApp Web and press Enter")

# Wait until chats are loaded
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'pane-side')))

# Function to save contact
def save_contact(contact_name, phone_number):
    with open('contacts.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([contact_name, phone_number])
    print(f"Saved contact: {contact_name} - {phone_number}")

# Function to check if contact is already saved
def is_contact_saved(phone_number):
    try:
        with open('contacts.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if phone_number in row:
                    return True
    except FileNotFoundError:
        return False
    return False

# Continuously monitor new messages
try:
    while True:
        # Find all chats in the chat list
        chat_list = driver.find_element_by_id('pane-side')
        chats = chat_list.find_elements_by_class_name('_2aBzC')

        for chat in chats:
            contact_name = chat.find_element_by_class_name('_3Tw1q').text
            chat.click()
            
            # Extract phone number
            try:
                phone_number = driver.find_element_by_xpath('//header//span[@dir="auto"]').text
            except:
                phone_number = None

            if phone_number and not is_contact_saved(phone_number):
                save_contact(contact_name, phone_number)

            time.sleep(1)

        time.sleep(5)  # Wait before checking for new messages again

except KeyboardInterrupt:
    print("Exiting...")

finally:
    driver.quit()
