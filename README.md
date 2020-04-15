# rll-parser
Parse a Rocket League stream/video and pull out relevant information for league stats.

# SETUP / DEPENDENCIES

- Install python3, pip3 (apt package python3-pip)
- Install opencv (easy method: `pip3 install opencv-python`)

# USAGE
- `python3 ParseRL.py <videoPath> <weekNum>`
- PARAM `videoPath`: string representing the path to the video file, not including the file name
- PARAM `weekNum`: integer representing the current gameweek
- Other notes:  
  - the video name should be 'videoPath + gameweek + weekNum + .mp4' ('/videoPath/gameweek1.mp4')
  - output frames will be placed in videoPath/gameweek#, where # is the weekNum ('/videopath/gameweek1/frame#.jpg')