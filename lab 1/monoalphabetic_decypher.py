ciphertext = """nkutf qmoio cop o cuqwfu gukr fmyojku, lfpw sekce gku zqp ekhfb zyopqxyetk,
czqmz lukytzw owwfewqke wk wzf fvxbkqwowqke kg fmyojku'p qejqtfekyp
xfkxbf la fmyojkuqoe czqwfp. cqwz wzf xylbqmowqke kg zyopqxyetk, qmoio
omzqfhfj qewfueowqkeob gorf. wzf lkks lfmorf o cfbb-sekce "qejqtfeqpw" ekhfb,
o rkhfrfew qe bowqe orfuqmoe bqwfuowyuf wzow opxqufj wk ufobqpr qe qwp
jfxqmwqke kg wzf rqpwufowrfew kg wzf qejqtfekyp.
"""

solving_key = 'YLWQNEFVZDOBCJASIMKGRXTPUH'

if __name__ == '__main__':
    deciphered_text = ''.join(solving_key[ord(c)-ord('a')] if 'a' <= c <= 'z' else c for c in ciphertext)
    print(deciphered_text)
