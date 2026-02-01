
###a

def a(n, k):
    k += 1              #4        k = k+1
    i = n               #2
    while i > 0:        #3*(n+1)
        i -= 1          #4


###b
def b(n, k):
    i = n                #2
    while i > 1:         #3* (m+1)
        k += 1           #4m
        i //= 2          #4m

# i = i//2 = i*2^-1
# n = 2^m -> m = log2(n)

# m = 0, n = 1: loop block: 0
# # m = 1, n = 2: loop block: 1
# # m = 2, n = 4: loop block: 2
# # m    , n    : loop block: m



def d(n, k):
    i = 0                           #2
    while i < n:                    #3(n+1)
        j = 0                       #2n
        while j < i * i:            #3((n-1)*n*(2*n-1)/6 + n )
            k += 1                  #4*(n-1)*n*(2*n-1)/6
            j += 1                  #4*(n-1)*n*(2*n-1)/6
        i += 1                      #4n
# sum in while i² = (n-1)*n*(2*n-1)/6


def e(n, k):
    i = 1                           #2
    while i < n:                    #3(m+1)
        j = 1                       #2m
        while j < n:                #3m*(m+1)
            k += 1                  #4m^2
            j *= 2                  #4m^2
        i *= 2                      #4m
# n = 2^m -> m = log2(n)



