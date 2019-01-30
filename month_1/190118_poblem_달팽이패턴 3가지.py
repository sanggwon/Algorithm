list_data = [[0]*5 for i in range(5)]
write_count = 1
num = 1
idx_i = 2
idx_j = 2
sw = -1

while write_count < 6:
    for i in range(write_count):
        list_data[idx_i][idx_j] = num
        idx_j += sw
        num += 1

    if write_count == 5 :
        break
    for i in range(write_count):
        list_data[idx_i][idx_j] = num
        idx_i += sw
        num += 1

    write_count += 1
    sw = -sw

print(list_data)


list_data = [[0]*5 for i in range(5)]
write_count = 1
num = 1
idx_i = 2
idx_j = 2
sw = -1

while write_count < 6:
    for i in range(write_count):
        list_data[idx_i][idx_j] = num
        idx_j -= sw
        num += 1

    if write_count == 5 :
        break
    for i in range(write_count):
        list_data[idx_i][idx_j] = num
        idx_i -= sw
        num += 1

    write_count += 1
    sw = -sw

print(list_data)

list_data = [[0]*5 for i in range(5)]
write_count = 1
num = 1
idx_i = 2
idx_j = 2
sw = -1

while write_count < 6:
    for i in range(write_count):
        list_data[idx_i][idx_j] = num
        idx_j += sw
        num += 1

    if write_count == 5 :
        break
    for i in range(write_count):
        list_data[idx_i][idx_j] = num
        idx_i += sw
        num += 1

    write_count += 1
    sw = -sw

print(list_data)


list_data = [[0]*5 for i in range(5)]
write_count = 1
num = 1
idx_i = 2
idx_j = 2
sw = -1

while write_count < 6:
    for i in range(write_count):
        list_data[idx_i][idx_j] = num
        idx_j += sw
        num += 1

    sw = -sw

    if write_count == 5 :
        break
    for i in range(write_count):
        list_data[idx_i][idx_j] = num
        idx_i += sw
        num += 1

    write_count += 1
    

print(list_data)