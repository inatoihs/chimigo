from sys import argv
import MeCab
import markovify
import time

def main():
    with open("chimi.txt",encoding='utf-8') as file:
        text = file.read()
    tagger = MeCab.Tagger("-O wakati")
    #text = tagger.parse(text)
    #model = markovify.Text(text, state_size=1)
    data = [tagger.parse(s) for s in text.split("\n") if s != ""]
    joinedData = "".join(data)
    model = markovify.NewlineText(joinedData, state_size=2)
    for i in range(100):
        sentence = model.make_short_sentence(150)
        if sentence==None:
            exit()
        sentence=sentence.replace(" ","")
        print(sentence)
        time.sleep(0.5)


if __name__ == "__main__":
    main()
