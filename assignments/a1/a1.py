import nltk
nltk.download('punkt')
nltk.download('gutenberg')
nltk.download('brown')

# Task 1 (1 mark)
def word_counts(text, words):
    """Return a vector that represents the counts of specific words in the text
    >>> word_counts("Here is sentence one. Here is sentence two.", ['Here', 'two', 'three'])
    [2, 1, 0]
    >>> emma = nltk.corpus.gutenberg.raw('austen-emma.txt')
    >>> word_counts(emma, ['the', 'a'])
    [4842, 3001]
    """
    return []

# Task 2 (1 mark)
def pos_counts(text, pos_list):
    """Return the sorted list of distinct words with a given part of speech
    >>> emma = nltk.corpus.gutenberg.raw('austen-emma.txt')
    >>> pos_counts(emma, ['DET', 'NOUN'])
    [14352, 32029]
    """
    return []

# Task 3 (1 mark)
import re
VC = re.compile('[aeiou]+[^aeiou]+', re.I)
def count_syllables(word):
    return len(VC.findall(word))

def compute_fres(text):
    """Return the FRES of a text.
    >>> emma = nltk.corpus.gutenberg.raw('austen-emma.txt')
    >>> compute_fres(emma) # doctest: +ELLIPSIS
    99.40...
    """
    return 0.0

# Task 4 (2 marks)
import re
regexp = re.compile('.*(st|nd|rd|th)$')
def annotateOD(listoftokens):
    """Annotate the ordinal numbers in the list of tokens
    >>> annotateOD("the second tooth".split())
    [('the', ''), ('second', 'OD'), ('tooth', '')]
    """
    result = []
    for t in listoftokens:
        if regexp.match(t):
            result.append((t, 'OD'))
        else:
            result.append((t, ''))
    return result
    
# DO NOT MODIFY THE CODE BELOW

def compute_f1(result, tagged):
    assert len(result) == len(tagged) # This is a check that the length of the result and tagged are equal
    correct = [result[i][0] for i in range(len(result)) if result[i][1][:2] == 'OD' and tagged[i][1][:2] == 'OD']
    numbers_result = [result[i][0] for i in range(len(result)) if result[i][1][:2] == 'OD']
    numbers_tagged = [tagged[i][0] for i in range(len(tagged)) if tagged[i][1][:2] == 'OD']
    if len(numbers_tagged) > 0:
        r = len(correct)/len(numbers_tagged)
    else:
        r = 0.0
    if len(numbers_result) > 0:
        p = len(correct)/len(numbers_result)
    else:
        p = 0.0
    return 2*r*p/(r+p)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    nltk.download('brown')
    tagged = nltk.corpus.brown.tagged_words(categories='news')
    words = [t for t, w in tagged]
    result = annotateOD(words)
    f1 = compute_f1(result, tagged)
    print("F1 score:", f1)
