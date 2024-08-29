import time
from random import randint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

import strings
import elements

def main():
    # Set up Chrome options to connect to an existing Chrome session
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

    # Initialize Chrome WebDriver with the options
    driver = webdriver.Chrome(options=chrome_options)

    # Open a new tab and navigate to the iHerb review page
    driver.execute_script("window.open('https://il.iherb.com/ugc/myaccount/review', '_blank');")
    driver.switch_to.window(driver.window_handles[-1])

    # Check if the correct web page is opened
    if not check_url(driver):
        print("[ERROR] Bad webpage opened (you are not in 'ugc/myaccount/review')")
        return

    while True:
        # Wait for 10 seconds before looking for the review title
        time.sleep(10)

        # Fill the title review
        if not fill_title(driver):
            break

        # Get the required themes
        required_themes = get_required_themes(driver)
        if required_themes is None:
            break

        # Build and fill the review text
        review_text = build_review_text(required_themes)
        if not fill_review(driver, review_text):
            break

        # Rate the product with 5 stars
        if not rate_product(driver, 5):
            break

        # Submit the review form
        if not click_submit(driver):
            break

        print("\n[SUCCESS] Finished one review")

        # Check if there are more review titles to process
        if not has_more_reviews(driver):
            break

    print("\n[SUCCESS] Finished all reviews")

def check_url(driver):
    return "ugc/myaccount/review" in driver.current_url

def fill_title(driver):
    try:
        title = driver.find_element(By.ID, elements.TITLE)
        title.clear()
        title.send_keys(strings.DEFAULT_TITLE[randint(0, len(strings.DEFAULT_TITLE) - 1)])
        return True
    except Exception as e:
        print(f"[ERROR] Can't find title: {e}")
        # Debugging: Print the page source or take a screenshot
        with open("page_source.html", "w", encoding="utf-8") as f:
            f.write(driver.page_source)
        driver.save_screenshot("screenshot.png")
        return False

def get_required_themes(driver):
    try:
        ul_element = driver.find_element(By.CLASS_NAME, elements.THEMES)
        list_items = ul_element.find_elements(By.TAG_NAME, "li")
        return [li.text for li in list_items]
    except Exception as e:
        print(f"[ERROR] Can't find required themes list: {e}")
        return None

def build_review_text(required_themes):
    review_text = ""
    for theme in required_themes:
        if theme in strings.THEME_STRINGS:
            review_text += (strings.THEME_STRINGS[theme] + strings.THEME_STRING_SEPARATOR)
    review_text += f"\n{strings.FINAL_STRING[randint(0, len(strings.FINAL_STRING) - 1)]}"
    return review_text

def fill_review(driver, review_text):
    try:
        review = driver.find_element(By.ID, elements.REVIEW)
        review.clear()
        review.send_keys(review_text)
        return True
    except Exception as e:
        print(f"[ERROR] Can't find review text box: {e}")
        return False

def click_submit(driver):
    try:
        send_button = driver.find_element(By.CLASS_NAME, elements.SEND_BUTTON)
        send_button.click()
        return True
    except Exception as e:
        print(f"[ERROR] Can't find 'submit' button: {e}")
        return False

def fill_search_input(driver, search_text):
    try:
        search_input = driver.find_element(By.CLASS_NAME, elements.SEARCH_INPUT)
        search_input.clear()
        search_input.send_keys(search_text)
        return True
    except Exception as e:
        print(f"[ERROR] Can't find search input: {e}")
        return False

def click_product_link(driver, product_name):
    try:
        product_link = driver.find_element(By.CLASS_NAME, elements.PRODUCT_LINK)
        product_link.click()
        return True
    except Exception as e:
        print(f"[ERROR] Can't find product link: {e}")
        return False

def rate_product(driver, rating_value):
    try:
        rating_input = driver.find_element(By.CSS_SELECTOR, f'input[name="ratingValue"][value="{rating_value}"]')
        driver.execute_script("arguments[0].click();", rating_input)
        return True
    except Exception as e:
        print(f"[ERROR] Can't find rating input: {e}")
        return False

def has_more_reviews(driver):
    try:
        # Check if there are more review titles to process
        driver.find_element(By.ID, elements.TITLE)
        return True
    except Exception:
        return False

if __name__ == '__main__':
    main()
