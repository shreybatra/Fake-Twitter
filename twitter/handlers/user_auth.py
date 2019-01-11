from twitter.models import User, Authentication


class UserAuthhandler:

	def authenticate(self, username, password):

		try:
			User.objects.get(
				username=username,
				password=password
			)
			return True

		except:
			return False


	def login_user(self, username):
	
		try:
			user = User.objects.get(username=username)
			auth = Authentication.objects.get(username=user)
			return False

		except:
			Authentication.objects.create(username=user)
			return True


	def logout_user(self, username):

		try:
			user = User.objects.get(username=username)
			auth = Authentication.objects.get(username=user)
			auth.delete()
			return True

		except:
			return False
