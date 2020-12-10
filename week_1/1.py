str = input("Enter a String:\t")
for i in range(len(str)):
    print (' '*i, str[i])
for i in range(len(str)):
    print (' '*(len(str)-i), str[i])  