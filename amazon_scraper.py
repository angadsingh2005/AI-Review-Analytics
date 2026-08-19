import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def scrape_amazon_reviews(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Referer': 'https://www.amazon.in/'
    }
    
    response = requests.get(url, headers=headers)
    print(f"HTTP Status Code: {response.status_code}")
    
    # Check if Amazon served a CAPTCHA page
    if "api-services-support@amazon.com" in response.text or "Captcha" in response.text:
        print("--> Amazon served a CAPTCHA page (Bot Detected).")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    reviews_list = []

    review_containers = soup.find_all('div', {'data-hook': 'review'})
    print(f"Found {len(review_containers)} review elements on the page.")

    for container in review_containers:
        text_element = container.find('span', {'data-hook': 'review-body'})
        review_text = text_element.text.strip() if text_element else None
        
        rating_element = container.find('i', {'data-hook': 'review-star-rating'})
        rating = rating_element.text.strip().split(' out of')[0] if rating_element else None

        if review_text:
            reviews_list.append({
                'review_text': review_text,
                'rating': rating
            })
            
    return reviews_list

# Use the cleaner product-reviews URL format for amazon.in
target_url = 'https://www.amazon.in/product-reviews/B0FMDL81GS/ref=cm_cr_dp_d_show_all_top?ie=UTF8&reviewerType=all_reviews'

extracted_data = scrape_amazon_reviews(target_url)

if extracted_data:
    df = pd.DataFrame(extracted_data)
    df.to_csv('amazon_raw_reviews.csv', index=False)
    print(f"Successfully saved {len(extracted_data)} reviews to CSV.")
else:
    print("No reviews extracted.")