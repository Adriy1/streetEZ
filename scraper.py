import json
import os
import ssl
import time

from bs4 import BeautifulSoup

import notif
import req

def get_new_links(html, ads):
    soup = BeautifulSoup(html, "html.parser")
    for ad in soup.find_all('a', class_='listingCard-globalLink jsGlobalListingCardLink'):
        link = ad["href"] if ad else None
        if not ad:
            continue

        ad_id = ad["aria-labelledby"]
        if ad_id not in ads:
            ads[ad_id] = {"link": link}
            print('sending:', link)
            notif.notifyTelegram(link)

    return ads

if __name__ == "__main__":
    # Don't check for certificate
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    ads = {}
    if os.path.exists("ads.json"):
        with open("ads.json", "r") as ads_data:
            ads = json.load(ads_data)

    while(True):
        print('running...')
        # get the links from the main page
        html = req.get().text
        ads = get_new_links(html, ads)
        with open("ads.json", "w") as ads_data:
            json.dump(ads, ads_data)

        print('sleeping for 60s...')
        time.sleep(60)
