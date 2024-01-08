n = int(input())
usernames = set()

for _ in range(n):
    user = input()
    usernames.add(user)
for users in usernames:
    print(users)
    