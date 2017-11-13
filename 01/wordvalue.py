from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY) as f:
    	add_data = f.read()
    words = add_data.split()
    return words

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    t = 0
    for c in word.upper():
    	if c in LETTER_SCORES:
    		t = t + LETTER_SCORES[c]
    return t

def max_word_value(words = load_words()):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    max_word = None
    max_score = 0
    for word in words:
    	score = calc_word_value(word)
    	if score > max_score:
    		max_score = score
    		max_word = word
    return max_word

if __name__ == "__main__":
    pass # run unittests to validate
