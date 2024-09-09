import random

friends = ["1","2","3","4","5","6"]

seed = random.random()

random.seed(seed)

who_will_pay = random.randint(0,len(friends)-1)

print(f"{friends[who_will_pay]} is going to pay the bill!")