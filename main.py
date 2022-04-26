import cv2, random, time
from keras.models import load_model
import numpy as np      

player_win_count = 0
computer_win_count = 0
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

def computer_choice():
    '''
    This function will generate a number between 1-3, which represents the computer choice in the game.
    1 = rock, 2 = scissors, 3 = paper.
    '''
    rng = random.randint(1,3)
    if rng == 1:
        X = 'Rock'
    elif rng == 2:
        X = 'Scissor'
    else:
        X = 'Paper'
    print("The computer chose " + X + "!")
    return X

def player_choice(accuracy = 0.5):
    '''
    This function will use the keras model and attempt to interpret your hand gesture into four outputs. 
    These outputs are: Rock, Paper, Scissors and Nothing/Unknown in case it couldn't determine what hand gesture was made.
    '''
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 
    data[0] = normalized_image
    prediction = model.predict(data)
    if prediction[0][0] > accuracy:
        Y = "Rock"
    elif prediction[0][1] > accuracy:
        Y = "Scissor"
    elif prediction[0][2] > accuracy:
        Y = "Paper"
    else:
        Y = "I did not catch that."
    print("You chose " + Y + "!")
    return Y

def game_evaluation(X, Y):
    '''
    This function will evaluate based on the X and Y values from previous functions whether the computer or the player wins the round.
    '''
    global player_win_count, computer_win_count
    if X == Y:
        print("Draw!")
    elif X == "Rock" and Y == "Paper":
        print("You win!")
        player_win_count += 1
    elif X == "Scissor" and Y == "Rock":
        print("You win!")
        player_win_count += 1
    elif X == "Paper" and Y == "Scissor":
        print("You win!")
        player_win_count += 1
    elif Y == 'Unknown':
        print('I was not able to decipher your hand gesture!')
    else:
        print("Computer wins!")
        computer_win_count +=1

def countdown(t):
    while t:
      mins = t // 60
      secs = t % 60
      timer = '{:02d}:{:02d}'.format(mins, secs)
      print(timer, end="\r") # overwrite previous line 
      time.sleep(1)
      t -= 1
    print('Rock Paper Scissor!!!')


print("Welcome to my game of rock, paper, scissors!")
answer = input("Do you want to play? Y/N ")
if answer != "Y".lower():
    quit()
print("Okay! Let's play best of three :)")
start_time = time.time()

while True: 
    ret, frame = cap.read()
    cv2.imshow('Rock_Paper_Scissor', frame)
    current_time = time.time()
    ready = True
    if int(current_time - start_time)%8 == 0 and int(current_time - start_time) > 1 and ready:
        game_evaluation(Y = player_choice(), X = computer_choice())
        print("Player score: ", player_win_count)
        print("Computer score: ", computer_win_count)
        ready = False
        countdown(3)
        ready = True
        if player_win_count == 3:
            print("You win the game!")
            break
        elif computer_win_count == 3:
            print("Computer wins the game!")
            break
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
cap.release()
cv2.destroyAllWindows()