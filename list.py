#declaring our list
names = ["John", "Bob", "Mosh", "Sam", "Mary"]
# print(names)

#change
names[0] = "James"
# print(names)

#index
# print(names[0:3])

#add item
names.append("Melvin")
# print(names)
#add at specific point
names.insert(3, "Sarah")
# print(names)

#remove
names.remove("Melvin")
# print(names)

#membership
# print("Sarah" in names)

#length of the list
# print(len(names))

#looping
for name in names:
    print(name)