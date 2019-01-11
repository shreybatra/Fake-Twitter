from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import json

from twitter.handlers import TweetHandler
from utils import check_login


@require_http_methods(['GET','POST','DELETE'])
def tweet(request):

	if request.method == 'POST':
		
		body = request.body.decode('utf8')
		body = json.loads(body)

		username = request.GET.get('username')
		tweet_text = body.get('tweet_text')

		if not (username and tweet_text):
			return JsonResponse({
				'data': {
					'msg': 'Invalid request'
					}
				}, status=400)

		if not check_login(username):
			return JsonResponse({
				'data': {
					'msg': 'Authentication failure. Please login.'
					}
				}, status=403)

		tweetHandler = TweetHandler()
		tweetHandler.create_tweet(username, tweet_text)

		return JsonResponse({
			'data': {
				'msg': 'Tweet created successfully.'
				}
			}, status=201)

	elif request.method == 'GET':
		
		body = request.body.decode('utf8')
		body = json.loads(body)

		username = request.GET.get('username')

		if not username:
			return JsonResponse({
				'data': {
					'msg': 'Invalid request'
					}
				}, status=400)

		if not check_login(username):
			return JsonResponse({
				'data': {
					'msg': 'Authentication failure. Please login.'
					}
				}, status=403)

		tweetHandler = TweetHandler()
		data, code = tweetHandler.get_tweets(username)

		return JsonResponse({
			'data': data
			}, status=code)
	else:

		body = request.body.decode('utf8')
		body = json.loads(body)

		username = request.GET.get('username')
		tweet_id = body.get('id')

		if not (username or tweet_id):
			return JsonResponse({
				'data': {
					'msg': 'Invalid request'
					}
				}, status=400)

		if not check_login(username):
			return JsonResponse({
				'data': {
					'msg': 'Authentication failure. Please login.'
					}
				}, status=403)

		tweetHandler = TweetHandler()
		if tweetHandler.delete_tweet(username, tweet_id):
			return JsonResponse({
				'data': {
					'msg': 'Tweet is successfully deleted.'
					}
				}, status=200)
		else:
			return JsonResponse({
				'data': {
					'msg': 'Tweet not found or cannot be deleted.'
					}
				}, status=404)
