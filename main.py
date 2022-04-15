from bs4 import BeautifulSoup
import requests, datetime

headers = requests.utils.default_headers()

headers.update(
    {
        'User-Agent': 'link-generator-crawler/1.0',
    }
)


sitemap_url = input("Enter URL for generating links from sitemap: ")
sitemap_request = requests.get(sitemap_url, allow_redirects=False, headers=headers)

sitemap_soup = BeautifulSoup(sitemap_request.text, 'xml')

#check if url is sitemap index file
if sitemap_soup.find_all('sitemapindex'):
    sitemap_locations = sitemap_soup.find_all('loc')

    for sitemap_location in sitemap_locations:
        sitemap_location_request = requests.get(sitemap_location.text, allow_redirects=False, headers=headers)
        sitemap_location_soup = BeautifulSoup(sitemap_location_request.text, 'xml')

        #check if page is xml sitemap
        if sitemap_location_soup.find_all('urlset'):
            urls = sitemap_location_soup.find_all('url')

            for url in urls:
                page = url.find('loc')
                print(page.text)
                






