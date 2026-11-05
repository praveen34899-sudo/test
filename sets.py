skills={"sql","python","excel"}
skills.add('power bi')
print(skills)
skills.update(["ml","ai"])
print(skills)
skills.discard("ml") #it remove the specified value if its available or not
print(skills)
skills.remove("ai") #it also remove the specified value but it not accept any other value which is not in the set
print(skills)
