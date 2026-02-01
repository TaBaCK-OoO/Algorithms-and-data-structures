"""Доведіть співвідношення



"""
# A1

'''∑𝑖 = 𝑂(𝑛)'''
def a_fast(n):
    return n * (n + 1) // 2     # O(1)

# A2
def a(n):
    s = 0                       # O(1)
    for i in range(1, n + 1):   # O(n)
        s += i                  # O(n)
    return s                    # O(1)

#proved sum = o(n)


#B
"""∑𝑖^2 = 𝑂(𝑛)   """

def b(n):
    s = 0                       # O(1)
    for i in range(1, n + 1):   # O(n)
        i *= i                  # O(n)
        s += i                  # O(n)

    return s                    # O(1)

#proved sum = o(n)

#C
'''𝑎^𝑖 = 𝑂(𝑛)'''
def c(a, n):
    s = 0                       # O(1)
    p = a                       # O(1)
    for i in range(1, n + 1):   # O(n)
        s += p                  # O(n)
        p *= a                  # O(n)

    return s                    # O(1)
#proved sum = o(n)

#D
'''∑i^i= 𝑂(𝑛^2)'''

def d(n):
    s = 0                       # O(1)
    for i in range(1, n + 1):   # O(n)
        k = i                   # O(n)
        for j in range(1, i):   # O(n^2)               # O(n)
            k *= i              # O(n^2)
            s += k              # O(n^2)
    return s                    # O(1)
#proved sum = o(n^2)

#E
'''∏ 1/(1 + 𝑖) = 𝑂(𝑛)'''


def e(n):
    m = 1                           # O(1)
    for i in range(1, n + 1):       # O(n)
        m *=  1 /(1+i)              # O(n)
    return m                        # O(1)
#proved sum = o(n)



#F
'''∏ 1/(1 + 𝑖!)= 𝑂(𝑛)'''

def f(n):
    m = 1
    j = 1                           # O(1)
    for i in range(1, n + 1):       # O(n)
        j *= i                      # O(n)
        m *=  1 /(1+j)              # O(n)
    return m                        # O(1)
#proved sum = o(n)

#G
'''∏ a^i/(1 + 𝑖!)= 𝑂(𝑛)'''
def g(a,n):
 m=1                           # O(1)
 t=a                           # O(1)
 j=1                           # O(1)
 for i in range(1, n+1):       # O(n)
  j *= i                       # O(n)
  m*=t/(1+j)                   # O(n)
  t*=a                         # O(n)
 return m                      # O(1)
#proved sum = o(n)



#H
'''∏ 1/(1 + 𝑖^m)= 𝑂(𝑛m)'''
def h(m, n):
    t = 1                           # O(1)
    for i in range(1, n + 1):       # O(n)
        j = 1                       # O(n)
        for p in range(1, m + 1):   # O(nm)
            j *= i                  # O(nm)
        t *= 1 / (1 + j)            # O(n)
    return t                        # O(1)
#proved sum = o(nm)



#I
'''∏ 1/(1 + 𝑖^i)= 𝑂(𝑛^2)'''
def i(n):
    t = 1                           # O(1)
    for i in range(1, n + 1):       # O(n)
        j = 1                       # O(n)
        for p in range(1, i + 1):   # O(n^2)
            j *= i                  # O(n^2)
        t *= 1 / (1 + j)            # O(n)
    return t                        # O(1)
#proved sum = o(n^2)








