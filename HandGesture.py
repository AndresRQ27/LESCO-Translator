import Leap

# class-level parameters
last_20_Frames = []
oldestFrame = 0


def wordAnalysis(frame):
    return 0


def numberAnalysis(fingers):
    if fingers == ["down","up","down","down","down"]:
        return 1
    if fingers == ["down","up","up","down","down"]:
        return 2
    if fingers == ["up","up","up","down","down"]:
        return 3
    if fingers == ["down","up","up","up","up"]:
        return 4
    if fingers == ["down","up","up","up","up"]:
        return 5
    if fingers == ["left","up","up","up","down"]: #TODO thumb could be up or left 
        return 6
    if fingers == ["left","up","up","down","up"]:
        return 7
    if fingers == ["left","up","down","up","up"]:
        return 8
    if fingers == ["left","down","up","up","up"]:
        return 9
    if fingers == ["up","down","down","down","down"]:
        return 1
    return 0
