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
    for token in word_tokens: # tokenizer_words.tokenize(text):  # "(w.lower() for w in tokens):
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

def text2int(textnum, numwords={}):
    if not numwords:
        units = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen",
        ]

        tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

        scales = ["hundred", "thousand", "million", "billion", "trillion"]

        numwords["and"] = (1, 0)
        for idx, word in enumerate(units): numwords[word] = (1, idx)
        for idx, word in enumerate(tens): numwords[word] = (1, idx * 10)
        for idx, word in enumerate(scales): numwords[word] = (10 ** (idx * 3 or 2), 0)

    current = result = 0
    for word in textnum.split():
        if word not in numwords:
            print("#############: ", word)
            # raise Exception("Illegal word: " + word)

        scale, increment = numwords[word]
        current = current * scale + increment
        if scale > 100:
            result += current
            current = 0
    return result + current


def clean_verbal_num(token):
    token = token.replace('-', ' ')
    token = token.replace('\n', ' ')
    token = token.replace(' and', ' ')
    token = token.replace('.', ' ')
    token = token.replace(':', ' ')
    token = token.replace(';', ' ')
    token = token.replace('!', ' ')
    token = token.replace('?', ' ')
    token = token.replace("'", ' ')
    token = token.replace('"', ' ')
    token = token.replace(',', ' ')
    return token


def num_tokenized():
    tokens = nltk.tokenize.regexp_tokenize(text, r'(( |\'|\")((((eleven)|(twelve)|(thirteen)|(fourteen)|(fifteen)|(sixteen)|(seventeen)|(eighteen)|(nineteen)|(twenty)|(thirty)|(forty)|(fifty)|(sixty)|(seventy)|(eighty)|(ninety)|(hundred)|(thousand)|(million)|(billion)|(trillion)|(zero)|(one)|(two)|(three)|(four)|(five)|(six)|(seven)|(eight)|(nine)|(ten)))( |-|\n|(and)|\.|,|:|;|\!|\?|\'|\")+)+)')
    tokens = [token[0] for token in tokens]
    tokens = [clean_verbal_num(token) for token in tokens]
    return tokens


def num_int_tokenized():
    tokens = nltk.tokenize.regexp_tokenize(text, r'\d+')
    return tokens


def biggest_number():
    num_tokens = num_tokenized()
    numbers = lambda sentence: text2int(sentence)
    max_verb = max(num_tokens, key=numbers)  # longest_sen, len(longest_sen)
    num_int_tokens = num_int_tokenized()
    max_int = max(num_int_tokens)
    if int(text2int(max_verb)) >= int(max_int):
        return max_verb
    return max_int


print("1. Lines count:", lines_count())  # count?
print("2. Words count:", real_words_list()[1])
print("3. Unique words count:", unique_words_set())  # needs fix to lower()
print("4.1. Words AVG in sentence:", avg_words_sentence())
print("4.2. Longest sentence: ", longest_sent())
print("5.1. Most popular word:", popular_word(0))
print("5.2. Most popular word exclude stop words:", popular_word(1))
print("6. Longest word sequence without 'k' words: ", longest_non_k_seq())
print("7. Biggest number: ", biggest_number())
print("8. Colors: ", popualr_color())
print("9.1. Names:", extract_names())
print("9.2. Most popular name: ", popular_name())