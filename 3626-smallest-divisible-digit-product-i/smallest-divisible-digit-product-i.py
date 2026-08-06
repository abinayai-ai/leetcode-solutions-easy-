class Solution:

  def smallestNumber(self,n,t):
    x = n
    while True:
      prod = 1
      temp = x
      while temp > 0:
        prod *= temp % 10
        temp //= 10

      if prod % t == 0:
        return x

      x += 1
        