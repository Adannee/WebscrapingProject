from bs4 import BeautifulSoup
import requests
from csv import writer

url = "https://www.airbnb.com/s/Europe/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&price_filter_input_type=0&price_filter_num_nights=5&place_id=ChIJhdqtz4aI7UYRefD8s-aZ73I&date_picker_type=flexible_dates&flexible_trip_lengths%5B%5D=one_month&flexible_trip_dates%5B%5D=december&source=structured_search_input_header&search_type=filter_change"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all('div', class_="cy5jw6o" )

with open('AirBnB.csv', 'w', encoding='utf8', newline='')as f:
    thewriter = writer(f)
    header = ['Title','Location','Price','Rate']
    thewriter.writerow(header)

    for list in lists:
        title = list.find('div', class_="t1jojoys dir dir-ltr").text
        location = list.find('span', class_="t6mzqp7 dir dir-ltr").text
        price = list.find('span', class_="a8jt5op dir dir-ltr").text
        rate = list.find('span', class_="r1dxllyb dir dir-ltr")

        info = [title, location, price, rate]
        thewriter.writerow(info)
