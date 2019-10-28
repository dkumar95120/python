def getLetterSequenceInWord(word):
    letterSeq = [word[0]]
    prev = word[0]
    for ch in word[1:]:
        if ch != prev:
            letterSeq.append(ch)
            prev = ch
    return letterSeq


def alphaSequence(words):
    sequence = getLetterSequenceInWord(words[0])
    for word in words[1:]:
        letterSeq = getLetterSequenceInWord(word)
        for i,c in enumerate(letterSeq):
            # find the minimum index of the successor letters if they are present in the sequence
            index = len(sequence)
            for j in range(i+1, len(letterSeq)):
                successor = letterSeq[j]
                if successor in sequence:
                    index = min(index,sequence.index(successor))
            # insert the letter ahead of the minimum index of the successor letters
            if index < len(sequence):
                sequence = sequence[:index] + [c] + sequence[index:]
            else:
                sequence.append(c)
    # now take out redundant letters keeping only their first occurence
    finalSeq = [sequence[0]]
    for c in sequence[1:]:
        if c not in finalSeq:
            finalSeq.append(c)
    return finalSeq


