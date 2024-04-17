import os
import sys
import math

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ORD_A = ord("A")
ENG_FREQS = [0.081238378, 0.014892788, 0.0271142, 0.043191829, 0.120195499, 0.023038568, 0.020257483, 0.059214604, 0.073054201, 0.00103125, 0.006895114, 0.039785412, 0.026115862, 0.069477738, 0.076811682, 0.018189498, 0.001124502, 0.060212942, 0.062807524, 0.090985886, 0.028776268, 0.011074969, 0.02094864, 0.001727893, 0.021135143, 0.000702128]

K1CT = "EMUFPHZLRFAXYUSDJKZLDKRNSHGNFIVJYQTQUXQBQVYUVLLTREVJYQTMKYRDMFD"
K1PT = "BETWEENSUBTLESHADINGANDTHEABSENCEOFLIGHTLIESTHENUANCEOFIQLUSION"

K2CT = "VFPJUDEEHZWETZYVGWHKKQETGFQJNCEGGWHKK?DQMCPFQZDQMMIAGPFXHQRLGTIMVMZJANQLVKQEDAGDVFRPJUNGEUNAQZGZLECGYUXUEENJTBJLBQCRTBJDFHRRYIZETKZEMVDUFKSJHKFWHKUWQLSZFTIHHDDDUVH?DWKBFUFPWNTDFIYCUQZEREEVLDKFEZMOQQJLTTUGSYQPFEUNLAVIDXFLGGTEZ?FKZBSFDQVGOGIPUFXHHDRKFFHQNTGPUAECNUVPDJMQCLQUMUNEDFQELZZVRRGKFFVOEEXBDMVPNFQXEZLGREDNQFMPNZGLFLPMRJQYALMGNUVPDXVKPDQUMEBEDMHDAFMJGZNUPLGESWJLLAETG"
K2PT = "ITWASTOTALLYINVISIBLEHOWSTHATPOSSIBLE?THEYUSEDTHEEARTHSMAGNETICFIELDXTHEINFORMATIONWASGATHEREDANDTRANSMITTEDUNDERGRUUNDTOANUNKNOWNLOCATIONXDOESLANGLEYKNOWABOUTTHIS?THEYSHOULDITSBURIEDOUTTHERESOMEWHEREXWHOKNOWSTHEEXACTLOCATION?ONLYWWTHISWASHISLASTMESSAGEXTHIRTYEIGHTDEGREESFIFTYSEVENMINUTESSIXPOINTFIVESECONDSNORTHSEVENTYSEVENDEGREESEIGHTMINUTESFORTYFOURSECONDSWESTxLAYERTWO"

K3CT = "ENDYAHROHNLSRHEOCPTEOIBIDYSHNAIACHTNREYULDSLLSLLNOHSNOSMRWXMNETPRNGATIHNRARPESLNNELEBLPIIACAEWMTWNDITEENRAHCTENEUDRETNHAEOETFOLSEDTIWENHAEIOYTEYQHEENCTAYCREIFTBRSPAMHHEWENATAMATEGYEERLBTEEFOASFIOTUETUAEOTOARMAEERTNRTIBSEDDNIAAHTTMSTEWPIEROAGRIEWFEBAECTDDHILCEIHSITEGOEAOSDDRYDLORITRKLMLEHAGTDHARDPNEOHMGFMFEUHEECDMRIPFEIMEHNLSSTTRTVDOHW?"
K3PT = "SLOWLYDESPARATLYSLOWLYTHEREMAINSOFPASSAGEDEBRISTHATENCUMBEREDTHELOWERPARTOFTHEDOORWAYWASREMOVEDWITHTREMBLINGHANDSIMADEATINYBREACHINTHEUPPERLEFTHANDCORNERANDTHENWIDENINGTHEHOLEALITTLEIINSERTEDTHECANDLEANDPEEREDINTHEHOTAIRESCAPINGFROMTHECHAMBERCAUSEDTHEFLAMETOFLICKERBUTPRESENTLYDETAILSOFTHEROOMWITHINEMERGEDFROMTHEMISTXCANYOUSEEANYTHINGQ?"

K4CT = "OBKRUOXOGHULBSOLIFBBWFLRVQQPRNGKSSOTWTQSJQSSEKZZWATJKLUDIAWINFBNYPVTTMZFPKWGDKZXTJCDIGKUHUAUEKCAR"
K4CR = "?????????????????????EASTNORTHEAST?????????????????????????????BERLINCLOCK???????????????????????"
K4CL = "EASTNORTHEASTBERLINCLOCK"


def genAlphabet(key: str) -> str: 
    processed = ""
    alpha = ""
    for c in key:
        if c not in alpha:
            alpha += c
    for c in ALPHABET:
        if c not in alpha:
            alpha += c
    return alpha    


def encryptVigenere(text: str, alphabet: str, key: str) -> str:
    kl = len(key)
    ki = [alphabet. index(x) for x in key]

    ct = ""

    for i in range(len(text)):
        c = text[i]
        
        if c not in ALPHABET:
            ct += c
            continue

        p = (alphabet.index(c) + 26 + ki[i%kl]) % 26
        ct += alphabet[p]

    return ct


