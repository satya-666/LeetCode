class Solution(object):
    def countCharacters(self, words, chars):
        char_count = {}
        for c in chars:
            if c in char_count:
                char_count[c] += 1
            else:
                char_count[c] = 1

        total = 0

        for word in words:
            word_count = {}
            for c in word:
                if c in word_count:
                    word_count[c] += 1
                else:
                    word_count[c] = 1

            valid = True
            for c in word_count:
                if c not in char_count or word_count[c] > char_count[c]:
                    valid = False
                    break

            if valid:
                total += len(word)

        return(total)
                