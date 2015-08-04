import pylast
import tweepy
import Keys

def tweet(status):
    # == OAuth Authentication ==
    #
    # This mode of authentication is the new preferred way
    # of authenticating with Twitter.
    auth = tweepy.OAuthHandler(Keys.TWITTER_API_KEY, Keys.TWIITER_API_SECRET)
    auth.secure = True
    auth.set_access_token(Keys.TWITTER_ACCESS_TOKEN, Keys.TWITTER_ACCESS_TOKEN_SECRET)
    
    api = tweepy.API(auth)
    
    # If the authentication was successful, you should
    # see the name of the account print out
    # print(api.me().name)
    
    # If the application settings are set for "Read and Write" then
    # this line should tweet out the message to your account's
    # timeline. The "Read and Write" setting is on https://dev.twitter.com/apps
    api.update_status(status=status)

def get_status():
    network = pylast.LastFMNetwork(api_key = Keys.LASTFM_API_KEY, api_secret =
        Keys.LASTFM_API_SECRET, username = Keys.LASTFM_USERNAME, password_hash = Keys.LASTFM_PASSWORD_HASH)
        
    top = network.get_user(Keys.LASTFM_USERNAME).get_top_artists(pylast.PERIOD_7DAYS, limit=3)
    
    artists = ['{0} ({1})'.format(a.item.name, a.weight) for a in top]
    if len(artists) == 3:
        return 'My Top 3 #lastfm Artists: {0}, {1} & {2}'.format(artists[0], artists[1], artists[2])
    elif len(artists) == 2:
        return 'My Top 2 #lastfm Artists: {0} & {1}'.format(artists[0], artists[1])
    elif len(artists) == 1:
        return 'My Top 1 #lastfm Artists: {0}'.format(artists[0])
    else:
        return 'My Top Zero #lastfm Artists: None'

def main():
    status = get_status()
    print status
    tweet(status)
    #My Top 3 #lastfm Artists: Foo Fighters (77), Tremonti (51) & Metallica (35) via @tweeklyfm
    
    
if __name__ == '__main__':
   	main()