def decryptVigenere(text: str, alphabet: str, key: str) -> str:
    kl = len(key)
    ki = [alphabet.index(x) for x in key]

    pt = ""

    for i in range(len(text)):
        c = text[i]
        
        if c not in ALPHABET:
            pt += c
            continue

        p = (alphabet.index(c) + 26 - ki[i%kl]) % 26
        pt += alphabet[p]

    return pt


def rotateCW(text: str, cols: int ) -> str:
    pad = 0 if len(text) % cols == 0 else cols - len(text) % cols
    padded = text
    # for i in range(pad):
    #     padded = "?" + padded
    for i in range(pad):
        padded += "?"

    rect = []

    height = int(len(padded)/cols)
    for y in range(height):
        rect.append(padded[y*cols:(y+1)*cols])

    transposed = ""
    for i in range(cols):
        for j in range(height-1, -1, -1):
            transposed += rect[j][i]
    return transposed


def rotateCCW(text: str, cols: int ) -> str:
    pad = 0 if len(text) % cols == 0 else cols - len(text) % cols
    padded = text
    for i in range(pad):
        padded += "?"

    rect = []

    height = int(len(padded)/cols)
    for y in range(height):
        rect.append(padded[y*cols:(y+1)*cols])

    transposed = ""
    for i in range(cols-1, -1, -1):
        for j in range(height):
            transposed += rect[j][i]
    return transposed


def histogram(text: str) -> list:
    histogram = [0 for x in range(26)]
    count = 0
    for c in text:
        if c in ALPHABET:
            histogram[ord(c) - ORD_A] += 1
            count += 1

    for i in range(26):
        histogram[i] = histogram[i]/count

    return histogram


def varianceFromEnglish(text: str) -> float:
    hist = histogram(text)
    variance = 0.0
    for x in range(26):
        variance += (ENG_FREQS[x]-hist[x])**2
    return variance


def hasCribLetters(text: str, crib: str):
    pos = []
    lt = len(text)
    for i in range(len(crib)):
        c = crib[i]
        for j in range(lt):
            if c == text[j] and j not in pos:
                pos.append(j)
                break
        else:
            return False

    return True


# #--- TESTS --------------------

# tmp = rotateCW(K3CT[:-1], 24)
# print(tmp)
# print(rotateCW(tmp, 8))
# print() 

# tmp = rotateCCW(K3PT[:-1], int(len(K3PT[:-1])/8))
# print(tmp)
# print(rotateCCW(tmp, int(len(K3PT[:-1])/24)))
# print()

# print(varianceFromEnglish(K1PT))
# print(varianceFromEnglish(K1CT))
# print()
# print(varianceFromEnglish(K2PT))
# print(varianceFromEnglish(K2CT))
# print()
# print(varianceFromEnglish(K3PT))
# print(varianceFromEnglish(K3CT))
# print()
# print(varianceFromEnglish(K4CT))
# print()

# #------------------------------


kalpha = genAlphabet("KRYPTOS")
matches = []

# pt = decryptVigenere(K4CT, kalpha, "EINSTEIN")
# print(pt)

# for s in range(2, 49):
#     tmp = rotateCW(pt, s)
#     print(tmp)
#     t = int(len(tmp)/s + 0.5)
#     pt = rotateCW(tmp, t)
#     print(pt)
#     if "BERLIN" in tmp or "BERLIN" in pt:
#         print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
#     print()

# exit()


with open("words.txt") as file:
    ct = K4CT
    # ct = K4CT[::-1]
    for line in file:
        word = line.rstrip().upper()
        if not word.isalpha():
            continue

        pt = decryptVigenere(ct, kalpha, word)
        match = hasCribLetters(pt, K4CL)
        if match:
            matches.append([word, varianceFromEnglish(pt), pt])

    matches.sort(key=lambda x: x[1])
    print(len(matches), "matches.")

    for i in range(len(matches)):
        if i % 1000 == 0:
            print(i, "...")
        # if matches[i][1] > 0.03:
        #     break

        # print(matches[i])
        for s in range(2, 49):
            pt = matches[i][2]

            cw  = rotateCW(pt, s)
            cws = cw.replace("?", "") 
            cwcw  = rotateCW(cw, int(len(cw)/s + 0.5))
            cwscw  = rotateCW(cws, int(len(cws)/s + 0.5))
            cwcws = cwcw.replace("?", "") 
            cwscws = cwscw.replace("?", "")

            ccw  = rotateCCW(pt, s)
            ccws = ccw.replace("?", "") 
            ccwccw  = rotateCCW(ccw, int(len(ccw)/s + 0.5))
            ccwsccw  = rotateCCW(ccws, int(len(ccws)/s + 0.5))
            ccwccws = ccwccw.replace("?", "") 
            ccwsccws = ccwsccw.replace("?", "")

            pts = [cws, cwcws, cwscws, ccws, ccwccws, ccwsccws]
            for w in pts:
                if "BERLIN" in w:
                    print(w, s, matches[i])




