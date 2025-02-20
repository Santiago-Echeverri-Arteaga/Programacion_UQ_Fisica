def primo(N):
    for i in range(2,N):
        if N % i == 0:
            return(False)
    return(True)
print(primo(13))