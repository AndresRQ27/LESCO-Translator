import Leap

def fingerOrientation(hand):
    # Verify when the thumb is "extended"; if it is extended left/right or just looking up
    """
    Function finger.is_extended
        Type:	boolean
        Whether or not the Pointable is more or less straight.

    Function finger.type
        0 = TYPE_THUMB
        1 = TYPE_INDEX
        2 = TYPE_MIDDLE
        3 = TYPE_RING
        4 = TYPE_PINKY

    @param hand: hand with the fingers to analyze
    @return: a list with the direction (up, down, left right, forward) of the fingers (thumb, index, middle, ring, pinky)
    """
    fingersDirection = []
    for finger in hand.fingers:

        if is_up(finger.direction):
            fingersDirection.append("up")
        elif is_forward(finger):
            fingersDirection.append("forward")
        elif is_down(finger.direction):
            fingersDirection.append("down")
        elif is_left(finger.direction):
            fingersDirection.append("left")
        elif is_right(finger.direction):
            fingersDirection.append("right")
        else:
            #print "Couldn't calculate finger " + finger.type
            fingersDirection.append("null")

        #print fingersDirection[len(fingersDirection)-1]

    return fingersDirection


def is_forward(finger):
    """
    Calculates is the finger is facing front by it's direction vector
    @param vector: contains the directions to analyze
    @return: boolean true if correct
    """
    if finger.hand.is_left:
        if finger.direction.y < -0.9:
            return True
        else:
            return False
    else:
        if finger.direction.y < -0.75:
            return True
        else:
            return False


def is_left(vector):
    """
    Calculates is the finger is facing left by it's direction vector
    @param vector: contains the directions to analyze
    @return: boolean true if correct
    """
    if vector.x < -0.3:
        return True
    else:
        return False


def is_right(vector):
    """
    Calculates is the finger is facing right by it's direction vector
    @param vector: contains the directions to analyze
    @return: boolean true if correct
    """
    if vector.x > 0.3:
        return True
    else:
        return False


def is_up(vector):
    """
    Calculates is the finger is facing up by it's direction vector
    @param vector: contains the directions to analyze
    @return: boolean true if correct
    """
    if vector.z < -0.3:
        return True
    else:
        return False


def is_down(vector):
    """
    Calculates is the finger is facing down by it's direction vector
    @param vector: contains the directions to analyze
    @return: boolean true if correct
    """
    if vector.z > 0.3:
        return True
    else:
        return False