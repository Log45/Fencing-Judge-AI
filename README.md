This project is meant to be able to accurately score Saber fencing bouts, hopefully eventually in real time with a camera input, but at least given a video of an already recorded fencing bout.

I plan to train this model on all the olympic saber fencing bouts I can find on youtube initially, and may include amateur bouts as well to diversify the data so that it is also able to score slower bouts.

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