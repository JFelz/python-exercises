import random

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

def greet(intro, x):
    """Prints a greeting with an introduction and a name."""
    print(f"{intro}")
    print("I\'m")
    print(x)

greet("Welcome","Ashley")

# Global scopes should be all uppercase to avoid modifying code - read but dont modify

GOOGLE_URL = 1234

def life_in_weeks(age):
    print(GOOGLE_URL)
    print(f"Your current age is: {age}")
    # 52 weeks in 1 year
    weeks_in_age = age * 52
    weeks_left = 4680 - weeks_in_age
    print(
        f"""You have {weeks_left // 52} years left until 90. Make them count!\n
          You have {weeks_left} weeks left.
          """
    )


life_in_weeks(39)


def calculate_love_score(name1="Angela Yu", name2="Jack Bauer"):
    arr = []
    it_true = 0
    it_love = 0
    
    name_1st = name1.lower()
    name_2nd = name2.lower()
    # store each name into an array
    for x in name_1st:
        arr += x

    for y in name_2nd:
        arr += y

    t_count = 0
    r_count = 0
    u_count = 0
    e_count = 0
    
    l_count = 0
    o_count = 0
    v_count = 0

    for letter in arr:
        if letter == "t":
            t_count = arr.count(letter)
        elif letter == "r":
            r_count = arr.count(letter)
        elif letter == "u":
            u_count = arr.count(letter)
        elif letter == "e":
            e_count = arr.count(letter)
        elif letter == "l":
            l_count = arr.count(letter)
        elif letter == "o":
            o_count = arr.count(letter)
        elif letter == "v":
            v_count = arr.count(letter)
        else:
            continue
        
        it_true = t_count + r_count + u_count + e_count
        it_love = l_count + o_count + v_count + e_count
        
        true_out = str(it_true)
        love_out = str(it_love)

    print(f"""
            T: {t_count}
            R: {r_count}
            U: {u_count}
            E: {e_count}
            total: {true_out}
            
            L: {l_count}
            O: {o_count}
            V: {v_count}
            E: {e_count}
            total: {love_out}
            
            Love Score = {int(true_out + love_out)}
            """)

calculate_love_score()
