import tweepy, time, os

auth = tweepy.OAuthHandler('vRD8ltyfY8Rp3yyhB0TfsDlfy', '9c9tk3EmZuVp8M9W3s6Knoy7kpopgwcP2WQZ8fFOMOfzWOa6qp')
auth.set_access_token('3016452746-9ScXdyGu8QA0YJbaVRol646XHsyYgwMWO7iOqQK', 'Snx9skeHp8GSlq54ckamUsuErZEamEIwUDJDnEYFuy6lh')
api = tweepy.API(auth)


name =raw_input('Input screen name to like and retweet: ')
read=open('cache.txt','r+')

def likeBot():
    tweets = api.user_timeline(name)
    for tweet in tweets:
        if (str(tweet.id) + " ") not in read.read() and tweet.author.screen_name == (name):
            read.write('%s '%(tweet.id))
            try:
                api.retweet(tweet.id)
                api.create_favorite(tweet.id)
            except:
                break
            print("Liked and Retweeted: %s" %tweet.text)
            print("Scanning Tweets")
        time.sleep(10)
while(True):
    likeBot()
    x=60
    while x > 0:
        print("Sleeping: %s"%x)
        x-=1
        time.sleep(1)
        os.system("clear")
