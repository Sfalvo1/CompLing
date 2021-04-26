def window():
    file_dict = { 1: "data\\acceptance.txt", 2: "data\\acceptance_self.txt", 3: "data\\anger.txt",
                  4: "data\\annoyance.txt", 5: "data\\anxiety.txt", 6: "data\\calmness.txt",
                  7: "data\\contentment.txt", 8: "data\\disgust.txt", 9: "data\\disgust_self.txt",
                  10: "data\\dislike.txt", 11: "data\\dislike_self.txt", 12: "data\\eagerness.txt",
                  13: "data\\fear.txt", 14: "data\\joy.txt", 15: "data\\melancholy.txt",
                  16: "data\\pleasantness.txt", 17: "data\\pleasantness_self.txt", 18: "data\\responsiveness.txt",
                  19: "data\\sadness.txt", 20: "data\\serenity.txt",}

    while True:
        inpnum = input("FileNum:")
        inp = input("utterance:")
        if inpnum == "q" or inp == "q":
            break
        else:
            add_to_file(file_dict[int(inpnum)], str(inp))


def add_to_file(file, utterance):
    with open(file, "a", encoding='utf-8') as f:
        f.write(utterance)
        f.write("\n")
        f.close()

if __name__ == '__main__':
    window()
