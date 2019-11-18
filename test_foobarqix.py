## Rules  http://codingdojo.org/kata/FooBarQix/
## If the number is divisible by 3, write “Foo” instead of the number
## If the number is divisible by 5, add “Bar”
## If the number is divisible by 7, add “Qix”
## For each digit 3, 5, 7, add “Foo”, “Bar”, “Qix” in the digits order.

from functools import reduce


dict_to_string = {
    3: 'Foo',
    5: 'Bar',
    7: 'Qix'
}


def convert(number):
    result = handleDivisibilityRule(number) + handleDigitsRule(number)
    if result:
        return result
    else:
        return str(number)


def handleDigitsRule(number): 
    f = list(filter(lambda x: int(x) in dict_to_string.keys(), str(number)))
    mapped = list(map(lambda x: dict_to_string[int(x)], f))
    if mapped:
        return reduce(lambda x, y: x + y, mapped)
    else:
        return ''


def handleDivisibilityRule(number): 
    result = ''.join([v for k, v in dict_to_string.items() if number % k == 0])
    return result


def test_general_case():
    assert convert(1) == '1'


def test_return_foo_when_divible_by_3():
    assert convert(6) == 'Foo'


def test_return_bar_when_divible_by_5():
    assert convert(10) == 'Bar'


def test_return_qix_when_divible_by_7():
    assert convert(14) == 'Qix'


def test_return_foofoo():
    assert convert(3) == 'FooFoo'

def test_return_barbarbar():
    assert convert(55) == 'BarBarBar'


def test_return_FooQix():
    assert convert(21) == 'FooQix'

