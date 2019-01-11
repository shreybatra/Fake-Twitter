from twitter.models import Tweet
from utils import authenticate_username


class TweetHandler:

	def create_tweet(self, username, tweet_text):

		Tweet.objects.create(
			username=authenticate_username(username),
			tweet_text=tweet_text
		)

		return None

	def get_tweets(self, username):

		try:
			data = Tweet.objects.filter(
				username=username
			)

			data = data.values()

			return list(data), 200
		except:
			return {
				'msg': 'Error is retrieving data.'
			}, 500

	def delete_tweet(self, username, tweet_id):

		try:
			tweet = Tweet.objects.get(
				username=username,
				id=tweet_id
			)

			tweet.delete()
			return True
		except:
			return False

