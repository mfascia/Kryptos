import os
import sys
import math

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

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


def hasCribLetters(text: str, crib: str) -> bool:
    for i in range(len(crib)):
        c = crib[i]
        if c in text:
            p = text.index(c)
            text = text[:p] + text[p+1:]
        else:
            return False
    return True    


print(hasCribLetters(K4CR, K4CL))



print(encryptVigenere(K1PT, genAlphabet("KRYPTOS"), "PALIMPSEST"))
print(K1CT)
print()
print(K1PT)


kalpha = genAlphabet("KRYPTOS")
count = 0
with open("words.txt") as file:
    for line in file:
        word = line.rstrip().upper()
        if not word.isalpha():
            continue

        pt = decryptVigenere(K4CT, kalpha, word)
        if hasCribLetters(pt, K4CL):
            count += 1
            if word.startswith("ABSC") or word.startswith("ORDIN") or word.startswith("PALIMP"):
                print(word, "->", pt)

    print(count)





