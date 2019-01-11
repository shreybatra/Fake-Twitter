from twitter.models import User, Follow

class FollowUnfollowHandler:

	def follow(self, user, fol_user):

		try:
			fol = Follow.objects.get(follower=user,following=fol_user)
			return False
		except:
			pass
		
		Follow.objects.create(follower=user,following=fol_user)

		return True

	def unfollow(self, user, fol_user):

		try:
			fol = Follow.objects.get(follower=user,following=fol_user)
		except:
			return False
		
		fol.delete()

		return True