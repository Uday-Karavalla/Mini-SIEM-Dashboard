with open("logs.txt", "r") as file:
    logs = file.readlines()

for log in logs:
    print(log.strip())