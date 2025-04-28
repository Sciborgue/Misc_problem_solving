class Solution(object):
    def fullJustify(self, words, maxWidth):
        current_width=0
        listofwords = []
        sentence_justif=[]
        #form a line
        i=0
        while i < len(words):
            #list the words in the next part of sentence
            while i < len(words) and current_width + len(words[i]) + len(listofwords)-1 <= maxWidth :
                current_width+= len(words[i])
                listofwords.append(words[i])
                i+=1
            #with these words, form the new sentence and add it to the final list
            #have the number of blank spaces
            b_spaces = maxWidth - current_width
            if i == len(words):
                sentence_justif.append(" ".join(listofwords)+" "*(b_spaces-(len(listofwords)-1)))
            else:
                supb_spaces = b_spaces % (len(listofwords)-1)
                if supb_spaces != 0:
                    listofwords[0]+=" "*supb_spaces
                    b_spaces-=supb_spaces
                inb_space=int(b_spaces/(len(listofwords)-1))
                sentence_justif.append((" "*inb_space).join(listofwords))
            current_width=0
            listofwords=[]
        return sentence_justif


words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 16

a = Solution()

print(a.fullJustify(words,maxWidth))