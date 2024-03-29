from selenium.webdriver.support import expected_conditions as EC
from utils.js_helper import is_in_viewport_script
from data import SCROLL_PAUSE_TIME
from time import sleep


class SeleniumUtils:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def get_element(self, locator):
        """Returns visible element"""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element

    def scroll(self, locator, top_offset=0):
        """Scroll to element by locator"""
        element = self.get_element(locator)
        y = element.location.get('y')
        self.driver.execute_script(f"window.scrollTo(0, {y - top_offset});")
        self.wait.until(lambda d: self.driver.execute_script(is_in_viewport_script, element))

        return element

    def scroll_and_click(self, locator, top_offset=100):
        """Scroll to element by locator using default (100 px) top offset, then click element"""
        element = self.scroll(locator, top_offset)
        element.click()

    def scroll_down(self):
        """Scroll to the page bottom"""
        # Get scroll height
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        while True:
            # Scroll down to bottom
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # Wait to load page
            sleep(SCROLL_PAUSE_TIME * 2)
            # Calculate new scroll height and compare with last scroll height
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
