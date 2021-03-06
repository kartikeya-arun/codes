def cipher(map_from, map_to, code):
    """ map_from, map_to: strings where each contain 
                          N unique lowercase letters. 
        code: string (assume it only contains letters also in map_from)
        Returns a tuple of (key_code, decoded).
        key_code is a dictionary with N keys mapping str to str where 
        each key is a letter in map_from at index i and the corresponding 
        value is the letter in map_to at index i. 
        decoded is a string that contains the decoded version 
        of code using the key_code mapping. """
    listFrom=list(map_from)
    listTo=list(map_to)
    decode=dict(zip(listFrom,listTo))
    decoded=''
    for i in code:
        if i in decode:
            decoded+=decode[i]
    return (decode,decoded)
