data = {'roll_num':[],
		'name':[],
		'age':[],
		'marks':[]}
	


# str=str(myList)
# rollNumbers="cs182019"
# key="roll_num"
# data[key].append(rollNumbers)
# str=data['roll_num']

def printDict():
    print(data)

def appendDict(dict):
    dict = []
    check="n"
    check = input("Do you want to enter a record ? press (y) to yes and any key for no: ")
    while check=='y':
            key='roll_num'
            record=input("Enter Roll Number :")
            dict[key].append(record)
            key='name'
            record=input("Enter Name :")
            dict[key].append(record)
            key='age'
            record=input("Enter Age :")
            dict[key].append(record)
            key='marks'
            record=input("Enter Marks :")
            dict[key].append(record)
            check = input("\nDo you want to enter a record ? press (y) or (any key) :") 
            

appendDict(data)
printDict()