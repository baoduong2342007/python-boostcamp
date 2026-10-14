"""W1-2: Word counter module."""
def word_count(text: str):
    text = text.lower()
    a = {}
    text += ' '
    tmp = ''
    for c in text:
        if c >= 'a' and c <= 'z':
            tmp += c
        else:
            if tmp != '':
                if tmp not in a:
                    a[tmp] = 1
                else:
                    a[tmp] += 1
                tmp = ''
    return a


def top_k(text: str, k: int):
    if k <= 0:
        return []
    a = sorted(word_count(text).items(), key=lambda x: (-x[1], x[0]))
    return a[:k]

    
