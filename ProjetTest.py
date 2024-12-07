from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()

try:

    driver.get("https://www.saucedemo.com/")

    # Test 1: Verify the width and height of the text area
    username_field = driver.find_element(By.ID, "user-name")
    password_field = driver.find_element(By.ID, "password")

    username_dimensions = username_field.size
    password_dimensions = password_field.size

    if username_dimensions and password_dimensions:
        print("Test 1 Passed: Username field dimensions: {username_dimensions}, Password field dimensions: {password_dimensions}")
    else:
        print("Test 1 Failed: Field dimensions are missing or incorrect!")

    #  Test 2: Verify placeholder text visible in the text area
    username_placeholder = username_field.get_attribute("placeholder")
    password_placeholder = password_field.get_attribute("placeholder")

    if username_placeholder == "Username" and password_placeholder == "Password":
        print("Test 2 Passed: Placeholder texts are correct!")
    else:
        print(f"Test 2 Failed: Incorrect placeholders! Username: {username_placeholder}, Password: {password_placeholder}")

    #  Test 3: Verify that the text area should be locked and fixed
    username_resizable = username_field.value_of_css_property("resize")
    password_resizable = password_field.value_of_css_property("resize")

    if username_resizable == "none" and password_resizable == "none":
        print("Test 3 Passed: Text areas are locked and fixed!")
    else:
        print(f"Test 3 Failed: Text areas are resizable! Username: {username_resizable}, Password: {password_resizable}")

    #  Test 4: Verify the button color same as per design
    login_button = driver.find_element(By.ID, "login-button")
    button_color = login_button.value_of_css_property("background-color")

    if button_color == "rgba(226, 35, 26, 1)":
        print("Test 4 Passed: Button color is correct!")
    else:
        print(f"Test 4 Failed: Button color is incorrect! Found: {button_color}")

    #  Test 5: Verify button enabled/clickable or not
    is_button_enabled = login_button.is_enabled()

    if is_button_enabled:
        print("Test 5 Passed: Login button is enabled and clickable!")
    else:
        print("Test 5 Failed: Login button is not enabled!")

    #  Test 6: Verify tooltip added and shown if required
    tooltip = login_button.get_attribute("title")

    if tooltip == "Click to login":
        print("Test 6 Passed: Tooltip is present and correct!")
    else:
        print(f"Test 6 Failed: Tooltip is incorrect or missing! Found: {tooltip}")

    # Test 7: Verify user can log in only with valid credentials
    username_field.clear()
    password_field.clear()
    username_field.send_keys("standard_user")
    password_field.send_keys("secret_sauce")
    login_button.click()

    if "inventory.html" in driver.current_url:
        print("Test 7 Passed: Login successful with valid credentials!")
    else:
        print("Test 7 Failed: Login failed with valid credentials!")

    # Test 8: Verify error message when entering invalid credentials
    driver.get("https://www.saucedemo.com/")  # Reset the page
    username_field = driver.find_element(By.ID, "user-name")
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    username_field.clear()
    password_field.clear()
    username_field.send_keys("invalid_user")
    password_field.send_keys("wrong_password")
    login_button.click()

    error_message = driver.find_element(By.XPATH, "//h3[@data-test='error']").text

    if "Username and password do not match" in error_message:
        print("Test 8 Passed: Error message displayed correctly for invalid credentials!")
    else:
        print(f"Test 8 Failed: Incorrect error message! Found: {error_message}")

    #  Test 9: Verify the button changes color on mouse hover
    actions = ActionChains(driver)
    actions.move_to_element(login_button).perform()
    hover_color = login_button.value_of_css_property("background-color")
    expected_hover_color = "rgba(200, 30, 20, 1)"  # Example color

    if hover_color == expected_hover_color:
        print("Test 9 Passed: Hover color is correct!")
    else:
        print(f"Test 9 Failed: Hover color is incorrect! Found: {hover_color}")

except Exception as e:
    print(f"An error occurred during the tests: {e}")

finally:

    driver.quit()
