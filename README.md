# Rock-Paper-Scissors
---

This is my first project under AiCore where I code a rock, paper, scissors game. The game is played with the webcam. It also uses a machine learning model that has been trained by me to distinguish between the three options in RPS (rock, paper or scissors). The model was made via [Teachable Machine](http://www.teachablemachine.withgoogle.com)

## Milestone 1
---

Using the website: teachable machine, one is able to create a machine learning model that can be trained using video or audio data. For this application, we will use the webcam to give the model a stream of pictures. The model will then, with a percentage accuracy, determine what hand gesture has been performed by the user. This is rock, paper, scissors after all..

This picture below shows how the model is about to be trained with the three options of rock, paper or scissors.

![Screenshot 2022-06-08 162702](https://user-images.githubusercontent.com/97681246/172657430-33b13375-2440-4e5d-b995-c21d5685fa48.png)

After the model has been trained, one is able to download the model and use it in our game code.

![Screenshot 2022-06-08 162739](https://user-images.githubusercontent.com/97681246/172657544-2df81620-cb3c-4167-b15f-9fe21b559ffb.png)

## Milestone 2
---

The game code structure will be as follows:
1. The computer's "hand" gesture will be determined through the introduction of randomness. To be specific, the computer will take a value of 1-3, at random, which each number signifying either rock, paper or scissors.
![image](https://user-images.githubusercontent.com/97681246/172658641-9b0ee7d5-d91c-4edd-a856-af9cefd55862.png)

2. The player will perform its hand gesture into the camera. The computer will then, based on the teachable machine model, determine which hand gesture was seen. The code will also set a accuracy of 50% meaning that if the model is atleast 50% positive about the shape, it will determine it to be what it sees.
![image](https://user-images.githubusercontent.com/97681246/172659546-ae9e281b-366e-45f1-8d70-45f20c90a77f.png)

3. The computer will now evaluate, based on the players hand gesture, which player has won the round.
![image](https://user-images.githubusercontent.com/97681246/172659796-0ed265a5-f865-4957-8a23-a7384f0438b7.png)


### **Limitations:**

The code will use the CPU speed of your system and introduce a "fake" timer. The timer will speed up for faster CPU's and slow down for slower CPU's. The reason for this is to appear as though the webcam stream of images never stops. I did not want an actual countdown that would stop the video feed/loop.
