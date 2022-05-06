import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests


class TestLogo(unittest.TestCase):
    URL = 'https://www.genadrop.com/'
    LOGO_HEIGHT = 47
    LOGO_WIDTH = 64
    LOGO_X = 32
    LOGO_Y = 8
    DELTA = 3
    LOGO_DESKTOP_SVG = f'{URL}static/media/genadrop-logo.e0e23971.svg'
    LOGO_DROP_SVG = f'{URL}static/media/drop.495aca87.svg'

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
        logo_div_element = self.driver.find_element(By.CLASS_NAME, "Navbar_logoContainer__1NhKc")
        self.assertTrue(logo_div_element.is_displayed(), 'Header logo div is not displayed.')

        # Verify urls for logo images
        logo_desktop = self.driver.find_element(By.CSS_SELECTOR, "img[class^='Navbar_logoDesktop']")
        self.assertEqual(logo_desktop.get_attribute('src'), self.LOGO_DESKTOP_SVG, 'Incorrect desktop logo svg url.')
        logo_drop = self.driver.find_element(By.CSS_SELECTOR, "img[class^='Navbar_drop']")
        self.assertEqual(logo_drop.get_attribute('src'), self.LOGO_DROP_SVG, 'Incorrect drop logo svg url.')

        # Verify image resources exist
        self.assertEqual(requests.head(self.LOGO_DESKTOP_SVG).status_code, 200,
                         f'Desktop logo svg file is not available, url: {self.LOGO_DESKTOP_SVG}')
        self.assertEqual(requests.head(self.LOGO_DROP_SVG).status_code, 200,
                         f'Drop logo svg file is not available, url: {self.LOGO_DROP_SVG}')

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


if __name__ == '__main__':
    unittest.main()
