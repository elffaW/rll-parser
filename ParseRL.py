import sys
import os
import cv2 

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

    # Path to video file (/basePath/with/gameweek#.mp4)
    vidObj = cv2.VideoCapture(gameweekPath + ".mp4") 
    # Used as counter variable 
    count = 0
    # checks whether frames were extracted 
    success = 1
    while success: 
        # skip ahead by specified number of seconds
        vidObj.set(cv2.CAP_PROP_POS_MSEC, SECONDS_PER_CAPTURE*1000*count)
        # vidObj object calls read 
        # function extract frames
        success, image = vidObj.read() 
        # Saves the frames with frame-count 
        if success:
            cv2.imwrite(gameweekPath + os.path.sep + "frame%d.jpg" % count, image)
        count += 1

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
    if not basePath.endswith(os.path.sep):
        basePath = basePath + os.path.sep
    try:
        weekNum = int(sys.argv[2])
    except ValueError:
        print("ERROR: second parameter needs to be an integer")
        UsageError()
    
    print("basePath: {0}, weekNum: {1}".format(basePath, weekNum))
    # Calling the function 
    # FrameCapture("/h/twitch/gameweek1.mp4")
    # video path is
    FrameCapture(basePath, weekNum)
