'''
We observe that a palindrome mirrors around its center.
Therefore, a palindrome can be expanded from its center, and there are only 2n - 12n−1 such centers.
You might be asking why there are 2n - 12n−1 but not nn centers?
The reason is the center of a palindrome can be in between two letters.
Such palindromes have even number of letters (such as "abba") and its center are between the two 'b's.
'''
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        index,length=0,0
        if len(s)<2:
            return s
        for i in range(len(s)):
            index1,length1=self.expand(s,i,i)
            index2,length2=self.expand(s,i,i+1)
            if length<max(length1,length2):
                if length1>length2:
                    index,length=index1,length1
                else:
                    index,length=index2,length2
            #print index,length
        return s[index:index+length]

    def expand(self,s,i,j):
        while(i>=0 and j<len(s) and s[i]==s[j]):
            i-=1
            j+=1
        return i+1,j-i-1
