from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from twitter.handlers import UserManagementHandler
import json


def home(request):
	return JsonResponse({
		'data':'Fake Twitter App built by ' \
			   'Shrey Batra for Postman interview.'
	})


@require_http_methods(['GET','POST'])
def user_management(request):

	if request.method == 'POST':
		
		body = request.body.decode('utf8')
		body = json.loads(body)

		username = body.get('username')
		password = body.get('password')
		first_name = body.get('first_name')
		email = body.get('email')

		if not (username and password and first_name and email):
			return JsonResponse({
				'data': {
					'msg': 'Invalid request body.'
				}
			}, status=400)

		userManagementHandler = UserManagementHandler()
		response = userManagementHandler.create_user(
			username=username,
			password=password,
			email=email,
			first_name=first_name
		)

		if response:
			return JsonResponse({
				'data': {
					'msg': 'User created successfully.'
				}
			}, status=201)

		else:
			return JsonResponse({
				'data': {
					'msg': 'Username already exists.'
				}
			}, status=409)

	else:

		userManagementHandler = UserManagementHandler()

		response = userManagementHandler.get_users()

		if type(response) == list:
			return JsonResponse({
				'data': response
			})

		else:
			return JsonResponse({
				'data': {
					'msg': 'Users cannot be due to - ' + response
				}
			}, status=500)
