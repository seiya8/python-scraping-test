import time
import base64
import PyChromeDevTools

chrome = PyChromeDevTools.ChromeInterface()
chrome.Network.enable()
chrome.Page.enable()

time.sleep(1)
chrome.Page.navigate(url='https://www.skyscanner.jp/')
chrome.wait_event("Page.loadEventFired", timeout=60)

chrome.Runtime.evaluate(expression="document.querySelector(`input[type='radio'][name='trip-type-selector'][aria-label='片道']`).checked = true;")
chrome.Runtime.evaluate(expression="document.querySelector(`input[type='checkbox'][name='destinationFlexible'][aria-label='近隣の空港も検索']`).checked = true;")

# 検索
time.sleep(1)
chrome.Runtime.evaluate(expression="document.querySelector(`button[aria-label='検索']`).click();")
chrome.wait_event("Page.loadEventFired", timeout=60)

# スクショ
res, msg = chrome.Page.captureScreenshot()
imgb64 = res['result']['data']
with open('skyscanner.png',  "wb" ) as f:
    f.write(base64.b64decode(imgb64))