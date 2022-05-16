import unittest
import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.selenium_utils import SeleniumUtils
from data import WINDOW_WIDTH, WINDOW_HEIGHT, TIMEOUT

class TestHomePage(unittest.TestCase):
    BASE_URL = 'https://www.genadrop.com/'
    MINT_URL = f'{BASE_URL}mint'
    LOGO_DESKTOP_SVG_URL = f'{BASE_URL}static/media/genadrop-logo.e0e23971.svg'
    LOGO_DROP_SVG_URL = f'{BASE_URL}static/media/drop.495aca87.svg'
    NEAR_FOUNDATION_URL = "https://near.foundation/"
    NEAR_FOUNDATION_TAB_TITLE = "NEAR Foundation"
    NEAR_FOUNDATION_PAGE_TITLE = "NEAR Foundation"
    MINORITY_PROGRAMMERS_URL = 'https://www.minorityprogrammers.com/'
    MINORITY_PROGRAMMERS_TAB_TITLE = 'MPA | Home'
    MPA_LINKEDIN_URL = 'https://linkedin.com/company/minority-programmers/'
    LOGO_HEIGHT = 47
    LOGO_WIDTH = 64
    LOGO_X = 32
    LOGO_Y = 8
    DELTA = 3
    MINT_TAB_TITLE = 'GenaDrop: No-Code Generative NFT creator, minter, & marketplace'
    MINT_PAGE_TITLE = 'Mint Your NFTs'
    HTTP_OK = 200

    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.sl = SeleniumUtils(self.driver)
        self.wait = WebDriverWait(self.driver, TIMEOUT)
        self.driver.set_window_size(WINDOW_WIDTH, WINDOW_HEIGHT)
        self.driver.get(self.BASE_URL)
        # Wait for homepage header to be displayed after animation disappears
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class^='Navbar_container']")))

    def tearDown(self):
        self.driver.quit()

    def test_desktop_header_logo(self):
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

    def test_header_mint_button(self):
        """Test Case ID: GD_HP002"""

        header_mint_button = self.driver.find_element(By.CSS_SELECTOR, "a[href='/mint'] li")
        header_mint_button.click()

        # Verify url
        actual_url = self.driver.current_url
        assert actual_url == self.MINT_URL, \
            f"Wrong redirection upon clicking 'Mint' button, actual url: '{actual_url}', expected url: '{self.MINT_URL}'"

        # Verify tab title
        actual_tab_title = self.driver.title
        assert actual_tab_title == self.MINT_TAB_TITLE, \
            f"Unexpected tab title for Mint page, actual: '{actual_tab_title}', expected: '{self.MINT_TAB_TITLE}'"

    def test_near_foundation_link(self):
        """ TC id: GD_HP008 """

        # Click NEAR Foundation image
        loc_near_foundation_image = (By.XPATH, "//img[@class='Orgs_org__2zmxJ'][2]")
        self.sl.scroll_and_click(loc_near_foundation_image)
        # Switch to new tab
        window_name = self.driver.window_handles[-1]
        self.driver.switch_to.window(window_name=window_name)

        actual_url = self.driver.current_url
        assert actual_url == self.NEAR_FOUNDATION_URL, \
            f"Wrong redirection upon clicking 'Near Foundation Link' button, actual url: '{actual_url}'" \
            f", expected url: '{self.NEAR_FOUNDATION_URL}' "

        # Verify tab title
        actual_title = self.driver.title
        assert actual_title == self.NEAR_FOUNDATION_TAB_TITLE, \
            f"Unexpected tab title for Mint page, actual: '{actual_title}'," \
            f"expected: '{self.NEAR_FOUNDATION_TAB_TITLE}'"

        # Verify page main area title
        actual_page_title = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//span[@class='sr-only']"))).text
        assert actual_page_title == self.NEAR_FOUNDATION_PAGE_TITLE, \
            f"Unexpected page title on Mint page, actual: '{actual_page_title}'," \
            f"expected: '{self.NEAR_FOUNDATION_PAGE_TITLE}'"

    def test_minority_programmers_link(self):
        """ TC id: GD_HP010 """
        element_mp = (By.XPATH, "//img[@class='Orgs_org__2zmxJ'][4]")
        self.sl.scroll_and_click(element_mp)

         # Switching windows
        tabs = self.driver.window_handles
        self.assertEqual(len(tabs), 2, f'Actual number of tabs: {len(tabs)}, expected 2 tabs.')
        self.assertEqual(self.driver.current_url, self.BASE_URL)
        self.driver.switch_to.window(tabs[1])
        actual_minority_programmers_url = self.driver.current_url
        assert actual_minority_programmers_url == self.MINORITY_PROGRAMMERS_URL, \
            f"Wrong redirection upon clicking 'Minority Programmers Link' button, actual url: '{actual_minority_programmers_url}'," \
            f", expected url: '{self.MINORITY_PROGRAMMERS_URL}' "

        # Verify tab title
        title = self.driver.title
        assert title == self.MINORITY_PROGRAMMERS_TAB_TITLE, \
            f"Unexpected title for Mint page, actual: '{title}'," \
            f"expected: '{self.MINORITY_PROGRAMMERS_TAB_TITLE}'"

    def test_footer_linkedIn_link(self):
        """Test Case ID: GD_HP028"""

        self.sl.scroll_down()
        loc_linkedin_icon_link = By.CSS_SELECTOR, f"div[class^=footer_social] > a[href='{self.MPA_LINKEDIN_URL}']"
        self.sl.get_element(loc_linkedin_icon_link).click()

        # Verify new tab opened
        tabs = self.driver.window_handles
        self.assertEqual(len(tabs), 2, f'Actual number of tabs: {len(tabs)}, expected 2 tabs.')

        # Verify urls for both tabs
        self.assertEqual(self.driver.current_url, self.BASE_URL)
        self.driver.switch_to.window(tabs[1])
        self.wait.until(lambda d: self.driver.current_url.startswith('https://www.linkedin.com/'))


if __name__ == '__main__':
    unittest.main()
