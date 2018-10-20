# coding=utf-8
import time

import Leap
from Leap import CircleGesture, SwipeGesture, KeyTapGesture, ScreenTapGesture
import FingerDirection


def rightHandAnalysis(frame):
    objectIdentified = "null"
    fingersDirection = FingerDirection.fingerOrientation(frame.hands[0])
    thumb_extended = frame.hands[0].fingers[0].is_extended

    #print str(fingersDirection)

    # for hand in frame.hands:
    #    for finger in hand.fingers:
    #        print "ID: " + str(finger.id) + " Direction: " \
    #              + str(finger.tip_position) + " Is extended: " + str(finger.is_extended) \
    #              + " Palm Position: " + str(finger.hand.palm_position)

    if frame.hands[0].palm_position.y < 500:
        if fingersDirection[0] == "up":
            if fingersDirection[1] == "down":
                if fingersDirection[2] == "down":
                    if fingersDirection[3] == "down":
                        if fingersDirection[4] == "down":
                            if frame.hands[0].fingers[0].tip_position.x > frame.hands[0].fingers[1].tip_position.x:
                                if frame.hands[0].fingers[1].tip_position.z + 10 \
                                        < frame.hands[0].fingers[0].bone(1).next_joint.z:
                                    objectIdentified = "n"
                                else:
                                    objectIdentified = "m"
                                # Hand must be close to the camera & Index finger must be raise a little but still down
                            else:
                                if frame.hands[0].fingers[1].tip_position.z \
                                        < frame.hands[0].palm_position.z + 10:
                                    objectIdentified = "a"  # Thumb a little apart
                                else:
                                    objectIdentified = "o"  # Fingers completely in front of the camera
                        elif fingersDirection[4] == "up":
                            if not thumb_extended:
                                if frame.hands[0].fingers[4].tip_position.x > frame.hands[0].fingers[1].tip_position.x:
                                    objectIdentified = "i"
                                else:
                                    objectIdentified = "j"
                            else:
                                objectIdentified = "y"

            elif fingersDirection[1] == "up":
                if fingersDirection[2] == "down":
                    if fingersDirection[3] == "down":
                        if fingersDirection[4] == "down":  # Gotta get close to recognize them right
                            if thumb_extended:
                                objectIdentified = "l"
                                if frame.gestures()[0].type == Leap.Gesture.TYPE_SWIPE:
                                    objectIdentified = "ll"

                            elif frame.hands[0].fingers[2].tip_position.z > frame.hands[0].palm_position.z:
                                objectIdentified = "k"
                            else:
                                objectIdentified = "d"

                elif fingersDirection[2] == "up":
                    if fingersDirection[3] == "down":
                        if fingersDirection[4] == "down":
                            if abs(frame.hands[0].fingers[1].tip_position.x
                                   - frame.hands[0].fingers[2].tip_position.x) > 30:
                                objectIdentified = "v"
                            elif abs(frame.hands[0].fingers[1].tip_position.x
                                     - frame.hands[0].fingers[2].tip_position.x) > 15:
                                objectIdentified = "u"  # Different for v and r
                            else:
                                objectIdentified = "r"  # Slightly tilted to the front to see the tips
                                if frame.gestures()[0].type == Leap.Gesture.TYPE_SWIPE:
                                    objectIdentified = "rr"
                    elif fingersDirection[3] == "up":
                        if fingersDirection[4] == "down":
                            objectIdentified = "w"
                        elif fingersDirection[4] == "up":
                            if not thumb_extended:
                                objectIdentified = "b"
                            else:
                                if frame.gestures()[0].type == Leap.Gesture.TYPE_SWIPE and abs(frame.hands[0].palm_velocity.x) > 750:
                                    objectIdentified = "adios"

            elif fingersDirection[1] == "left":
                if fingersDirection[3] != "left":
                    if fingersDirection[4] != "left":
                        objectIdentified = "ch"
                        # Do it slightly under the camera

            elif fingersDirection[1] == "forward":
                if fingersDirection[2] == "up":
                    if fingersDirection[3] == "up":
                            if frame.hands[0].fingers[0].tip_position.x < frame.hands[0].fingers[1].tip_position.x + 10:
                                objectIdentified = "f"
                            else:
                                objectIdentified = "t"

                elif fingersDirection[2] == "forward":
                    if fingersDirection[3] == "forward":

                        if frame.hands[0].palm_velocity.y > 250:
                            objectIdentified = "despacio"  # Very to the right
                        elif fingersDirection[4] == "forward":
                            objectIdentified = "e"  # Tilted slightly back, maybe confuse with a

            elif fingersDirection[1] == "right":
                if fingersDirection[2] == "right":
                    if fingersDirection[3] == "right":
                        if fingersDirection[4] == "right":
                            if frame.hands[0].palm_velocity.x > 850:
                                objectIdentified = "llamar"

        elif fingersDirection[0] == "forward":
            if fingersDirection[1] == "forward":
                if fingersDirection[2] == "forward":
                    if fingersDirection[3] == "forward":
                        if fingersDirection[4] == "forward":
                            objectIdentified = "c"  # Gotta get close to recognize them right & maybe confused with e

                elif fingersDirection[2] == "down":
                    objectIdentified = "p"

        elif fingersDirection[1] == "left":  # INDEX FINGER, no thumb
            if fingersDirection[2] == "left":
                if abs(frame.hands[0].palm_velocity.x) > 600:
                    objectIdentified = "Puntarenas"
                else:
                    objectIdentified = "h"
            elif fingersDirection[2] == "down":
                if fingersDirection[3] == "down":
                    if fingersDirection[4] == "down":
                        objectIdentified == "p"  # Must be way above the camera
            else:
                objectIdentified = "g"
            # Do it slightly under the camera

        elif fingersDirection[0] == "left":
            if fingersDirection[1] == "forward":
                if fingersDirection[2] == "down":
                    if fingersDirection[3] == "down":
                        if fingersDirection[4] == "down":
                            pass
                            #objectIdentified = "x"

        elif fingersDirection[0] == "down":
            if fingersDirection[1] == "down":
                if frame.hands[0].fingers[1].is_extended and not fingersDirection[4] == "down":
                    objectIdentified = "q"

    # Z is left for its movement
    return objectIdentified


