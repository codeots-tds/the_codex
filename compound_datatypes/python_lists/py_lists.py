import time
programming_languages = ['C', 'Python', 'C++', 'Java', 'Kotlin', 'Ruby']
programming_languages2 = ['C', 'Python', 'C++', 'Java', 'Kotlin', 'Ruby']
add_languages = ['JavaScript', 'CoBal', 'Typescript', 'C#', 'Lua', 'R', 
'Php', 'Bash', 'Assembly', 'SQL']

#for loop
start_time = time.time()
for lang in add_languages:
    programming_languages += [lang]
end_time = time.time()
print(programming_languages, end_time - start_time)
print("-------------------------------------------")
print("-------------------------------------------")
#List comprehension
start_time2 = time.time()
programming_languages2 += [pro_lang for pro_lang in add_languages]
end_time2 = time.time()
print(programming_languages2, end_time2 - start_time2)