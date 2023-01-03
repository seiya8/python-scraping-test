import base64
import PyChromeDevTools

chrome = PyChromeDevTools.ChromeInterface()
chrome.Network.enable()
chrome.Page.enable()

chrome.Page.navigate(url='https://www.google.com/')
chrome.wait_event("Page.loadEventFired", timeout=60)

res, msg = chrome.Page.captureScreenshot()
imgb64 = res['result']['data']
with open('google.png',  "wb" ) as f:
    f.write(base64.b64decode(imgb64))
