from twitter.models import User

class UserManagementHandler:

	def create_user(self, username, password, email, first_name):

		# password dhang se
		try:
			User.objects.create(
				username=username,
				password=password,
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
