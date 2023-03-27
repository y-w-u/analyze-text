from enum import Enum


class ServiceType(str, Enum):
    bigram = "bigram"
    word_count = "word-count"
