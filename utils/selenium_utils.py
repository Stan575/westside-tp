from selenium.webdriver.support.wait import WebDriverWait


class SeleniumUtils:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)

    def scroll_and_click(self, locator, top_offset=100):
        element = self.driver.find_element(locator[0], locator[1])
        y = element.location.get('y')
        self.driver.execute_script(f"window.scrollTo(0, {y - top_offset});")

        is_visible_script = """function isScrolledIntoView(element) {
                                            var rect = element.getBoundingClientRect();
                                            var elemTop = rect.top;
                                            var elemBottom = rect.bottom;
                                            var isVisible = (elemTop >= 0) && (elemBottom <= window.innerHeight);
                                            return isVisible;
                                        }
                                   return isScrolledIntoView(arguments[0]);"""

        self.wait.until(lambda d: self.driver.execute_script(is_visible_script, element))

        element.click()
