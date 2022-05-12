import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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

    def tearDown(self):
        self.driver.quit()

    def test_tweet_redirect_first_left(self):
        original_window = self.driver.current_window_handle

        iframe = self.wait.until(EC.presence_of_element_located((By.ID, "twitter-widget-0")))

        self.driver.switch_to.frame(iframe)

        self.wait.until(EC.element_to_be_clickable((By.TAG_NAME, "article"))).send_keys('\n')

        self.driver.switch_to.window(self.driver.window_handles[1])

        tweet_h2_text = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h2>span")))
        tweet_author_text = self.wait.until(
            EC.presence_of_element_located((By.XPATH, '(//div[@data-testid="tweetText"])[1]')))

        self.assertEqual('Tweet', tweet_h2_text.text, 'Text are not equals!')
        self.assertTrue(tweet_author_text.text.startswith(self.TWEET_TEXT))

        self.driver.close()
        self.driver.switch_to.window(original_window)
        self.driver.switch_to.default_content()


if __name__ == '__main__':
    unittest.main()
