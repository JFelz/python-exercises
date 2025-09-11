import random
import random_util

print(random_util.x)
coin_toss = random.randint(0, 1)
if coin_toss == 0:
    print("Tails")
else:
    print("Heads")


states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia"]


states_of_america.append("JojoLand")
print(states_of_america)


friends = ["Jovanni", "Noah", "Trey", "Ben"]
random_roulette = random.randint(0, len(friends) - 1)
print(friends[random_roulette])
# or
# print(random.choice(friends))

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen[0][2])