# Rock-Paper-Scissors
---

This is my first project under AiCore where I code a rock, paper, scissors game.

The game is played with the webcam. It also uses a machine learning model that has been trained by me to distinguish between the three options in RPS (rock, paper or scissors). The model was made via [Teachable Machine](http://www.teachablemachine.withgoogle.com)

##### **Limitations:**

The code will use the CPU speed of your system to cheat and introduce a "fake" timer. The timer will speed up for faster CPU's and slow down for slow CPU's. The reason for this is to appear as though the stream of imgaes never stops. I did not want a countdown that would stop the video feed. Another alternative would be to use the frequency rate of the camera (fps) and use that instead of the cpu rate I used. 