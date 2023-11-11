import requests
from bs4 import BeautifulSoup

def get_article_body(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the HTML element containing the article body
        # This is a generic example, and you might need to inspect the HTML structure of the specific website you're working with
        article_body_element = soup.find('div', class_='article-body')  # Adjust according to your HTML structure

        if article_body_element:
            # Extract and return the text content of the article body
            return article_body_element.get_text()

    # If the request was not successful or the article body wasn't found, return None
    return None

# Example usage
url = 'https://www.rtvslo.si/svet/bliznji-vzhod/najvecji-bolnisnici-v-gazi-zmanjkalo-goriva-izrael-znova-uvedel-stiriurni-rok-za-evakuacijo/687804'
article_body = get_article_body(url)

if article_body:
    print(article_body)
else:
    print("Failed to fetch the article body.")

