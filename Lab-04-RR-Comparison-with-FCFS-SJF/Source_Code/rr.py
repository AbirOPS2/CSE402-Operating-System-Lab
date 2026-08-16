processes = [
    ["P1", 0, 7],
    ["P2", 1, 4],
    ["P3", 2, 15],
    ["P4", 3, 11],
    ["P5", 4, 20],
    ["P6", 4, 9],
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
print(f"{'Pid':<4}{'AT':<4}{'BT':<4}{'CT':<4}{'TAT':<4}{'WT':<4}")
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
print("Round Robin TQ=5")

tq = 5
rr_lst = sorted(processes, key=lambda x: x[1])

remaining_bt = {p[0]: p[2] for p in rr_lst}
at_map = {p[0]: p[1] for p in rr_lst}
bt_map = {p[0]: p[2] for p in rr_lst}

queue = []
time = 0
i = 0
ct_rr = {}

queue.append(rr_lst[0][0])
i = 1

while queue:
    pid = queue.pop(0)
    run = min(tq, remaining_bt[pid])
    time += run
    remaining_bt[pid] -= run


    while i < len(rr_lst) and rr_lst[i][1] <= time:
        queue.append(rr_lst[i][0])
        i += 1

    if remaining_bt[pid] > 0:
        queue.append(pid)
    else:
        ct_rr[pid] = time

rr_tat = []
rr_wt = []

print("pid", "at", "bt", "ct", "tat", "wt")
for p in rr_lst:
    pid, at, bt = p[0], p[1], p[2]
    turnaround = ct_rr[pid] - at
    waiting = turnaround - bt
    rr_tat.append(turnaround)
    rr_wt.append(waiting)
    print(pid, at, bt, ct_rr[pid], turnaround, waiting)

rr_avg_tat = sum(rr_tat) / len(rr_lst)
rr_avg_wt = sum(rr_wt) / len(rr_lst)

print("avg tat =", rr_avg_tat)
print("avg wt =", rr_avg_wt)



print()
print("Comparison")

results = {
    "FCFS": (fcfs_avg_tat, fcfs_avg_wt),
    "SJF": (sjf_avg_tat, sjf_avg_wt),
    "Round Robin": (rr_avg_tat, rr_avg_wt),
}

for name, (avg_tat, avg_wt) in results.items():
    print(f"{name}: Avg TAT = {avg_tat:.2f}, Avg WT = {avg_wt:.2f}")

best_wt = min(results, key=lambda k: results[k][1])
best_tat = min(results, key=lambda k: results[k][0])

print(f"\n{best_wt} is better (lowest avg waiting time)")
print(f"{best_tat} is better (lowest avg turnaround time)")
