class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # make a new dict
        # loop through each character
        # if htat hcaracter isnt in our dict already, add it
        # increment the count, update max count if its larger
        # if we have ti already, reset the dict, set count to 0


        count = 0
        max_count = 0

        for i in range(len(s)):
            d = {}
            count = 0
            for j in range(i, len(s)):
                if s[j] in d:
                    break
                else:
                    d[s[j]] = 1 
                    count += 1
                
                if count > max_count:
                    max_count = count
        
        return max_count