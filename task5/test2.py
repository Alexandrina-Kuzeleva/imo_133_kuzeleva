import requests
from bs4 import BeautifulSoup

def parse_hotels(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    hotels = []

    hotel_elements = soup.find_all('div', class_='hotel-card')
    for hotel_element in hotel_elements:
        name = hotel_element.find('h3', class_='hotel-card__title').text.strip()
        address = hotel_element.find('div', class_='hotel-card__address').text.strip()
        rating = hotel_element.find('span', class_='hotel-card__rating-value').text.strip()
        price = hotel_element.find('span', class_='hotel-card__price-value').text.strip()

        hotel = {
            'name': name,
            'address': address,
            'rating': rating,
            'price': price
        }
        hotels.append(hotel)

    return hotels

url = 'https://hotel.tutu.ru/offers?business=0&check_in=2023-10-07&check_out=2023-10-08&contract=&filters[0]=optionFiltersList.rating.rating_more_zero&filters[1]=optionFiltersList.distance_to_center.distance_to_center_any_distance&filters[2]=optionFiltersList.extra_bed.extra_bed_no_value&geo_id=2657260&geo_name=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0&geo_type=locality&room[0]=1.&search_id=d05b1c4f-24f5-4296-bba3-f38eeba62f0e&sorting=relevanceDesc'
hotels = parse_hotels(url)
for hotel in hotels:
    print(hotel)