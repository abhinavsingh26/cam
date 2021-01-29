temps = [234, 456, 357, 334, 567, -9999, 243, 324]

a = [ temp / 10 if temp != -9999 else 0 for temp in temps]
#for temp in temps:
    #a.append(temp / 10)

print(a)
