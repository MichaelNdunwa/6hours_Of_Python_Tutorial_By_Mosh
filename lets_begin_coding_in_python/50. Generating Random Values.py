import random

members = ["Michael", "Ndunwa", "Chidera"]
appointed_leader = random.choice(members)
two_leaders = random.choices(members, k=2)
print(appointed_leader)
print(two_leaders)