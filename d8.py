text_file = open('d8.txt', 'r')
lines = text_file.read().split()

data = [int(i) for i in lines]
# data = [2, 3, 1, 3, 0, 1, 90, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2]
#       A-----------------------------------------------------------
#             B-------------------------- C-----------------
#                   D-------                    E-------
# metadata = 90+99+10+11+12+2+1+1+2
# print metadata
# total = 138+90 = 228
# print total
print data

metas = []
def remove_children(data):
    global metas
    global c
    while len(data)>1:
        for i in range(0,len(data),2):
            node = data[i]
            if node == 0:
                meta = data[i+1]
                idx0 = i
                idx1 = i+1+meta
                metas.extend(data[i+2:i+2+meta])
                data[i-2] += -1
                data = data[:idx0]+data[idx1+1:]
                break
            else:
                continue
    return metas, data

metas,data = remove_children(data)
print sum(metas)


