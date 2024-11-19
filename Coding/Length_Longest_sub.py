def lengthOfLongestSubstring(self, s):        
        """
        :type s: str
        :rtype: int
        """
        char_set = set()
        start = 0
        max_length = 0
        for i in range(len(s)):
            while s[i] in char_set:
                char_set.remove(s[start])
                start += 1
            char_set.add(s[i])
            max_length = max(max_length, i - start + 1)
        return max_length