import jsonStore
import soup

def main():
    scraped_data = soup.scrape_data('https://www.republika.co.id/')
    jsonStore.store(scraped_data)


if __name__== '__main__':
    main()