print("Hello World!")

x_position = 10
print(x_position)

x_position = 15
print(x_position)

pi = 3.14
pi = 3.14159
print(pi)

x_position = 15.0
print(x_position)

print(type(x_position))

is_game_over = False
is_game_over = True

print(is_game_over)
print(type(is_game_over))

is_game_over = 1
print(is_game_over)
print(type(is_game_over))

name = 'Danny'
is_game_over_text = "False"
age_as_a_string = "5"
print(name)
print(type(name))

age = 27
name_and_age = "Danny: {} {}".format(age, age)
print(name_and_age)

# + - * / $ // ** =

x_position = 10
# x_position = 11
forward = x_position + 1
print(forward)
backward = x_position - 1
print(backward)

remainder = 5 % 2
print(remainder)
floor_division = 5 // 2
print(floor_division)

five_squared = 5 ** 2
print(five_squared)

x_position = x_position + 1
print(x_position)
x_position += 1
print(x_position)

first_name = "Danny "
first_name = "Riggleman"
print(first_name + last_name)

# > >= < <= == != not or and

x_position = 1
end_position = 10

is_at_end = x_position == end_position
print(is_at_end)
is_at_halfway = x_position >= end_position / 2
print(is_at_halfway)

not_is_at_end = not is_at_end
print(not_is_at_end)

score = 10
is_game_over = score >= 10 and is_at_end
print(is_game_over)
score = 9
is_game_over = score >= 10 or is_at_end
print(is_game_over)

name = [5, True, "string"]

enemy_positions = [5,10,15]
enemy_positions = [5,10,15,20]
print(enemy_positions)

print(len(enemy_positions))
print(enemy_positions[0])
print(enemy_positions[3])

enemy_positions[0] = 6
print(enemy_positions)

enemy_positions[0:2]

enemy_positions.append(25)
print(enemy_positions)

enemy_positions.insert(1, 9)
print(enemy_positions)

enemy_positions.remote(6)
print(enemy_positions)

del(enemy_positions[2])
print(enemy_positions)

high_score = ("Danny", 120)
print(high_score)

high_score = ("Kimberly", 150)
print(high_score)

# high_score[0] = "fassfsd" # Errors, Tuples are immuatable
name = high_score[0]
print(name)

print(len(high_score))

print("Danny" in high_score)

print(name[0])
print(name[0:2])
print("Hol" in name)
print(len(name))

actions = {"r":1, "l":-1}
print(actions)

print(actions["r"])
print(actions["g"]) # ERROR: Doesn't exist
print(acitons.get("g")) # Returns None, handles it gracefully

actions["r"] = 2
actions["u"] = 1 # Since the key doesn't exist, it get's inserted automatically
print(actions)

print(actions.items())
print(actions.keys())
print(actions.values())

del(actions["u"])
print(actions)
actions.pop("r")
print(actions)

print("l" in actions)

key = "r"

# Control flow - if statements
if key == "r":
    print("move right")
elif key == "l":
    print("move left")
else:
    print("invalid key")

print("done")

# Control flow - while loops
position = 0
end_position = 5
enemy_position = 5

while position < end_position:
    position += 1
    print(position)
    if position == enemy_position:
        print("Game Over!")
        break

if position == end_posiiton:
    print("You have reached the end")


continue # skips the rest of the loop iteration and jumps to the next, useful if we don't want code to run for a specific iteration of our loop

enemy_positions = [5, 10, 15]

# Control flow - for in loops
for enemy_position in enemy_positions:
    if enemy_position == 10:
        continue
    print(enemy_position)

for i in range(0,5):
    print("Hello")

position = 0

# move_player() # Errors, function hasn't been created yet
def move_player():
    global position # global for variables outside the f(x), or the variable at the 'global' scope, outside of move_player()'s scope
    position += 1
    print(position)
    # x_position = position

# x_position

move_player()

position = 0

def move_player(position, by_amount): # no global, it's bad practice, generally try to avoid globals
    position += by_amount
    return position

position = move_player(position, 5)
position = move_player(position, 7)
print(position)

class GameObject:

    def __init__(self, name, x_pos, y_pos):
        self.name = name
        self.x_pos = x_pos
        self.y_pos = y_pos

    def move(self, x_amount, y_amount):
        self.x_pos += x_amount
        self.y_pos += y_amount

game_object = GameObject("Enemy", 1, 2)
print(game_object.name)
game_object.name = "Enemy 1"
print(game_object.name)

print(game_object.x_pos)
print(game_object.y_pos)
game_object.damage = 5 # Valid despite "damage" not existing in our class, though it's not great practice

game_object.move(5,10)
print(game_object.x_pos)
print(game_object.y_pos)

other_game_object = GameObject("Player", 2, 0)
print(other_game_object.name) # Player
print(other_game_object.x_pos) # 2
print(other_game_object.y_pos) # 0

one_int = 5
another_int = one_int
print(one_int) # 5
print(another_int) # 5

another_int = 10
print(one_int) # 5
print(another_int) # 10

other_game_object = game_object
print(other_game_object.name)

other_game_object.name = "new name"
print(other_game_object.name)
print(game_object.name)

class GameObject:

    def __init__(self, name, x_pos, y_pos):
        self.name = name
        self.x_pos = x_pos
        self.y_pos = y_pos

    def move(self, x_amount, y_amount):
        self.x_pos += x_amount
        self.y_pos += y_amount

game_object = GameObject("Enemy", 1, 2)

class Enemy(GameObject):
    def __init__(self, name, x_pos, y_pos, health):
        super().__init__(name, x_pos, y_pos)
        self.health = health
    
    def take_damage(self, amount):
        self.health -= amount

    
game_object = GameObject("Game object", 1, 2)
enemy = Enemy("Enemy", 5, 10, 100)

print(game_object.name) # Game object
print(enemy.name) # Enemy

enemy.take_damage(20)
print(enemy.health) # 80