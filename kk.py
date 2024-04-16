import os
import sys

K1_CT = "EMUFPHZLRFAXYUSDJKZLDKRN?SHGNFIVJYQTQUXQBQVYUVLLTREVJYQTMKYRDMFD"
K1_PT = "BETWEENSUBTLESHADINGANDTHEABSENCEOFLIGHTLIESTHENUANCEOFIQLUSION"
K1_KEYWORD = "KRYPTOS"
K1_INDICATOR = "PALIMPSEST"

K2_CT =  "VFPJUDEEHZWETZYVGWHKKQETGFQJNCEGGWHKK?DQMCPFQZDQMMIAGPFXHQRLGTIMVMZJANQLVKQEDAGDVFRPJUNGEUNAQZGZLECGYUXUEENJTBJLBQCRTBJDFHRRYIZETKZEMVDUFKSJHKFWHKUWQLSZFTIHHDDDUVH?DWKBFUFPWNTDFIYCUQZEREEVLDKFEZMOQQJLTTUGSYQPFEUNLAVIDXFLGGTEZ?FKZBSFDQVGOGIPUFXHHDRKFFHQNTGPUAECNUVPDJMQCLQUMUNEDFQELZZVRRGKFFVOEEXBDMVPNFQXEZLGREDNQFMPNZGLFLPMRJQYALMGNUVPDXVKPDQUMEBEDMHDAFMJGZNUPLGESWJLLAETG"
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
		elif keyword[k] not in alphabet:
			pt += "?"
		else:
			pt += letter(index(c, alphabet) - index(keyword[k], alphabet), alphabet)
		k = (k+1) % len(keyword)
	return pt


def quagmire3_encode(pt, keyword, indicator, alphabet=None):
	if not alphabet:
		alphabet = gen_alphabet(keyword)
	return vigenere_encode(pt, indicator, alphabet)


def quagmire3_decode(ct, keyword, indicator, alphabet=None):
	if not alphabet:
		alphabet = gen_alphabet(keyword)
	return vigenere_decode(ct, indicator, alphabet)


def frequencies(text, alphabet=ALPHABET):
	freq = [(c, text.count(c)) for c in alphabet]
	return freq


def test_otp(pt, ct, alphabet=ALPHABET):
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


def raised_letters_expand(text):
	# 0123456
	# endYAhR
	expanded = ""
	k = 0
	i = 0
	while i < len(text):
		if k % 7 in [3, 4, 6]:
		# if k % 7 in [0, 1, 2, 5]:
			expanded += "?"
		else:
			expanded += text[i]
			i += 1
		k += 1
	return expanded


def raised_letters_contract(text):
	# 0123456
	# endYAhR
	contracted = ""
	i = 0
	while i < len(text):
		if i % 7 not in [3, 4, 6]:
		# if i % 7 not in [0, 1, 2, 5]:
			contracted += text[i]
		i += 1
	return contracted


def raised_letters_shuffle(text):
	shuffled = ""
	left = text
	while len(left) > 3:
		i = 0
		tmp	= ""
		while i<len(left):
			if i % 7 in [3, 4, 6]:
				shuffled += left[i]
			else:
				tmp += left[i]
			i += 1
		left = tmp	

	shuffled += left
	return shuffled


def raised_letters_shuffle2(text):
	shuffled = ""
	left = text
	
	i = 0
	tmp	= ""
	while i<len(left):
		if i % 7 in [3, 4, 6]:
			shuffled += left[i]
		else:
			tmp += left[i]
		i += 1

	shuffled += tmp[::-1]
	return shuffled


