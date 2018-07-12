from queue import *


def test_shift():
   colors = Queue()
   colors.shift("Blue")
   assert colors.count() == 1

   colors.shift("Orange")
   assert colors.count() == 2
   colors.unshift()
   assert colors.count() == 1


def test_unshift():
    colors = Queue()
    colors.shift("Red")
    colors.shift("Green")
    colors.shift("Pink")
    colors.unshift()
    assert colors.count() == 2

def test_first():
    colors = Queue()
    colors.shift("Red")
    colors.shift("Blue")
    colors.shift("Yellow")
    colors.shift("Green")
    assert colors.first() == "Red"
    colors.unshift()
    assert colors.first() == "Blue"
    colors.unshift()
    assert colors.first() == "Yellow"
    colors.unshift()
    assert colors.first() == "Green"
    colors.unshift()
    assert colors.first() == None


def test_last():
    colors = Queue()
    colors.shift("Red")
    colors.shift("Blue")
    colors.shift("Green")
    colors.shift("Yellow")
    colors.shift("Brown")
    assert colors.last() == "Brown"
    colors.unshift()
    assert colors.last() == "Brown"
    colors.shift("Orange")
    assert colors.last() == "Orange"
