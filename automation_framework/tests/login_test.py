
import time 
from typeguard import typechecked
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By






driver  = webdriver.Chrome()


# type checking function 

# def typecheck(x):
#     print(f"the type of this variable {type(x)} ")


# typecheck(x)

# type check function ends here 



@typechecked
def login_function(driver:webdriver, url:str ,username:str, password:str) -> None :

    driver.get(url)
    # open the website for 10 mins

    #locate the elements 
    username_field = driver.find_element(By.ID, "email")  # Adjust locator as needed
    password_field = driver.find_element(By.ID, "password")  # Adjust locator as needed
    submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")

    print(type(username_field))
    print (type(password_field))

    # first clear the input fields
    
    #fill the username for the username input field
    

    # wrong credentials scenarios 
    # wrong username and wrong userid 

    #2 wrong username and correct password 
    #3 correct username and wrong password
    # 4  correct username and correct userid 
    username_field.clear()
    username_field.send_keys(username)
    password_field.clear()
    password_field.send_keys(password)

    # sleep for 5 sec 
    time.sleep(5)
    submit_button.click()
    
    time.sleep(10)

    # the driver close the website after 30 second 
    # write your logic here

   




url:str = "http://43.205.73.33/"
username:str  = "admin@ripplr.in" # paste your username here 
password:str  = "M@ver!ck" # paste your password here 

login_function(driver, url, username, password )


           # opens the web application based on the url
    




# login function starts here








# login function ends here 


    

