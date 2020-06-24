import time

from selenium.webdriver.common.by import By

from drivers import *

from src import CLUSTER_ROUTE, LOGIN_KEY, PIPELINE_LIM
from src.nodejsagents import NodejsAgent
from src.jenkins import Jenkins


def main():
    jenkins = NodejsAgent()
    driver.maximize_window()
    driver.get(CLUSTER_ROUTE)

    driver.find_element(By.ID, "details-button").click()
    driver.find_element(By.ID, "proceed-link").click()
    driver.find_element(By.XPATH, "/html/body/div/div[2]/a").click()

    if LOGIN_KEY in driver.title:
        Jenkins.loginfirsttry()
        Jenkins.jenkinsconsole()
        time.sleep(5)
        jenkins.setnodejs12agentimages()
        jobname = Jenkins.getpipelinename(PIPELINE_LIM)
        Jenkins.createpipelinejob(jobname)
        jenkins.pipelinejobsteps()
        Jenkins.buildjob()
        Jenkins.getbuildlogs()
    else:
        Jenkins.logintryagain()
        Jenkins.jenkinsconsole()
        jenkins.setnodejs12agentimages()
        jobname = Jenkins.getpipelinename(PIPELINE_LIM)
        Jenkins.createpipelinejob(jobname)
        jenkins.pipelinejobsteps()
        Jenkins.buildjob()
        Jenkins.getbuildlogs()
    while 1 == 1:
        time.sleep(30)


if __name__ == '__main__':
    main()
