import tweepy

# consumer keys and access tokens, used for authentication 
consumer_key = 'TzhbLbg2xZM8j3DoIyTs9ZEJK'
consumer_secret = '6XJ2BUBAr2pCb7V0IJYLfy3b8rlapaOZ4bMbUXTbf95UJV7h9K'
access_token = '2655681531-NheA4n3VHUAmsIhwWRtU6yzRpldEuFLPYUeBy7L'
access_token_secret = 'V1AWnr9G5XbRsUeRw84G7ZzsUdf6ZhZ3SLmCmuZq2cLzY'

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
 
# creation of the actual interface, using authentication
# tweepy.api — Twitter API wrapper. This class provides a wrapper for the API as provided by Twitter.
api = tweepy.API(auth)

# tweeting
#api.update_status("#Meldermatix #AI model is pretty cool")

# Get information about yourself
user = api.me()
print('Name: ' + user.name)
print('Location: ' + user.location)
print('Friends: ' + str(user.friends_count))
print('Followers: ' + str(user.followers_count))
