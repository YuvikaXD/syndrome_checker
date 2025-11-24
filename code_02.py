#---------------------------------------
#symptom checker
#---------------------------------------
#Features:
#1.Take symptoms as input
#2. Calculate score based on common symptoms
#3. Display basic wellness guuidance
#----------------------------------------
def get_symptoms():
    print("===Simple symptom checker===")
    print("Enter symptom seperated by commas")
    print("Example: fever, cough, headache\n")

    user_input=input("Enter symptoms:").lower().strip()

    if user_input == "":
        print("\nNo symptoms entered.\n")
        return[]
    return[s.strip() for s in user_input.split(",")]

def calculate_score(symptom_list):
    """calculate symptom severity score."""
    score=0

    if "fever" in symptom_list:
        score+=2
    if "cough" in symptom_list:
        score+=2
    if "headache" in symptom_list:
        score+=1
    if "cold" in symptom_list or "runny nose" in symptom_list:
        score+=1
    if "fatigue" in symptom_list or "tired" in symptom_list:
        score+=1
    if "body pain" in symptom_list:
        score+=2
    if "throat pain" in symptom_list or "sore throat" in symptom_list:
        score+=1

    return score

def show_result(score):
    """display basic wellness suggestion based on score."""
    print("\n===Result===")

    if score>=6:
        print("You might be feeling significantly unwell.")
        print("Please take rest and consider consulting a doctor.")
    elif 3<= score <6:
        print("you may have a mild viral condition or common cold.")
        print("Very mild symptoms detected. Keep yourself hydrated and rested.")
    elif 1<= score <3:
        print("Very mild symptoms detected.Keep yourself hydrated and rested.")
    else:
        print("No noticeable symptoms entered.You seem okay!")

    print("\nNote:This is not a medical diagnosis-just a simple Python-based checker.\n")
#--------------------------MAIN PROGRAM--------------------------------------------
symptoms=get_symptoms()
score=calculate_score(symptoms)
show_result(score)