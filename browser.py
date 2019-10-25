import praw
import login

client_id = 'gMuenas4Y-YSDA'
client_secret = 'KUjFTaUkYH8yRJDjr9Ea8IBYNJ0'

reddit = praw.Reddit(client_id, client_secret, username=login.username,
                     password=login.password, user_agent='reddit_browser')


