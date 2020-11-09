l1 = [[3,2,3], [2,0,2], [3, 0, 1]]
l2 = [[3, 2, 3], [2, 0, 2], [3, 0, 1], [3, 1, 0]]

print("L1:", sorted(l1, key=lambda k: (k[1], k[2])))
print("L2:", sorted(l2, key=lambda k: (k[1], k[2])))