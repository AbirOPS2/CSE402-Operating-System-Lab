import numpy as np


lst = [
    ["p0", 3, 1],
    ["p1", 5, 3],
    ["p2", 2, 2],
    ["p3", 1, 2],
    ["p4", 6, 3],

]

lst.sort(key=lambda x: x[1])
print(lst)

ct = []
tat = []
wt = []

time = 0

for p in lst:
    pid, at, bt = p[0], p[1], p[2]

    if time < at:
        time = at
    time += bt

    completion = time
    turnaround = completion - at
    waiting = turnaround - bt

    ct.append(completion)
    tat.append(turnaround)
    wt.append(waiting)

print("pid", "at", "bt", "ct", "tat", "wt")
for i in range(len(lst)):
    pid = lst[i][0]
    at = lst[i][1]
    bt = lst[i][2]
    print(pid, at, bt, ct[i], tat[i], wt[i])

total_tat = 0
total_wt = 0

for i in range(len(lst)):
    total_tat = total_tat + tat[i]
    total_wt = total_wt + wt[i]

avg_tat = total_tat / len(lst)
avg_wt = total_wt / len(lst)

print("Average TAT =", avg_tat)
print("Average WT =", avg_wt)
