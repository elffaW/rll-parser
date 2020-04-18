import sys
import os
import cv2
import numpy as np
from tesserocr import PyTessBaseAPI

FRAMES_PER_SECOND = 60
SECONDS_PER_CAPTURE = 15

# Function to extract frames 
# @param basePath string path to gameweek#.mp4 video, ends with OS path separator
# @param weekNum int current gameweek number to parse
def FrameCapture(basePath, weekNum):
    gameweekPath = basePath + 'gameweek' + str(weekNum)
    if not os.path.exists(gameweekPath):
        print("{0} doesn't exist, creating it...".format(gameweekPath))
        os.mkdir(gameweekPath)

    # scoreboard location based on 1280 x 800 image
    # TODO: maybe make this a percentage so it can adapt to different resolutions?
    scoreboard_UpperLeft = ( 340, 195 )
    scoreboard_LowerRight = ( 1165, 520 )
    allWhite = cv2.imread("masks/allWhite.jpg")
    scoreboardMask = cv2.rectangle(allWhite, scoreboard_UpperLeft, scoreboard_LowerRight, 0, -1, 4)
    scoreboardMask = cv2.bitwise_not(scoreboardMask)
    # cv2.imwrite("scoreboardMask.jpg", scoreboardMask)
    # intermissionTemplate = cv2.imread("masks/intermission.jpg")

    thresholdLower = ( 0, 0, 0, 0 )
    thresholdUpper = ( 179, 148, 174, 0 )
    # Path to video file (/basePath/with/gameweek#.mp4)
    vidObj = cv2.VideoCapture(gameweekPath + ".mp4") 
    # Used as counter variable 
    count = 108
    # checks whether frames were extracted 
    success = 1
    while success and count < 110:
        print("----------------------------------------------------------------------------------")
        print("Processing frame number {0} ({1})".format(count, SECONDS_PER_CAPTURE*1000*count))
        # skip ahead by specified number of seconds
        vidObj.set(cv2.CAP_PROP_POS_MSEC, SECONDS_PER_CAPTURE*1000*count)
        # read the image at specified frame
        success, image = vidObj.read() 
        # save the image
        if success:
            maskImg = cv2.bitwise_and(image, scoreboardMask)
            thresholdImg = cv2.inRange(maskImg, thresholdLower, thresholdUpper)
            # cv2.imshow("matchResult", matchResult8)
            cv2.imwrite(gameweekPath + os.path.sep + "%04dframe.jpg" % count, thresholdImg)
            with PyTessBaseAPI() as api:
                api.SetImageFile(gameweekPath + os.path.sep + "%04dframe.jpg" % count)
                print("TEXT:")
                print(api.GetUTF8Text())
                print("CONFIDENCES:")
                print(api.AllWordConfidences())
        count += 1
        print("----------------------------------------------------------------------------------")

def UsageError():
    print("USAGE: `python3 ParseRL.py <videoPath> <weekNum>`")
    print("PARAM videoPath: string representing the path to the video file, not including the file name")
    print("PARAM weekNum: integer representing the current gameweek")
    print("\t- the video name should be 'videoPath + gameweek + weekNum + .mp4' ('/videoPath/gameweek1.mp4')")
    print("\t- output frames will be placed in videoPath/gameweek#, where # is the weekNum ('/videopath/gameweek1/frame#.jpg')")
    exit(1)

# Driver Code 
if __name__ == '__main__':
    if len(sys.argv) != 3:
        UsageError()

    basePath = str(sys.argv[1])
    weekNum = str(sys.argv[2])
    if not basePath.endswith(os.path.sep):
        basePath = basePath + os.path.sep
    
    print("basePath: {0}, weekNum: {1}".format(basePath, weekNum))
    # Calling the function 
    # FrameCapture("/h/twitch/gameweek1.mp4")
    # video path is
    FrameCapture(basePath, weekNum)
