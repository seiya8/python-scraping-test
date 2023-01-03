import PyChromeDevTools
import time

chrome = PyChromeDevTools.ChromeInterface()
chrome.Network.enable()
chrome.Page.enable()

start_time = time.time()
chrome.Page.navigate(url='https://www.google.com/')
chrome.wait_event("Page.loadEventFired", timeout=60)
end_time = time.time()

print (f'Page Loading Time: {end_time-start_time} s')
