import sys
import re

def lex(characters, token):
    pos = 0
    tokens = []
    while pos < len(characters):
        match = None
        for token in token:
            pattern, tag = token
            regex = re.compile(pattern)
            match = regex.match(characters, pos)
            if match:
                text = match.group(0)
                if tag:
                    token = (text, tag)
                    tokens.append(token)
                break
        if not match:
            sys.stderr.write('Caracter invalido: %s\n' % characters[pos])
            sys.exit(1)
        else:
            pos = match.end(0)
    return tokens
