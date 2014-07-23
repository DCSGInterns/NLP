 #http://eprints.eemcs.utwente.nl/23268/01/sac13-senticon.pdf

import re


def get_emoticon_lexicon(smiley):
    happy = [':-)', ':)', ':o)', ':]', '=]', '8)', '=)', ':}']
    if smiley in happy:
        return 0.5

    laughing = [':-D', ':D', '8-D', '8D', '=-D', '=D']
    if smiley in laughing:
        return 1.0

    sad = ['>:[', ':-(', ':(', ':-[', ':[', ':{']
    if smiley in sad:
        return -0.5

    angry = [':@', '>:(']
    if smiley in angry:
        return -1.0

    crying = [":'("]
    if smiley in crying:
        return -1.0

    tears_of_happiness = [":')"]
    if smiley in tears_of_happiness:
        return 1.0

    evil = ['>:)', '>;)', '>:-)']
    if smiley in evil:
        return -0.75

    angel = ['O:-)', '0:-)', '0:)']
    if smiley in angel:
        return 0.75

    hesitant = ['>:/', ':-/', ':/', '=/']
    if smiley in hesitant:
        return -0.25
 
    wink = [';-)', ';)', ';-]', ';]', ';D']
    if smiley in wink:
        return 0.25

    return 0

emoticon_count = 0 

def get_score(chunked):
	global emoticon_count

	emoticon_count = 0 
	score = 0
	emoticons = "[o0O]?[<>]?[:;=8][\-o\*\']?[\)\]\(\[dDpP/\:\}\{@\|]"
	for current_word in chunked:
		if re.match(emoticons,current_word):     
			t = get_emoticon_lexicon(current_word)
			#print t
			#print current_word
			score = score + t
			if t != 0:
				emoticon_count += 1
			#print t
	return score 

def get_count():
	global emoticon_count
	return emoticon_count