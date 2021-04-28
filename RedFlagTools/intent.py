def check_input(input):
    approved_list = ["1","2","3"]
    if input not in approved_list:
        return False
    else:
        return True

def window():
    file_dict = { 1: "intent\\affective.txt", 2: "intent\\not_affective.txt", 3: "intent\\prescriptive.txt" }

    while True:
        inpnum = input("FileNum:")
        if check_input(inpnum) is False:
            continue
        if inpnum == "q":
            break
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