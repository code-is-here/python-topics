for i in zip([1,2,3], ['a','b','c']):
	print(i)

print("=========")

for i in zip([1,2,3]):
	print(i)

print("========")

for i in zip([1,2,3],['a','b','c'],['#','!','@']):
	print(i)



print(set(zip([1,2],[3,4,5])))

print("========")

z=zip([1,2,3],['a','b','c'],['#','*','$'])
a,b,c = zip(*z)
print(a,b)