import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]



#option1
print(random.choice(friends))

#option2
random_friend=random.randint(0,4)
print(friends[random_friend])