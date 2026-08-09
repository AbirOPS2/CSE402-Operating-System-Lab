processes = [
    ["p1", 3, 3],
    ["p2", 2, 5],
    ["p3", 5, 4],
    ["p4", 1, 3],
    ["p5", 6, 2],
]


process = [{"pid": p[0], "at": p[1], "bt": p[2]} for p in processes]

n = len(process)
completed = []
time = 0
done = 0
is_done = [False] * n

while done < n:
    ready = [p for i, p in enumerate(process) if p["at"] <= time and not is_done[i]]
    if not ready:
        time = min(p["at"] for i, p in enumerate(process) if not is_done[i])
        continue

    current = min(ready, key=lambda p: p["bt"])
    idx = process.index(current)

    start = max(time, current["at"])
    finish = start + current["bt"]
    tat = finish - current["at"]
    wt = tat - current["bt"]

    completed.append({**current, "ct": finish, "tat": tat, "wt": wt})
    is_done[idx] = True
    time = finish
    done += 1

print("SJF")
print(f"{'Pd':<4}{'AT':<4}{'BT':<4}{'CT':<4}{'TAT':<4}{'WT':<4}")
for p in completed:
    print(f"{p['pid']:<4}{p['at']:<4}{p['bt']:<4}{p['ct']:<4}{p['tat']:<5}{p['wt']:<4}")

sjf_avg_tat = sum(p["tat"] for p in completed) / n
sjf_avg_wt = sum(p["wt"] for p in completed) / n

print(f"Avg TAT: {sjf_avg_tat}")
print(f"Avg WT: {sjf_avg_wt}")



print()
print("FCFS")

lst = sorted(processes, key=lambda x: x[1])   # AT onujayi sort
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
    print(lst[i][0], lst[i][1], lst[i][2], ct[i], tat[i], wt[i])

fcfs_avg_tat = sum(tat) / len(lst)
fcfs_avg_wt = sum(wt) / len(lst)

print("avg tat =", fcfs_avg_tat)
print("avg wt =", fcfs_avg_wt)



print()
print("Comparison")

if fcfs_avg_wt < sjf_avg_wt:
    print("FCFS is better (lower avg waiting time)")
elif fcfs_avg_wt > sjf_avg_wt:
    print("SJF is better (lower avg waiting time)")
else:
    print("Both are equal in avg waiting time")

if fcfs_avg_tat < sjf_avg_tat:
    print("FCFS is better (lower avg turnaround time)")
elif fcfs_avg_tat > sjf_avg_tat:
    print("SJF is better (lower avg turnaround time)")
else:
    print("Both are equal in avg turnaround time")
