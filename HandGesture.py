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


def numberAnalysis(frame):
    if str(frame.hands[0]) != "Invalid Hand":
        fingersDirection = FingerDirection.fingerOrientation(frame.hands[0])
        thumb_extended = frame.hands[0].fingers[0].is_extended
        if fingersDirection == ["up", "up", "down", "down", "down"]:
            print 1
        elif fingersDirection == ["up", "up", "up", "down", "down"] and not thumb_extended:
            print 2
        elif fingersDirection == ["up", "up", "up", "down", "down"]:
            print 3
        elif fingersDirection == ["up", "up", "up", "up", "up"] and not thumb_extended:
            print 4
        elif fingersDirection == ["up", "up", "up", "up", "up"]:
            print 5
        elif fingersDirection == ["up", "up", "up", "up", "down"] and not thumb_extended:
            print 6
        elif fingersDirection == ["up", "up", "up", "down", "up"] and not thumb_extended:
            print 7
        elif fingersDirection == ["up", "up", "down", "up", "up"] and not thumb_extended:
            print 8
        elif fingersDirection == ["up", "down", "up", "up", "up"] and not thumb_extended:
            print 9
        elif fingersDirection == ["up", "down", "down", "down", "down"]: #TODO: implementar movimiento
            print 10
    else:
        print "Invalid Hand"
