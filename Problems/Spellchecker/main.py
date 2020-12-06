dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']

words = input().split()
outWords = []

for word in words:
    if not (word in dictionary):
        outWords.append(word)

if len(outWords) == 0:
    print("OK")
else:
    for word in outWords:
        print(word)
