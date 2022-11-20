def gcd(a: int, b: int) -> int:
   while b:
      a, b = b, a % b
   return a

def mcd(n:int, m:int) ->float:
   return (n * m)/gcd(n, m)

print(mcd(14, 30))


