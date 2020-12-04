def letter_inc(letter):
    """
    >>> letter_inc('a')
    'b'
    >>> letter_inc('z')
    'a'
    """
    return chr((((ord(letter)-97)+1)%26)+97)

def str_inc(s):
    """
    >>> str_inc('aaa')
    'aab'
    >>> str_inc('aaz')
    'aba'
    >>> str_inc('zzz')
    'aaaa'
    """
    out = ""
    inc = True
    for i in range(len(s)-1,-1,-1):
        if inc:
            la = s[i]
            lb = letter_inc(la)
            if lb in ['i','l','o']:
                lb = letter_inc(lb)
            if lb > la:
                inc = False
            out += lb
        else:
            out += s[i]
    if inc:
        out += 'a'
    return out[::-1]

def distinct_pairs(s):
    """
    >>> distinct_pairs('abcd')
    False
    >>> distinct_pairs('aacc')
    True
    >>> distinct_pairs('affbcdee')
    True
    """
    if len(s) < 4:
        return False

    pairs = []
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            if s[i] not in pairs:
                pairs.append(s[i])
    return len(pairs) >= 2

def check_straight(s):
    """
    >>> check_straight('abcgfojhoi')
    True
    >>> check_straight('adcgfojhoi')
    False
    """
    if len(s) < 3:
        return False
    for i in range(len(s)-2):
        a = ord(s[i])
        b = ord(s[i+1])
        c = ord(s[i+2])
        if b == (a+1) and c == (b+1):
            return True
    return False

def valid_chars_only(s):
    """
    >>> valid_chars_only('abcd')
    True
    >>> valid_chars_only('abcdi')
    False
    """
    return 'i' not in s and 'o' not in s and 'l' not in s

def check_valid(s):
    """
    >>> check_valid('hijklmmn')
    False
    >>> check_valid('abbceffg')
    False
    >>> check_valid('abbcegjk')
    False
    >>> check_valid('abcdefgh')
    False
    >>> check_valid('abcdffaa')
    True
    >>> check_valid('ghijklmn')
    False
    >>> check_valid('ghjaabcc')
    True
    """
    return valid_chars_only(s) and check_straight(s) and distinct_pairs(s) and len(s) == 8

def inc_to_next_valid(s):
    """
    >>> inc_to_next_valid('abcdefgh')
    'abcdffaa'
    >>> inc_to_next_valid('ghijklmn')
    'ghjaabcc'
    """
    s = str_inc(s)
    while not check_valid(s):
        if len(s) > 8:
            raise Exception("No more valid passwords, length exceeded!")
        s = str_inc(s)
    return s

if __name__=='__main__':
    import doctest
    doctest.testmod()

    nxt = inc_to_next_valid('vzbxkghb')
    print(nxt)
    nxt = inc_to_next_valid(nxt)
    print(nxt)