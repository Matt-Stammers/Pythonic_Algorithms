# This one will convert digits to their hex equivalent as it is base 16. It returns the remainder.

def toStr(n,base):
   convertString = "0123456789ABCDEF"
   if n < base:
      return convertString[n]
   else:
      return toStr(n//base,base) + convertString[n%base]

print(toStr(1453,16))

# It can easily be adapted to convert things to binary form:

def toStr(n,base):
   convertString = "0123456789"
   if n < base:
      return convertString[n]
   else:
      return toStr(n//base,base) + convertString[n%base]

print(toStr(1453,2))
