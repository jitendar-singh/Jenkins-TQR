import time

from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from agents import *
from selenium.webdriver.support.wait import WebDriverWait

from drivers import *


class NodejsAgent:
    @classmethod
    def pipelinejobsteps(cls):
        driver.find_element(By.XPATH,
                            "//*[@id='main-panel']/div/div/div/form/table/tbody/tr[2]/td[3]/textarea").send_keys(
            "Sample pipeline build to test nodejs agent & maven agent")
        driver.find_element(By.XPATH, "//*[@id='main-panel']/div/div/div/form/table/tbody/tr[148]/td[3]/select").click()
        driver.find_element(By.XPATH,
                            "//*[@id='main-panel']/div/div/div/form/table/tbody/tr[148]/td[3]/select/option[2]").click()
        driver.find_element(By.XPATH, "//*[@id='main-panel']/div/div/div/form/table/tbody/tr[149]/td[2]/table/tbody/tr["
                                      "12]/td[3]/select").click()
        driver.find_element(By.XPATH, "//*[@id='main-panel']/div/div/div/form/table/tbody/tr[149]/td[2]/table/tbody/tr["
                                      "12]/td[3]/select/option[2]").click()
        time.sleep(5)
        driver.find_element(By.XPATH, "//*[@id='main-panel']/div/div/div/form/table/tbody/tr[149]/td[2]/table/tbody/tr["
                                      "13]/td[2]/table/tbody/tr[5]/td[3]/div/div[1]/table/tbody/tr[1]/td["
                                      "3]/input").send_keys("https://github.com/akram/scrum-planner.git")
        driver.find_element(By.ID, "yui-gen5-button").click()
        time.sleep(5)
        driver.find_element(By.XPATH, "//*[@id='yui-gen13-button']").click()

    @classmethod
    def setnodejs12agentimages(cls):
        # time.sleep(5)
        print("Manage Jenkins")
        driver.find_element(By.XPATH, "//*[@id='tasks']/div[4]/a[2]").click()

        '''
        Explicit wait for Configure Clouds option
        //*[@id="main-panel"]/div[13]/a/img
        '''
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='main-panel']/div[13]/a/img")))
        element.click()
        print("Clicked the cloud & Node configure button")

        '''
         Explicitly waiting for the configure clouds link.
         //*[@id="tasks"]/div[4]/a[2]
        '''
        waitconfigclouds = WebDriverWait(driver, 10)
        congifurecloud = waitconfigclouds.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='tasks']/div[4]/a[2]")))
        congifurecloud.click()
        print("Clicked the configure cloud link")

        '''
             Explicitly waiting for the pod template button.
             //*[@id="yui-gen50-button"]
        '''

        waitbutton = WebDriverWait(driver, 20)
        try:
            button = waitbutton.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='yui-gen50-button']")))
            button.click()
            print("Clicked the pod template button")
        except (NoSuchElementException, ElementNotVisibleException, TimeoutException):
            print("Exception: Pod Templates button not ready")

        try:
            waitnodejs = WebDriverWait(driver, 10)
            nodejstemplate = waitnodejs.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='yui-gen53-button']")))
            nodejstemplate.click()
            # driver.find_element(By.XPATH, ).click()
            print("Clicked pod button")
            podname = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='yui-gen45"
                                                                                                "']/table/tbody/tr[1]/td["
                                                                                                "3]/input")))
            driver.find_element(By.XPATH, "//*[@id='yui-gen45']/table/tbody/tr[1]/td[3]/input").clear()
            driver.find_element(By.XPATH, "//*[@id='yui-gen45']/table/tbody/tr[1]/td[3]/input").send_keys("nodejs12")
            print("Changed the pod name: " + nodejs12)
            print(podname)
        except (NoSuchElementException, ElementNotVisibleException, TimeoutException):
            print("EXCEPTION: In pod name block")

        try:
            podlabel = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='yui-gen45"
                                                                                                 "']/table/tbody/tr["
                                                                                                 "6]/td[3]/input")))
            driver.find_element(By.XPATH, "//*[@id='yui-gen45']/table/tbody/tr[6]/td[3]/input").clear()
            driver.find_element(By.XPATH, "//*[@id='yui-gen45']/table/tbody/tr[6]/td[3]/input").send_keys("nodejs12")
            print("Changed pod label: " + nodejs12)
            print(podlabel)
            print("Changing the docker image")
            driver.find_element(By.XPATH, "//*[@id='yui-gen27']/table/tbody/tr[5]/td[3]/input").clear()
            print("Changing the docker image")
            driver.find_element(By.XPATH, "//*[@id='yui-gen27']/table/tbody/tr[5]/td[3]/input").send_keys(nodejs12)
            print("Changed the docker image")
        except (NoSuchElementException, ElementNotVisibleException, TimeoutException):
            print("EXCEPTION: In pod label section ")

        driver.find_element(By.XPATH, "//*[@id='yui-gen55']").click()
        print("Click on Apply")

        waitsave = WebDriverWait(driver, 10)
        elementsave = waitsave.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='yui-gen72-button']")))
        elementsave.click()
        print("Click on Save")

    # def createpipelinejob(self):
    #     super().createpipelinejob()
