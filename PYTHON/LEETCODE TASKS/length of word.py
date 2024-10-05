s= " Rose is beautiful "
w = s.strip().split()
print(w)
if not s or not w:
    print(0)
else:
    print(w[-1])
    print(len(w[-1]))
print("___________________________________")
# step 2 
class solution:
  def lengthOfLastWord(self, s: str) -> int:
     if s.split():
        return len(s.split()[-1])
     return 0
s = "hello world"
obj = solution
obj.lengthOfLastWord()



# step 3
# split fnctn automatically ignores those spaces 
name = "  Uma   Saraswathi "
find = name.split()
print(find)
    
