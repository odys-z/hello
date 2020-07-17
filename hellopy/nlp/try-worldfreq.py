'''
https://pypi.org/project/wordfreq/#description
'''

from wordfreq import zipf_frequency, get_frequency_dict

f = zipf_frequency('frequency', 'en')
print('word: "{0}"\tfrequency: {1}'.format('frequency', f))

d = get_frequency_dict('en', wordlist='best')

f = open('freq.word', 'w')

# frequency > 0.0001, words = 1068
cnt = 0;
for w in d:
    if d[w] > 0.0001:
        cnt += 1
        f.write('{0} {1}\n'.format(w, d[w]))

f.close()

print("Writen {} lines into freq.word.".format(cnt))
