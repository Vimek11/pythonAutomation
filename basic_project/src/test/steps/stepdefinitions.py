from time import sleep
from behave import *
from selenium import webdriver
import time

@given('launch chrome browser')
def launchChromeBrowser(context):
    context.driver = webdriver.Chrome(executable_path="chromedriver\chromedriver.exe")


@when('open google home Page')
def openGoogleHomePage(context):
    context.driver.get("https://www.google.com")

@then('verify that the logo  present on page')
def verifyThatTheLogoPresentOnPage(context):
    print("------------------------------------->fin")
    time.sleep(4)

@then('close browser')
def closeBrowser(context):
    print("------------------------------------->fin")