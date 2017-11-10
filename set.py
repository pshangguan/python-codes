a=set([1,2,3,4,5,3,6,1])
print(a)

str="this is a long string with a lot of words"

words=str.split()
print(words)

for n in range(len(words)):
    print(words[n])

b=set(words)
print(b,len(b))
for n in range(len(b)):
    print(list(b)[n])
