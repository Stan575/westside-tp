import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import TIMEOUT, WINDOW_WIDTH, WINDOW_HEIGHT
from utils.selenium_utils import SeleniumUtils
from utils.test_helper import TestHelper


class TestGenaDropHomePage(unittest.TestCase):
    HOME_PAGE_URL = 'https://www.genadrop.com/'
    DOCS_URL = 'https://www.genadrop.com/docs'
    READ_THE_DOCS_TAB_TITLE = 'GenaDrop: No-Code Generative NFT creator, minter, & marketplace'
    EXPECTED_ANSWER = '''To promote the decentralized stack, we do not have a backend to store assets. \
Rather this is handled on the client-side. We only save contract references for things like \
collections on Algorand onto a database to build the marketplace with an Ethereum familiar UI.'''

    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.wait = WebDriverWait(self.driver, TIMEOUT)
        self.sl = SeleniumUtils(self.driver, self.wait)
        self.test_helper = TestHelper(self.driver, self.wait)
        self.driver.set_window_size(WINDOW_WIDTH, WINDOW_HEIGHT)
        self.driver.get(self.HOME_PAGE_URL)
        self.test_helper.wait_home_page_to_load()

    def tearDown(self) -> None:
        self.driver.quit()

    def test_read_the_docs_btn(self):
        """Test Case ID GD_HP011"""
        # Verify the read the docs btn is displayed
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@href="/docs"]')))
        read_docs_btn = self.driver.find_element(By.XPATH, '//a[@href="/docs"]')
        self.assertTrue(read_docs_btn.is_displayed(), "Read the docs button is not displayed")

        # Verify that the read the docs btn redirects the user to https://www.genadrop.com/docs
        docs_button_locator = (By.CSS_SELECTOR, 'button > span')
        self.wait.until(EC.visibility_of_element_located(docs_button_locator))
        self.sl.scroll_and_click(docs_button_locator)
        self.wait.until(lambda d: self.driver.current_url == 'https://www.genadrop.com/docs')

        # Verify the docs url
        actual_read_docs_url = self.driver.current_url
        assert self.DOCS_URL == actual_read_docs_url, \
            f"Wrong URL! actual URL: '{actual_read_docs_url},' expected to be: '{self.DOCS_URL}'"

        # Verify the read the docs tab title
        actual_read_docs_title = self.driver.title
        assert actual_read_docs_title == self.READ_THE_DOCS_TAB_TITLE, \
            f"Wrong title. Actual title: '{actual_read_docs_title}' expected to be: '{self.READ_THE_DOCS_TAB_TITLE}'"

    def test_q_and_a_section(self):
        """Test Case ID GD_HP024"""
        q_genadrop_save_my_assets = (By.XPATH, "//p[text()='Does GenaDrop save my assets?']")

        # Scroll to the element and click on it
        self.sl.scroll_and_click(q_genadrop_save_my_assets)

        # Verify the answer is displayed after click
        a_genadrop_saves_my_assets = self.driver.find_element\
            (By.XPATH, '//div[@class="FAQCard_answer__3-7tF FAQCard_dropdown__RN75J"]/p')
        self.assertTrue(a_genadrop_saves_my_assets.is_displayed(), 'The answer is NOT displayed')

        # Verify the actual_answer is equal to expected_answer
        actual_answer = a_genadrop_saves_my_assets.text
        self.assertEqual(self.EXPECTED_ANSWER, actual_answer, f'Actual answer: {actual_answer} \
        to be equal to {self.EXPECTED_ANSWER}')

        # Verify the answer is NOT displayed after click on the question for the second time
        self.driver.find_element(By.XPATH, "//p[text()='Does GenaDrop save my assets?']").click()
        self.wait.until(EC.invisibility_of_element_located(a_genadrop_saves_my_assets))
        self.assertFalse(a_genadrop_saves_my_assets.is_displayed())

    def test_support_contact_us_footer(self):
        """Test Case ID GD_HP037"""

        # Navigate to the footer of the home page and click on contact us link
        contact_us_btn_locator = (By.XPATH, "//a[text()='Contact Us']")
        self.sl.scroll_and_click(contact_us_btn_locator, 0)

        # Switch focus to the new tab and verify that actual url is equal to expected_contact_us_url
        expected_contact_us_url = 'https://linktr.ee/MinorityProgrammers'
        new_tab = self.driver.window_handles
        self.driver.switch_to.window(new_tab[-1])
        self.assertEqual(expected_contact_us_url, self.driver.current_url, f'Wrong url. \
        Expected {self.driver.current_url} to be equal to {expected_contact_us_url} ')

        # Verify the title of the new tab (contact us) is equal to actual_contact_us_title
        actual_contact_us_title = 'Minority Programmers | Linktree'

        contact_us_page_title = self.driver.title
        assert contact_us_page_title == actual_contact_us_title, f'Wrong title! \
        Expected {contact_us_page_title} to be equal to {actual_contact_us_title}'


if __name__ == '__main__':
    unittest.main()
