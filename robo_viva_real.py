import time
from humancursor import WebCursor
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from BrowserConfig import Config
from ScrollRandomization import ScrollRandomization
from MouseRandomization import Mouse
from Navigation import Navigation
from Data import Extraction, MetaData
from TimeRandomization import TimeRandomization


# Configurações
configurations = Config()
wait = configurations.wait
driver = configurations.driver
cursor = WebCursor(driver)

#Mouse.mouse_passing_to_random_elements(driver, cursor)

# Main function

start_time = time.time()
last_page = 3
total_page_ads = 0
current_page = Navigation.current_page(wait, driver)
while current_page <= last_page:
    Mouse.init_mouse(driver, cursor, wait)
    wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="results-main__panel js-list"]')))
    page_ads = Extraction.all_page_houses_extraction(wait, driver)
    total_page_ads += page_ads
    ScrollRandomization.scroll_to_element_by_xpath(wait, driver, '//ul[@class="pagination__wrapper"]')
    Navigation.next_page(wait, driver, cursor)
    current_page = Navigation.current_page(wait, driver)
TimeRandomization.secrets_very_long_wait()
driver.quit()
end_time = time.time()

MetaData.get_extraction_info(wait, driver, start_time, end_time, last_page, current_page, total_page_ads)











