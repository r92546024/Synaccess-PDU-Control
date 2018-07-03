#####  https://www.cnblogs.com/shaosks/p/6879541.html>


### Test 1
print ('###########Test1####################')
def xxxList(val,list=[]):
    list.append(val)
    return list

def NormalList(val,list=None):
    if list == None:
        list = []
    list.append(val)
    return list

list1=xxxList(10)
list2=xxxList(123,[])
list3=xxxList('a')

print (list1)
print (list2)
print (list3)



### Test 2
print ('#########Test2######################')
def multipliers():
    return [lambda x : i * x for i in range(4)]

print ( [m(2)for m in multipliers() ] )




#### Test 3
print ('#########Test3######################')
class Parent(object):
    x=1

class Child1(Parent):
    pass

class Child2(Parent):
    pass

print ( Parent.x, Child1.x, Child2.x )
Child1.x = 2
print ( Parent.x, Child1.x, Child2.x )
Parent.x = 3
print ( Parent.x, Child1.x, Child2.x )




#### Test 4
print ('#########Test4######################')
def div1(x,y):
    print ("%s/%s = %s" %(x,y, x/y) )

def div2(x,y):
    print("%s//%s = %s"%(x,y, x//y))


div1(5,2)
div1(5.,2)
div2(5,2)
div2(5.,2.)




#### Test 5
print ('#########Test5######################')

list = ['a','b','c','d','e']

print (list[3])
print (list[1:3])
print (list[10:])

print (list[-3])
print (list[-3:])
print (list[:-10])






#### Test 6
print ('#########Test6######################')

list = [[]]*5
print (list) # output?

list[0].append(10)
print (list)# output?

list[1].append(20)
print (list)# output?

list.append(30)
print (list)# output?


matrix=[]
matrix.append([])
matrix.append([])
matrix[0].append(3)
matrix[0].append(5)
matrix[0].append(6)
matrix[0].append(7)
matrix[0].append(8)
matrix[1].append(4)
matrix[1].append(5)
matrix[1].append(3)
matrix[1].append(2)
matrix[1].append(3)
print(matrix)

#### Test 7
print ('#########Test7######################')
#a[start:end:step] # start through not past end, by step

list = [ 1 , 3 , 5 , 8 , 10 , 13 , 18 , 36 , 78 ]

# method 1
print ( [x for x in list[::2] if x % 2 == 0] )

# method 2
listA = []
for x in list[::2] :
    if x % 2 ==0 :
        listA.append(x)

print (listA)





#### Test 8
print ('#########Test8######################')

class DefaultDict(dict):
    def __missing__(self,key):
        return []

d=DefaultDict()
d['florp']=127

print (d)



### Lambda
print ('#########lambda######################')
SUM  = lambda x,y,z : x+y+z
print (SUM(1,2,3))

f = lambda x: x ** x
print(f(2))

g = lambda x, y: x * y
print(g(2, 6))