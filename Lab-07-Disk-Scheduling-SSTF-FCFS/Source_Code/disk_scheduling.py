requests = [3, 60, 10, 25, 30, 4]
total_head_movement = 0
seek_seq = []
current_head = 41

pending_requests = list(requests)

while pending_requests:
    closest_req = min(pending_requests, key=lambda req: abs(current_head - req))
    distance = abs(current_head - closest_req)
    total_head_movement += distance
    current_head = closest_req
    seek_seq.append(closest_req)
    pending_requests.remove(closest_req)
print("Total_head_movement:", total_head_movement)
print("Seek Sequence:", seek_seq)

print("FCFS")

total_head_movement = 0
current_head = 41
seek_seq = []

for req in requests:
    distance = abs(current_head - req)
    total_head_movement += distance
    seek_seq.append(req)
    current_head = req

print(total_head_movement)
print(seek_seq)
