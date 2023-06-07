#!/usr/bin/python3
# get subs
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    if counts is None:
        counts = {}

    # Base case: stop recursion if word_list is empty
    if not word_list:
        print_sorted_counts(counts)
        return

    # Make a request to the Reddit API
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "RecursiveBot"}
    params = {"after": after} if after else None
    response = requests.get(url, headers=headers, params=params)

    # Check if the subreddit is valid
    if response.status_code != 200:
        print("Invalid subreddit or no posts match.")
        return

    data = response.json()
    posts = data["data"]["children"]

    # Extract titles and update word counts
    for post in posts:
        title = post["data"]["title"].lower()
        count_keywords(title, word_list, counts)

    # Check if there are more posts to fetch
    after = data["data"]["after"]
    if after:
        count_words(subreddit, word_list, after, counts)
    else:
        print_sorted_counts(counts)


def count_keywords(title, word_list, counts):
    for word in word_list:
        if word in title:
            counts[word] = counts.get(word, 0) + title.count(word)


def print_sorted_counts(counts):
    sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))

    for word, count in sorted_counts:
        print(f"{word}: {count}")


# Example usage
count_words("programming", ["python", "java", "javascript", "python"])
