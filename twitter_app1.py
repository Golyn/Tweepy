import tweepy

# consumer keys and access tokens, used for OAuth  
consumer_key = 'TzhbLbg2xZM8j3DoIyTs9ZEJK'
consumer_secret = '6XJ2BUBAr2pCb7V0IJYLfy3b8rlapaOZ4bMbUXTbf95UJV7h9K'
access_token = '2655681531-NheA4n3VHUAmsIhwWRtU6yzRpldEuFLPYUeBy7L'
access_token_secret = 'V1AWnr9G5XbRsUeRw84G7ZzsUdf6ZhZ3SLmCmuZq2cLzY'

#OAuth process, using the keys and tokens
#creating authentication instance
def OAuth():
    try:
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        return auth
    except Exception as e:
        return None

#storing authentication instance in a variable
oauth = OAuth()
# creating API instance
api = tweepy.API(oauth)

#posting a tweet with the 'update.status' method
#api.update_status('#tweepy is bae')
print('tweet posted with python')

#getting info. about my profile info using "api.me()"
user = api.me()
print('Name: ' + user.name)
print('Location: ' + user.location)
print('Friends: ' + str(user.friends_count))
print('Followers: ' + str(user.followers_count))

# Get information about other users
users = api.get_user('@Kwatino')
print('Name: ' + users.name)
print('Location: ' + users.location)
print('Friends: ' + str(users.friends_count))
print('Followers: ' + str(users.followers_count))
