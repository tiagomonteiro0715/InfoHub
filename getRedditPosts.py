import requests

mysubreddits = [
    "InternetIsBeautiful",
    "gradadmissions",
    "AskReddit",
    "AskAcademia",
    "AskHistorians",
    "C_Programming",
    "coolguides",
    "ECE",
    "explainlikeimfive",
    "learnmachinelearning",
    "LifeProTips",
    "Python",
    "YouShouldKnow",
    "travel",
    "personalfinance",
    "philosophy",
    "science",
    "technology"
]

headers = {"User-Agent": "Mozilla/5.0"}  # Reddit API requires a user-agent header
params = {"limit": 30, "t": "week"}

with open("top_posts.md", "w", encoding="utf-8") as f:
    for subreddit in mysubreddits:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json"
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()
            posts = data["data"]["children"]
            f.write(f"# Top posts from r/{subreddit}\n\n")
            for post in posts:
                title = post["data"]["title"]
                link = f"https://www.reddit.com{post['data']['permalink']}"
                f.write(f"## {title}\n\n")
                f.write(f"[Link]({link})\n\n")
            f.write("---\n\n")  # Add a horizontal line between subreddits
        else:
            print(f"Error: Failed to retrieve data from Reddit API for r/{subreddit}")

print("Successfully wrote top posts to file.")
