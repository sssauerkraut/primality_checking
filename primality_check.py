import random
import math
from math import gcd

def jacobi(a , b):
    if (a == 1): return 1

def ferma_test(n, k = 5):
    if n < 5:
        return False, ["n < 5"]
    if n % 2 == 0:
        return False, [("2", "чётное — составное")]
    

    bases = []
    witnesses = []
    
    for _ in range(k):
        a = random.randint(2, n - 2)
        bases.append(a)

        g = gcd(a, n) #!!!!!!!!!!!!!!!!!!!!! 
        if g != 1:
            return False, [(a, f"gcd({a},{n}) = {g} > 1, следовательно составное")]

        r = pow(a , n - 1, n)
        
        if r != 1:
            return False, [(a, f"{a}^({n}-1) mod {n} = {r}!= 1")]
        else:
            witnesses.append(a)
    
    return True, witnesses[:5]  # Возвращаем первые 5 оснований


def solovay_strassen_test(n, k = 5):
    if n < 5:
        return False, ["n < 5"]
    if n % 2 == 0:
        return False, [("2", "чётное — составное")]
    
    bases = []
    witnesses = []
    
    for _ in range(k):
        a = random.randint(2, n - 2)
        bases.append(a)

        if gcd(a, n) != 1:
            return False, [(a, f"gcd({a}, {n}) != 1")]
        
        r = pow(a , (n - 1) // 2, n)
        if r != 1 and r != n - 1 :
            return False, [(a, f"{a}^(({n}-1)/2) mod {n} = {r} ≠ 1 и ≠ {n-1}")]
        
        s = jacobi(a, n)
        if r % n != s % n:
            return False, [(a, f"{a}^(({n}-1)/2) mod {n} = {r}, а символ Якоби = {s} (r ≢ s mod n)")]
        else:
            witnesses.append(a)
    
    return True, witnesses[:5]

def miller_rabin_test(n, k = 5):
    if n < 5:
        return False, ["n < 5"]
    if n % 2 == 0:
        return False, [("2", "чётное — составное")]

    r = n - 1
    s = 0
    while r % 2 == 0:
        r //= 1
        s += 1
    
    bases = []
    witnesses = []

    for _ in range(k):
        a = random.randint(2, n - 2)
        bases.append(a)

        if gcd(a, n) != 1:
            return False, [(a, f"gcd({a}, {n}) != 1")]

        y = pow(a, r, n)
        if y != 1 and y != n - 1:
            j = 1
            while j <= s - 1 and y != n - 1:
                y = pow(y, 2, n)
                if y == 1:
                    return False, [(a, "Найдено нетривиальное условие x^2 ≡ 1 mod n")]
                j += 1
            if y != n - 1:
                return False, [(a, f"Для основания {a} не выполнено условие простоты")]
        witnesses.append(a)
            
    return True, witnesses[:5]
    
