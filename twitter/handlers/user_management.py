from twitter.models import User
import hashlib

class UserManagementHandler:

	def create_user(self, username, password, email, first_name):
		'''Creates a new User object in database.'''
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
		'''Gets a list of users present in the database.'''
		try:
			data = User.objects.all()
			data = data.values('username', 'email')
			return list(data)

		except Exception as err:
			return str(err)
