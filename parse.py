import re

def parse(query: str) -> dict:
    text = query
    pattern_query = r'(\w+)='
    pattern_str = r'=(\w+)'
    key = re.findall(pattern_query, text)
    value = re.findall(pattern_str, text)
    dictionary = dict(zip(key, value))
    print(dictionary)
    return{dict}

if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}

    assert parse('http://example.com/?name=ferret&') == {'name': 'ferret'}
    assert parse('http://example.com/?color=purple&&') == {'color': 'purple'}
    assert parse('http://example.com/?color=purple&&name=ferret&&') == {'color': 'purple', 'name': 'ferret'}
    assert parse('http://example.com/?name=ferret&name==Dima&color==purple') == {'name': 'ferret', 'name': 'Dima'}
    assert parse('http://example.com/?&') == {}
    assert parse('http://example.com/?&&name=ferret&name=Dima&&') == {'name': 'ferret', 'name': 'Dima'}
    assert parse('http://example.com/?&==&') == {}
    assert parse('http://example.com/?name===Bob&&') == {'name': 'Bob'}
    assert parse('http://example.com/?home==&') == {}
    assert parse('http://example.com/?&&&month==april&&&') == {'month': 'april'}

