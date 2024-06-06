import requests
from newsapi import NewsApiClient
from arxiv import Search, arxiv
import unidecode


# users can modify these parameters
neurotech_wordlist = ["Brain-Computer Interfaces", "Neurofeedback", "Neuroprosthetics"]
search_news = True
search_discord = False
search_journals = True
query_keywords = neurotech_wordlist[0]
start_date_str = "2024-05-10" # format: YYYY-MM-DD
end_date_str = "2024-05-15" # with the free plan you can only access news articles within a month

# initialize clients only once
arxiv_instance = arxiv.Client() 
newsapi_instance = NewsApiClient(api_key="") # make sure to replace

# newsapi uses an AND operation regarding keywords 
if search_news:
    # newsapi searches for the exact keywords
    news_results = newsapi_instance.get_everything(q=query_keywords, from_param=start_date_str, to=end_date_str, sort_by="relevancy", language="en") 
    articles = news_results['articles']
    headlines = [article['title'] for article in articles]
    published_dates = [article['publishedAt'] for article in articles]
    
    print(f"number of articles found: {len(news_results['articles'])}")

    for i in range(len(headlines)):
        print("title: {headlines[i]}")
        print("description: {descriptions[i]}")
        print("published at: {published_dates[i]}")

if search_journals:
    arxiv_search_query = f"all:+{query_keywords} AND submittedDate:[{start_date_str}, {end_date_str}]"
    search = Search(query=arxiv_search_query, sort_by = arxiv.SortCriterion.SubmittedDate) # search object
    results = arxiv_instance.results(search)

    paper_results = list(results)
    for paper in paper_results:
        print(f"title: {paper.title}")
        print(f"summary: {paper.summary}"s) # abstract
        print(paper.published_date.strftime('%Y-%m-%d'))