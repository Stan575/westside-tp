import unittest

import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class TestLogo(unittest.TestCase):
    NEAR_FOUNDATION_URL = "https://near.foundation/"
    NEAR_FOUNDATION_TAB_TITLE = "NEAR Foundation"
    NEAR_FOUNDATION_PAGE_TITLE = "NEAR Foundation"
    URL = 'https://www.genadrop.com/'
    LOGO_HEIGHT = 47
    LOGO_WIDTH = 64
    LOGO_X = 32
    LOGO_Y = 8
    DELTA = 3
    LOGO_DESKTOP_SVG_URL = f'{URL}static/media/genadrop-logo.e0e23971.svg'
    LOGO_DROP_SVG_URL = f'{URL}static/media/drop.495aca87.svg'
    HTTP_OK = 200

    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.wait = WebDriverWait(self.driver, 5)
        self.driver.set_window_size(1600, 1050)
        self.driver.get(self.URL)

    def tearDown(self):
        self.driver.quit()

    def test_desktop_header_logo(self):
        # Wait for homepage header to be displayed
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class^='Navbar_container']")))

        # Verify header logo div is displayed
        logo_div_element = self.driver.find_element(By.CSS_SELECTOR, "div[class^='Navbar_logoContainer']")
        self.assertTrue(logo_div_element.is_displayed(), 'Header logo div is not displayed.')

        # Verify urls for logo images
        logo_desktop = self.driver.find_element(By.CSS_SELECTOR, "img[class^='Navbar_logoDesktop']")
        self.assertEqual(logo_desktop.get_attribute('src'), self.LOGO_DESKTOP_SVG_URL,
                         'Incorrect desktop logo svg url.')
        logo_drop = self.driver.find_element(By.CSS_SELECTOR, "img[class^='Navbar_drop']")
        self.assertEqual(logo_drop.get_attribute('src'), self.LOGO_DROP_SVG_URL, 'Incorrect drop logo svg url.')

        # Verify image resources exist
        self.assertEqual(requests.head(self.LOGO_DESKTOP_SVG_URL).status_code, self.HTTP_OK,
                         f'Desktop logo svg file is not available, url: {self.LOGO_DESKTOP_SVG_URL}')
        self.assertEqual(requests.head(self.LOGO_DROP_SVG_URL).status_code, self.HTTP_OK,
                         f'Drop logo svg file is not available, url: {self.LOGO_DROP_SVG_URL}')

        # Get header logo size and location data
        logo_rectangle = logo_div_element.rect
        actual_logo_height = logo_rectangle.get('height')
        actual_logo_width = logo_rectangle.get('width')
        actual_logo_location_x = logo_rectangle.get('x')
        actual_logo_location_y = logo_rectangle.get('y')

        # Verify size of header logo
        self.assertAlmostEqual(actual_logo_height, self.LOGO_HEIGHT, delta=self.DELTA,
                               msg=f'Header logo actual height: {actual_logo_height}, expected: {self.LOGO_HEIGHT}')
        self.assertAlmostEqual(actual_logo_width, self.LOGO_WIDTH, delta=self.DELTA,
                               msg=f'Header logo actual width: {actual_logo_width}, expected: {self.LOGO_WIDTH}')

        # Verify location of header logo
        self.assertAlmostEqual(actual_logo_location_x, self.LOGO_X, delta=self.DELTA,
                               msg=f'Header logo actual location x: {actual_logo_location_x}, expected: {self.LOGO_X}')
        self.assertAlmostEqual(actual_logo_location_y, self.LOGO_Y, delta=self.DELTA,
                               msg=f'Header logo actual location y: {actual_logo_location_y}, expected: {self.LOGO_Y}')

    def test_near_foundation_link(self):
        """ TC id: GD_HP008 """
        near_foundation_link = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//img[@class='Orgs_org__2zmxJ'][2]")))
        near_foundation_link.click()
        window_name = self.driver.window_handles[-1]
        self.driver.switch_to.window(window_name=window_name)
        actual_near_foundation_url = self.driver.current_url
        assert actual_near_foundation_url == self.NEAR_FOUNDATION_URL, \
            f"Wrong redirection upon clicking 'Near Foundation Link' button, actual url: '{actual_near_foundation_url}'" \
            f", expected url: '{self.NEAR_FOUNDATION_URL}' "

        # Verify tab title
        actual_near_foundation_title = self.driver.title
        assert actual_near_foundation_title == self.NEAR_FOUNDATION_TAB_TITLE, \
            f"Unexpected tab title for Mint page, actual: '{actual_near_foundation_title}'," \
            f"expected: '{self.NEAR_FOUNDATION_TAB_TITLE}'"

        # Verify page main area title
        actual_page_title = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//span[@class='sr-only']"))).text
        assert actual_page_title == self.NEAR_FOUNDATION_PAGE_TITLE, \
            f"Unexpected page title on Mint page, actual: '{actual_page_title}'," \
            f"expected: '{self.NEAR_FOUNDATION_PAGE_TITLE}' "


if __name__ == '__main__':
    unittest.main()
