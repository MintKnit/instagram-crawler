import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class Crawler:
    def _generate_chrome_option(self):
         # Create a ChromeOptions object
        options = webdriver.ChromeOptions()
        # Add the option to preserve cookies
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-browser-side-navigation")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-infobars")
        options.add_argument("start-maximized")
        options.add_argument("disable-popup-blocking")
        options.add_argument("--disable-default-apps")
        options.add_argument("--enable-automation")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-single-click-autofill")
        options.add_argument("--enable-features=NetworkService,NetworkServiceInProcess")
        options.add_argument("--disable-background-networking")
        options.add_argument("--disable-background-timer-throttling")
        options.add_argument("--disable-backgrounding-occluded-windows")
        options.add_argument("--disable-breakpad")
        options.add_argument("--disable-client-side-phishing-detection")
        options.add_argument("--disable-default-plugins")
        options.add_argument("--disable-hang-monitor")
        options.add_argument("--disable-ipc-flooding-protection")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--disable-prompt-on-repost")
        options.add_argument("--disable-sync")
        options.add_argument("--force-color-profile=srgb")
        options.add_argument("--metrics-recording-only")
        options.add_argument("--password-store=basic")
        options.add_argument("--use-mock-keychain")
        options.add_argument("--disable-translate")
        options.add_argument("--disable-web-security")
        return options

    def __init__(self, webdriver_path):
        # Initialize the webdriver with the options
        self.driver = webdriver.Chrome(executable_path=webdriver_path, options=self._generate_chrome_option())
        self.driver.implicitly_wait(5)
    
    def login(self, login_page, username, password):
        # navigate to Instagram's login page
        self.driver.get(login_page)
        username_input = self.driver.find_element(By.NAME, "username")
        password_input = self.driver.find_element(By.NAME, "password")
        username_input.send_keys(username)
        password_input.send_keys(password)
        # find the login button and click it
        login_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        login_button.click()


    def scrap(self, hashtag_name):
        self.driver.get(f"https://www.instagram.com/explore/tags/{hashtag_name}/")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        article = self.driver.find_element(By.XPATH, "//article")
        elements = article.find_elements(By.XPATH, "//a[@role='link']")
        links = [element.get_attribute("href") for element in elements if element.get_attribute("href").startswith("https://www.instagram.com/p/")]

        print(len(links))
        for link in links:     
            self.driver.get(link)
            time = self.driver.find_element(By.XPATH, "//time")
            print(link, time.get_attribute("datetime"))
            sleep(3)

if __name__ == "__main__":
    webdriver_path = '../../lib/chromedriver'
    crawler = Crawler(webdriver_path)

    # username = "ampersandOr_"
    # password = input()
    # login_page = "https://www.instagram.com/accounts/login/"
    # crawler.login(login_page, username, password)
    # print("wait for the login...(3s)")
    # sleep(3)
    print("go scrapping")
    hashtag_names = ["햄버거", "피자",  "김밥", "국밥", "초밥", "삼겹살", "소고기", "곱창", "회"]
    for hashtag_name in hashtag_names:
        crawler.scrap(hashtag_name)
        print("done")


