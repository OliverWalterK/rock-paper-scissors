# Rock-Paper-Scissors
---

This is my first project under AiCore where I code a rock, paper, scissors game. The game is played with the webcam. It also uses a machine learning model that has been trained by me to distinguish between the three options in RPS (rock, paper or scissors). The model was made via [Teachable Machine](http://www.teachablemachine.withgoogle.com)

### Milestone 1
---

Using the website: teachable machine, one is able to create a machine learning model that can be trained using video or audio data. For this application, we will use the webcam to give the model a stream of pictures. The model will then, with a percentage accuracy, determine what hand gesture has been performed by th user. This is rock, paper, scissors after all..

![Screenshot 2022-06-08 162702](https://user-images.githubusercontent.com/97681246/172657430-33b13375-2440-4e5d-b995-c21d5685fa48.png)

This shows how the model is about to be trained with the three options of rock, paper or scissors.

![Screenshot 2022-06-08 162739](https://user-images.githubusercontent.com/97681246/172657544-2df81620-cb3c-4167-b15f-9fe21b559ffb.png)

After the model has been trained, one is able to download the model and use it in our game code.

### Milestone 2
---

The game code structure will be as follows:
1.

### **Limitations:**

The code will use the CPU speed of your system and introduce a "fake" timer. The timer will speed up for faster CPU's and slow down for slower CPU's. The reason for this is to appear as though the webcam stream of images never stops. I did not want an actual countdown that would stop the video feed/loop.
