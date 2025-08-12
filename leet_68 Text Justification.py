# https://leetcode.com/problems/text-justification/description/

"""Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is inserted between words.

Note:

    A word is defined as a character sequence consisting of non-space characters only.
    Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
    The input array words contains at least one word.



Example 1:

Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]

Example 2:

Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
Note that the second line is also left-justified because it contains only one word.

Example 3:

Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]



Constraints:

    1 <= words.length <= 300
    1 <= words[i].length <= 20
    words[i] consists of only English letters and symbols.
    1 <= maxWidth <= 100
    words[i].length <= maxWidth

"""


class Solution(object):
    def fullJustify(self, words, maxWidth):
        # 0. Get an array with words lengths
        tempo_list = []
        counter = 0
        sentence_justif = []
        # Loop over the array
        for word in words:
            counter += len(word) + 1
            if counter > maxWidth + 1:
                # Manage the 1-element lists
                if len(tempo_list) == 1:
                    onlyword = tempo_list[0] + " " * (maxWidth - len(tempo_list[0]))
                    sentence_justif.append(onlyword)
                else:
                    # creation of list of blanks
                    nb_blanks = maxWidth - sum([len(w) for w in tempo_list])
                    slots = len(tempo_list) - 1
                    base_value = nb_blanks // slots
                    L = [
                        (
                            (base_value + 1) * " "
                            if i < nb_blanks % slots
                            else base_value * " "
                        )
                        for i in range(slots)
                    ]
                    # list of words and blanck spaces
                    sentence = [None] * (len(tempo_list) + slots)
                    sentence[::2] = tempo_list
                    sentence[1::2] = L
                    print(sum([len(x) for x in sentence]))
                    sentence_justif.append("".join(sentence))
                counter = len(word) + 1
                tempo_list = [word]
            else:
                tempo_list.append(word)

        # Address the last line
        if tempo_list:
            final = " ".join(tempo_list) + " " * (
                maxWidth - sum([len(word) for word in tempo_list]) - len(tempo_list) + 1
            )
            sentence_justif.append(final)
        return sentence_justif


words = [
    "Science",
    "is",
    "what",
    "we",
    "understand",
    "well",
    "enough",
    "to",
    "explain",
    "to",
    "a",
    "computer.",
    "Art",
    "is",
    "everything",
    "else",
    "we",
    "do",
]
maxWidth = 20

a = Solution()
print(a.fullJustify(["What", "must", "be", "acknowledgment", "shall", "be"], 16))
# print(a.fullJustify(words,maxWidth))
