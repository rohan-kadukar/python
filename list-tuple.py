# Create an list
# # Lists are mutable(can change)
list=[1,2,3,5,7,9,8,4,6]
# METHODS
# Find max no. in list
print(max(list))
# Find min no. in list
print(min(list))
# For sort an list --> It changes original list
list.sort()
print(list)
# Reverse an list --> It changes original list
list.reverse()
print(list)
#  Joint no. in list at last
#  Append changes original list
list.append(10)
print(list)
# Insert element at perticular positin in list
list.insert(10,11)  #changes original list
print(list)
# Removing an element
list.remove(10)
print(list)
# delete last element
list.pop()
print(list)


# # # Tuple
# # tuple are immutable(can not change)
# eg
tp=(1,2,3,5,69,8,7)
t=(1,)
print(tp)
print(t)