def main(argv):
	print(ALPHABET)
	
	# for x in range(0,26):
	# 	print(rotate_alphabet(KRYPTOS_ALPHABET, x)) 

	# print(index("D"))
	# print(caesar("MARC", -52))
	# print(vigenere_encode("ABCDEFGH", "ABAB"))
	print(quagmire3_decode(K1_CT, K1_KEYWORD, K1_INDICATOR))
	print(quagmire3_decode(K2_CT, K2_KEYWORD, K2_INDICATOR))

	key = quagmire3_decode(K4_CT, K2_KEYWORD, "?????????????????????EASTNORTHEAST???????????????????BERLINCLOCK?????????????????????????????????")
	print(key)
	pt = quagmire3_decode(K4_CT, K2_KEYWORD, key)
	print(pt)
	return

	print(test_otp(K1_PT, K1_CT, KRYPTOS_ALPHABET))

	file1 = open('words.txt', 'r')
	words = [x[:-1].upper() for x in file1.readlines()]
	nb_words = len(words)
	alp = gen_alphabet(K2_KEYWORD)


	# exp_ct = "".join(["?" + x for x in K4_CT[::-1]])
	# print(exp_ct)

	# cribs = ["CLOCK", "BERLIN", "EASTNO", "NORTH"]
	# wc = 0
	# for w in words:
	# 	if wc % 1000 == 0:
	# 		print(wc, "/", len(words))
	# 	exp_pt = quagmire3_decode(exp_ct, K2_KEYWORD, w, alphabet=alp)[1::2]
	# 	for crib in cribs:
	# 		if crib in exp_pt:
	# 			print("?????????????????????EASTNORTHEAST???????????????????BERLINCLOCK?????????????????????????????????")
	# 			print(exp_pt, w)
	# 			i = exp_pt.index(crib)
	# 			pad = "".join([" " for x in range(i)])
	# 			pad += "".join(["^" for x in range(len(crib))])
	# 			print(pad)
	# 			print()
	# 	wc += 1



	# exp_ct = raised_letters_expand(K4_CT[::-1])
	# print(exp_ct)
	# alp = gen_alphabet(K2_KEYWORD)

	# cribs = ["CLOCK", "BERLIN", "EASTNO", "NORTH"]
	# wc = 0
	# for w in words:
	# 	if wc % 2360 == 0:
	# 		print(wc, "/", len(words))
	# 	exp_pt = quagmire3_decode(exp_ct, "", w, alphabet=alp)
	# 	pt = raised_letters_contract(exp_pt)
	# 	for crib in cribs:
	# 		if crib in pt:
	# 			print("?????????????????????EASTNORTHEAST???????????????????BERLINCLOCK?????????????????????????????????")
	# 			print(pt, w)
	# 			i = pt.index(crib)
	# 			pad = "".join([" " for x in range(i)])
	# 			pad += "".join(["^" for x in range(len(crib))])
	# 			print(pad)
	# 			print()
	# 	wc += 1




	ct = raised_letters_shuffle2(K4_CT)
	print(K4_CT)
	print(ct)

	# # ct = "".join(["E" + x if x == "K" else x for x in K4_CT])
	# # print(ct, len(ct))

	cribs = ["CLOCK", "BERLIN", "NORTH"]
	wc = 0
	for w in words:
		if wc % 1000 == 0:
			print(wc, "/", len(words))
		pt = quagmire3_decode(ct, K2_KEYWORD, w, alphabet=alp)
		for crib in cribs:
			if crib in pt:
				print("?????????????????????EASTNORTHEAST???????????????????BERLINCLOCK?????????????????????????????????")
				print(pt, w)
				i = pt.index(crib)
				pad = "".join([" " for x in range(i)])
				pad += "".join(["^" for x in range(len(crib))])
				print(pad)
				print()
		wc += 1




	# otp = test_otp("?????????????????????EASTNORTHEAST???????????????????BERLINCLOCK?????????????????????????????????", K4_CT)
	# for x in range(0,26):
	# 	print(caesar(otp, x))

	# print(frequencies(K4_CT))
	
	# print("?????????????????????EASTNORTHEAST???????????????????BERLINCLOCK?????????????????????????????????")
	# use_k4ct_to_lookup_k123ct_and_pick_matching_k123pt()

if __name__ == "__main__":
	main(sys.argv)  