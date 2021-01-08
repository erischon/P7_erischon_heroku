import re
import nltk
import json


class GPParser:
    """ """

    def __init__(self):
        """ """
        pass

    def lowercase(self, value):
        """ I lowercase the text. """
        return value.lower()

    def punctuation(self, value):
        """ I remove the punctuations. """
        value = re.sub('_', ' ', value)
        value = re.sub(',', ' ', value)
        value = re.sub('\'', ' ', value)
        value = re.sub(r'[^\w\s]','', value)
        value = re.sub(r'\s+',' ',value)
        return value

    def tokenization(self, value):
        """ I create tokens. """
        searched_words = nltk.word_tokenize(value)
        for word in searched_words:
            if len(word) == 1:
                searched_words.remove(word)
        return searched_words

    def remove_stopwords(self, value):
        """ I remove the French stopwords. """
        with open("grandpy/stop_words.json", encoding="utf-8") as json_file:
            stopwords = json.load(json_file)
        key_words = [word for word in value if word not in stopwords["stop_words"]]
        return key_words

    def parser(self, value):
        """ I parse the query. """
        value = self.lowercase(value)
        value = self.punctuation(value)
        value = self.tokenization(value)
        value = self.remove_stopwords(value)
        value.append("wiki")
        searched_words = " "
        return searched_words.join(value)

if __name__ == "__main__":
    parser = GPParser()
    
    # === Tests of methods ===
    # print(parser.lowercase("ToTO"))
    # print(parser.punctuation("hop,hop, hop, zut: ça v;a plus! ..../_ super..."))
    # print(parser.tokenization("c est top parce que j ai réussi à faire nimp"))
    # print (parser.remove_stopwords(['est', 'top', 'toujours', 'abord', 'parce', 'que', 'ai', 'réussi', 'faire', 'nimp']))
    # print (parser.remove_stopwords(['vives', 'toujours', 'puisque', 'orléans', 'pure', '16', 'camille']))
    # print(parser.parser("je cherche l'adresse de la maison de la radio à paris ou à marseille"))