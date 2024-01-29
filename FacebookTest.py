from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
import os

# Replace with the path to your geckodriver executable
geckodriver_path = '/usr/local/bin/geckodriver'

# Fetching credentials from environment variables
email = os.getenv('FB_EMAIL')
password = os.getenv('FB_PASSWORD')

# Setting up Firefox options for headless mode (uncomment if you're running in an environment without a GUI)
firefox_options = Options()
firefox_options.headless = True

# Create a new instance of the Firefox driver
driver = webdriver.Firefox(options=firefox_options, executable_path=geckodriver_path)

try:
    # Open Facebook login page
    driver.get('https://www.facebook.com/')

    # Find the email and password input fields and enter your login credentials
    email_field = driver.find_element(By.ID, 'email')
    password_field = driver.find_element(By.ID, 'pass')

    email_field.send_keys(email)
    password_field.send_keys(password)

    # Submit the login form
    password_field.send_keys(Keys.RETURN)

    # Using WebDriverWait to wait for the logout button to be visible
    wait = WebDriverWait(driver, 10)
    logout_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@aria-label='Account']")))

    # Verify if login was successful
    if logout_button.is_displayed():
        print("Login successful!")
    else:
        print("Login failed!")

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Close the browser window
    driver.quit()
