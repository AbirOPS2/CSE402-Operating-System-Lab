print("Non preemptive")

processes = [
    {'name': 'p1', 'AT':0, 'BT':3, 'priority': 3},
    {'name': 'p2', 'AT':1, 'BT':4, 'priority': 2},
    {'name': 'p3', 'AT':2, 'BT':6, 'priority': 4},
    {'name': 'p4', 'AT':3, 'BT':4, 'priority': 6},
    {'name': 'p5', 'AT':5, 'BT':2, 'priority': 10},
]

time = 0
completed = []
n = len(processes)

while len(completed) < n:
    available = [p for p in processes if p['AT'] <= time and p not in completed]

    if not available:
        time = time + 1
        continue

    current = min(available, key=lambda p: p['priority'])

    start = time
    time += current['BT']
    end = time

    current['CT'] = end
    current['TAT'] = end - current['AT']
    current['WT'] = current['TAT'] - current['BT']
    completed.append(current)


print(f"{'process':<10}{'AT':<6}{'BT':<6}{'CT':<6}{'TAT':<6}{'WT':<6}")
for p in completed:
    print(f"{p['name']:<10}{p['AT']:<6}{p['BT']:<6}{p['CT']:<6}{p['TAT']:<6}{p['WT']:<6}")

avg_tat = sum(p['TAT'] for p in completed) / n
avg_wt = sum(p['WT'] for p in completed) / n


print("Avg TAT:", avg_tat)
print("Avg WT:", avg_wt)

processes = {
    'P1': {'AT': 0, 'BT': 3, 'priority': 3, 'remaining': 3},
    'P2': {'AT': 1, 'BT': 4, 'priority': 2, 'remaining': 4},
    'P3': {'AT': 2, 'BT': 6, 'priority': 4, 'remaining': 6},
    'P4': {'AT': 3, 'BT': 4, 'priority': 6, 'remaining': 4},
    'P5': {'AT': 5, 'BT': 2, 'priority': 10, 'remaining': 2},
}

time = 0
completed = {}
n = len(processes)

while len(completed) < n:

    available = [p for p, d in processes.items() if d['AT'] <= time and d['remaining'] > 0]

    if not available:
        time += 1
        continue


    current = min(available, key=lambda p: processes[p]['priority'])


    processes[current]['remaining'] -= 1
    time += 1


    if processes[current]['remaining'] == 0:
        at, bt = processes[current]['AT'], processes[current]['BT']
        ct = time
        tat = ct - at
        wt = tat - bt
        completed[current] = {'AT': at, 'BT': bt, 'CT': ct, 'TAT': tat, 'WT': wt}

print(" ")
print("PREEMPTIVE PRIORITY SCHEDULING")
print(f"{'Process':<10}{'AT':<6}{'BT':<6}{'CT':<6}{'TAT':<6}{'WT':<6}")
for p, d in completed.items():
    print(f"{p:<10}{d['AT']:<6}{d['BT']:<6}{d['CT']:<6}{d['TAT']:<6}{d['WT']:<6}")

avg_tat1 = sum(d['TAT'] for d in completed.values()) / n
avg_wt1 = sum(d['WT'] for d in completed.values()) / n
print(f"\nAvg TAT = {avg_tat1}")
print(f"Avg WT = {avg_wt1}")

print("Compare")


avg_wt_non_preemptive = avg_wt
avg_wt_preemptive = avg_wt1

avg_tat_non_preemptive = avg_tat
avg_tat_preemptive = avg_wt1

print("Avg WT Non-Preemptive:", avg_wt_non_preemptive, " Preemptive:", avg_wt_preemptive)
print("Avg TAT Non-Preemptive:", avg_tat_non_preemptive, " Preemptive:", avg_tat_preemptive)

if avg_wt_non_preemptive < avg_wt_preemptive:
    print("Non Preemptive is better (lower waiting time)")
else:
    print("Preemptive is better (lower waiting time)")
