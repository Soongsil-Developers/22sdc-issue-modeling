import re

from mecab import MeCab


PATTERN = re.compile(r"[^%s]" % "가-힣a-zA-Z")
URL_PATTERN = re.compile(
    r"((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2," r"6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*"
)
SPACE_PATTERN = re.compile(r"\s+")

tokenizer = MeCab()


def cleansing(sent):
    res = URL_PATTERN.sub(" ", sent)
    res = PATTERN.sub(" ", res)
    res = SPACE_PATTERN.sub(" ", res)
    return res


def tokenize(sent):
    with open("stopwords-ko.txt", "r", encoding="utf-8") as f:
        stopwords = f.readlines()
    tokens = tokenizer.morphs(sent.strip())
    tokens = [tok for tok in tokens if len(tok) > 1 and tok not in stopwords]
    return tokens
