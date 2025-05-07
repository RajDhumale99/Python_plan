import random
import task

# print(task.new)
# random_integer = random.randint(1, 5)
# print(random_integer)

random_heads_tails = random.choice(["heads", "Tails"])
print(random_heads_tails)

name = (["Raj", "Pratik", "Yogesh"])
random_names = random.choice(name)


# List 
fruits = ["Mango", "apple", "Banana"]
games = ["GTA", "CSGO", "Spiderman" ,"COD"]
fruits[0] = "Orange"
print(fruits)

# Nested List
all_list = [fruits, games]
print(all_list[1][3])
