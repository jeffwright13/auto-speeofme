#!/usr/bin/python

def main():
    import time
    from selenium import webdriver
    
    # Runtime variables
    base_url = "http://speedof.me"
    title = "SpeedOf.Me"

    # Add in adblocker extension for fast load time
    ublock = "uBlock.firefox.xpi"
    ffprofile = webdriver.FirefoxProfile()
    ffprofile.add_extension(ublock)
    
    # Launch browser using Selenium driver
    print "Launching broswer..."
    browser = webdriver.Firefox()
    print "Getting URL..."
    browser.get(base_url)
    print "Asserting title..."
    assert title in browser.title
    print "Sleeping..."
    time.sleep(5)
    
    # Close all browser windows
    for window in browser.window_handles:
        browser.switch_to_window(window)
        browser.close()

if __name__ == '__main__':
    main()

