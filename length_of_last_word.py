class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        is_empty = False
        for i in s:
            if i != " ":
                is_empty = True
        if not is_empty:
            return 0

        last_letter = 0
        last_space = -1
        for i in xrange(len(s) - 1, -1, -1):
          if s[i] != " " and last_letter == 0:
            last_letter = i
          if last_letter != 0 and last_space == -1:
            if s[i] == ' ':
              last_space = i
        if last_space == -1 and last_letter == 0:
          if s[0] != " ":
            return 1
          return 0

        return last_letter - last_space