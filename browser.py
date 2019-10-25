import praw
import login

client_id = '37vflv4sf4SxNA'
client_secret = 'U9dY8AHct7LgzmiCEfPvymbyr8Y'

reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, username=login.username,
                     password=login.password, user_agent='reddit_browser')

subreddit = reddit.subreddit('DragonBallLegends')

hot_dblegends = subreddit.hot(limit=5)

for submission in hot_dblegends:
    if not submission.stickied:     # pinned submissions
        print(f'{submission.title} Up: {submission.ups} Down: {submission.downs} Visited: {submission.visited}')
