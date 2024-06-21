grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

student_list = sorted(students)#сортировка множества по возрастанию
sred_bal = [(sum(grades[0]) / len(grades[0])),#суммируем оценки и делим на кол-во оценок
                     (sum(grades[1]) / len(grades[1])),
                     (sum(grades[2]) / len(grades[2])),
                     (sum(grades[3]) / len(grades[3])),
                     (sum(grades[4]) / len(grades[4]))]
sred_bal_students = dict(zip(student_list, sred_bal))#создаем словарь и объединяем элементы
print(sred_bal_students)
