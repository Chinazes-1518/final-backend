import json

with open('randompcs.json', 'r') as f:
    data = json.load(f)

mtx = [[-1] * 4 for _ in range(4)]

newchunks = []

for i, chunk in enumerate(data):
    edgetop = chunk[63]
    edgebottom = chunk[0]
    edgeright = [chunk[i][63] for i in range(63)]
    edgeleft = [chunk[i][0] for i in range(63)]
    newchunks.append((i, edgetop, edgebottom, edgeright, edgeleft))

# print(newchunks)


def iswhite(arr):
    return all(map(lambda z: z == 255, arr))


def i_have(i):
    for m in mtx:
        if i in m:
            return True
    return False


def diff(r1, r2):
    differences = [abs(r1[i] - r2[i]) for i in range(63)]
    avg_diff = sum(differences) / len(differences)
    return avg_diff


TOP = 1
BOTTOM = 2
RIGHT = 3
LEFT = 4


def get_edge(i, j, side):
    return newchunks[mtx[i][j]][side]


running = True
i = 0
# z = 0
while running:
    if not i_have(i):
        # for i, top, bottom, right, left in newchunks:
        _, top, bottom, right, left = newchunks[i]
        topw, bottomw, rightw, leftw = iswhite(top), iswhite(bottom), iswhite(right), iswhite(left)
        if topw and leftw:
            mtx[0][0] = i
        elif topw and rightw:
            mtx[0][3] = i
        elif bottomw and leftw:
            mtx[3][0] = i
        elif bottomw and rightw:
            mtx[3][3] = i
        else:
            if (topw and mtx[0][0] != -1) or (topw and mtx[0][3] != -1):
                diff_0_1 = diff(newchunks[mtx[0][0]][3], left)
                diff_2_3 = diff(right, newchunks[mtx[0][3]][4])
                # print(i, diff_0_1, diff_2_3)
                if diff_0_1 < diff_2_3:
                    mtx[0][1] = i
                else:
                    mtx[0][2] = i
            if (bottomw and mtx[3][0] != -1) or (bottomw and mtx[3][3] != -1):
                diff_0_1 = diff(newchunks[mtx[3][0]][3], left)
                diff_2_3 = diff(right, newchunks[mtx[3][3]][4])
                # print(i, diff_0_1, diff_2_3)
                if diff_0_1 < diff_2_3:
                    mtx[3][1] = i
                else:
                    mtx[3][2] = i
            if (leftw and mtx[0][0] != -1) or (leftw and mtx[3][0] != -1):
                diff_0_1 = diff(newchunks[mtx[0][0]][2], top)
                diff_2_3 = diff(bottom, newchunks[mtx[3][0]][1])
                # print(i, diff_0_1, diff_2_3)
                if diff_0_1 < diff_2_3:
                    mtx[1][0] = i
                else:
                    mtx[2][0] = i
            if (rightw and mtx[0][3] != -1) or (rightw and mtx[3][3] != -1):
                diff_0_1 = diff(newchunks[mtx[0][3]][2], top)
                diff_2_3 = diff(bottom, newchunks[mtx[3][3]][1])
                # print(i, diff_0_1, diff_2_3)
                if diff_0_1 < diff_2_3:
                    mtx[1][3] = i
                else:
                    mtx[2][3] = i
            if not topw and not bottomw and not leftw and not rightw and (
                mtx[1][0] != -1 and mtx[0][1] != -1 and
                mtx[1][3] != -1 and mtx[0][2] != -1 and
                mtx[2][0] != -1 and mtx[3][1] != -1 and
                mtx[3][2] != -1 and mtx[2][3] != -1
            ):
                changes = []
                avgarr = {}
                if mtx[1][1] == -1:
                    diff1 = diff(top, get_edge(0, 1, BOTTOM))
                    diff2 = diff(left, get_edge(1, 0, RIGHT))
                    avg = (diff1 + diff2) / 2
                    avgarr[(1, 1)] = avg
                if mtx[1][2] == -1:
                    diff1 = diff(top, get_edge(0, 2, BOTTOM))
                    diff2 = diff(right, get_edge(1, 3, LEFT))
                    avg = (diff1 + diff2) / 2
                    avgarr[(1, 2)] = avg
                if mtx[2][1] == -1:
                    diff1 = diff(bottom, get_edge(3, 1, TOP))
                    diff2 = diff(left, get_edge(2, 0, RIGHT))
                    avg = (diff1 + diff2) / 2
                    avgarr[(2, 1)] = avg
                if mtx[2][2] == -1:
                    diff1 = diff(bottom, get_edge(3, 2, TOP))
                    diff2 = diff(right, get_edge(2, 3, LEFT))
                    avg = (diff1 + diff2) / 2
                    avgarr[(2, 2)] = avg
                # print(i, avgarr)
                pppoint = sorted(avgarr.items(), key=lambda kv: kv[1])[0][0]
                # print(pppoint)
                mtx[pppoint[0]][pppoint[1]] = i


    i = (i + 1) % len(newchunks)
    # if i == 15:
    #     z += 1
    #     if z == 3:
    #         running = False
    #         break
    # running = any(map(lambda z: z == -1, mtx))
    running = False
    for row in mtx:
        if -1 in row:
            running = True
            break


print(*mtx, sep='\n')

new_mtx = [[0] * 256 for _ in range(256)]

for i, row in enumerate(mtx):
    for j, col in enumerate(row):
        for z in range(64):
            new_mtx[z + (3 - i) * 64][j * 64:(j + 1) * 64] = data[col][z]

print(*new_mtx, sep='\n')

with open('merged.json', 'w') as f:
    json.dump(new_mtx, f)