def leftHandAnalysis(frame):
    number = "null"
    fingersDirection = FingerDirection.fingerOrientation(frame.hands[0])
    thumb_extended = frame.hands[0].fingers[0].is_extended

    #print str(fingersDirection)
    if frame.hands[0].palm_position.y < 500:
        if fingersDirection[1] == "right":
            if fingersDirection[4] == "left":
                number = "ella"

        elif frame.hands[0].palm_velocity.x < -850:
            number = "10"
        elif fingersDirection == ["up", "up", "down", "down", "down"]:
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

            if frame.hands[0].fingers[0].tip_position.x < frame.hands[0].fingers[2].tip_position.x:
                number = "s"
            elif frame.hands[0].fingers[0].tip_position.x < frame.hands[0].fingers[1].tip_position.x + 10:
                number = "0"

            #print str(frame.hands[0].palm_velocity.x)

    return number


def farAwayGestures(frame):
    thumb_extended = frame.hands[0].fingers[0].is_extended
    index_extended = frame.hands[0].fingers[1].is_extended
    fingersDirection = FingerDirection.fingerOrientation(frame.hands[0])
    objectIdentified = "null"

    if len(frame.hands) == 1:
        if fingersDirection[0] == "left" and fingersDirection[1] == "up" and not frame.hands[0].fingers[3].is_extended:
            if abs(frame.hands[0].palm_velocity.z) > 400:
                objectIdentified = "Limon"
        elif abs(frame.hands[0].palm_velocity.x) > 850 and abs(frame.hands[0].palm_velocity.y) < 650 and not thumb_extended \
                and 450 > abs(frame.hands[0].palm_velocity.z) and not index_extended:
            objectIdentified = "Guanacaste"

        elif frame.hands[0].palm_velocity.z < -1000 and 650 > abs(frame.hands[0].palm_velocity.y) \
                and 650 > abs(frame.hands[0].palm_velocity.x):
            objectIdentified = "Alajuela"

        elif frame.hands[0].palm_velocity.z > 700  and not thumb_extended\
                and frame.hands[0].fingers[0].tip_position.x - 15 > frame.hands[0].fingers[4].tip_position.x:
            objectIdentified = "Heredia"

        elif abs(frame.hands[0].palm_velocity.y) > 750 and thumb_extended and 350 > abs(frame.hands[0].palm_velocity.x)\
                and 350 > abs(frame.hands[0].palm_velocity.z) and not index_extended:
            objectIdentified = "Cartago"

    elif len(frame.hands) == 2:
        if frame.hands[0].is_left:
            handTracked = frame.hands[1]
        else:
            handTracked = frame.hands[0]
            if handTracked.palm_velocity.z > 750:
                objectIdentified = "San Jose"

    return objectIdentified
