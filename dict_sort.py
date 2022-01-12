Dict={
    'somu':18,
    'ram':12, 
    'bheem':25
}

student=list(Dict.keys())
student.sort()
print(student)

for i in range(0,len(student)):
    dict={}
    dict[student[i]]=Dict[student[i]]
    print(dict)


'''set1={"a","a","a"}
print(set1)'''