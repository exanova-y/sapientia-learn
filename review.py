import requests
from newsapi import NewsApiClient

newsapi_instance = NewsApiClient(api_key="") # make sure to replace

neurotech_wordlist = ["Brain-Computer Interfaces", "Neurofeedback", "Neuroprosthetics"]

# users can modify these search queries
query_keywords = neurotech_wordlist[0]
start_date_str = "2024-05-10" # format: YYYY-MM-DD
end_date_str = "2024-05-15" # with the free plan you can only access news articles within a month

news_results = newsapi_instance.get_everything(q=query_keywords, from_param=start_date_str, to=end_date_str, sort_by="relevancy", language="en") 
print(f"number of articles found: {len(news_results['articles'])}")

for article in news_results['articles']:
    print(f"Title:{article['title']}")
    print(f"Description: {article['description']}")
    print(f"Published At: {article['publishedAt']}")
    print("=============")