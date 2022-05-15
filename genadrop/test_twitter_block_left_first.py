import time
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.selenium_utils import SeleniumUtils as SU

class TestLogo(unittest.TestCase):
    URL = 'https://www.genadrop.com/'
    TWEET_TEXT = "We are happy to announce our partnership w/ the #NEAR Foundation for Genadrop our no code solution for creating generative art."
    HTTP_OK = 200

    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.wait = WebDriverWait(self.driver, 5)
        self.driver.set_window_size(1600, 1050)
        self.driver.get(self.URL)
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class^='Navbar_container']")))

    def tearDown(self):
        self.driver.quit()

    def test_tweet_redirect_first_left(self):
        """Test case id: GD_HP012"""
        # save window handle
        original_window = self.driver.current_window_handle
        # scroll down to widgets
        SU.scroll(SU(self.driver), (By.XPATH, "(//iframe)[1]"))
        # save iframe #1 and switch to
        iframe = self.wait.until(EC.presence_of_element_located((By.ID, "twitter-widget-0")))
        self.driver.switch_to.frame(iframe)
        # click on widget
        self.driver.find_element(By.TAG_NAME, "article").click()
        #save text from twit - first 30 substring
        widget_twit_text = (self.driver.find_element(By.XPATH, "//article/div/div[@lang='en']")).text[0:30]
        # switch to opened new tab
        self.driver.switch_to.window(self.driver.window_handles[1])
        # get text of twit title
        tweet_h2_text = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "h2>span")))
        # get element - twit's article
        tweet_on_twitter_page = self.wait.until(
            EC.presence_of_element_located((By.XPATH, '(//article/div)[1]//div[@lang="en"]')))

        # Assert - verify twit's title
        self.assertEqual('Tweet', tweet_h2_text.text, 'Text are not equals!')
        # Assert - verify article text starts with text from widget
        self.assertTrue(tweet_on_twitter_page.text.startswith(widget_twit_text),"Opened wrong Twitter article!")

        # close opened tab
        self.driver.close()
        # get back to first window(iframe)
        self.driver.switch_to.window(original_window)
        # return to the default content(quit from iframe)
        self.driver.switch_to.default_content()

    def test_FAQ_What_Type_Of_NFT_Can_I_Mint(self):
        """Test case id: GD_HP025"""
        expected_answer_text = "Genadrop supports the Minting of 1 of 1 image and collections generated on GenaDrop.\n To Mint 1 0f 1 NFT select your NFT file[supported file format: png], add metadata file and click export"

        # wait until some of parts of page fully displayed
        self.wait.until(EC.visibility_of_element_located((By.ID, "twitter-widget-0")))

        #scroll to the last FAQ question
        SU.scroll(SU(self.driver), (By.XPATH, "//div[text()='Frequently Asked Questions']/following-sibling::div/div[last()]"))

        # getting last question from FAQ block
        freq_asked_question = self.driver.find_element(
            By.XPATH, "//div[text()='Frequently Asked Questions']/following-sibling::div/div[last()]")

        # click on question to release answer text
        freq_asked_question.click()

        # get answer text
        answer_text = freq_asked_question.find_element(By.XPATH, ".//span[text()='A.']/following-sibling::p").text

        # split text into list to compare
        exp_a = expected_answer_text.split(" ")
        act_a = answer_text.split(" ")

        # assertion - by text and by list
        self.assertEqual(answer_text, expected_answer_text,"The text does not match!")
        self.assertEqual(exp_a, act_a,"The text does not match!")

if __name__ == '__main__':
    unittest.main()
