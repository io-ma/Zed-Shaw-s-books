lexicon = {
    "north": 'direction',
    "south": 'direction',
    "east": 'direction',
    "west": 'direction',
    "up" : 'direction',
    "down" : 'direction',
    "left" : 'direction',
    "right": 'direction',
    "go": 'verb',
    "stop": 'verb',
    "sleep": 'verb',
    "kill": 'verb',
    "eat": 'verb',
    "the": 'stop',
    "in": 'stop',
    "of": 'stop',
    "bear": 'noun',
    "princess": 'noun',
    "door": 'noun',
    "cabinet": 'noun'
}

def check_number(str):
    try:
        return int(str)

    except ValueError:
        return None


def scan(sentence):
    results = []
    words = sentence.split()
    for word in words:
        if word in lexicon:
            results.append((lexicon[word], word))
        elif check_number(word):
            results.append(('number', word))
        else:
            results.append(('error', word))

    return results
