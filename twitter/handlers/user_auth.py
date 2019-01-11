from twitter.models import User, Authentication
import hashlib

class UserAuthhandler:

	def authenticate(self, username, password):

		password = hashlib.sha256(password.encode())
		try:
			User.objects.get(
				username=username,
				password=password.hexdigest()
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
