#!/usr/bin/python

def main():
    from selenium import webdriver
    
    base_url = "http://speedof.me"
    title = "SpeedOf.Me"
    
    # Launch browser using Selenium driver
    browser = webdriver.Firefox()
    browser.get(base_url)
    assert title in browser.title
    
    # Kill browser
    browser.quit()

if __name__ == '__main__':
    main()

