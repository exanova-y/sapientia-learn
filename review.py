import requests
from newsapi import NewsApiClient
import arxiv

# users can modify these parameters
neurotech_wordlist = ["Brain-Computer Interfaces", "Neurofeedback", "Neuroprosthetics"]
search_news = False
search_discord = False
search_journals = True
query_keywords = neurotech_wordlist[0]


start_date_str = "2024-05-01" # format: YYYY-MM-DD
end_date_str = "2024-05-15" # with the free plan you can only access news articles within a month

# initialize clients only once
arxiv_instance = arxiv.Client() 
newsapi_instance = NewsApiClient(api_key="") # make sure to replace

# newsapi uses an AND operation regarding keywords 
if search_news:
    # newsapi searches for the exact keywords
    # set maximum of 10 results
    news_results = newsapi_instance.get_everything(q=query_keywords, from_param=start_date_str, PageSize=10, pages=1, to=end_date_str, sort_by="relevancy", language="en") 
    articles = news_results['articles']
    headlines = [article['title'] for article in articles]
    descriptions = [article['description'] for article in articles]
    published_dates = [article['publishedAt'] for article in articles]
    
    print(f"number of articles found: {len(news_results['articles'])}")

    for i in range(len(headlines)):
        print(f"title: {headlines[i]}")
        print(f"description: {descriptions[i]}")
        print(f"published at: {published_dates[i]}")

if search_journals:
    print('searching arxiv...')
    arxiv_search_query = f"all:+{query_keywords} AND submittedDate:[{start_date_str}, {end_date_str}]"
    search = arxiv.Search(query=arxiv_search_query, max_results=10, sort_by = arxiv.SortCriterion.SubmittedDate) # search object
    results = list(arxiv_instance.results(search)) # DeprecationWarning: The 'Search.results' method is deprecated, use 'Client.results' instead

    print(f"Found {len(results)} papers on arxiv")
    for paper in results:
        print(f"title: {paper.title}")
        print(f"summary: {paper.summary}") # abstract
        print(f"published date: {paper.published.strftime('%Y-%m-%d')}") # a date time object
        print("====")