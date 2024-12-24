immutable_war = 1,2,'a','b'
print(immutable_war)
immutable_war = (1,2,'a','b')
print(immutable_war)
print(type(immutable_war))
immutable_war = ([1,2],'a')
print(immutable_war)
immutable_war [0][1] =3
print(immutable_war)
mutable_list = [1,2,3,'a','b','banana']
print(mutable_list)
print(type(mutable_list))
mutable_list[5] = 'Modifaide'
print(mutable_list)
mutable_list.remove(3)
print(mutable_list)



