# install

https://www.nltk.org/howto/wordnet.html

```
    pip install --user -U nltk
    pip show numpy
```

# install data

>>> import nltk
>>> nltk.download('wordnet')
[nltk_data] Error loading wordnet: <urlopen error [Errno 111]
[nltk_data]     Connection refused>

download word.zip:

page: http://www.nltk.org/nltk_data/

download: https://raw.githubusercontent.com/nltk/nltk_data/gh-pages/packages/corpora/wordnet.zip

save to /home/nltk_data

unpack wordnet.zip into /home/nltk_data/corpora

# config pydev

Add pydev library folder: wordnet.

(Eclipse) Add *Forced Buildin*: nltk

see https://stackoverflow.com/questions/2112715/how-do-i-fix-pydev-undefined-variable-from-import-errors

# related resource

https://wordnet.princeton.edu/related-projects

http://projects.csail.mit.edu/jwi/

