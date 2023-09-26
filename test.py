file = open("token.txt", "r")
read = file.readlines()

TOKEN = read[0]
print(TOKEN)

# with open("token.txt") as token_file:
#     TOKEN = token_file.readline(0)
#     print(TOKEN)