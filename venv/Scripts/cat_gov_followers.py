# this code returns all FOLLOWERS from the user @catalan_gov

import csv
import time
import tweepy

#authorization
auth = tweepy.OAuthHandler(APP_KEY, APP_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
api = tweepy.API(auth)

def retrieve_followers_from_user(user):
    # make a list of followers in CSV-file
    with open("cat_gov_followers.csv", 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(["id", "name", "location"])
        # extracting all followers of user profile
        users = tweepy.Cursor(api.followers, screen_name=user).items()
        while True:
            try:
                u = users.next()
                writer.writerow([u.id, u.screen_name, u.location])
            except tweepy.TweepError:
                print('Rate limit exceeded. Sleeping for 15 minutes')
                time.sleep(15*60)
                u = users.next()
                writer.writerow([u.id, u.screen_name, u.location])
                continue
            except StopIteration:
                break

if __name__ == '__main__':
    retrieve_followers_from_user('catalan_gov')