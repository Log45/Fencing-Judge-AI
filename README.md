This project is meant to be able to accurately score Saber fencing bouts, hopefully eventually in real time with a camera input, but at least given a video of an already recorded fencing bout.

I plan to train this model on all the olympic saber fencing bouts I can find on youtube initially, and may include amateur bouts as well to diversify the data so that it is also able to score slower bouts.

TODO:
- Choose a classification model
- Create a dataset to train the model on
- (Maybe create a program to automatically trim videos into single points to train the data on.)

R&D Log:

5/16/23
- Project folder has been created, I'm beginning to research the best classification models for CV in PyTorch (https://pytorch.org/vision/stable/models.html)
- While I figure out which model to use, I'm going to continue following and hopefully finish Daniel Burke's PyTorch course. (https://www.youtube.com/watch?v=V_xro1bcAuA&t=32243s)
- In order to save A LOT of time, I'm also pursuing a method to automatically cut videos to be a viable piece of data. 
- - To better develop this dataset, I am using pytube to download videos from youtube (code gotten from https://www.freecodecamp.org/news/python-program-to-download-youtube-videos/)