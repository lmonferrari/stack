from stackapi import StackAPI, StackAPIError

SITE = StackAPI('pt.stackoverflow')

me = 201329  # your id user
try:
    answers = SITE.fetch('users/{ids}/answers', ids=[me])
    answer_id = [a['answer_id'] for a in answers['items']]
except StackAPIError as e:
    print(e.message)

print(f'Answers: {len(answer_id)}')

links = [f'https://pt.stackoverflow.com/questions/{qid}/' for qid in answer_id]

for link in links:
    print(link)
