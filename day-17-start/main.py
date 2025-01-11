class User:

    def __init__(self,user_id,username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.followings = 0

    def follow(self,user):
        user.followers +=1
        self.followers +=1

user_1 = User("001","necati")
user_2 = User("002","efe")

user_1.follow(user_2)

print(user_1.followers)
print(user_1.followings)
print(user_2.followers)
print(user_2.followings)

