#!/usr/bin/python

def main():
    import time
    from selenium import webdriver
    counter = 1
    
    # Runtime variables
    base_url = "http://speedof.me"
    title = "SpeedOf.Me"

    # Add in adblocker extension for fast load time
    ublock = "uBlock.firefox.xpi"
    ffprofile = webdriver.FirefoxProfile()
    ffprofile.add_extension(ublock)
    
    # Launch browser using Selenium driver
    print "Launching browser..."
    browser = webdriver.Firefox()
    print "Getting URL..."
    browser.get(base_url)
    print "Asserting title..."
    assert title in browser.title

    # LOOP
    while (1):
        print "Running test #" + str(counter) + "..."
        browser.find_element_by_id("btnStart").click()
        print "Sleeping..."
        time.sleep(120)
        counter += 1
    
if __name__ == '__main__':
    main()