student=[("Amit",89),("Ram",87),("abc",90)]
sorted_student=sorted(student,key=lambda x:x[1],reverse=True)
# sorted_student=sorted(student,key=lambda x:x[0],reverse=True)  for sorting using name or key
print(sorted_student)