append items

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)




insert items

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)



extend items

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)


Add Any Iterable
The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
