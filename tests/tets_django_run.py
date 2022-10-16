import pytest
from selenium import webdriver

def test_init_django():
    browser = webdriver.Chrome()
    browser.get('http://localhost:8000')
    assert 'The install worked successfully! Congratulations!' in browser.title