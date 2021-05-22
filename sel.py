from selenium import webdriver
import time
import smtplib, ssl

def sendanemail (info):

    port = 465  # For SSL
    username='sherifmohamedamr97'
    password='aljwre2345jkedf%H'

    FROM = 'sherif@sherif.com'
    # 'sherifmohamedamr97', 'sdlf#2orgK'
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("sherifmohamedamr97@gmail.com", password)
        sender_email = "sherifmohamedamr97@gmail.com"
        receiver_email = "sherifd30@gmail.com"
        
        message = """\
        Subject: Hi there

        This message is sent from Python."""
        server.sendmail(sender_email, receiver_email, message+info)
        #server.quit()

driver = webdriver.Firefox()

while True:
    driver.get("https://www.bestbuy.com/site/searchpage.jsp?_dyncharset=UTF-8&id=pcat17071&iht=y&intl=nosplash&keys=keys&ks=960&list=n&sc=Global&st=3090&type=page&usc=All%20Categories")


    #ids = driver.find_element_by_class_name('add-to-cart-button')
    #ids = driver.find_elements_by_xpath("//button[@class='*add-to-cart-button']")
    ids = driver.find_elements_by_xpath("//*[contains(text(), 'Add to Cart')]")
    device_sku_id='0' 
    for ii in ids:
        ### {'class': 'btn btn-primary btn-sm btn-block btn-leading-ficon add-to-cart-button', 'data-sku-id': '6441554', 'style': 'padding:0 8px', 'type': 'button'}
        try:
            if ii.get_attribute("data-sku-id")!='6441554' and ii.get_attribute("type")=='button' and \
                ii.get_attribute('class') =='btn btn-primary btn-sm btn-block btn-leading-ficon add-to-cart-button':
                time.sleep(1)
                device_sku_id = ii.get_attribute("data-sku-id")
                ii.click()
                print ('button clicked')
                time.sleep(2)
                new_buttons = driver.find_elements_by_xpath("//*[contains(text(), 'Go to Cart')]")
                for new_button in new_buttons:
                    print (new_button.get_attribute("class"), new_button.get_attribute("type"))
                break

        except Exception as e:
            print (e)

    driver.get("https://www.bestbuy.com/cart")
    time.sleep(1)
    button_checkout = driver.find_elements_by_xpath("//*[contains(text(), 'Checkout')]")
    for iii in button_checkout:
        if iii.get_attribute("type") == "button":
            sendanemail(" found device " + device_sku_id )
            iii.click()

    #send an email (smtplib)
    time.sleep(50)




# to close browser
# driver.close()