'''
https://pypi.org/project/wordfreq/#description
'''

from wordfreq import zipf_frequency, get_frequency_dict

'''
f = zipf_frequency('frequency', 'en')
print('word: "{0}"\tfrequency: {1}'.format('frequency', f))
'''

d = get_frequency_dict('en', wordlist='best')

'''
f = open('e-5 4e-6_.word', 'w')
# frequency > 0.0001, words = 1068
cnt = 0;
for w in d:
    if d[w] > 0.000004 and d[w] < 0.00001:
        cnt += 1
        f.write('{0} {1}\n'.format(w, d[w]))

f.close()

print("Writen {} lines into freq.word.".format(cnt))
'''

def get_wordfreq(frange):
    fname, whigh, wlow = frange
    f = open('{}.freq.word'.format(fname), 'w')
    cnt = 0;
    for w in d:
        if wlow <= d[w] and d[w] < whigh:
            cnt += 1
            f.write('{0} {1}\n'.format(w, d[w]))

    f.close()

    print("{} : {}".format(fname, cnt))

'''
1_e-4     : 1087
e-4_e-5   : 5996
e-5_4e-6  : 5583
4e-6_2e-6 : 6402
2e-6_e-6  : 9118
e-6_e-7   : 63566
e-7_0     : 210249
'''
grades = [
      ('1_e-4',         1.0, 0.0001),
      ('e-4_e-5',    0.0001, 0.00001),
      ('e-5_4e-6',  0.00001, 0.000004),
      ('4e-6_2e-6',0.000004, 0.000002),
      ('2e-6_e-6', 0.000002, 0.000001),
      ('e-6_e-7',  0.000001, 0.0000001),
      ('e-7_0',   0.0000001, 0.0)
      ]

for fg in grades:
    get_wordfreq(fg)
