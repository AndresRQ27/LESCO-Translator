import FingerDirection
import Leap


def analyzer(hands, sentence):
    firstHandDirection = FingerDirection.fingerOrientation(hands[0])
    secondHandDirection = FingerDirection.fingerOrientation(hands[1])

    if firstHandDirection == ["up", "down", "down", "down", "down"]:
        if secondHandDirection == ["up", "down", "down", "down", "down"]:
            handsClose(sentence)
            sentence = []

        elif secondHandDirection == ["up", "up", "up", "up", "up"]:
            handClose_handUp(sentence)
            print str(sentence)

    return sentence


def handClose_handUp(sentence):
    sentence.append(" ")
    print "Space added"


def handsClose(sentence):
    print "Gonna read sentence"
    sentence.append(" ")
    for i in range(0, len(sentence)):
        print sentence[i]
    print "Sentence read"
