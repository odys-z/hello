from unittest import TestCase

def question_func2(n):
    n += 1
    return ['answer-2.1', 'answer-2.2', n]

t = TestCase()
answer = question_func2(3)
t.assertEqual('answer-2.1', answer[0])
t.assertEqual('answer-2.2', answer[1])
t.assertEqual(4, answer[2])

print('question_func2 OK!')
