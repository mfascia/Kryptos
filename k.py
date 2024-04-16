import os
import sys

K1_CT = "EMUFPHZLRFAXYUSDJKZLDKRNSHGNFIVJYQTQUXQBQVYUVLLTREVJYQTMKYRDMFD"
K1_PT = "BETWEENSUBTLESHADINGANDTHEABSENCEOFLIGHTLIESTHENUANCEOFIQLUSION"
K1_KEYWORD = "KRYPTOS"
K1_INDICATOR = "PALIMPSEST"

K2_CT = "VFPJUDEEHZWETZYVGWHKKQETGFQJNCEGGWHKK?DQMCPFQZDQMMIAGPFXHQRLGTIMVMZJANQLVKQEDAGDVFRPJUNGEUNAQZGZLECGYUXUEENJTBJLBQCRTBJDFHRRYIZETKZEMVDUFKSJHKFWHKUWQLSZFTIHHDDDUVH?DWKBFUFPWNTDFIYCUQZEREEVLDKFEZMOQQJLTTUGSYQPFEUNLAVIDXFLGGTEZ?FKZBSFDQVGOGIPUFXHHDRKFFHQNTGPUAECNUVPDJMQCLQUMUNEDFQELZZVRRGKFFVOEEXBDMVPNFQXEZLGREDNQFMPNZGLFLPMRJQYALMGNUVPDXVKPDQUMEBEDMHDAFMJGZNUPLGESWJLLAETG"
K2_PT = "ITWASTOTALLYINVISIBLEHOWSTHATPOSSIBLE?THEYUSEDTHEEARTHSMAGNETICFIELDXTHEINFORMATIONWASGATHEREDANDTRANSMITTEDUNDERGRUUNDTOANUNKNOWNLOCATIONXDOESLANGLEYKNOWABOUTTHIS?THEYSHOULDITSBURIEDOUTTHERESOMEWHEREXWHOKNOWSTHEEXACTLOCATION?ONLYWWTHISWASHISLASTMESSAGEXTHIRTYEIGHTDEGREESFIFTYSEVENMINUTESSIXPOINTFIVESECONDSNORTHSEVENTYSEVENDEGREESEIGHTMINUTESFORTYFOURSECONDSWESTXLAYERTWO"
K2_KEYWORD = "KRYPTOS"
K2_INDICATOR = "ABSCISSA"

K3_CT = "ENDYAHROHNLSRHEOCPTEOIBIDYSHNAIACHTNREYULDSLLSLLNOHSNOSMRWXMNETPRNGATIHNRARPESLNNELEBLPIIACAEWMTWNDITEENRAHCTENEUDRETNHAEOETFOLSEDTIWENHAEIOYTEYQHEENCTAYCREIFTBRSPAMHHEWENATAMATEGYEERLBTEEFOASFIOTUETUAEOTOARMAEERTNRTIBSEDDNIAAHTTMSTEWPIEROAGRIEWFEBAECTDDHILCEIHSITEGOEAOSDDRYDLORITRKLMLEHAGTDHARDPNEOHMGFMFEUHEECDMRIPFEIMEHNLSSTTRTVDOHW?"
K3_PT = "SLOWLYDESPARATLYSLOWLYTHEREMAINSOFPASSAGEDEBRISTHATENCUMBEREDTHELOWERPARTOFTHEDOORWAYWASREMOVEDWITHTREMBLINGHANDSIMADEATINYBREACHINTHEUPPERLEFTHANDCORNERANDTHENWIDENINGTHEHOLEALITTLEIINSERTEDTHECANDLEANDPEEREDINTHEHOTAIRESCAPINGFROMTHECHAMBERCAUSEDTHEFLAMETOFLICKERBUTPRESENTLYDETAILSOFTHEROOMWITHINEMERGEDFROMTHEMISTXCANYOUSEEANYTHINGQ?"

K4_CT = "OBKRUOXOGHULBSOLIFBBWFLRVQQPRNGKSSOTWTQSJQSSEKZZWATJKLUDIAWINFBNYPVTTMZFPKWGDKZXTJCDIGKUHUAUEKCAR"

K12_CT = K1_CT + K2_CT
K12_PT = K1_PT + K2_PT

K123_CT = K1_CT + K2_CT + K3_CT
K123_PT = K1_PT + K2_PT + K3_PT

K1234_CT = K1_CT + K2_CT + K3_CT + K4_CT

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def gen_alphabet(keyword):
	alphabet = ""
	for c in keyword:
		if c not in alphabet:
			alphabet += c
	for c in ALPHABET:
		if c not in alphabet:
			alphabet += c
	return alphabet

