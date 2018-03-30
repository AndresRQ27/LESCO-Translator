# coding=utf-8
import Leap
import FingerDirection

# class-level parameters
last_20_Frames = []
oldestFrame = 0


def wordAnalysis(frame):
    fingersDirection = FingerDirection.fingerOrientation(frame.hands[0])
    if fingersDirection[0] == "up":
        if fingersDirection[1] == "down":
            if fingersDirection[2] == "down":
                if fingersDirection[3] == "down":
                    if fingersDirection[4] == "down":
                        print "a"  # TODO or n or o. Gotta be specific. ñ with frontal movement
                    elif fingersDirection[4] == "up":
                        print "i"  # TODO if there is speed, it's a j

        elif fingersDirection[1] == "up":
            if fingersDirection[2] == "forward":
                if fingersDirection[3] == "down":
                    if fingersDirection[4] == "down":
                        print "k"

            elif fingersDirection[2] == "down":
                if fingersDirection[3] == "down":
                    if fingersDirection[4] == "down":
                        print "d"

            elif fingersDirection[2] == "up":
                if fingersDirection[3] == "down":
                    if fingersDirection[4] == "down":
                        print "u"  # Different for v
                elif fingersDirection[3] == "up":
                    if fingersDirection[4] == "down":
                        print "w"

        elif fingersDirection[1] == "left":
            if fingersDirection[2] == "left":
                print "ch"

            elif fingersDirection[2] == "up":
                if fingersDirection[3] == "down":
                    if fingersDirection[4] == "down":
                        print "r"  # TODO apply movement for rr

        elif fingersDirection[1] == "forward":
            if fingersDirection[2] == "up":
                if fingersDirection[3] == "up":
                    if fingersDirection[4] == "up":
                        print "t"

    elif fingersDirection[0] == "right":
        if fingersDirection[1] == "up":
            if fingersDirection[2] == "up":
                if fingersDirection[3] == "up":
                    if fingersDirection[4] == "up":
                        print "b"

        elif fingersDirection[1] == "down":
            if fingersDirection[2] == "down":
                if fingersDirection[3] == "down":
                    if fingersDirection[4] == "down":
                        print "e"  # TODO different for m or s (maybe s y backwards)

                elif fingersDirection[3] == "null":  # in case of not detected, else implement backwards
                    print "q"

    elif fingersDirection[0] == "forward":
        if fingersDirection[1] == "forward":
            if fingersDirection[2] == "forward":
                if fingersDirection[3] == "forward":
                    if fingersDirection[4] == "forward":
                        print "c"

            elif fingersDirection[2] == "up":
                if fingersDirection[3] == "up":
                    if fingersDirection[4] == "up":
                        print "f"

            elif fingersDirection[2] == "down":
                print "p"

    elif fingersDirection[0] == "left":
        if fingersDirection[1] == "left":
            if fingersDirection[2] == "right":  # Maybe a problem
                print "g"
            elif fingersDirection[2] == "left":
                print "h"

        elif fingersDirection[1] == "up":
            if fingersDirection[2] == "down":
                if fingersDirection[3] == "down":
                    if fingersDirection[4] == "down":
                        print "l"  # TODO apply movement for "ll"

        elif fingersDirection[1] == "forward":
            if fingersDirection[2] == "down":
                if fingersDirection[3] == "down":
                    if fingersDirection[4] == "down":
                        print "x"

        elif fingersDirection[1] == "down":
            if fingersDirection[2] == "down":
                if fingersDirection[3] == "down":
                    if fingersDirection[4] == "right":
                        print "y"

    # Z is left for its movement

    return 0


def numberAnalysis(fingers):
    if fingers == ["down", "up", "down", "down", "down"]:
        return 1
    if fingers == ["down", "up", "up", "down", "down"]:
        return 2
    if fingers == ["up", "up", "up", "down", "down"]:
        return 3
    if fingers == ["down", "up", "up", "up", "up"]:
        return 4
    if fingers == ["down", "up", "up", "up", "up"]:
        return 5
    if fingers == ["left", "up", "up", "up", "down"]:  # TODO thumb could be up or left
        return 6
    if fingers == ["left", "up", "up", "down", "up"]:
        return 7
    if fingers == ["left", "up", "down", "up", "up"]:
        return 8
    if fingers == ["left", "down", "up", "up", "up"]:
        return 9
    if fingers == ["up", "down", "down", "down", "down"]:
        return 1
    return 0
