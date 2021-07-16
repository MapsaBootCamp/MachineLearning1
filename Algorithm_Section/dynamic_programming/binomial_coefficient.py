def binomial(n, k, dp={}):
    assert (n >= 0 and k >= 0), "lotfan riazi yad begir"

    if k == 0 or n == k:
        return 1

    if (n, k) not in dp:
        result = binomial(n-1, k) + binomial(n-1, k-1)
        dp[(n, k)] = result
        return result
    else:
        return dp[(n, k)]


print(binomial(5, 4))
