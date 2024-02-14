from time import sleep

from humancursor import WebCursor
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from BrowserConfig import Config
from ScrollRandomization import ScrollRandomization
from MouseRandomization import Mouse
from TimeRandomization import TimeRandomization
from SheetManipulations import SheetManipulations

# Main Function
sleep(5)
# Configurações
configurations = Config()
wait = configurations.wait
driver = configurations.driver
cursor = WebCursor(driver)


# Actions

SheetManipulations.extraction_headers()


driver.quit()




