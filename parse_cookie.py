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

