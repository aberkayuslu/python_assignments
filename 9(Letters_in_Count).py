letter = str(input("Please Enter Your Sentence: "))


dic = {}

for i in letter:

    letter_count = letter.count(i)
    dic[i]= letter_count

print(dic)
