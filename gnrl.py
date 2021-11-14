import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer

tokenizer_words = RegexpTokenizer(r'\w+')
tokenizer_sen = RegexpTokenizer(r'(?<=[^.])[.](?=[^.])')
tokenizer_k = RegexpTokenizer(r'((^[^kK]+)?([ ])?[ ][^kK]+)(?!([^kK\s]*k[\S]*))')
tokenizer_lines = RegexpTokenizer(r'^')
path = input("Insert text file path: ")
reader = open(path, "r")
text = reader.read()
word_tokens = tokenizer_words.tokenize(text)
sentences = nltk.tokenize.sent_tokenize(text)

color_text = """
white
black
red
blue
yellow
gray
pink
orange
purple
green
brown
gold
silver"""

colors = nltk.tokenize.word_tokenize(color_text)



def no_k_tokenized():
    tokens = nltk.tokenize.regexp_tokenize(text, r'(((^[^kK]+)?[ ][^kK]+)+(?!([^kK\s]*k[\S]*)))')
    tokens = [token[0] for token in tokens]
    return tokens


def longest_non_k_seq():
    k_tokens = no_k_tokenized()
    word_count = lambda sentence: len(word_tokenize(sentence))
    return max(k_tokens, key=word_count)  # longest_sen, len(longest_sen)


def real_words_list():
    return word_tokens, len(word_tokens)


def sent_count():
    tokens = tokenizer_sen.tokenize(text)
    return len(tokens)


def lines_count():
    tokens = tokenizer_lines.tokenize(text)
    return len(tokens)


def unique_words_set():
    tokens = real_words_list()
    counter = 0
    unique_set = set()
    temp_set = set()
    for token in word_tokens:  # tokenizer_words.tokenize(text):  # "(w.lower() for w in tokens):
        if token in unique_set:
            if token not in temp_set:
                temp_set.add(token)
                counter -= 1
        else:
            unique_set.add(token)
            counter += 1
    return counter


def avg_words_sentence():
    return real_words_list()[1] / lines_count()


def longest_sent():
    word_count = lambda sentence: len(word_tokenize(sentence))
    return max(sentences, key=word_count)  # the longest sentence by word count


def words_without_stopwords():
    x = set()
    stop = set(stopwords.words('english') + list(string.punctuation))
    x = [i for i in word_tokens if i.lower() not in stop]
    return x


def popular_word(exclude_stopwords):
    x = set()
    if exclude_stopwords == 1:
        x = words_without_stopwords()
    else:
        x = [i for i in word_tokens]
    all_word_dist = nltk.FreqDist(w.lower() for w in x)
    return all_word_dist.most_common(1)  # .keys()


def popualr_color():
    x = set()
    x = [i for i in word_tokens if i in colors]
    all_word_dist = nltk.FreqDist(w.lower() for w in x)
    return all_word_dist.items()  # .keys()


def lower(text):
    return text.lower()

def extract_names():
    words = word_tokenize(text, language='english')
    pos = nltk.pos_tag(words)
    tree = nltk.ne_chunk(pos, binary=False)
    stop = set(stopwords.words('english') + list(string.punctuation))
    x = set()
    x = set(
        " ".join(i[0] for i in t)
        for t in tree
        if hasattr(t, "label") and t.label() == "PERSON"
    )
    temp = x.copy()
    for item in temp:
        w = word_tokenize(item, language='english')
        for word in w:
            if lower(word) in stop or word == " ":
                if item in x:
                    x.remove(item)
    return x


def popular_name():
    #multi read...
    x = extract_names()
    max = 0
    max_item = 0
    for item in x:
        tokenizer_name = RegexpTokenizer(r'' + item)
        w = tokenizer_name.tokenize(text)
        if len(w) > max:
            max = len(w)
            max_item = item
    return max_item, max




print("1. Lines count:", lines_count())  # count?
print("2. Words count:", real_words_list()[1])
print("3. Unique words count:", unique_words_set())  # needs fix to lower()
print("4.1. Words AVG in sentence:", avg_words_sentence())
print("4.2. Longest sentence: ", longest_sent())
print("5.1. Most popular word:", popular_word(0))
print("5.2. Most popular word exclude stop words:", popular_word(1))
print("6. Longest word sequence without 'k' words: ", longest_non_k_seq())
print("7. ")
print("8. Colors: ", popualr_color())
print("9.1. Names:", extract_names())
print("9.2. Most popular name: ", popular_name())

