###
# Building an escape room game.
#
#   Room contains several objects
#   Player needs to code to escape.
#
#   Players piece together clues to get the code to escape
#   Each item can be looked at, touched, or smelled
#   Each sense provides new information
#   Player discerns information from interactions with objects
#
#   Entirely text-based.
#       Run in the terminal
#       Prints prompts to capture user response
#       Run until palyer wins or loses (3 bad guesses)
#
#   Game Components (Objects and Classes)
#       Game Object
#       Room
#       Game
#
#   Game Objects
#       
###

#print_value = "Hello, world!"
#print(print_value)
#input("Enter your name.")
#name = input("Enter your name.\n")
#print(name)

class GameObject:
    name = ""
    appearance = ""
    feel = ""
    smell = ""

# Set up an instance of GameObject with name, appearance, feel, and smell.
    def __init__(self, name, appearance, feel, smell):
       self.name = name
       self.appearance = appearance
       self.feel = feel
       self.smell = smell
    
    #Return a string representing object appearance.
    def look(self):
        return f"You look at the {self.name}. {self.appearance}. \n"

    #Return a string representing object feel.
    def touch(self):
        return f"You touch at the {self.name}. {self.touch}. \n"
        
    #Return a string representing object smell.
    def smell(self):
        return f"You smell at the {self.name}. {self.smell }. \n"

class Room:
    # Our Room class has an escape code and a list of game objects as attributes/fields
    escape_code = 0
    game_objects = []

    # Set up an instance of Room with escape code and game objects. 
    def __init__(self, escape_code, game_objects):
       self.escape_code = escape_code
       self.game_objects = game_objects

    # Returns whether the code of the room matches the code entered by the player
    def check_code(self, code):
        return escape_code == self.code 

    # Returns a list with all the names of the objects we have in our room
    def get_game_object_names(self):
        names = []
        for object in self.game_objects:
            names.append(object.name)
        return names

class Game:

    # Number of attempts the player has made on the escape code of the room
    def __init__(self):
        self.attempts = 0
        objects = self.create_Objects()
        # Instantiating our room object
        self.room = Room(731, objects)
        
    # Returns a list with all the objects we're going to have in our escape room
    def create_Objects(self):
        return [
            GameObject(
                "Sweater",
                "It's a blue sweater that had the number 12 switched on it.",
                "Someone has unstitched the second number, leaving only the 1.",
                "The sweater smells of laundry detergent."
            ),
            GameObject(
                "Chair",
                "It's a wooden chair with only 3 legs.",
                "Someone had deliberately snapped off one of the legs.",
                "It smells like old wood."
            ),
            GameObject(
                "Journal",
                "The final entry states that the final time should hours, then minutes, then seconds. (H-M-S)",
                "The cover is worn and several pages are missing.",
                "It smells like musty leather."
            ),
            GameObject(
                "Bowl of soup",
                "It appears to be tomato soup.",
                "It has cooled down to room temperature.",
                "You detect 7 different herbs and spices."
            ),
            GameObject(
                "Clock",
                "One hour hand is pointing towards the soup, the minute hand towards the chair, and the second hand towards the sweater.",
                "The battery compartment is open and empty.",
                "It smells of plastic."
            )
        ]

    # For each turn, we want to present the prompt to the player
    def take_turn(self):
        prompt = self.get_room_prompt()
        selection = int(input(prompt))
        if selection >= 1 and selection <= 5:
            self.select_object(selection -1)
            self.take_turn()
        else:
            is_code_correct = self.guess_code(selection)
            if is_code_correct:
                print("Congratulations, you win!")
            else:
                if self.attempts == 3:
                    print("Game over, you ran out of guesses. Better luck next time!")
                else:
                    printf("Incorrect, you have used {self.attempts}/3 attempts.\n")
                    self.take_turn()
    
    # Shows the option to enter the code or interact further with the objects in the room
    def get_room_prompt(self):
        prompt = "Enter the 3 digit lock code, or choose an item to interact with:\n"
        names = self.room.get_game_object_names()
        index = 1
        for name in names:
            prompt += f"{index}. {name}\n"
            index += 1
        return prompt

    
    #Print out an interaction (look, smell, or touch) with the object at the specified index
    def select_object(self, index):
        selected_object = self.room.game_objects[index]
        prompt = self.get_object_interaction_string(selected_object.name)
        interaction = input(prompt)
        clue = self.interact_with_object(selected_object, interaction)
        print(clue)
    
    # Return a string containing the possible interactions along with an object's name
    def get_object_interaction_string(self, name):
        return f"How do you want to interact with {name}?\n1. Look\n2. Touch\n3. Smell\n"

    # Shows the interaction message to the player
    def interact_with_object(self, object, interaction):
        if interaction == "1":
            return object.look()
        elif interaction == "2":
            return object.touch()
        else:
            return object.smell()

    # Compares the code entered to the code of the room
    def guess_code(self, code):
        if self.room.check_code(code):
            return True
        else:
            # If the codes don't match, increases attempts variable by 1
            self.attempts += 1
            return False

        
# Here we're creating an object of our Game class 
# and calling on its take_turn() method
#game = Game()
#game.take_turn()

#Testing class with two rooms as examples
class RoomTests:
    def __init__(self):
        self.room_1 = Room(111,[
            GameObject(
                "Sweater",
                "It's a blue sweater that had the number 12 switched on it.",
                "Someone has unstitched the second number, leaving only the 1.",
                "The sweater smells of laundry detergent."
            ),
            GameObject(
                "Chair",
                "It's a wooden chair with only 3 legs.",
                "Someone had deliberately snapped off one of the legs.",
                "It smells like old wood.")
            ])
        self.room_2 = Room(222,[])

    # Function to test that the escape code of room 1 is 111
    def test_check_code(self):
        print(self.room_1.check_code(111) == True)
        print(self.room_1.check_code(222) == False)
    
    # Function to test the returned list of objects' names of each room
    def test_get_game_object_names(self):
        print(self.room_1.get_game_object_names() == ["Sweater", "Chair"] )
        print(self.room_2.get_game_object_names() == [])

# Instantiating the test class and calling its methods
tests = RoomTests()

tests.test_check_code
tests.test_get_game_object_names()
    