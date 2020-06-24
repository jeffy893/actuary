#Selenium References


#To import webdriver module in python use below import statement

from selenium import webdriver

'''
Driver setup:
Firefox:
firefoxdriver = webdriver.Firefox(executable_path="Path to Firefox driver")
Chrome:
chromedriver = webdriver.Chrome(executable_path="Path to Chrome driver")
Internet Explorer:
iedriver = webdriver.IE(executable_path="­Pat­h To­ IEDriverServer.exe")
Edge:
edgedriver = webdriver.Edge(executable_path="­Pat­h To­ MicrosoftWebDriver.exe")
Opera:
operadriver = webdriver.Opera(executable_path="­Pat­h To­ operadriver")
Safari:
SafariDriver now requires manual installation of the extension prior to automation

Browser Arguments:
–headless
To open browser in headless mode. Works in both Chrome and Firefox browser
–start-maximized
To start browser maximized to screen. Requires only for Chrome browser. Firefox by default starts maximized
–incognito
To open private chrome browser
–disable-notifications
To disable notifications, works Only in Chrome browser

Example:
'''

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")
options.add_argument("--start-maximized")
options.add_argument("--disable-notifications")
options.add_argument("--incognito")

driver = webdriver.Chrome(chrome_options=options, executable_path="Path to driver")


#or

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--incognito","--start-maximized","--headless")
driver = webdriver.Chrome(chrome_options=options, executable_path="Path to driver")

#To Auto Download chrome

from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("download.default_directory=")

driver = webdriver.Chrome(chrome_options=options, executable_path="Path to chrome driver")


'''
We can add any MIME types in the list. MIME for few types of files are given below.

Text File (.txt) – text/plain
PDF File (.pdf) – application/pdf
CSV File (.csv) – text/csv or "application/csv"
MS Excel File (.xlsx) – application/vnd.openxmlformats-officedocument.spreadsheetml.sheet or application/vnd.ms-excel
MS word File (.docx) – application/vnd.openxmlformats-officedocument.wordprocessingml.document
Zip file (.zip) – application/zip
Note:
The value of browser.download.folderList can be set to either 0, 1, or 2.

0 – Files will be downloaded on the user’s desktop.
1 – Files will be downloaded in the Downloads folder.
2 – Files will be stored on the location specified for the most recent download
'''

'''
Open specific Chrome browser using Binary:
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.binary_location = ""
driver = webdriver.Chrome(chrome_options=options, executable_path="")
driver.get(‘http://google.com/’)
'''

#Read Browser Details:

driver.title
driver.window_handles
driver.current_window_handles
driver.current_url
driver.page_source

#Go to a specified URL:

driver.get("http://google.com")
driver.back()
driver.forward()
driver.refresh()

#Locating Elements:
'''
driver.find_element_by_ – To find the first element matching the given locator argument. Returns a WebElement
driver.find_elements_by_ – To find all elements matching the given locator argument. Returns a list of WebElement
'''

'''
By ID
<input id="q" type="text" />
'''
element = driver.find_element_by_id("q")

'''
By Name
<input id="q" name="search" type="text" />
'''
element = driver.find_element_by_name("search")

'''
By Class Name
<div class="username" style="display: block;">…</div>
'''
element = driver.find_element_by_class_name("username")

'''
By Tag Name
<div class="username" style="display: block;">…</div>
'''

element = driver.find_element_by_tag_name("div")

'''
By Link Text
<a href="#">Refresh</a>
'''

element = driver.find_element_by_link_text("Refresh")

'''
By Partial Link Text
<a href="#">Refresh Here</a>
'''

element = driver.find_element_by_partial_link_text("Refresh")

'''
By XPath
<form id="testform" action="submit" method="get">
Username: <input type="text" />
Password: <input type="password" />
</form>
'''

element = driver.find_element_by_xpath("//form[@id='testform']/input[1]"")


'''
By CSS Selector
<form id='testform' action='submit' method='get'>
<input class='username' type='text' />
<input class='password' type='password' />
</form>
'''

element = driver.find_element_by_css_selector("form#testform>input.username")


#Important Modules to Import:

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options



#Python Selenium commands for operation on elements:

#button/link/image:

click()
get_attribute()
is_displayed()
is_enabled()

#Text field:

send_keys()
clear()

#Checkbox/Radio:

is_selected()
click()

'''
Select:
Find out the select element using any element locating strategies and then select options from list using index, visible text or option value.
'''

select = Select(driver.find_element_by_id(""))

select.select_by_index(1)
select.select_by_value("") # pass value
select.select_by_visible_text("") # pass visible text

#Element properties:

is_displayed()
is_selected()
is_enabled()

T
#These methods return either true or false.

#Read Attribute:

get_attribute("")

#Get attribute from a disabled text box

driver.find_element_by_id("id").get_attribute("value");

#Screenshot:

from selenium import webdriver

driver = webdriver.Firefox(executable_path='[Browser Driver Path]')
driver.get('[URL to Open]')

driver.get_screenshot_as_file('sample_screenshot_2.png')
driver.save_screenshot('sample_screenshot_1.png')
