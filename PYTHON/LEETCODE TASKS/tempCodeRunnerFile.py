class solution:
  def lengthOfLastWord(self, s: str) -> int:
     if s.split():
        return len(s.split()[-1])
     return 0
s = "hello world"
obj = solution
obj.lengthOfLastWord()


