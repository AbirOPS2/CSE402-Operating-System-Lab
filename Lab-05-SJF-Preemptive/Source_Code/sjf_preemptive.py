process = ["P1", "P2", "P3", "P4", "P5"]

AT = [4, 2, 1, 0, 3]
BT = [2, 2, 3, 6, 1]

n = len(process)
quantum = 2

remaining = BT.copy()

CT = [0] * n
TAT = [0] * n
WT = [0] * n

time = 0
completed = 0

while completed < n:

    x = -1


    for i in range(n):

        if AT[i] <= time and remaining[i] > 0:

            if x == -1 or remaining[i] < remaining[x]:
                x = i

    
    if x == -1:
        time += 1

    else:


        if remaining[x] > quantum:
            time += quantum
            remaining[x] -= quantum

        else:
            time += remaining[x]
            remaining[x] = 0

            CT[x] = time
            completed += 1




for i in range(n):

    TAT[i] = CT[i] - AT[i]
    WT[i] = TAT[i] - BT[i]



print("Process\tAT\tBT\tCT\tTAT\tWT")

for i in range(n):

    print(process[i], "\t",
          AT[i], "\t",
          BT[i], "\t",
          CT[i], "\t",
          TAT[i], "\t",
          WT[i])


avg_tat = sum(TAT) / n
avg_wt = sum(WT) / n

print("\nAverage TAT =", avg_tat)
print("Average WT =", avg_wt)
