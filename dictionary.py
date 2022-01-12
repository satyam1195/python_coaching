dict={
    'roll': 123,
    'name':'raaj',
    'contact':1234,
    'email':'123@gmail.com',
    'address':'lucknow',

}

print(dict['roll'])
dict['roll']=415
print(dict['roll'])


'''for i in dict:
    print(dict[i],end="")'''

#update
lst=[1,2,3,4,5,6,7]
dict={}
for x in range(0,len(lst)):
    dict.update({'Var %s'%x:lst[x]})
print(dict)