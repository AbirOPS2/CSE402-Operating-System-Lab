# Page Replacement Algorithm (FIFO)
reference = [1, 2, 3, 4, 2, 3, 1]
frame_size = 3

frame = []
hit = 0
fault = 0

for page in reference:

    if page in frame:
        hit += 1
        print(page, "->", frame, "Hit")

    else:
        fault += 1

        if len(frame) < frame_size:
            frame.append(page)
        else:
            frame.pop(0)
            frame.append(page)

        print(page, "->", frame, "Fault")

hit_ratio = (hit / len(reference)) * 100
fault_ratio = (fault / len(reference)) * 100

print("Total Hit =", hit)
print("Total Fault =", fault)
print("Hit Ratio =", round(hit_ratio,2),"%")
print("Fault Ratio =", round(fault_ratio, 2),"%")
