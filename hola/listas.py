word = "hola"

print(word.splitlines)

print(word.title())

lst = ['abc', 123, 'def', 10.5, 62, ['g', 'h', 'i']]
print(lst[4:6])
print(len(lst))

lst.append("hola")
print(lst)

lst.remove("hola")
print(lst)

lst.pop(0)
print(lst)

lst.insert(5, "Hola como estas")
print(lst)

lst.sort()
print(lst)