### 0x16-api_advanced
API advanced
I continued to practice querying API's in this advanced project, this time working with the Reddit API.

Tests ✔️
tests: Folder of test files for all tasks. Provided by Holberton School.
Function Prototypes ���
Prototypes for functions written in this project:

File	Prototype
0-subs.py	def number_of_subscribers(subreddit)
1-top_ten.py	def top_ten(subreddit)
2-recurse.py	def recurse(subreddit, hot_list=[])
100-count.py	def count_words(subreddit, word_list)
Tasks ���
0. How many subs?

0-subs.py: Python function that returns the total number of subscribers for a given subreddit.
Returns 0 if an invalid subreddit is given.
1. Top Ten

1-top_ten.py: Python function that prints the top ten hottest posts for a given subreddit.
Prints None if an invalid subreddit is given.
2. Recurse it!

2-recurse.py: Python function that recursively returns a list of titles for all hot articles on a given subreddit.
Returns None if no results are found on the given subreddit.
3. Count it!

100-count.py: Python function that recursively prints a sorted count of given keywords parsed from titles of all hot articles on a given subreddit.
Keywords are case-insensitive and delimited by spaces.
Results are printed in descending order by count.
Words with identical counts are sorted alphabetically.
Words with no matches are skipped.
Results are based on the number of times a keyword appears - ie., java java java counts as three separate instances of java



## API Advanced
> This repo covers how to use the Reddit API and how to recurse.

### Resources:
* [Reddit API](https://www.reddit.com/dev/api/)

### Environment
* Language: Python 3.4.3
* OS: Ubuntu 14.04 LTS
* Style guidelines: [PEP 8 (version 1.7) for Python 3.5](https://www.python.org/dev/peps/pep-0008/) || [Google Style Python Docstrings](http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)
---
### Authors
John Mwega
