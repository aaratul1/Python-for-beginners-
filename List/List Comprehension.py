List Comprehension

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)



With list comprehension you can do all that with only one line of code:


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)



The Syntax
newlist = [expression for item in iterable if condition == True]



Condition
The condition is like a filter that only accepts the items that evaluate to True.
Only accept items that are not "apple":

newlist = [x for x in fruits if x != "apple"]










The condition if x != "apple"  will return True for all elements other than "apple", making the new list contain all fruits except "apple".
newlist = [x for x in fruits]














