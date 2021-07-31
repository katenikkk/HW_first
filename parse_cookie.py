import re

def parse_cookie(query: str) -> dict:
    text = query
    pattern_query = r'(\w+)*;?='
    pattern_str = r'=(\w+\S);'
    key = re.findall(pattern_query, text)
    value = re.findall(pattern_str, text)
    dictionary = dict(zip(key, value))
    print(dictionary)
    return {dict}


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}

    assert parse_cookie(';name=Bob;color=white;') == {'name': 'Bob', 'color': 'white'}
    assert parse_cookie(';nam==&&;') == {}
    assert parse_cookie('sub==Andrew;&&') == {'sub': 'Andrew'}
    assert parse_cookie('number=8907;') == {'number': '8907'}
    assert parse_cookie('999====&&7') == {}
    assert parse_cookie(';name=Bob;&&color=white;??') == {'name': 'Bob', 'color': 'white'}
    assert parse_cookie('sub=Andrew;home==Boston;&') == {'sub': 'Andrew', 'home': 'Boston'}
    assert parse_cookie('&&???===home?') == {}
    assert parse_cookie(':;&*name&&=Mike&name=Barbara;') == {'name': 'Barbara'}
    assert parse_cookie('name=Dima;sub==Andrew;&&') == {'name': 'Dima', 'sub': 'Andrew'}


