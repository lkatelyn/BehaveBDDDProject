from lib2to3.pgen2 import driver

from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from wrapper.reusableMethods import reusableClass

use_step_matcher("re")


class stepClass(reusableClass):

    @given('User Navigate to Orange Url "https://opensource-demo\.orangehrmlive\.com/"')
    def step_impl(context):
        reusableClass.initilizeDriver()
        reusableClass.getBaseURL("https://opensource-demo.orangehrmlive.com/")

    @when("User enter the UserName and Password")
    def step_impl(context):
        reusableClass.enterByID("txtUsername", "Admin")
        reusableClass.enterByID("txtPassword", "admin123")

    @then("User click log in button")
    def step_impl(context):
        reusableClass.clickByID("btnLogin")
