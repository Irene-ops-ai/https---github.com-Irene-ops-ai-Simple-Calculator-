from collections import deque

er_queu = deque()

er_queu.append("Broken Arm")
er_queu.append("Severe Burns")
er_queu.appendleft("Heart Attack")

print("ER_Queu:", er_queu)

while er_queu:
    current = er_queu.popleft()
    print(f"Treating: {current} Remaining-> {er_queu}")

