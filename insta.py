from selenium.webdriver import Edge
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import Edge, EdgeOptions
from selenium.webdriver.common.by import By
import time

# Replace the path with the location of your Edge WebDriver executable
options = EdgeOptions()
options.use_chromium = True
driver = Edge(executable_path='C:/Users/mthas/OneDrive/Desktop/python/project for upwork/insta/edgedriver_win64/msedgedriver.exe', options=options)

# Login to Instagram
driver.get('https://www.instagram.com/accounts/login/')
# Wait for the page to load
time.sleep(2)

# Enter your username and password
username_input = driver.find_element(By.NAME, 'username')
username_input.send_keys('your username')

password_input = driver.find_element(By.NAME,'password')
password_input.send_keys('your password')

# Submit the login form
password_input.submit()
time.sleep(2)

# Load the list of Instagram profile URLs and loop through them
with open('insta/profile_list.txt', 'r') as f:
    profile_list = f.read().splitlines()

for profile_url in profile_list:
    driver.get(profile_url + 'following/')
    time.sleep(2)
    following_list = driver.find_elements(By.XPATH, '//div[@role="dialog"]//a')
    following_usernames = [following.get_attribute('href') for following in following_list]
    if 'https://www.instagram.com/your_username' in following_usernames:
        print(f'{profile_url} is following you back!')
    else:
        print(f'{profile_url} is not following you back.')
    time.sleep(10) # Wait for 10 seconds before visiting the next profile

# Close the WebDriver when you're done
driver.quit()