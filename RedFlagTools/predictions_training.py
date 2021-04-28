import pandas as pd

main_csv = "giga_csv_final.csv"
main_index = {0: 0, 1: 0, 2: 1002, 3: 2002, 4: 3002, 5: 4002, 6: 5002, 7: 6002, 8: 7002, 9: 8002, 10:9002}
fieldnames = ['Tweet', 'Category', 'Correct', 'Reviewed']
lines = []
# len(df.loc[(df['Category'] == "Anger") & (df['Correct'] >0 )])

def set_correction(pos, inp):
    #print("Set Correction Called")
    df.iat[int(pos), 2] = inp
    df.iat[int(pos), 3] = True
    df.to_csv(main_csv, index=False)

def get_category_accuracy(category):
    return  len(df.loc[(df['Category'] == category) & (df['Correct'] > 0 )]) / 1000

def get_total_accuracy():
    return len(df.loc[df['Correct'] == 1]) / 10000

def get_total():
    total = float(len(df.loc[df['Reviewed'] == True]))
    return [total, total/10000]

def draw_menu():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Choose where to start")
    print("1: Acceptance  2:Acceptance Self  3:Anger  4:Annoyance  5: Anxiety")
    print("6: Calmness  7:Contentment  8:Disgust  9:Disgust Self  10: Dislike Self")
    print("0: Start from first False")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

def work_row(key):
    row_counter = main_index[key]
    while True:

        # Continues to next unreviewed text
        if df.iloc[key + row_counter][3] == True:
            row_counter += 1
            continue

        category = df.iloc[key + row_counter][1]
        total_accuracy = get_total_accuracy()
        total = get_total()

        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(f"Total Accuracy: {total_accuracy}   {category} Accuracy: {get_category_accuracy(category)}       Total Done:{total[0]} / 10000  (%{total[1]*100})")
        print(f"Text||| {df.iloc[key + row_counter][0]} ")

        inp = input("[1/0/Q]: ")
        if inp.isdigit() == False and inp.lower() == "q":
            break
        if inp.isnumeric() and int(inp) in [1,0]:
            set_correction(key + row_counter, int(inp))
            row_counter += 1
        else:
            continue

def main():
    draw_menu()
    while True:
        inpnum = input("0-9 || Q:")
        if inpnum.isdigit() == False and inpnum.lower() == "q":
            break
        if inpnum.isdigit() and int(inpnum) >= 0 and int(inpnum) < 11:
            work_row(int(inpnum))
        else:
            print("Invalid Entry")
            continue

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__ == '__main__':
    df = pd.read_csv(main_csv)
    main()
