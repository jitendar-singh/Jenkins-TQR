import os

from selenium import webdriver

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
DRIVER_BIN = os.path.join(PROJECT_ROOT, "chromedriver:linux")
driver = webdriver.Chrome(executable_path=DRIVER_BIN)
