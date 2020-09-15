from flask import Flask, request
from amazon import scrape_amazon
from notify import send_mail
import threading, time

app = Flask(__name__)

@app.route('/price_monitor', methods=['POST'])
def index():
    site = request.form['site']
    url = request.form['link']
    interval = float(request.form['interval']);
    email = request.form['email']
    price = scrape_amazon(url)
    threading.Thread(target = request_monitor, args=(site,url,interval,email,price)).start() 
    return "Request received", 200

def request_monitor(site,url,interval,email,price):
    while(1):
        time.sleep(interval)
        if site == "Amazon":
            new_price = scrape_amazon(url)
            print(new_price)
            if(new_price != price):
                send_mail("<senders email>",email,"Price change Alert!","The price of your product has recently changed. Follow this <a href="+url+">link</a>.")
                break
                
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)   

    
    
