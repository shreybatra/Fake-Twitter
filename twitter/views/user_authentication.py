from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from twitter.models import User
from twitter.handlers import UserAuthhandler
import json

from utils import check_login


@require_http_methods(['PATCH'])
def user_login(request):
	'''Login a user.

	Request Parameters -
		request - Django request object.

	Response Parameters - 
		200 - Login successful.
		400 - Invalid request. (missing parameters or username)
		401 - Invalid Credentials.
		409 - User is already logged in.
	'''
	body = request.body.decode('utf8')
	body = json.loads(body)

	username = request.GET.get('username')
	password = body.get('password')

	if not (username and password):
		return JsonResponse({
			'data': {
				'msg': 'Invalid request body.'
			}
		}, status=400)

	userAuthhandler = UserAuthhandler()
	auth = userAuthhandler.authenticate(
		username=username,
		password=password
	)

	if auth:
		if check_login(username):
			return JsonResponse({
				'data': {
					'msg': 'User is already logged in.'
				}
			}, status=409)

		else:
			if userAuthhandler.login_user(username):
				return JsonResponse({
					'data': {
						'msg':'Login successful.'
					}
				})

			else:
				return JsonResponse({
					'data': {
						'msg': 'Username not found.'
					}
				}, status=404)

	else:
		return JsonResponse({
			'data': {
				'msg': 'Invalid credentials'
			}
		}, status=401)


@require_http_methods(['PATCH'])
def user_logout(request):
	'''Logout a user.

	Request Parameters -
		request - Django request object.

	Response Parameters - 
		200 - Logout Successful.
		400 - Invalid request. (missing parameters or username) 
		400 - Invalid username or user already logged out.
	'''
	body = request.body.decode('utf8')
	body = json.loads(body)

	username = request.GET.get('username')

	if not username:
		return JsonResponse({
			'data': {
				'msg': 'Invalid request.'
				}
			}, status=400)

	userAuthhandler = UserAuthhandler()
	
	if userAuthhandler.logout_user(username):
		return JsonResponse({
			'data': {
				'msg': 'Logout successful.'
			}
		})

	return JsonResponse({
		'data': {
			'msg': 'Invalid username or user already logged out.'
			}
		}, status=400)


