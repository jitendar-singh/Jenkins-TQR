import random
import string
import time

from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, TimeoutException

from drivers import *
from selenium.webdriver.common.by import By


class Jenkins:
    @staticmethod
    def getpipelinename(pipeline):
        pipelinename = string.ascii_letters + string.digits
        return ''.join((random.choice(pipelinename) for i in range(pipeline)))

    @staticmethod
    def loginfirsttry():
        print("Inside first try")
        driver.find_element(By.XPATH, "/html/body/div/div/main/div/ul/li[1]/a").click()
        driver.find_element(By.ID, "inputUsername").send_keys("kubeadmin")
        driver.find_element(By.ID, "inputPassword").send_keys("MjTzN-aIo4K-QskYG-xTeay")
        driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/div[4]/button").click()

    @staticmethod
    def logintryagain():
        print("Inside logintryagain")
        driver.find_element(By.ID, "details-button").click()
        driver.find_element(By.ID, "proceed-link").click()
        # driver.find_element(By.XPATH, "/html/body/div/div[2]/a").click()
        driver.find_element(By.XPATH, "/html/body/div/div/main/div/ul/li[1]/a").click()
        driver.find_element(By.ID, "inputUsername").send_keys("kubeadmin")
        driver.find_element(By.ID, "inputPassword").send_keys("MjTzN-aIo4K-QskYG-xTeay")
        driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/div[4]/button").click()

    @staticmethod
    def jenkinsconsole():
        print("Inside Jenkins console")
        try:
            driver.find_element(By.XPATH, "/html/body/form/div[2]/input[1]").click()
        except (NoSuchElementException, ElementNotVisibleException, TimeoutException):
            print("EXCEPTION: Inside jenkins console section ")

    @staticmethod
    def jenkinslogout():
        print("Logging you out")
        driver.find_element(By.XPATH, "//*[@id='header']/div[3]/a[2]/span").click()

    @staticmethod
    def createpipelinejob(job):
        jobname = "sample pipeline" + "-" + job
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, "//*[@id='tasks']/div[1]/a[2]").click()
        driver.find_element(By.ID, "name").clear()
        driver.find_element(By.ID, "name").send_keys(jobname)
        driver.find_element(By.XPATH, "//*[@id='j-add-item-type-standalone-projects']/ul/li[2]/label/span").click()
        time.sleep(5)
        driver.find_element(By.ID, "ok-button").click()

    @staticmethod
    def buildjob():
        driver.find_element(By.XPATH, "//*[@id='tasks']/div[4]/a[2]").click()

    @staticmethod
    def getbuildlogs():
        driver.find_element(By.XPATH, "//*[@id='breadcrumbs']/li[1]/a").click()
        driver.find_element(By.XPATH, "//*[@id='tasks']/div[3]/a[2]").click()
        driver.find_element(By.XPATH, "//*[@id='projectStatus']/tbody/tr[2]/td[5]/a/img").click()

