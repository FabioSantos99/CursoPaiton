i = 1

while i <= 10:
   print("TABUADA do", i)
   for j in range(1, 11, 1):
      print("{} x {} = {}".format(i, j, i * j))
   i += 1