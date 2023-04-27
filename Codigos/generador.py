def all_even(N):
    n=0
    while n<N:
        yield n
        n+=2

a = ((i,i**2,i**3) for i in all_even(13) if not i%3)
#print(list(a))
for j in (("Apple" if i<3 else "Pie") for i in range(8)):
    print(j)
