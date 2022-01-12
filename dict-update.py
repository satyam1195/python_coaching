dict={
    "roll": '123',
    'college': "BBD",
    "sub": 'mech'

}

dict1={
    "roll": '576',
    'college': "VIT",
    "sub":'manf'

}

print(dict)
dict.update(dict1)
print(dict)


#print('sub' in dict1)
if 'sub' in dict1:
    print('true')
    print(dict['sub'])
else:
    print('No')

dict["marks"]=100
dict["height"]=5.6
print(dict)
#print(dict1["per"])
print(dict.get("per"))

for key in dict:
    print(key)

#print(dict.pop())
dict.pop('roll')
dict.pop('sub')
print(dict)

