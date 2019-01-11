from twitter.models import Authentication, User


def check_login(username):
	'''Checks if a username is already logged in.'''
	try:
		user = User.objects.get(username=username)
		auth = Authentication.objects.get(username=user)
		return True
	except:
		return False


def authenticate_username(username):
	'''Authenticates if user with given username is present in database.'''
	try:
		user = User.objects.get(username=username)
		return user
	except:
		return False