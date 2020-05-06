'''
17. Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive, return all possible letter combinations
that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.
Note that 1 does not map to any letters.

'''

from typing import List
import unittest

from utils import Assrt

'''
Runtime: 32 ms, faster than 41.02% of Python3 online submissions for Letter Combinations of a Phone Number.
Memory Usage: 14 MB, less than 5.88% of Python3 online submissions for Letter Combinations of a Phone Number.
'''
class Solution:
    dials = {'2': ['a', 'b', 'c'],
             '3': ['d', 'e', 'f'],
             '4': ['g', 'h', 'i'],
             '5': ['j', 'k', 'l'],
             '6': ['m', 'n', 'o'],
             '7': ['p', 'q', 'r', 's'],
             '8': ['t', 'u', 'v'],
             '9': ['w', 'x', 'y', 'z']
             }
    def letterCombinations(self, digits: str) -> List[str]:
        if (digits is None or len(digits) == 0):
            return []
        res = Solution.dials[digits[len(digits) - 1]]
        for cx in reversed(digits[0 : -1]):
            res2 = list()
            for a in Solution.dials[cx]:
                for ix in range(len(res)):
                    res2.append(a + res[ix])
            res = res2
        return res

eq = Assrt.Eq()
class Test(unittest.TestCase):

    def testName(self):
        s = Solution()
        eq.strArr(['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf'],
                 s.letterCombinations('23'))

        eq.strArr([], s.letterCombinations(''))

        eq.strArr([], s.letterCombinations(None))

        eq.strArr(['a', 'b', 'c'], s.letterCombinations('2'))

        eq.strArr(['w', 'x', 'y', 'z'], s.letterCombinations('9'))

        eq.strArr(['adg', 'aeg', 'afg', 'bdg', 'beg', 'bfg', 'cdg', 'ceg', 'cfg',
                   'adh', 'aeh', 'afh', 'bdh', 'beh', 'bfh', 'cdh', 'ceh', 'cfh',
                   'adi', 'aei', 'afi', 'bdi', 'bei', 'bfi', 'cdi', 'cei', 'cfi',],
                 s.letterCombinations('234'))

        eq.strArr(["mp","mq","mr","ms","np","nq","nr","ns","op","oq","or","os"],
                  s.letterCombinations('67'))

        eq.strArr(["adgjmp","adgjmq","adgjmr","adgjms","adgjnp","adgjnq","adgjnr","adgjns","adgjop","adgjoq","adgjor","adgjos","adgkmp","adgkmq","adgkmr","adgkms","adgknp","adgknq","adgknr","adgkns",
        "adgkop","adgkoq","adgkor","adgkos","adglmp","adglmq","adglmr","adglms","adglnp","adglnq","adglnr","adglns","adglop","adgloq","adglor","adglos","adhjmp","adhjmq","adhjmr","adhjms","adhjnp",
        "adhjnq","adhjnr","adhjns","adhjop","adhjoq","adhjor","adhjos","adhkmp","adhkmq","adhkmr","adhkms","adhknp","adhknq","adhknr","adhkns","adhkop","adhkoq","adhkor","adhkos","adhlmp","adhlmq",
        "adhlmr","adhlms","adhlnp","adhlnq","adhlnr","adhlns","adhlop","adhloq","adhlor","adhlos","adijmp","adijmq","adijmr","adijms","adijnp","adijnq","adijnr","adijns","adijop","adijoq","adijor",
        "adijos","adikmp","adikmq","adikmr","adikms","adiknp","adiknq","adiknr","adikns","adikop","adikoq","adikor","adikos","adilmp","adilmq","adilmr","adilms","adilnp","adilnq","adilnr","adilns",
        "adilop","adiloq","adilor","adilos","aegjmp","aegjmq","aegjmr","aegjms","aegjnp","aegjnq","aegjnr","aegjns","aegjop","aegjoq","aegjor","aegjos","aegkmp","aegkmq","aegkmr","aegkms","aegknp",
        "aegknq","aegknr","aegkns","aegkop","aegkoq","aegkor","aegkos","aeglmp","aeglmq","aeglmr","aeglms","aeglnp","aeglnq","aeglnr","aeglns","aeglop","aegloq","aeglor","aeglos","aehjmp","aehjmq",
        "aehjmr","aehjms","aehjnp","aehjnq","aehjnr","aehjns","aehjop","aehjoq","aehjor","aehjos","aehkmp","aehkmq","aehkmr","aehkms","aehknp","aehknq","aehknr","aehkns","aehkop","aehkoq","aehkor",
        "aehkos","aehlmp","aehlmq","aehlmr","aehlms","aehlnp","aehlnq","aehlnr","aehlns","aehlop","aehloq","aehlor","aehlos","aeijmp","aeijmq","aeijmr","aeijms","aeijnp","aeijnq","aeijnr","aeijns",
        "aeijop","aeijoq","aeijor","aeijos","aeikmp","aeikmq","aeikmr","aeikms","aeiknp","aeiknq","aeiknr","aeikns","aeikop","aeikoq","aeikor","aeikos","aeilmp","aeilmq","aeilmr","aeilms","aeilnp",
        "aeilnq","aeilnr","aeilns","aeilop","aeiloq","aeilor","aeilos","afgjmp","afgjmq","afgjmr","afgjms","afgjnp","afgjnq","afgjnr","afgjns","afgjop","afgjoq","afgjor","afgjos","afgkmp","afgkmq",
        "afgkmr","afgkms","afgknp","afgknq","afgknr","afgkns","afgkop","afgkoq","afgkor","afgkos","afglmp","afglmq","afglmr","afglms","afglnp","afglnq","afglnr","afglns","afglop","afgloq","afglor",
        "afglos","afhjmp","afhjmq","afhjmr","afhjms","afhjnp","afhjnq","afhjnr","afhjns","afhjop","afhjoq","afhjor","afhjos","afhkmp","afhkmq","afhkmr","afhkms","afhknp","afhknq","afhknr","afhkns",
        "afhkop","afhkoq","afhkor","afhkos","afhlmp","afhlmq","afhlmr","afhlms","afhlnp","afhlnq","afhlnr","afhlns","afhlop","afhloq","afhlor","afhlos","afijmp","afijmq","afijmr","afijms","afijnp",
        "afijnq","afijnr","afijns","afijop","afijoq","afijor","afijos","afikmp","afikmq","afikmr","afikms","afiknp","afiknq","afiknr","afikns","afikop","afikoq","afikor","afikos","afilmp","afilmq",
        "afilmr","afilms","afilnp","afilnq","afilnr","afilns","afilop","afiloq","afilor","afilos","bdgjmp","bdgjmq","bdgjmr","bdgjms","bdgjnp","bdgjnq","bdgjnr","bdgjns","bdgjop","bdgjoq","bdgjor",
        "bdgjos","bdgkmp","bdgkmq","bdgkmr","bdgkms","bdgknp","bdgknq","bdgknr","bdgkns","bdgkop","bdgkoq","bdgkor","bdgkos","bdglmp","bdglmq","bdglmr","bdglms","bdglnp","bdglnq","bdglnr","bdglns",
        "bdglop","bdgloq","bdglor","bdglos","bdhjmp","bdhjmq","bdhjmr","bdhjms","bdhjnp","bdhjnq","bdhjnr","bdhjns","bdhjop","bdhjoq","bdhjor","bdhjos","bdhkmp","bdhkmq","bdhkmr","bdhkms","bdhknp",
        "bdhknq","bdhknr","bdhkns","bdhkop","bdhkoq","bdhkor","bdhkos","bdhlmp","bdhlmq","bdhlmr","bdhlms","bdhlnp","bdhlnq","bdhlnr","bdhlns","bdhlop","bdhloq","bdhlor","bdhlos","bdijmp","bdijmq",
        "bdijmr","bdijms","bdijnp","bdijnq","bdijnr","bdijns","bdijop","bdijoq","bdijor","bdijos","bdikmp","bdikmq","bdikmr","bdikms","bdiknp","bdiknq","bdiknr","bdikns","bdikop","bdikoq","bdikor",
        "bdikos","bdilmp","bdilmq","bdilmr","bdilms","bdilnp","bdilnq","bdilnr","bdilns","bdilop","bdiloq","bdilor","bdilos","begjmp","begjmq","begjmr","begjms","begjnp","begjnq","begjnr","begjns",
        "begjop","begjoq","begjor","begjos","begkmp","begkmq","begkmr","begkms","begknp","begknq","begknr","begkns","begkop","begkoq","begkor","begkos","beglmp","beglmq","beglmr","beglms","beglnp",
        "beglnq","beglnr","beglns","beglop","begloq","beglor","beglos","behjmp","behjmq","behjmr","behjms","behjnp","behjnq","behjnr","behjns","behjop","behjoq","behjor","behjos","behkmp","behkmq",
        "behkmr","behkms","behknp","behknq","behknr","behkns","behkop","behkoq","behkor","behkos","behlmp","behlmq","behlmr","behlms","behlnp","behlnq","behlnr","behlns","behlop","behloq","behlor",
        "behlos","beijmp","beijmq","beijmr","beijms","beijnp","beijnq","beijnr","beijns","beijop","beijoq","beijor","beijos","beikmp","beikmq","beikmr","beikms","beiknp","beiknq","beiknr","beikns",
        "beikop","beikoq","beikor","beikos","beilmp","beilmq","beilmr","beilms","beilnp","beilnq","beilnr","beilns","beilop","beiloq","beilor","beilos","bfgjmp","bfgjmq","bfgjmr","bfgjms","bfgjnp",
        "bfgjnq","bfgjnr","bfgjns","bfgjop","bfgjoq","bfgjor","bfgjos","bfgkmp","bfgkmq","bfgkmr","bfgkms","bfgknp","bfgknq","bfgknr","bfgkns","bfgkop","bfgkoq","bfgkor","bfgkos","bfglmp","bfglmq",
        "bfglmr","bfglms","bfglnp","bfglnq","bfglnr","bfglns","bfglop","bfgloq","bfglor","bfglos","bfhjmp","bfhjmq","bfhjmr","bfhjms","bfhjnp","bfhjnq","bfhjnr","bfhjns","bfhjop","bfhjoq","bfhjor",
        "bfhjos","bfhkmp","bfhkmq","bfhkmr","bfhkms","bfhknp","bfhknq","bfhknr","bfhkns","bfhkop","bfhkoq","bfhkor","bfhkos","bfhlmp","bfhlmq","bfhlmr","bfhlms","bfhlnp","bfhlnq","bfhlnr","bfhlns",
        "bfhlop","bfhloq","bfhlor","bfhlos","bfijmp","bfijmq","bfijmr","bfijms","bfijnp","bfijnq","bfijnr","bfijns","bfijop","bfijoq","bfijor","bfijos","bfikmp","bfikmq","bfikmr","bfikms","bfiknp",
        "bfiknq","bfiknr","bfikns","bfikop","bfikoq","bfikor","bfikos","bfilmp","bfilmq","bfilmr","bfilms","bfilnp","bfilnq","bfilnr","bfilns","bfilop","bfiloq","bfilor","bfilos","cdgjmp","cdgjmq",
        "cdgjmr","cdgjms","cdgjnp","cdgjnq","cdgjnr","cdgjns","cdgjop","cdgjoq","cdgjor","cdgjos","cdgkmp","cdgkmq","cdgkmr","cdgkms","cdgknp","cdgknq","cdgknr","cdgkns","cdgkop","cdgkoq","cdgkor",
        "cdgkos","cdglmp","cdglmq","cdglmr","cdglms","cdglnp","cdglnq","cdglnr","cdglns","cdglop","cdgloq","cdglor","cdglos","cdhjmp","cdhjmq","cdhjmr","cdhjms","cdhjnp","cdhjnq","cdhjnr","cdhjns",
        "cdhjop","cdhjoq","cdhjor","cdhjos","cdhkmp","cdhkmq","cdhkmr","cdhkms","cdhknp","cdhknq","cdhknr","cdhkns","cdhkop","cdhkoq","cdhkor","cdhkos","cdhlmp","cdhlmq","cdhlmr","cdhlms","cdhlnp",
        "cdhlnq","cdhlnr","cdhlns","cdhlop","cdhloq","cdhlor","cdhlos","cdijmp","cdijmq","cdijmr","cdijms","cdijnp","cdijnq","cdijnr","cdijns","cdijop","cdijoq","cdijor","cdijos","cdikmp","cdikmq",
        "cdikmr","cdikms","cdiknp","cdiknq","cdiknr","cdikns","cdikop","cdikoq","cdikor","cdikos","cdilmp","cdilmq","cdilmr","cdilms","cdilnp","cdilnq","cdilnr","cdilns","cdilop","cdiloq","cdilor",
        "cdilos","cegjmp","cegjmq","cegjmr","cegjms","cegjnp","cegjnq","cegjnr","cegjns","cegjop","cegjoq","cegjor","cegjos","cegkmp","cegkmq","cegkmr","cegkms","cegknp","cegknq","cegknr","cegkns",
        "cegkop","cegkoq","cegkor","cegkos","ceglmp","ceglmq","ceglmr","ceglms","ceglnp","ceglnq","ceglnr","ceglns","ceglop","cegloq","ceglor","ceglos","cehjmp","cehjmq","cehjmr","cehjms","cehjnp",
        "cehjnq","cehjnr","cehjns","cehjop","cehjoq","cehjor","cehjos","cehkmp","cehkmq","cehkmr","cehkms","cehknp","cehknq","cehknr","cehkns","cehkop","cehkoq","cehkor","cehkos","cehlmp","cehlmq",
        "cehlmr","cehlms","cehlnp","cehlnq","cehlnr","cehlns","cehlop","cehloq","cehlor","cehlos","ceijmp","ceijmq","ceijmr","ceijms","ceijnp","ceijnq","ceijnr","ceijns","ceijop","ceijoq","ceijor",
        "ceijos","ceikmp","ceikmq","ceikmr","ceikms","ceiknp","ceiknq","ceiknr","ceikns","ceikop","ceikoq","ceikor","ceikos","ceilmp","ceilmq","ceilmr","ceilms","ceilnp","ceilnq","ceilnr","ceilns",
        "ceilop","ceiloq","ceilor","ceilos","cfgjmp","cfgjmq","cfgjmr","cfgjms","cfgjnp","cfgjnq","cfgjnr","cfgjns","cfgjop","cfgjoq","cfgjor","cfgjos","cfgkmp","cfgkmq","cfgkmr","cfgkms","cfgknp",
        "cfgknq","cfgknr","cfgkns","cfgkop","cfgkoq","cfgkor","cfgkos","cfglmp","cfglmq","cfglmr","cfglms","cfglnp","cfglnq","cfglnr","cfglns","cfglop","cfgloq","cfglor","cfglos","cfhjmp","cfhjmq",
        "cfhjmr","cfhjms","cfhjnp","cfhjnq","cfhjnr","cfhjns","cfhjop","cfhjoq","cfhjor","cfhjos","cfhkmp","cfhkmq","cfhkmr","cfhkms","cfhknp","cfhknq","cfhknr","cfhkns","cfhkop","cfhkoq","cfhkor",
        "cfhkos","cfhlmp","cfhlmq","cfhlmr","cfhlms","cfhlnp","cfhlnq","cfhlnr","cfhlns","cfhlop","cfhloq","cfhlor","cfhlos","cfijmp","cfijmq","cfijmr","cfijms","cfijnp","cfijnq","cfijnr","cfijns",
        "cfijop","cfijoq","cfijor","cfijos","cfikmp","cfikmq","cfikmr","cfikms","cfiknp","cfiknq","cfiknr","cfikns","cfikop","cfikoq","cfikor","cfikos","cfilmp","cfilmq","cfilmr","cfilms","cfilnp",
        "cfilnq","cfilnr","cfilns","cfilop","cfiloq","cfilor","cfilos"],
        s.letterCombinations('234567'))
        