KRYPTOS_ALPHABET = gen_alphabet("KRYPTOS")

def index(c, alphabet=ALPHABET):
	return alphabet.index(c)


def letter(i, alphabet=ALPHABET):
	return alphabet[i % len(alphabet)]


def rotate_alphabet(alphabet, offset):
	o = offset % 26
	a = alphabet[o:] + alphabet[0:o]
	return a


def caesar(pt, offset, alphabet=ALPHABET):
	ct=""
	for c in pt:
		if c not in alphabet:
			ct += c
		else:
			ct += letter(index(c,alphabet)+offset,alphabet)
	return ct


def vigenere_encode(pt, keyword, alphabet=ALPHABET):
	ct = ""
	k = 0
	for c in pt:
		if c not in alphabet:
			ct += c
		else:
			ct += letter(index(c, alphabet) + index(keyword[k], alphabet), alphabet)
			k = (k+1) % len(keyword)
	return ct


def vigenere_decode(ct, keyword, alphabet=ALPHABET):
	pt = ""
	k = 0
	for c in ct:
		if c not in alphabet:
			pt += c
		else:
			pt += letter(index(c, alphabet) - index(keyword[k], alphabet), alphabet)
			k = (k+1) % len(keyword)
	return pt


def quagmire3_encode(pt, keyword, indicator):
	alphabet = gen_alphabet(keyword)
	return vigenere_encode(pt, indicator, alphabet)


def quagmire3_decode(ct, keyword, indicator):
	alphabet = gen_alphabet(keyword)
	return vigenere_decode(ct, indicator, alphabet)


def frequencies(text, alphabet=ALPHABET):
	freq = [(c, text.count(c)) for c in alphabet]
	return freq


def test_opt(pt, ct, alphabet=ALPHABET):
	otp = ""
	for i in range(0, len(pt)):
		c = ct[i]
		p = pt[i]
		if p not in alphabet or c not in alphabet:
			otp += p
		else:
			x = index(c, alphabet)
			y = index(p, alphabet)
			otp += letter(x - y, alphabet)
	return otp


def use_k4ct_to_lookup_k123ct_and_pick_matching_k123pt():
	'''
	src = K123_CT, dst = K123_PT, offset = 67, k = -1, alphabet = ALPHABET
		 --> IIFOUCNGEUEASTIFANIOCPEEOLDARTEEFSGSHACNTITBSEERHTWAAAHSATHMRLFARAOSSIETSHTEGOANEHIEBIFMNSESYRMTY
	src = K123_CT, dst = K123_PT, offset = -63, k = 19, alphabet = ALPHABET
		---> EITEXHFCIOEKIESOTESTOIIUPATUINCNNOCXPNYAMEERWRIOONEEGITNREYNRAEWIGSTRMITOINOHGSHEEH?NIOTOEBERLINF
	'''
	strings = []
	src = K3_CT
	dst = K3_CT
	alphabet = ALPHABET

	for offset in range(-100, 100):
		if offset==0:
			continue
		for k in range(-20, 20):
			if k==0:
				continue
			code = ""
			p = 0

			for c in K4_CT:
				sp = p
				if not c in src:
					code += "#"
					continue
				while True:
					if src[p] == c:
						code += dst[(p+offset) % len(dst)]
						sp = p
						p = (p+k) % len(src)
						break
					p = (p+k) % len(src)
					if p == sp:
						break
				
			for x in range(0, 26):
				shifted = caesar(code, x, alphabet)
				if "BERLIN" in shifted:
					print(shifted, offset, k)


def main(argv):
	# print(ALPHABET)
	
	# for x in range(0,26):
	#     print(rotate_alphabet(ka, x)) 

	# print(index("D"))
	# print(caesar("MARC", -52))
	# print(vigenere_encode("ABCDEFGH", "ABAB"))
	# print(quagmire3_decode(K1_CT, K1_KEYWORD, K1_INDICATOR))
	# print(quagmire3_decode(K2_CT, K2_KEYWORD, K2_INDICATOR))

	# print(test_opt(K1_PT, K1_CT, KRYPTOS_ALPHABET))

	# otp = test_opt("?????????????????????EASTNORTHEAST???????????????????BERLINCLOCK?????????????????????????????????", K4_CT)
	# for x in range(0,26):
	# 	print(caesar(otp, x))

	# print(frequencies(K4_CT))
	
	print("?????????????????????EASTNORTHEAST???????????????????BERLINCLOCK?????????????????????????????????")
	use_k4ct_to_lookup_k123ct_and_pick_matching_k123pt()

if __name__ == "__main__":
	main(sys.argv)  