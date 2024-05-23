import requests

cookies = {
    'g_state': '',
    '_actor': 'eyJpZCI6IlVHVHhyNWN0ZklGZ3BoN2V1NU5IREE9PSJ9--70e11b3a06e37e42fe0e3143c9f863819d1d5c5b',
    '_se_t': 'f377f6da-018a-4bf8-ad64-3155787b024b',
    'se_lsa': '2024-05-22+19%3A16%3A56+-0400',
    'recommended_default_sort': '2024-05-22',
    'last_search_tab': 'rentals',
    'ezab_uds_srp_tabs': 'test',
    'ezab': '%7B%22uds_srp_tabs%22%3A%22test%22%7D',
    'savedZoom': '13',
    'windowHeight': '931',
    'zjs_user_id': 'null',
    'zg_anonymous_id': '%225574527b-10c3-44b6-ad9c-74e578299a17%22',
    'google_one_tap': '0',
    'zjs_anonymous_id': '%22f377f6da-018a-4bf8-ad64-3155787b024b%22',
    '_ses': 'Vkp3VGZ1TmRPRkVQTFlkNkhYaHN3WWlaRmNHNHErU243N1F3SXVxS1ozRFU3THZoOGdnQXIzTVRmZjFqclJDZHdEL3hQTGEvL1JQTEFkL1oyYzJRT1I2UzJNQm9YRENHVkwyUmhkdWlQaDR6dW03OVJkT3Z0MUZFbEZyZFZSRDl0WDFlc0ZOdXRWWUpSc1pBVUVPQ2Z0Wlh5d1YrcHRocng5ajE2MUE0UFkrM3h5MTZtWlRyczB5NWNPZWIvaVBpcnh4WGVzNWphMXQ1MmtIdy8rVCtBY0crVHdha3VobUhtYy9rcUE5V1NKSzd4RDBKR0czM3pZcmZvY0dVdjFLOTVlaW1kbnNPamFORHpBNiszS254K0tFQUh3WlJWcDZQSCtYMTY0a1FPRlBKaXlaaFpmK08zQUJSajAwNU9zUG94L0REcGpTSE1ScGpDclBnd3RFbWJLeGd2ZFZBY2pERHA2T2NjNHRKNit4SThoSkFjK1JkK1RVNjF4cEdWaDR2M0VOcHlwY1RKdFJaV013MThhOGViWktmZHBEQkwrdS9JU2U1R01rSmYybHMxbEVPeU43MCtBUFpwSUxkUWo0clJUd0xIVmRCeUcwdjVVaFZqV1hxY0Fyd2EzK2JNVHdyRXcwT0xzRTRvYTV6MmI3R01CV0pPUlZMZlRXRGlhNVBlaldjYmRpUTZHYVZ4R2pQdmZvNUlnPT0tLVo2L3ZqUXZLTUFZV003aHlZRmk3MXc9PQ%3D%3D--6359bd9552649c7ee943cd1c98be45175f54568b',
    'windowWidth': '1365',
    'savedMapDataInRect': '40.724,40.811,-74.004,-73.832',
    'savedMapDataCenterLat': '40.7675',
    'savedMapDataCenterLong': '-73.918',
    'savedMapDataZoom': '13',
}

headers = {
    'authority': 'streeteasy.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    # 'cookie': 'g_state=; _actor=eyJpZCI6IlVHVHhyNWN0ZklGZ3BoN2V1NU5IREE9PSJ9--70e11b3a06e37e42fe0e3143c9f863819d1d5c5b; _se_t=f377f6da-018a-4bf8-ad64-3155787b024b; se_lsa=2024-05-22+19%3A16%3A56+-0400; recommended_default_sort=2024-05-22; last_search_tab=rentals; ezab_uds_srp_tabs=test; ezab=%7B%22uds_srp_tabs%22%3A%22test%22%7D; savedZoom=13; windowHeight=931; zjs_user_id=null; zg_anonymous_id=%225574527b-10c3-44b6-ad9c-74e578299a17%22; google_one_tap=0; zjs_anonymous_id=%22f377f6da-018a-4bf8-ad64-3155787b024b%22; _ses=Vkp3VGZ1TmRPRkVQTFlkNkhYaHN3WWlaRmNHNHErU243N1F3SXVxS1ozRFU3THZoOGdnQXIzTVRmZjFqclJDZHdEL3hQTGEvL1JQTEFkL1oyYzJRT1I2UzJNQm9YRENHVkwyUmhkdWlQaDR6dW03OVJkT3Z0MUZFbEZyZFZSRDl0WDFlc0ZOdXRWWUpSc1pBVUVPQ2Z0Wlh5d1YrcHRocng5ajE2MUE0UFkrM3h5MTZtWlRyczB5NWNPZWIvaVBpcnh4WGVzNWphMXQ1MmtIdy8rVCtBY0crVHdha3VobUhtYy9rcUE5V1NKSzd4RDBKR0czM3pZcmZvY0dVdjFLOTVlaW1kbnNPamFORHpBNiszS254K0tFQUh3WlJWcDZQSCtYMTY0a1FPRlBKaXlaaFpmK08zQUJSajAwNU9zUG94L0REcGpTSE1ScGpDclBnd3RFbWJLeGd2ZFZBY2pERHA2T2NjNHRKNit4SThoSkFjK1JkK1RVNjF4cEdWaDR2M0VOcHlwY1RKdFJaV013MThhOGViWktmZHBEQkwrdS9JU2U1R01rSmYybHMxbEVPeU43MCtBUFpwSUxkUWo0clJUd0xIVmRCeUcwdjVVaFZqV1hxY0Fyd2EzK2JNVHdyRXcwT0xzRTRvYTV6MmI3R01CV0pPUlZMZlRXRGlhNVBlaldjYmRpUTZHYVZ4R2pQdmZvNUlnPT0tLVo2L3ZqUXZLTUFZV003aHlZRmk3MXc9PQ%3D%3D--6359bd9552649c7ee943cd1c98be45175f54568b; windowWidth=1365; savedMapDataInRect=40.724,40.811,-74.004,-73.832; savedMapDataCenterLat=40.7675; savedMapDataCenterLong=-73.918; savedMapDataZoom=13',
    'if-none-match': 'W/"4f5f855b455884b64c7f797b3b5a2804"',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Brave";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'sec-gpc': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
}


def get():
    response = requests.get(
        'https://streeteasy.com/1-bedroom-apartments-for-rent/nyc/price:2300-2700%7Carea:401,403%7Cbaths%3E=1%7Cin_rect:40.724,40.811,-74.004,-73.832',
        cookies=cookies,
        headers=headers,
    )
    return response
