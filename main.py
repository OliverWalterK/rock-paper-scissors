import cv2, random, time
from keras.models import load_model
import numpy as np      

player_win_count = 0
computer_win_count = 0
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

def computer_choice():

    rng = random.randint(1,3)
    if rng == 1:
        X = 'Rock'
    elif rng == 2:
        X = 'Scissor'
    else:
        X = 'Paper'

    print("The computer chooses " + X + "!")
    return X

def player_choice(prediction, accuracy = 0.7):

    if prediction[0][0] > accuracy:
        Y = "Rock"
    elif prediction[0][1] > accuracy:
        Y = "Scissor"
    elif prediction[0][2] > accuracy:
        Y = "Paper"
    else:
        Y = "Unknown."

    print("You chooses " + Y + "!")
    return Y

def game_evaluation(X, Y):

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
    else:
        print("Computer wins!")
        computer_win_count +=1

def get_prediction(frame):
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 
    data[0] = normalized_image
    prediction = model.predict(data)
    return prediction

def countdown(t):
    while t:
      mins = t // 60
      secs = t % 60
      timer = '{:02d}:{:02d}'.format(mins, secs)
      print(timer, end="\r") # overwrite previous line 
      time.sleep(1)
      t -= 1
    print('Rock Paper Scissor!!!')


print("Welcome to rock, paper, scissors!")
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
        prediction = get_prediction(frame)
        game_evaluation(Y = player_choice(prediction), X = computer_choice())
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