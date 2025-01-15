simple_array = [[2, 5, 8], [3, 7, 4], [1, 6, 9]]
print(simple_array)
print(simple_array[1])
simple_array[2][1] = 5
print(simple_array[1][2])
print(simple_array[2][1])
simple_array[1].append(3)

data_set = {"A": {"x":54, "y":82, "z":91}, "B": {"x":75, "y":74, "z":80 }}
print(data_set["A"])
print(data_set["B"]["y"])

for i in data_set:
    print(data_set[i]["y"])

data_set["B"]["y"] = 53
print(data_set["B"]["y"])

grades_list = [[45, 37, 54], [62, 58, 59], [49, 47, 60], [78, 83, 62]]
grades_dictionaries = {"Susan": {"Math": 45, "Eng": 37, "Sci": 54}, "Peter":{"Math": 62, "Eng": 58, "Sci": 59}, "Ezra": {"Math": 49, "Eng": 64, "Sci": 84}}

def input_score():
    name = input("Enter the name of the student: ")
    mscore = int(input("Enter the student's result in Mathematics: "))
    escore = int(input("Enter the student's result in English: "))
    sscore = int(input("Enter the student's result in Science: "))
    grades[name] = {"Math": mscore, "Eng": escore, "Sci": sscore}

grades = {}
num = int(input("Enter the number of students whose marks you want to enter: "))

for i in range (0, num):
    input_score()

print(grades)