

# print('x y z')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             if ((x or y) <=(z == x)) == False:
#                 print(x, y, z)
                

#2
# print("x y z w")
# for x in range(0, 2):
#     for y in range(0, 2):
#         for z in range(0, 2):
#             for w in range(0, 2):
#                 if ((x and (not y)) or (y == z) or (not w)) == False:
#                     print(x, y, z, w)
                    

#3
# print("x y z w")
# for x in range(0, 2):
#     for y in range(0, 2):
#         for z in range(0, 2):
#             for w in range(0, 2):
#                 if ((( x <= y) == (y <= z)) and (y or w)) == True:
#                     print(x, y, z, w)


#4
# print("x y z w")
# for x in range(0, 2):
#     for y in range(0, 2):
#         for z in range(0, 2):
#             for w in range(0, 2):
#                 if (x and (not y) or (y == z) or (not w)) == False:
#                     print(x, y, z, w)
                    
#5
# print('x y z w F')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 F = ((x <= y) == (z <= (not w)) and (z or y))
#                 print(x, y, z, w, int(F))
                
#6
print('x y z w F1 F2')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F1 = ((w == x) and (z <=y))
                F2 = ((w <= x) <= (y == z))
                print(x, y, z, w, int(F1), ' ',  int(F2))