import FingerDirection
import SintacticoSemantico
import LeapMotion_Detection
import Leap


def analyzer(hands, sentence):
    firstHandDirection = FingerDirection.fingerOrientation(hands[0])
    secondHandDirection = FingerDirection.fingerOrientation(hands[1])

    #print str(firstHandDirection)
    #print str(secondHandDirection)

    if hands[0].palm_position.y < 500 or hands[1].palm_position.y < 500:
        if firstHandDirection == ["up", "down", "down", "down", "down"]:
            if secondHandDirection == ["up", "down", "down", "down", "down"]:
                handsClose(sentence)
                sentence = []

            elif secondHandDirection == ["up", "up", "up", "up", "up"]:
                handClose_handUp(sentence)
                print str(sentence)

        elif firstHandDirection[2] == "left":
            if firstHandDirection[3] == "left":
                if firstHandDirection[4] == "left":
                    if secondHandDirection[2] == "right":
                        if secondHandDirection[3] == "right":
                            if secondHandDirection[4] == "right":

                                sentence.append("vivir")
                                print "vivir"

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
    wordsList = SintacticoSemantico.semantico(sentence)
    LeapMotion_Detection.procesar(wordsList)

