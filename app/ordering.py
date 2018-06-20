from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options 
import os
from ..config import token, rr_url
from . import utils
from . import constants


driver = webdriver.PhantomJS()
driver.get(rr_url)

