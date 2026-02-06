# make this performance task ready for submission
# To give the user a fun experience hearing knock knock jokes
#JAFET, AARON p1

answers = []

def countdown(sec):
    import time
    for i in range(sec, 0, -1):
        print(i)
        time.sleep(1)
        
def choose_joke(question):
    
    if question == "robbers":
        input("Knock Knock ")
        input("Calder ")
        print("Calder police - I've been robbed!")

    elif question == "tanks":
        input("Knock Knock ")
        input("Tank ")
        input("You are welcome! ")

    elif question == "pencils":
        input("Knock Knock ")
        input("Broken pencil ")
        input("Nevermind, it's pointless! ")

    answers.append(question)
    return input("Do you want to hear another joke or are you finished? ")


countdown(5)
print("Initiation complete.")

joke = input("Do you want to hear a joke? ")
if joke == "no":
    print("Okay suit yourself!")

while joke == "yes":
    print("Great, Let's Play")
    question = input("Do you want to hear a joke about robbers, tanks, or pencils? ")
    joke = choose_joke(question)
    
if joke == "finished":
    rate = int(input("Please rate our game 1-10! "))
    print(str(rate * 10) + " percent satisfaction rate") 
    friend = input("Would you recommend this game to a friend? ")

    if friend == "yes" or friend == "maybe":
        print("Thanks, we appreciate it. ")
        print("The number of jokes were:", len(answers))
    else:
        print("Sorry you did not enjoy it. ")
