#*
# Project Definitions:
#   Definition 1:
#       We want to diagnose a user's state of dehydration based on a short questionairre.
#           A) Yes-or-No Type questions. B) Previous responses to determine next questions. C) Server/some/no dehydration.
#   Definition 2:
#       We want to retrieve and add dehyrdration diagnoses.
#           A) Display a list of patients and their diagnoses. B) Store new diagnoses to the list.
#   
# Project Design:
#   1. Run a new diagnoses and store the results.
#   2. Display a list of previous patient and diagnoses.
#
# How will it work?
#   Text-based program that will run within the Terminal/CMD Prompt.
#       1. Display prompt/question.
#       2. Process user text input.
#
# Diagnosis Algorithm
#   Access the Child's General Appearance -> Normal || Irritable/Lethargic
#       Normal -> Assess the Child's Eyes
#           Assess the Child's Eyes -> Eyes Normal/Slightly Sunken || Eyes Very Sunken
#               Eyes Normal/Slightly Sunken -> No Dehydration
#               Eyes Very Sunken -> Severe Dehydration
#       Irritable/Lethargic -> Assess the Child's Skin Pinch
#           Assess the Child's Skin Pinch -> Skin Pinch Normal || Skin Pinch Slow
#               Skin Pinch Normal -> Some Dehydration
#               Skin Pinch Slow -> Severe Dehydration
#
#
# Program Entry Point
#   Start the program and respond to user selection.
#       Write a main function.
#       Direct flow according to user selection.
#
# Start a new diagnosis
#   Enter diagnosis mode and capture user information.
#       Implement the start diagnosis function.
#       Store user's name and start questionnaire.
#
# Flow
#   Begin > Ask for appearance > Process text input > User response: (Irritable/lethargic > Ask fro skin pinch) (Normal > Ask for eye appearance.)
#   Assass User's Eyes - Inquire about eye appearance and output a diagnosis.abs]
#       Write a function to assess a user's eyes.
#       Output either "No dehydration" or "Sever dehydration"
#
#   Display Diagnoses
#       Store and print previous patients and their diagnoses.
#           Create a list of patient-diagnosis strings.
#           Write a function to print the list.
#           Save any new diagnosis to the list.
#
#   Handle User Errors
#       We must handle and respond to invalid inputs.
#           Ensure each user input is valid
#           Handle invalid input safely
#
# TODO: Complete unit and integration tests.
# *#


# Note that """ allows you to break a string into multiple lines so you can better visualize it.
welcome_prompt = """Welcome doctor, what would you like to do today?\n 
- To list all patients, press 1\n 
- To run a new diagnosis, press 2\n
- To quit, press q\n"""

name_prompt = "What is the patient's name?\n"

appearance_prompt = """How is the patient's general appearance?\n 
- 1: Eyes normal or slightly sunken\n 
- 2: Eyes are very sunken\n"""

eye_prompt = """How are the patient's eyes?\n 
- 1: Normal appearance\n 
- 2: Irritable or lethargic\n"""

skin_prompt = """How is the patient's skin when you pinch it?\n 
- 1: Normal skin pinch\n 
- 2: Slow skin pinch\n"""

error_message = "Could not save patient and diagnosis due to invalid input."

severe_dehydration = "Severe dehydration"
some_dehydration = "Some dehydration"
no_dehydration = "No dehydration"

patients_and_diagnoses = [
    "Danny: Severe dehydration",
    "Kimberly: Some dehydration",
    "Joe: No dehydration"

]

def list_patients():
    for patient in patients_and_diagnoses:
        print(patient)

def save_new_diagnosis(name, diagnosis):
    if name == "" or diagnosis == "":
        print(error_message)
        return
    final_diagnosis = name + ": " + diagnosis
    patients_and_diagnoses.append(final_diagnosis)
    print("Final diagnosis:", final_diagnosis,"\n")

def assess_eyes(eyes):
    if eyes == "1":
        return no_dehydration
    elif eyes == "2":
        return severe_dehydration
    else:
        return ""

def assess_skin(skin):
    if skin == "1":
        return some_dehydration
    elif skin == "2":
        return severe_dehydration
    else:
        return ""

def assess_appearance():
    appearance = input(appearance_prompt)
    if appearance == "1":
        eyes = input(eye_prompt)
        return assess_eyes()
    elif appearance == "2":
        skin = input(skin_prompt)
        return assess_skin()
    else:
        return ""

def start_new_diagnosis():
    name = input(name_prompt)
    diagnosis = assess_appearance()
    save_new_diagnosis(name, diagnosis)

def main():
    while(True):
        selection = input(welcome_prompt)
        if selection == "1":
            list_patients()
        elif selection == "2":
            start_new_diagnosis()
        elif selection == "q":
            return

main()

# Unit Tests
#def test_assess_skin():
#
# #    print(assess_skin("2") = severe_dehydration)
 #   print(assess_skin("") = "")

#test_assess_skin()

# Integration Tests
def test_assess_appearance():
    print(assess_appearance())

test_assess_appearance()

# Take a minute and account for the Social, Economic, and Enviromental perspectices. What are the pros and cons?
# Data Considerations
# Make the project more sophisticated. Add more edge cases. Improve usability. Find similar scenarios to model.
# Explore real world examples.
