import random
from TimeRandomization import TimeRandomization
import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait


class Config:

    @staticmethod
    def random_httpheader_useragent():
        user_agents = [
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36",
            "user-agent=Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
            "user-agent=Mozilla/5.0 (Windows NT 10.0; WOW64; rv:70.0) Gecko/20100101 Firefox/70.0",
            "user-agent=Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
            "user-agent=Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)",
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19042",
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.100.0",
            "user-agent=Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36 OPR/65.0.3467.48"
        ]
        return random.choice(user_agents)

    def __init__(self):
        #my_user_agent = Configurations.random_httpheader_useragent()
        self.options = uc.ChromeOptions()
        #self.options.add_argument(f"--user-agent={my_user_agent}")
        self.options.add_argument("--disable-gpu")  # Elimina processos residuais do chrome
        self.driver = uc.Chrome(options=self.options, version_main=120)
        self.wait = WebDriverWait(self.driver, 10)
        #self.options.add_argument(f"user-agent={my_user_agent}")
        #Randomization.very_long_wait()
        #self.driver.get('https://httpbin.org/headers')
        #self.driver.get('https://nowsecure.nl')
        self.driver.get('https://www.vivareal.com.br/venda/pernambuco/recife/casa_residencial/#onde=Brasil,Pernambuco,Recife,,,,,,BR%3EPernambuco%3ENULL%3ERecife,,,')
        #TimeRandomization.very_long_wait()
