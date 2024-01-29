from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

# Set the path to geckodriver (replace with your actual path)
geckodriver_path = '/usr/local/bin/geckodriver'

# Create Firefox options
firefox_options = Options()

# Set the binary location of Firefox
firefox_options.binary_location = '/usr/bin/firefox'  # Update this path as needed

# Create a new instance of the Firefox driver
driver = webdriver.Firefox(executable_path=geckodriver_path, options=firefox_options)

# Open Facebook login page
driver.get('https://www.facebook.com/')

# Find the email and password input fields and enter your login credentials
email_field = driver.find_element('id', 'email')
password_field = driver.find_element('id', 'pass')

email_field.send_keys('your_facebook_email@example.com')
password_field.send_keys('your_facebook_password')

# Submit the login form
password_field.send_keys(Keys.RETURN)

# Wait for a few seconds to allow the login process to complete
time.sleep(5)

# Verify if login was successful by checking for the presence of the logout button
logout_button = driver.find_element('xpath', "//div[@aria-label='Account']")
if logout_button.is_displayed():
    print("Login successful!")
else:
    print("Login failed!")

# Close the browser window
driver.quit()
