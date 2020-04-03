
list = [[1,2,3],4,5,6,[8,9],[[44,55,66],[66,77],["hello","python","welcome"]]]
print(list[0][-1]) #3
print(list[2]) #5
print(list[5][0][1])#55

print(list[5][1][1])#77

print(list[5][0][0])#44

print(list[5][1][0])#66
                                                 
print(list[5][2][0])#hello
print(list[5][2][1])#python
print(list[5][2][2])#welcome
print(list[5][2][0][2:])#llo
                                               
print(list[5][2][1][2:])#thon

print(list[5][2][-1][-4:])#come
































