students = ["Kenny", "Harry", "Adora"]
mascots = ["Dog", "Cat", "Bird"]
houses = ["A House", "B House", "C House"]
stud_dic = {}
for i in range(len(students)):
    print(i + 1, students[i])
    stud_dic[houses[i]] = [students[i], mascots[i]]
    

for i in stud_dic:
    print(f"{stud_dic[i][0]} is in {i}, which has a mascots that looks like a {stud_dic[i][1]}.")
        