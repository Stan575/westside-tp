import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.selenium_utils import SeleniumUtils
from data import WINDOW_WIDTH, WINDOW_HEIGHT, TIMEOUT

class TestHomePage(unittest.TestCase):
    URL = 'https://www.genadrop.com/'
    ALGORAND_FOUNDATION_URL = 'https://www.algorand.com/'
    ALGORAND_FOUNDATION_TITLE = 'Algorand | The Blockchain for FutureFi | Algorand'
    HERDROP_URL = 'https://www.herdrop.com/'
    HERDROP_TITLE = 'H.E.R. Drop'
    FAQ_QUESTION_6 = 'How Many Editions Of An NFT Can Create?'
    FAQ_ANSWER_6 = 'You can select how many NFTs (must be less than possible combinations that can be produced)'

    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.wait = WebDriverWait(self.driver, TIMEOUT)
        self.driver.set_window_size(WINDOW_WIDTH, WINDOW_HEIGHT)
        self.su = SeleniumUtils(self.driver)
        self.driver.get(self.URL)
        # Wait for homepage header to be displayed after animation disappears
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class^='Navbar_container']")))

    def tearDown(self):
        self.driver.quit()

    def test_algorand_foundation_link(self):
        """Test Case ID: GD_HP009"""
        algorand_foundation_locator = (By.XPATH, "//img[contains(@src ,'org2')]")
        self.su.scroll_and_click(algorand_foundation_locator, 100)
        # algorand_foundation_link.click()

        # Verify URL
        self.driver.switch_to.window(self.driver.window_handles[1])
        actual_url = self.driver.current_url
        assert actual_url == self.ALGORAND_FOUNDATION_URL, \
            f"Wrong redirection for Algorand Foundation link, actual url: '{actual_url}', " \
            f"expected url: '{self.ALGORAND_FOUNDATION_URL}'"

        # Verify tab title
        actual_tab_title = self.driver.title
        assert actual_tab_title == self.ALGORAND_FOUNDATION_TITLE,\
            f"Wrong title for Algorand Foundation page, actual: '{actual_tab_title}'," \
            f" expected: '{self.ALGORAND_FOUNDATION_TITLE}'"

    def test_faq_question_6(self):
        """Test Case ID: GD_HP022"""
        faq_question_6_locator = (By.XPATH, '(//div[contains(@class, "FAQCard_question")]/p)[6]')
        # faq_questions = self.driver.find_elements(faq_question_locator)

        # Verify if the question is correct
        faq_questions_6 = self.wait.until(EC.visibility_of_element_located(faq_question_6_locator))
        assert self.FAQ_QUESTION_6 == faq_questions_6.text, \
            f"Wrong question found, actual: '{self.FAQ_QUESTION_6}', " \
            f" expected: '{faq_questions_6.text}'"

        # Verify if the answer is correct
        self.su.scroll_and_click(faq_question_6_locator)
        faq_answer_6_locator = (By.XPATH, '(//div[contains(@class, "FAQCard_answer")]/p)[6]')
        faq_answer_6 = self.wait.until(EC.visibility_of_element_located(faq_answer_6_locator))
        assert self.FAQ_ANSWER_6 == faq_answer_6.text, \
            f"Wrong answer found, actual: '{self.FAQ_ANSWER_6}', " \
            f" expected: '{faq_answer_6.text}'"


    def test_herdrop_link(self):
        """Test Case ID: GD_HP035"""
        self.su.scroll_down()
        herdrop_locator = (By.XPATH, "//a[@href='https://www.herdrop.com']")
        self.su.get_element(herdrop_locator).click()

        # Verify URL
        actual_url = self.driver.current_url
        assert actual_url == self.HERDROP_URL, \
            f"Wrong redirection for HerDrop link, actual url: '{actual_url}', " \
            f"expected url: '{self.HERDROP_URL}'"

        # Verify tab title
        actual_tab_title = self.driver.title
        assert actual_tab_title == self.HERDROP_TITLE, \
            f"Wrong title for HerDrop page, actual: '{actual_tab_title}'," \
            f" expected: '{self.HERDROP_TITLE}'"

if __name__ == '__main__':
    unittest.main()
