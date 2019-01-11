from twitter.models import User
import hashlib

class UserManagementHandler:

	def create_user(self, username, password, email, first_name):

		password = hashlib.sha256(password.encode())
		try:
			User.objects.create(
				username=username,
				password=password.hexdigest(),
				email=email,
				first_name=first_name
			)
			return True
		except:
			return False

	def get_users(self):

		try:
			data = User.objects.all()
			data = data.values('username', 'email')
			return list(data)

		except Exception as err:
			return str(err)
