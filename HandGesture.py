# coding=utf-8
import Leap
import FingerDirection

# class-level parameters
thread_array = []
current_object = ""
last_object = ""


def wordAnalysis(frame):
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
                                print "n"  # TODO: analyze movement
                            else:
                                print "m"
                            # Hand must be close to the camera & Index finger must be raise a little but still down
                        else:
                            if frame.hands[0].fingers[1].tip_position.z \
                                    < frame.hands[0].palm_position.z + 10:
                                print "a"  # Thumb a little apart
                            else:
                                print "o"  # Fingers completely in front of the camera
                    elif fingersDirection[4] == "up" and not thumb_extended:
                        print "i"  # TODO if there is speed, it's a j

        elif fingersDirection[1] == "up":
            if fingersDirection[2] == "down":
                if fingersDirection[3] == "down":
                    if fingersDirection[4] == "down":  # Gotta get close to recognize them right
                        if thumb_extended:
                            print "l"  # TODO: implement gesture for LL
                        elif frame.hands[0].fingers[2].tip_position.z > frame.hands[0].palm_position.z:
                            print "k"
                        else:
                            print "d"

            elif fingersDirection[2] == "up":
                if fingersDirection[3] == "down":
                    if fingersDirection[4] == "down":
                        if abs(frame.hands[0].fingers[1].tip_position.x
                               - frame.hands[0].fingers[2].tip_position.x) > 30:
                            print "v"
                        elif abs(frame.hands[0].fingers[1].tip_position.x
                                 - frame.hands[0].fingers[2].tip_position.x) > 8:
                            print "u"  # Different for v and r
                        else:
                            print "r"  # Slightly tilted to the front to see the tips
                elif fingersDirection[3] == "up":
                    if fingersDirection[4] == "down":
                        print "w"
                    elif fingersDirection[4] == "up" and not thumb_extended:
                        print "b"

        elif fingersDirection[1] == "left":
            if fingersDirection[3] != "left":
                if fingersDirection[4] != "left":
                    print "ch"
                    # Do it slightly under the camera

        elif fingersDirection[1] == "forward":
            if fingersDirection[2] == "up":
                if fingersDirection[3] == "up":
                    if fingersDirection[4] == "up":
                        if frame.hands[0].fingers[0].tip_position.x < frame.hands[0].fingers[1].tip_position.x:
                            print "f"
                        else:
                            print "t"

            elif fingersDirection[2] == "forward":
                if fingersDirection[3] == "forward":
                    if fingersDirection[4] == "forward":
                        print "e"  # Tilted slightly back, maybe confuse with a

    elif fingersDirection[0] == "right":
        if fingersDirection[1] == "down":
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
                        print "c"  # Gotta get close to recognize them right

            elif fingersDirection[2] == "down":
                print "p"

    elif fingersDirection[1] == "left":
        if fingersDirection[2] == "left":  # Maybe a problem
            print "h"
        else:
            print "g"
        # Do it slightly under the camera

    elif fingersDirection[0] == "left":
        if fingersDirection[1] == "forward":
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
        elif fingersDirection == ["up", "down", "down", "down", "down"]:  # TODO: implementar movimiento
            print 10
    else:
        print "Invalid Hand"
