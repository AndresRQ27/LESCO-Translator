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
    @return: a vector with the direction (up, down, left right, front) of the fingers (thumb, index, middle, ring, pinky)

    index, middle, ring, pinky can only be front, up or down
    thumb can be front, up, left or right
    """
    fingersDirection = []
    for finger in hand.fingers:
        # Test is_extended method
        """
        if finger.is_extended:
            print "The finger is extended"
        """

        if is_up(finger.direction):
            fingersDirection.append("up")
        elif is_down(finger.direction):
            fingersDirection.append("down")
        elif is_left(finger.direction):
            fingersDirection.append("left")
        elif is_right(finger.direction):
            fingersDirection.append("right")
        elif is_front(finger.direction):
            fingersDirection.append("front")
        else:
            print "Couldn't calculate finger " + finger.type
            fingersDirection.append("null")

    return fingersDirection


def is_front(vector):
    """
    Calculates is the finger is facing front by it's direction vector
    @param vector: contains the directions to analyze
    @return: boolean true if correct
    """
    return True


def is_left(vector):
    """
    Calculates is the finger is facing left by it's direction vector
    @param vector: contains the directions to analyze
    @return: boolean true if correct
    """
    return True


def is_right(vector):
    """
    Calculates is the finger is facing right by it's direction vector
    @param vector: contains the directions to analyze
    @return: boolean true if correct
    """
    return True


def is_up(vector):
    """
    Calculates is the finger is facing up by it's direction vector
    @param vector: contains the directions to analyze
    @return: boolean true if correct
    """
    return True


def is_down(vector):
    """
    Calculates is the finger is facing down by it's direction vector
    @param vector: contains the directions to analyze
    @return: boolean true if correct
    """
    return True