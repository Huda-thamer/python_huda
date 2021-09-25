"""
Instructions:

1. Create a class named ReversedString that inherits from StringOperations class
2. Implement the function reverse
3. reverse function should be a one liner function that returns the reverse string to_be_reversed
4. Instantiate the class ReversedString
5. Print to show your function implementation result
"""


class StringOperations:

  def init(self, to_be_reversed):
    self.to_be_reversed = to_be_reversed
  
  def reverse(self):
      return self.to_be_reversed[::-1]
      raise NotImplemented('This method need to be implemented')


class ReversedString(StringOperations):

  def init(self):
    my_str = input("Enter any string to reverse it: ")
    StringOperations.init(self, my_str)

rs =  ReversedString()
print(rs.reverse())