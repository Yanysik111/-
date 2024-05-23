grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = sorted(students)
average1= sum(grades[0])/len(grades[0])
average2 = sum(grades[1])/len(grades[1])
average3 = sum(grades[2])/len(grades[2])
average4 = sum(grades[3])/len(grades[3])
average5 = sum(grades[4])/len(grades[4])
result = dict()
result[students[0]] = average1
result[students[1]] = average2
result[students[2]] = average3
result[students[3]] = average4
result[students[4]] = average5
print(result)