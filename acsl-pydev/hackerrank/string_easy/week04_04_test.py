from unittest.case import TestCase

from string_easy.week04_04 import solve

t = TestCase()
t.assertEqual('1',
              solve('1'))

t.assertEqual('', solve(''))
t.assertEqual('A', solve('A'))
t.assertEqual('1234a', solve('1234a'))
t.assertEqual('1234a B', solve('1234a b'))
t.assertEqual('A 1 De 11 Ppp', solve('A 1 de 11 ppp'))
t.assertEqual('A A1 He11ow', solve('a A1 he11ow'))
t.assertEqual('Xa Tep', solve('xA tep'))

t.assertEqual('Q W E R T Y U I O P A S D F G H J  K L Z X C V B N M Q W E R T Y U I O P A S D F G H J  K L Z X C V B N M',
    solve('q w e r t y u i o p a s d f g h j  k l z x c v b n m Q W E R T Y U I O P A S D F G H J  K L Z X C V B N M'))

t.assertEqual('Df 13k 1l32l; F2p9sdf234c 2q3q;usn- 4 Q 9348n  Uew  Q Nqw 9r [0439p34p 4i; L 34- Ciq09 Af  Wvtv Seezs Dfar  Dfcdsfva We Wes 1dctvvrfwcrevregwev  Wervw  Wwertvw45v5',
    solve('df 13k 1l32l; f2p9sdf234c 2q3q;usn- 4 q 9348n  uew  q nqw 9r [0439p34p 4i; l 34- CIQ09 Af  WVTV SEEZS DFAr  dfCdsFVA WE wes 1dctvvrfWCRevREgwev  weRVW  wweRTVw45V5'))

print('\nTest OK: solve()')
