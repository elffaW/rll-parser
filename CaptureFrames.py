# Program To Read video 
# and Extract Frames 
import cv2 

FRAMES_PER_SECOND = 60
SECONDS_PER_CAPTURE = 15

# Function to extract frames 
def FrameCapture(path): 
    # Path to video file 
    vidObj = cv2.VideoCapture(path) 
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
            cv2.imwrite("/h/twitch/gameweek1/frame%d.jpg" % count, image)
        count += 1
  
# Driver Code 
if __name__ == '__main__': 
    # Calling the function 
    FrameCapture("/h/twitch/gameweek1.mp4") 
