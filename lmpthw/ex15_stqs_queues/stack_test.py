from stack import *

def test_push():
    colors = Stack()
    colors.push("Phtalo Blue")
    assert colors.count() == 1
    colors.push("Ultramarine Blue")
    assert colors.count() == 2

def test_pop():
    colors = Stack()
    colors.push("Magenta")
    colors.push("Alizarin")
    assert colors.pop() == "Alizarin"
    assert colors.pop() == "Magenta"
    assert colors.pop() == None


def test_top():
    colors = Stack()
    colors.push("Cadmium Red Light")
    assert colors.get_top() == "Cadmium Red Light"
    colors.push("Hansa Yellow")
    assert colors.get_top() == "Hansa Yellow"
    colors.push("Pthalo Green")
    assert colors.get_top() == "Pthalo Green"

