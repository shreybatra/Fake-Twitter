from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from twitter.handlers import FollowUnfollowHandler
import json

from utils import check_login, authenticate_username


@require_http_methods(['PATCH'])
def follow_user(request):
	'''Follows a user.

	Request Parameters -
		request - Django request object.

	Response Parameters - 
		200 - Followed successfully.
		400 - Invalid request. (missing parameters or username)
		400 - Cannot follow self.
		400 - Invalid username or follow_user.
		403 - Authentication failure.
		409 - Already followed.
	'''
	body = request.body.decode('utf8')
	body = json.loads(body)

	username = request.GET.get('username')
	follow_user = body.get('follow_user')

	if not (username and follow_user):
		return JsonResponse({
			'data': {
				'msg': 'Invalid request.'
			}
		}, status=400)

	if not check_login(username):
		return JsonResponse({
			'data': {
				'msg': 'Authentication failure. Please login.'
			}
		}, status=403)

	if username == follow_user:
		return JsonResponse({
			'data': {
				'msg': 'Cannot follow self.'
			}
		}, status=400)

	user = authenticate_username(username) 
	fol_user = authenticate_username(follow_user)

	if not (user and fol_user):
		return JsonResponse({
			'data': {
				'msg': 'Invalid username or follow_user.'
			}
		}, status=400)

	followUnfollowHandler = FollowUnfollowHandler()
	response = followUnfollowHandler.follow(user,fol_user)

	if response:
		return JsonResponse({
			'data': {
				'msg': 'Followed user successfully.'
			}
		})

	else:
		return JsonResponse({
			'data': {
				'msg': 'The requested user is already followed.'
			}
		}, status=409)


@require_http_methods(['PATCH'])
def unfollow_user(request):
	'''Unfollows a user.

	Request Parameters -
		request - Django request object.

	Response Parameters - 
		200 - Unfollowed successfully.
		400 - Invalid request. (missing parameters or username)
		400 - Cannot unfollow self.
		400 - Invalid username or unfollow_user.
		403 - Authentication failure.
		409 - Already unfollowed.
	'''
	body = request.body.decode('utf8')
	body = json.loads(body)

	username = request.GET.get('username')
	unfollow_user = body.get('unfollow_user')

	if not (username and unfollow_user):
		return JsonResponse({
			'data': {
				'msg': 'Invalid request.'
				}
			}, status=400)

	if not check_login(username):
		return JsonResponse({
			'data': {
				'msg': 'Authentication failure. Please login.'
				}
			}, status=403)

	if username == unfollow_user:
		return JsonResponse({
			'data': {
				'msg': 'Cannot unfollow self.'
				}
			}, status=400)

	user = authenticate_username(username) 
	unfol_user = authenticate_username(unfollow_user)

	if not (user and unfol_user):
		return JsonResponse({
			'data': {
				'msg': 'Invalid username or unfollow_user.'
			}
		}, status=400)


	followUnfollowHandler = FollowUnfollowHandler()
	response = followUnfollowHandler.unfollow(user,unfol_user)

	if response:
		return JsonResponse({
			'data': {
				'msg': 'Unfollowed user successfully.'
			}
		})

	else:
		return JsonResponse({
			'data': {
				'msg': 'The requested user is already unfollowed.'
			}
		}, status=409)