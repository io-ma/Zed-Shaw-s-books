from nose.tools import *
from ex48 import lexicon, parser


# we need to test the sentence
def test_sentence():
    s1 = parser.Sentence(
        ('noun', "soap"), ('verb', "hear"), ('noun', "pillow"))
    assert s1.verb == "hear"
    assert s1.subject == "soap"
    assert s1.object == "pillow"


# testing peek
def test_peek():
    word_list = []
    word_list = lexicon.scan("princess kill bear")
    word = word_list[0]
    assert_false(parser.peek(None))
    assert_true(parser.peek(word_list))


def test_match():
    word_list = []
    assert_false(parser.match(None, 'noun'))
    word_list = lexicon.scan("bear eat princess")
    assert_equal(('noun', "bear"), parser.match(word_list, 'noun'))
    assert_equal(None, parser.match(word_list, ''))

def test_skip():
    word_list = lexicon.scan("princess kill bear")
    word_type = ['noun', 'verb', 'noun']
    wrd_type = word_type[0]
    assert_equal(parser.peek(word_list), wrd_type)

def test_parse_verb():
    word_list = lexicon.scan("kill the bear")
    assert_equal(parser.peek(word_list), 'verb')
    assert_raises(Exception, parser.parse_verb, [('stop', "the"),
                                                ('noun', "bear")])

def test_parse_object():
    word_list = lexicon.scan("go to the north door")
    next_word = parser.peek(word_list)
    assert_raises(Exception, parser.parse_object, [('verb', "go"),
                                                ('stop', "to"),
                                                ('stop', "the")])

def test_parse_subject():
    word_list = "princess kill bear"
    next_word = parser.peek(word_list)
    assert_raises(Exception, parser.parse_subject, [('stop', "the")])

def test_parse_sentence():
    word_list = lexicon.scan("princess kill the bear")
    subj = parser.parse_subject(word_list)
    verb = parser.parse_verb(word_list)
    obj = parser.parse_object(word_list)
    assert parser.Sentence(subj, verb, obj)








