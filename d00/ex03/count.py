import string


def text_analyzer(text=None):
    if text is not None:
        upper = sum(map(str.isupper, text))
        lower = sum(map(str.islower, text))
        space = sum(map(str.isspace, text))
        total = sum(map(str.isascii, text))
        punctuation = 0
        for char in text:
            if char in string.punctuation:
                punctuation += 1
        print('The text contains {} characters:'.format(total))
        print('- {} upper letters'.format(upper))
        print('- {} lower letters'.format(lower))
        print('- {} punctuation marks'.format(punctuation))
        print('- {} spaces'.format(space))
    else:
        print('What is the text to analyse?')
        text = input()
        text_analyzer(text)
