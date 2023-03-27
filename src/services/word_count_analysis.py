import re
from collections import Counter


def word_count_analysis(text: str):
    words = re.findall(r'\w+', text.lower())
    return dict(Counter(words).most_common())
