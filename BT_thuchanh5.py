with open('50.srt', 'r', encoding='utf-8') as file:
    db = file.readlines()
for line in db:
    print(line.strip())