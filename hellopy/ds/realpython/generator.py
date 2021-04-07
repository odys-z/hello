'''
Tutorial: How to use generator and yield in python

see https://realpython.com/introduction-to-python-generators/
cvs data:
onpage: https://realpython.com/bonus/generators-yield/
github: https://raw.githubusercontent.com/realpython/materials/master/generators/techcrunch.csv

Created on 8 Nov 2019
@author: odys-z@github.com
'''

class FoundSeeker(object):

    def seek(self, flpath, roundtype):
        lines = (line for line in open(flpath))
        rows = (l.rstrip().split(",") for l in lines)
        headers = next(rows)
        amts = (dict(zip(headers, row))
                for row in rows)
        
        amount = 0
#         total = sum(int(amt_ditc['raisedAmt'] for amt_dict in amts))
        for i in (i for i in amts if i['round'] == roundtype):
            # print(i)
            amount += int(i['raisedAmt'])
        
        return amount
