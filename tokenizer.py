def my_word_tokenize(wordTokenize):
    wt = wordTokenize.split(" ")
    # Split with lots of the signs, but it is not working good as I think.
    # It is need to complete or debug.
    #
    # wt = re.split(r'(\W+)', wordTokenize)
    return wt