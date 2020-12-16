from unittest import TestCase

def question_func1():
    return 'answer-1'

t = TestCase()
answer = question_func1()
t.assertEqual('answer-1', answer)

print('question_func1 OK!')


