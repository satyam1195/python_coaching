demo={
    "roll": 123,
    "sub":"phy",
    "marks": 75,
}

demo.setdefault("father","mark")

print(demo)
demo.setdefault("roll",145)
#demo.setdefault("father","ram")
print(demo)
demo1=demo

cpdemo=demo.copy()
print(cpdemo)
print(id(cpdemo))
print(id(demo1))
print(len(demo))


demo={
    "roll":123,
    "sub":"remote",
    "marks":100
}

demo1={
    "marks":100,
    "roll":123,
    "sub":"remote"
}
print(demo==demo1)