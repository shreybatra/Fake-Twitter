# Fake Twitter Application
## Developed by Shrey Batra for Postman Interview


This application is only the backend part exposing a number of API's given below.

To setup the application follow the steps - 
- Install python > v3.5.2
- Install virtualenv - ```pip install virtualenv```
- Make a virtualenv - ```virtualenv venv```
- Activate the environment - ```source venv/bin/activate```
- Install packages with command ```pip install -r requirements.txt```
- Install PostgreSQL via brew/apt-get/installer.
- Create database and user with following confirguration -
```
User name - faketwitteruser
Db Name - faketwitter
Password - faketwitter

GRANT ALL PRIVILEGES ON DATABASE faketwitter TO faketwitteruser;
```
- Change directory to folder base - ```cd fake_twitter_project```
- Run migrations by - ```python manage.py migrate```
- Run the server - ```python manage.py runserver```



## API Endpoints -->


### 1. User registration (Create User)
endpoint - */fake_twitter/v1/user* **POST**
Sample request body (all keys necessary) - 
```
{
	"username": "shreybatra",
	"first_name": "shrey",
	"password": "test123",
	"email": "shreybatra97@gmail.com"
}
```
Sample responses - 
- 201 - User successfully created.
- 400 - Invalid request body.
- 409 - Username already present.



**Note: - ALL endpoints furthur than this require username in URL for authentication.
No API below will work if the user is not logged in.**


### 2. User Login
endpoint - */fake_twitter/v1/authenticate/_login?username={username}* **PATCH**
Sample request body (all keys necessary) - 
```
{
	"password": "test123"
}
```
Sample responses - 
- 200 - Login successful.
- 400 - Invalid request. (missing parameters or username)
- 401 - Invalid Credentials.
- 409 - User is already logged in.


### 3. User Logout
endpoint - */fake_twitter/v1/authenticate/_logout?username={username}* **PATCH**
Sample request body (all keys necessary) - 
```
	(Empty body)
```
Sample responses - 
- 200 - Logout Successful.
- 400 - Invalid request. (missing parameters or username) 
- 400 - Invalid username or user already logged out.


### 4. Follow a user
endpoint - */fake_twitter/v1/user/_follow?username={username}* **PATCH**
Sample request body (all keys necessary) - 
```
{
	"follow_user": "user_xyz"
}
```
Sample responses -
- 200 - Followed successfully.
- 400 - Invalid request. (missing parameters or username)
- 400 - Cannot follow self.
- 400 - Invalid username or follow_user.
- 403 - Authentication failure.
- 409 - Already followed.


### 5. Unfollow a user
endpoint - */fake_twitter/v1/user/_unfollow?username={username}* **PATCH**
Sample request body (all keys necessary) - 
```
{
	"unfollow_user": "user_xyz"
}
```
Sample responses -
- 200 - Unfollowed successfully.
- 400 - Invalid request. (missing parameters or username)
- 400 - Cannot follow self.
- 400 - Invalid username or unfollow_user.
- 403 - Authentication failure.
- 409 - Already unfollowed.


### 6. Create a tweet
endpoint - */fake_twitter/v1/tweet?username={username}* **POST**
Sample request body (all keys necessary) - 
```
{
	"tweet_text": "Some tweet body."
}
```
Sample responses - 
- 201 - Tweet created successfully.
- 400 - Invalid request. (missing parameters or username)
- 403 - Authentication failure.


### 7. Read tweets
endpoint - */fake_twitter/v1/tweet?username={username}* **GET**
Sample responses - 
- 200 - List of tweets of given username.
- 400 - Invalid request. (missing parameters or username)
- 403 - Authentication failure.


### 8. Delete tweet
endpoint - */fake_twitter/v1/tweet?username={username}* **DELETE**
Sample request body (all keys necessary) - 
```
{
	"id":3
}
```
Sample responses - 
- 200 - Tweet deleted successfully.
- 400 - Invalid request. (missing parameters or username)
- 403 - Authentication failure.
- 404 - tweet with given id not found.


####**Extra endpoint to retrive users -**
endpoint - */fake_twitter/v1/user* **GET**
Sample responses -
- 200 - List of users.
