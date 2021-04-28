file_dict = { 1: "intent\\affective.txt", 2: "intent\\not_affective.txt", 3: "intent\\prescriptive.txt" }

total = 0

for i in range(1,4):
    with open(file_dict[i], "r", encoding='utf-8') as f:
        try:
            lines = f.read().split('\n')
            total += len(lines)
            print(file_dict[i], ": ", len(lines))
            f.close()
        except UnicodeDecodeError:
            print("UnicodeDecodeError in", file_dict[i])

print("Total: ", total)