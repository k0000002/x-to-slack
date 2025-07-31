import requests
import os

bearer_token = os.environ["TWITTER_BEARER_TOKEN"]
slack_webhook_url = os.environ["SLACK_WEBHOOK_URL"]
keyword = os.environ.get("KEYWORD", "ボートレース")

search_url = "https://api.twitter.com/2/tweets/search/recent"
query_params = {
    'query': keyword,
    'tweet.fields': 'created_at,author_id',
    'max_results': 10,
}
headers = {"Authorization": f"Bearer {bearer_token}"}
response = requests.get(search_url, headers=headers, params=query_params)
tweets = response.json().get("data", [])

if not tweets:
    print("No tweets found.")
    exit()

for tweet in tweets:
    message = f"https://twitter.com/i/web/status/{tweet['id']}\n{tweet['text']}"
    requests.post(slack_webhook_url, json={"text": message})
