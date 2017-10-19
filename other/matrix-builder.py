# ex = {
#     0: {0:1},
#     0: {1:2},
#     1: {0:3},
#     1: {1:4}
# }

#print ex

# num=3
def matrix_builder(num, i):
    a = {}
    while i < num:
        a[i] = {i:i+1}
        a[i+1] = {i+1:9}
        i+=1
    print a

matrix_builder(2, 0)
