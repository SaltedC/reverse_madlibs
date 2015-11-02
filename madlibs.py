    
def random_verb():
    random_num = randit(0, 1)
    if random_num == 0:
        return "run"
    else:
        return "kayak"

def random_noun():
    random_num = randit(0, 1)
    if random_num == 0:
        return "sofa"
    else:
        return "llama"

def word_transformer(word):
    if word == "NOUN":
        return random_noun
    else if word == "VERB":
        return random_verb()

def process_madlib(madlib):
    processed = ''
    index = 0
    box_length = 4
    while index < len(madlib):
        frame = madlib[index:index + box_length]
        to_add = word_transformer(frame)
        processed += to_add
        if len(to_add)
