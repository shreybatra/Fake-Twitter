from twitter.models import Authentication, User


def check_login(username):
	try:
		user = User.objects.get(username=username)
		auth = Authentication.objects.get(username=user)
		return True
	except:
		return False


def authenticate_username(username):
	try:
		user = User.objects.get(username=username)
		return user
	except:
		return False