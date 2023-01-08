import time

programming_languages = ['C', 'Python', 'C++', 'Java', 'Kotlin', 'Ruby']
add_languages = ['JavaScript', 'CoBal', 'Typescript', 'C#', 'Lua', 'R', 
'Php', 'Bash', 'Assembly', 'SQL']

#Append:
# programming_languages.append(add_languages[2])
# programming_languages += [add_languages[0]]

#Extend:
# programming_languages.extend(add_languages[3:5])

#Insert:
# programming_languages.insert(1, add_languages[6])
# programming_languages.insert(2, add_languages[2:4])

#Index:
# index_loc = programming_languages.index(add_languages[6])
# print(programming_languages,index_loc)

#Copy
programming_languages2 = programming_languages.copy()

#Pop
# programming_languages2.pop(3)

#Clear
# programming_languages2.clear()

#Remove
# print(programming_languages2)
# programming_languages2.remove("Java")
# print(programming_languages2)

#Reverse
# print(programming_languages2)
# programming_languages2.reverse()
# print(programming_languages2)

#Sort
# print(programming_languages2)
# programming_languages2.sort()
# programming_languages2.sort(reverse = True)
# print(programming_languages2)

#Count
programming_languages2 += ['Java']
# programming_languages2.sort(reverse = True)
print(programming_languages2)
print(programming_languages2.count('Java'))