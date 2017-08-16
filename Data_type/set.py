val1= set("abcdefg")
print(val1)
val2= set("ghijk")
print(val2)
val1.add(5)
val1.update([4,6,5])
print(val1)

#val1.discard(5)
#print(val1)
#val1.remove('c')
#print(val1)
#temp=val1.pop()
#print(temp)
#val1.clear()

val3=val1|val2
print(val3)

val3=val1&val2
print(val3)

val3=val1^val2
print(val3)

val3=val1-val2
print(val3)

va=val1.isdisjoint(val2)
print(va)

val1.intersection_update(val2) #update the set val1 to the result
print(val1)
