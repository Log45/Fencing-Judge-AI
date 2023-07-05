This project is meant to be able to accurately score Saber fencing bouts, hopefully eventually in real time with a camera input, but at least given a video of an already recorded fencing bout.

I plan to train this model on all the olympic saber fencing bouts I can find on youtube initially, and may include amateur bouts as well to diversify the data so that it is also able to score slower bouts.

Fencing Dataset (clips of bouts from world cups, olympics, and college club fencing):
https://drive.google.com/drive/folders/1VmFhBmm88Z9LU0zVJsLevOETzgLU8qim?usp=sharing 

TODO:
- Choose a classification model
- Create a dataset to train the model on
    - Maybe create a program to automatically trim videos into single points to train the data on.

R&D Log:

5/16/23
- Project folder has been created, I'm beginning to research the best classification models for CV in PyTorch (https://pytorch.org/vision/stable/models.html)
- While I figure out which model to use, I'm going to continue following and hopefully finish Daniel Bourke's PyTorch course. (https://www.youtube.com/watch?v=V_xro1bcAuA&t=32243s)
- In order to save A LOT of time, I'm also pursuing a method to automatically cut videos to be a viable piece of data. 
    - To better develop this dataset, I am using pytube to download videos from youtube (code gotten from https://www.freecodecamp.org/news/python-program-to-download-youtube-videos/)
        - pytube seems like it will work (though downloads seem pretty slow), but I keep running into an age-restriction issue even when I am signed into YouTube
        - the program is confirmed to work with non-age-restricted content, but I still need to make it work for age-restricted videos like fencing tournaments
        - (it seems like no matter what youtube account I use, it still claims that I am not logged in and does not allow "age restricted" content to be downloaded.)
        - it honestly might just be easier to use a youtubetomp4 website instead (https://en.y2mate.is/) seems to work (try not to accidentally download a virus)

5/17/23
- I've found multiple hours of fencing bouts to use for the data set, now I am starting to download them into the yt_downloads folder.
    - Later, I'm going to need to edit them all down to single touches in order to get concise training data (this is going to take so many hours...)
- It will be helpful later to train the model on specific happenings of fencing (like point line, parry-reposte, attack-no, etc...)
- **Note** Do not try to open any video longer than 15 minutes in VSC, it will crash.
- For future reference, do not push gigabytes of data into a repo in one push

5/18/23
- Apparently people have already done this, but I'm just gonna cope and carry on doing it anyway. (Allez Go, https://github.com/sholtodouglas/fencing-AI, probably more)

5/30/23
- Currently, I'm going through Daniel Bourke's PyTorch course and I just want to note that the actual scoring of the fencing bout is probably going to be a classification problem
- (Might need to use BCEWithLogitLoss and SGD or CrossEntropyLoss)
- If I do go down the painstaking route of making an app for visualizing the model and the bout itself, I might be able to use and modify YOLOv5, see https://pytorch.org/hub/ultralytics_yolov5/

6/25-6/26/23
- Finally taking the time to sort through the fencing clips I downloaded; I now have around 200 clips edited to the length of a touch and now I need to finish editing the last few bouts in the Budapest World Cup video. 
    - Once I’m done with Budapest, I’m gonna download more clips from my list of videos and begin editing them

- Along with the professionally scored videos; I’m going to get videos from fencing tournaments and bouts during my time fencing at RIT and edit/label those 

- In addition to labeling touches from bouts; I need to get a lot of picture of fencing sabers to train the ai to recognize smaller portions of the bouts 
    - I also am going to need to take the touches and break them up into different actions to train the ai on so it will be able to give reason for its calls 

- During all of this I also am gonna need to implement some cv to trace different body parts and weapons for better representation and understanding by the model 
    (This is going to be a long project 😭)

- Need to create a Dropbox for all the fencing clips and link to that Dropbox in the readme file 
- After creating a Dropbox and realizing it has a 2gb limit, I'm just going to make a google drive folder to hold all the clips

6/27/23
- I finished cutting the tournament from Budapest, I know have 364 touches that need to be labeled.
- I'm uploading all of the datapoints to a google drive folder that will be linked below and at the top of the readme:
    - https://drive.google.com/drive/folders/1VmFhBmm88Z9LU0zVJsLevOETzgLU8qim?usp=sharing 
- Resource for labeling video frames with YOLOv4: 
    - https://www.youtube.com/watch?v=9b5g-smg5Mo 

7/4/23
- After talking with my mentor at BNL, here are more things to look into:
    - Segment Anything Model (by META) to annotate data
        - https://github.com/facebookresearch/segment-anything 
        - @article{kirillov2023segany,
            title={Segment Anything},
            author={Kirillov, Alexander and Mintun, Eric and Ravi, Nikhila and Mao, Hanzi and Rolland, Chloe and Gustafson, Laura and Xiao, Tete and Whitehead, Spencer and Berg, Alexander C. and Lo, Wan-Yen and Doll{\'a}r, Piotr and Girshick, Ross},
            journal={arXiv:2304.02643},
            year={2023}
            }
    - Go to papers with code and look into:
        - Activity recognition
        - Human pose estimation