from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from utils.selenium_utils import SeleniumUtils


class TestHelper(SeleniumUtils):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)

    def wait_home_page_to_load(self):
        # Wait for homepage header to be displayed after animation disappears
        self.get_element((By.CSS_SELECTOR, "div[class^='Navbar_container']"))
        # Wait for 4 iframes to be present (Tweeter iframes)
        self.wait.until(lambda d: len(self.driver.find_elements(By.TAG_NAME, 'iframe')) >= 4)
