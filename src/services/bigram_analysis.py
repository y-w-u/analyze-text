import nltk


def bigram_analysis(text: str):
    tokens = nltk.RegexpTokenizer(r'\w+').tokenize(text.lower())
    if (len(tokens)) < 2:
        return []
    freq_dist = nltk.FreqDist(nltk.bigrams(tokens))
    highest_freq = freq_dist.most_common()[0][1]
    return [list(e[0]) for e in freq_dist.items() if e[1] == highest_freq]
