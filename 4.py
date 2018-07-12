n=str(input())
if n in('a','e','i','o','u'):
  print("Vowel")
elif(ord(n)>=32) &(ord(n)<=47):
  print("invalid")
else:
  print("Consonants")
