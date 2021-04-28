file_dict = { 1: "data\\acceptance.txt", 2: "data\\acceptance_self.txt", 3: "data\\anger.txt",
                  4: "data\\annoyance.txt", 5: "data\\anxiety.txt", 6: "data\\calmness.txt",
                  7: "data\\contentment.txt", 8: "data\\disgust.txt", 9: "data\\disgust_self.txt",
                  10: "data\\dislike.txt", 11: "data\\dislike_self.txt", 12: "data\\eagerness.txt",
                  13: "data\\fear.txt", 14: "data\\joy.txt", 15: "data\\melancholy.txt",
                  16: "data\\pleasantness.txt", 17: "data\\pleasantness_self.txt", 18: "data\\responsiveness.txt",
                  19: "data\\sadness.txt", 20: "data\\serenity.txt",}

total = 0

for i in range(1,20):
    with open(file_dict[i], "r", encoding='utf-8') as f:
        try:
            lines = f.read().split('\n')
            total += len(lines)
            print(file_dict[i], ": ", len(lines))
            f.close()
        except UnicodeDecodeError:
            print("UnicodeDecodeError in", file_dict[i])

print("Total: ", total)
