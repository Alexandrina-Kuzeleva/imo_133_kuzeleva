import requests
from bs4 import BeautifulSoup as BS

def main():
    cookies = {
        'SESSIONID': 'e7061023-cef4-44d5-a923-aad9ea0d8259',
        'servercookie3__cross_domain_secured': '4538e6d814342b600597452de0a9c785',
        'servercookie3__cross_domain': '898bfdbd60f226b7c77e687eb5c2e850',
        'reference_token': 'anonymous_ref',
        '_ga': 'GA1.3.1408444234.1696611090',
        '_gid': 'GA1.3.2055652524.1696611090',
        'rai': '0fa0fbc137363c756c84463cb00ee4e7',
        'tmr_detect': '0%7C1696611734616',
        'tutuid_access_token': 'af25e33d9aab749749bd3ac1c1a79c1255ff4daf663c971a5cbbf62d983216ad',
        'tmr_lvid': 'b2a8ea63a1b820ea967918aef2ada679',
        'tmr_lvidTS': '1696611087216',
        '_gcl_au': '1.1.2017475333.1696611809',
        '_gid': 'GA1.2.250675738.1696611812',
        '_ym_uid': '1696611090341099450',
        '_ym_d': '1696611812',
        'cto_bundle': 'vpAjy19YREdHbEhJRkpLaW54eXRPVEtxWHB4aDE2Y3klMkJGcXN4SG1DSSUyQlBiJTJGNTlOZ1hDbUMxcXdYOHolMkI5MTB6VXg1N2xSdFR2Z3kxc2dTR2JUJTJCcmFUeHM0MVZHR2JpWjN0WFRObkVaNlZ0Y1RZUnRXbGoyQVp4NkNzT0ElMkJxV1pHaURQdjVvNU84SUxyV1lldWhWTDFHa1IxQkElM0QlM0Q',
        '_ym_isad': '1',
        '_dc_gtm_UA-37653253-1': '1',
        '_gat_UA-37653253-29': '1',
        '_ga': 'GA1.1.286337280.1696611812',
        '_ga_5HS1N1X1F6': 'GS1.1.1696611970.1.0.1696611970.60.0.0',
        '_ga_5RD719CDBK': 'GS1.1.1696611970.1.0.1696611970.0.0.0',
        'tutuid_csrf': 'R1vU1oh-V6TCCB20U1kMCjAA',
        'mindboxDeviceUUID': 'c305b285-757c-4a46-bd82-2f4c73f99985',
        'directCrm-session': '%7B%22deviceGuid%22%3A%22c305b285-757c-4a46-bd82-2f4c73f99985%22%7D',
    }

    headers = {
        'authority': 'hotel.tutu.ru',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'ru,en-US;q=0.9,en;q=0.8',
        # 'cookie': 'SESSIONID=e7061023-cef4-44d5-a923-aad9ea0d8259; servercookie3__cross_domain_secured=4538e6d814342b600597452de0a9c785; servercookie3__cross_domain=898bfdbd60f226b7c77e687eb5c2e850; reference_token=anonymous_ref; _ga=GA1.3.1408444234.1696611090; _gid=GA1.3.2055652524.1696611090; rai=0fa0fbc137363c756c84463cb00ee4e7; tmr_detect=0%7C1696611734616; tutuid_access_token=af25e33d9aab749749bd3ac1c1a79c1255ff4daf663c971a5cbbf62d983216ad; tmr_lvid=b2a8ea63a1b820ea967918aef2ada679; tmr_lvidTS=1696611087216; _gcl_au=1.1.2017475333.1696611809; _gid=GA1.2.250675738.1696611812; _ym_uid=1696611090341099450; _ym_d=1696611812; cto_bundle=vpAjy19YREdHbEhJRkpLaW54eXRPVEtxWHB4aDE2Y3klMkJGcXN4SG1DSSUyQlBiJTJGNTlOZ1hDbUMxcXdYOHolMkI5MTB6VXg1N2xSdFR2Z3kxc2dTR2JUJTJCcmFUeHM0MVZHR2JpWjN0WFRObkVaNlZ0Y1RZUnRXbGoyQVp4NkNzT0ElMkJxV1pHaURQdjVvNU84SUxyV1lldWhWTDFHa1IxQkElM0QlM0Q; _ym_isad=1; _dc_gtm_UA-37653253-1=1; _gat_UA-37653253-29=1; _ga=GA1.1.286337280.1696611812; _ga_5HS1N1X1F6=GS1.1.1696611970.1.0.1696611970.60.0.0; _ga_5RD719CDBK=GS1.1.1696611970.1.0.1696611970.0.0.0; tutuid_csrf=R1vU1oh-V6TCCB20U1kMCjAA; mindboxDeviceUUID=c305b285-757c-4a46-bd82-2f4c73f99985; directCrm-session=%7B%22deviceGuid%22%3A%22c305b285-757c-4a46-bd82-2f4c73f99985%22%7D',
        'if-none-match': 'W/"3b686-QAKvsWeDwqpYJJ+fcUKXv+RnEG0"',
        'referer': 'https://hotel.tutu.ru/offers?business=0&check_in=2023-10-07&check_out=2023-10-08&contract=&filters[0]=optionFiltersList.rating.rating_more_zero&filters[1]=optionFiltersList.distance_to_center.distance_to_center_any_distance&filters[2]=optionFiltersList.extra_bed.extra_bed_no_value&geo_id=2657260&geo_name=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0&geo_type=locality&room[0]=1.&search_id=d05b1c4f-24f5-4296-bba3-f38eeba62f0e&sorting=relevanceDesc',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    }

    response = requests.get(
        'https://hotel.tutu.ru/offers/vid-api/offers?geoId=2657260&geoType=8&checkInDate=2023-10-07&checkOutDate=2023-10-08&guestsList[]=%7B%22adultCount%22:1,%22childrenList%22:[]%7D&isBusinessTrip=false&filtersList=%7B%22optionFiltersList%22:[%7B%22id%22:%22rating%22,%22selectedItemsList%22:[%22rating_more_zero%22]%7D,%7B%22id%22:%22distance_to_center%22,%22selectedItemsList%22:[%22distance_to_center_any_distance%22]%7D,%7B%22id%22:%22extra_bed%22,%22selectedItemsList%22:[%22extra_bed_no_value%22]%7D],%22rangeFiltersList%22:[],%22buttonFiltersList%22:[],%22shortcutsList%22:[]%7D&searchId=d05b1c4f-24f5-4296-bba3-f38eeba62f0e&timeZone=%2B0300&orderBy=relevance+desc&sutochno=true&bronevik=true&shortOfferParams=true',
        cookies=cookies,
        headers=headers,
    )


'''url = '' #ссылка на сайт
def f():
    r = requests.get(url)
    soup = BS(r.content, 'html.parser')
    data = soup.find('a') #инфа которавя должна найтись
    print(data)'''

    data = response.json()

    with open('data.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False,)




if __name__ == '__main__':
    main()
