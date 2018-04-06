# coding=utf-8
from threading import Timer

import Leap
import FingerDirection

def wordAnalysis(frame):
    letter = "null"
    fingersDirection = FingerDirection.fingerOrientation(frame.hands[0])
    thumb_extended = frame.hands[0].fingers[0].is_extended

    # for hand in frame.hands:
    #    for finger in hand.fingers:
    #        print "ID: " + str(finger.id) + " Direction: " \
    #              + str(finger.tip_position) + " Is extended: " + str(finger.is_extended) \
    #              + " Palm Position: " + str(finger.hand.palm_position)

    if fingersDirection[0] == "up":
        if fingersDirection[1] == "down":
            if fingersDirection[2] == "down":
                if fingersDirection[3] == "down":
                    if fingersDirection[4] == "down":
                        if frame.hands[0].fingers[0].tip_position.x > frame.hands[0].fingers[1].tip_position.x:
                            if frame.hands[0].fingers[1].tip_position.z + 10 \
                                    < frame.hands[0].fingers[0].bone(1).next_joint.z:
                                letter = "n"  # TODO: analyze movement
                            else:
                                letter = "m"
                            # Hand must be close to the camera & Index finger must be raise a little but still down
                        else:
                            if frame.hands[0].fingers[1].tip_position.z \
                                    < frame.hands[0].palm_position.z + 10:
                                letter = "a"  # Thumb a little apart
                            else:
                                letter = "o"  # Fingers completely in front of the camera
                    elif fingersDirection[4] == "up":
                        if not thumb_extended:
                            letter = "i"  # TODO if there is speed, it's a j
                        else:
                            letter = "y"

        elif fingersDirection[1] == "up":
            if fingersDirection[2] == "down":
                if fingersDirection[3] == "down":
                    if fingersDirection[4] == "down":  # Gotta get close to recognize them right
                        if thumb_extended:
                            letter = "l"  # TODO: implement gesture for LL
                        elif frame.hands[0].fingers[2].tip_position.z > frame.hands[0].palm_position.z:
                            letter = "k"
                        else:
                            letter = "d"

            elif fingersDirection[2] == "up":
                if fingersDirection[3] == "down":
                    if fingersDirection[4] == "down":
                        if abs(frame.hands[0].fingers[1].tip_position.x
                               - frame.hands[0].fingers[2].tip_position.x) > 30:
                            letter = "v"
                        elif abs(frame.hands[0].fingers[1].tip_position.x
                                 - frame.hands[0].fingers[2].tip_position.x) > 8:
                            letter = "u"  # Different for v and r
                        else:
                            letter = "r"  # Slightly tilted to the front to see the tips
                elif fingersDirection[3] == "up":
                    if fingersDirection[4] == "down":
                        letter = "w"
                    elif fingersDirection[4] == "up" and not thumb_extended:
                        letter = "b"

        elif fingersDirection[1] == "left":
            if fingersDirection[3] != "left":
                if fingersDirection[4] != "left":
                    letter = "ch"
                    # Do it slightly under the camera

        elif fingersDirection[1] == "forward":
            if fingersDirection[2] == "up":
                if fingersDirection[3] == "up":
                    if fingersDirection[4] == "up":
                        if frame.hands[0].fingers[0].tip_position.x < frame.hands[0].fingers[1].tip_position.x:
                            letter = "f"
                        else:
                            letter = "t"

            elif fingersDirection[2] == "forward":
                if fingersDirection[3] == "forward":
                    if fingersDirection[4] == "forward":
                        letter = "e"  # Tilted slightly back, maybe confuse with a

            elif fingersDirection[2] == "down":
                if fingersDirection[3] == "down":
                    if fingersDirection[4] == "down":
                        letter = "x"

    elif fingersDirection[0] == "forward":
        if fingersDirection[1] == "forward":
            if fingersDirection[2] == "forward":
                if fingersDirection[3] == "forward":
                    if fingersDirection[4] == "forward":
                        letter = "c"  # Gotta get close to recognize them right & maybe confused with e

            elif fingersDirection[2] == "down":
                letter = "p"

    elif fingersDirection[1] == "left":  # INDEX FINGER, no thumb
        if fingersDirection[2] == "left":
            letter = "h"
        elif fingersDirection[2] == "down":
            if fingersDirection[3] == "down":
                if fingersDirection[4] == "down":
                    letter == "p"  # Must be way above the camera
        else:
            letter = "g"
        # Do it slightly under the camera

    elif fingersDirection[0] == "left":
        if fingersDirection[1] == "forward":
            if fingersDirection[2] == "down":
                if fingersDirection[3] == "down":
                    if fingersDirection[4] == "down":
                        letter = "x"

    elif fingersDirection[0] == "down":
        if fingersDirection[1] == "down":
            if frame.hands[0].fingers[1].is_extended and not fingersDirection[4] == "down":
                letter = "q"

    # Z is left for its movement
    return letter


def numberAnalysis(frame):
    number = "null"
    fingersDirection = FingerDirection.fingerOrientation(frame.hands[0])
    thumb_extended = frame.hands[0].fingers[0].is_extended
    if fingersDirection == ["up", "up", "down", "down", "down"]:
        number = "1"
    elif fingersDirection == ["up", "up", "up", "down", "down"] and not thumb_extended:
        number = "2"
    elif fingersDirection == ["up", "up", "up", "down", "down"]:
        number = "3"
    elif fingersDirection == ["up", "up", "up", "up", "up"] and not thumb_extended:
        number = "4"
    elif fingersDirection == ["up", "up", "up", "up", "up"]:
        number = "5"
    elif fingersDirection == ["up", "up", "up", "up", "down"] and not thumb_extended:
        number = "6"
    elif fingersDirection == ["up", "up", "up", "down", "up"] and not thumb_extended:
        number = "7"
    elif fingersDirection == ["up", "up", "down", "up", "up"] and not thumb_extended:
        number = "8"
    elif fingersDirection == ["up", "down", "up", "up", "up"] and not thumb_extended:
        number = "9"
    elif fingersDirection == ["up", "down", "down", "down", "down"]:  # TODO: implementar movimiento
        if frame.hands[0].fingers[0].tip_position.x < frame.hands[0].fingers[1].tip_position.x:
            number = "s"
        else:
            number = "10"

    return number
