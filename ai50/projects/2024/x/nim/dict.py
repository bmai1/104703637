d = dict()

state = (1, 2, 3, 4, 5)
action = (1, 1)

d[(state, action)] = 1

print(d[(state, action)])

q_max = 0
q_max = max(q_max, d[tuple([state, action])])

print(q_max)