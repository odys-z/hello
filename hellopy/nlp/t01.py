'''
[wordnet howto](https://www.nltk.org/howto/wordnet.html)

Created on 13 Jul 2020

@author: odys-z@github.com
'''

from nltk.corpus import wordnet as wn

def main():
    t = wn.synsets('dog')
    s = wn.synset('dog.n.01')
    print(t)
    print( '\n{0} definition/examples/lemmas:'.format(s.name() ))
    print( s.definition() )
    print( s.examples() )
    print( s.lemmas() )
    for lm in s.lemmas():
        print(lm.name())

if __name__ == '__main__':
    main()