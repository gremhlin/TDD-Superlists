from selenium import webdriver
import time

print("1")
browser = webdriver.Chrome()
print("2")
browser.get('http://localhost:8000')
print("3")
assert 'Django' in browser.title
