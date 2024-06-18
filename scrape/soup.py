from datetime import datetime
import requests
from bs4 import BeautifulSoup

def scrape_data(url, limit=10):
    # page
    page = requests.get(url)
    # object
    soup = BeautifulSoup(page.text, 'html.parser')

    unsigned_list = soup.find('ul', class_= 'list-group wrap-latest')
    content_list = unsigned_list.find_all('li', class_ = 'list-group-item list-border conten1')
    data = []

    for content in content_list[:limit]:
        colum_div = content.find('div', class_='col-md-9')
        if colum_div:
            caption_div = colum_div.find('div', class_='caption')
            if caption_div:
                date_div = caption_div.find('div', class_='date')
                if date_div:
                    category = caption_div.find('span', class_='kanal-info')
                    time = date_div.text.replace(category.text.strip(), "").strip()
                    heading = caption_div.find('h3').find('span')  # Extract text from h3 tag
                    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    item_dict = {
                        "Judul": heading.text.strip(),
                        "Kategori": category.text.strip(),
                        "Waktu-Publish": time[2:],
                        "Waktu-Scrapping": date
                    }
                    data.append(item_dict)

    return data