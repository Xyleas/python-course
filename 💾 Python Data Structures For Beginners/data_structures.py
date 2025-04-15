import random as r

[1,2,3]
[1,'a',2]
l = []
l = [1,2,3]
l = [[1,2,3],[4,5,6]]
l = [1,2,3,4,5]
l[4] # Returns 5 (0 based indexing)
l[0]
l[-1] # Returns 5, last element of the list.
l[-5]
l[0] = 10
l
del l[0]
l
l[0:2] # Slicing syntax 2nd value is exclusive, returns [2,3]
l[0:2] = [20, 30]
l # Returns [20,30,4,5]
l[0:2] = [20, 30, 40, 50]
l # Returns [20, 30, 40, 50, 4, 5]
l[0:2] = []
l # Returns [40, 50, 4, 5]
l.append(6)
l # Returns [40, 50, 4, 5, 6]
l.extend([7,8])
l
l + [9, 10] # Returns [40, 50, 4, 5, 6, 7, 8, 9, 10]
l.insert(1,100)
l # Returns [40, 100, 50, 4, 5, 6, 7, 8]
l[1] = 100
l # Returns [40, 100, 50, 4, 5, 6, 7, 8]
l.remove(100)
l # Returns [40, 50, 4, 5, 6, 7, 8]
l.pop(4) # Returns 6
l # Returns [40, 50, 4, 5, 7, 8]
l.clear() # Clears the list. Same as:
l = []
l.index(50) # Returns 1
l.sort()
l # Returns [4, 5, 7, 8, 40, 50]
l.reverse() 
l # Returns  [50, 40, 8, 7, 5, 4]
len(l) # Returns 6
l= [1,2,3,4,5]
for n in l:
    print(n)
1 in l # Returns True
50 in l # Returns False
[n for n in l if n > 3] # Returns [4,5]
[n* 2 for n in l] # Returns [2,4,6,8,10]
new_list = []
for n in l:
    if n > 3: new_list.append(n)
new_list # Returns [4,5]

# Strings 
string = 'This is a string!'
string[0] # Returns 'T'
string[0:5] # Returns 'This ' 
string[0] = 'A' # Returns an error, strings are immuatable in Python.
string.index('a') # Returns 8
string.count('i') # Returns 3
string.replace('a', 'the') # Returns 'This is the string!'

# Dictionaries (a mapping type)
d = {} # Returns {}
d = {'apple': 2, 'pear': 3} # Returns {'apple': 2, 'pear': 3}
d['apple'] # Returns 2
d['blueberry'] = 1 # Returns {'apple': 2, 'pear': 3, 'blueberry': 1}
d.keys() # Returns dict_keys(['apple', 'pear', 'blueberry'])
d.values() # Returns dict_values([2,3,1])
list(d.keys()) # Returns ['apple', 'pear', 'blueberry']
d.get('apple', 'default') # Returns 2
d.get('a', 'default') # Returns 'default'
d['a'] # Crashes, not as safe as d.get('value', 'defaultValue')
d.pop('apple') # Returns 2, d = {'pear': 3, 'blueberry': 1}
for k, v in d.items():
    print(k, v)
# Prints pear 3 blueberry 1
{k.upper(): v*2 for k, v in d.items()} # Returns {'PEAR': 6, 'BLUEBERRY': 2}

# Tuples
l = [1,2,3] # List (brackets)
t = (1,2,3) # Tuple (paranthesis)
t[0] # Returns 1
t[0:1] # Returns (1,)
l[0] = 5 # [5,2,3]
t[0] = 5 # TypeError, Tuples are immuatable
td = {[1,2]: 1} # TypeError Lists are unhashable (doesn't work)
td = {(1,2): 1} # {(1,2): 1}

def tuple_example():
    return('apple', 'fruit', 2.99)

fruit, kind, price = tuple_example()
fruit # Returns 'apple'
kind # Returns 'fruit'
price # Returns 2.99
t = fruit, kind, price # New tuple ('apple', 'fruit', 2.99)

# Sets (no duplicates)
a = set() # Empty set
a = {1,2,3,4} # Similar to dictionary, empty set notation already in use so the constructor must be called for an empty set.
a.add(4) # Returns {1,2,3,4}
a.add(5) # Returns {1,2,3,4,5}
b = {4,5,6,7}
a & b # {4,5}
a | b # {1,2,3,4,5,6,7}

# Challenge
# Challenge: Write a function that takes a list and ouptuts a list of tuples that contain each unique element of the list alongside the number of times that element appears in the list.
# For example, if the input is [1,2,2,3,4,4,5,1]
# The output would be [(1,2), (2,2), (3,1), (4,2), (5,1)]

def list_count(l):
    output = []
    seen = set()

    for n in l:
        if n not in seen:
            seen.add(n)
            n_count = l.count(n)
            output.append(n, n_count)

        return output

l = [1,2,2,3,4,4,5,1]
print(list_count(1))

# RPG Mini-project

player_health = 100
enemy_health = 100

moves = {"normal": (0, -20),
        "special": (5, -10),
        "heal": (15,0),
        "last stand": (-15, -30)}
moves_keys = list(moves.keys())

def report(player_health, enemy_health):
    print(f"""Player health: {player_health}
        Enemy health: {enemy_health}
        """)

report(player_health, enemy_health)

def check_game_over(player_health, enemy_health):
    if player_health <= 0 and enemy_health > 0:
        print("GAME OVER: Enemy wins.")
        return False
    elif enemy_health <= 0 and player_health > 0:
        print("GAME OVER: Player Wins.")
    elif enemy_health <= 0 and palyer_health <= 0:
        print("DRAW.")
        return False
    else:
        return True

current_turn = 1

# Game loop
running = True
while running:

    # Player turn
    if current_turn == 1:
        print("PLAYER TURN")

        valid_input = False
        while valid_input == False:
            player_input = input("Select move... \n")
            valid_input = player_input.lower() in moves_keys or player_input.lower() == 'quit'
            if not valid_input:
                print("Invalid move. Try again.")

        # Quit the game
        if player_input.lower() == 'quit':
            running = False
            break

        selected = moves[player_input.lower()]
        print("You selected: ", player_input)

        player_health += selected[0]
        enemy_health += selected[1]

        report(player_health, enemy_health)
        running = check_game_over(player_health, enemy_health)

    # Enemy turn
    elif current_turn == -1:
        print("ENEMY TURN")
        enemy_input = r.randint(0,3)
        selected = moves[moves_keys[enemy_input]]
        print("Enemy selected : ", moves_keys[enemy_input])

        enemy_health += selected[0]
        player_health += selected[1]

        report(player_health, enemy_health)
        running = check_game_over(player_health, enemy_health)

    # Turn swap
    current_turn *= -1