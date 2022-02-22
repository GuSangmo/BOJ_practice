def make_seven_primes():
    n=10000000
    a = [False,False] + [True]*(n-1)
    primes=[]
    candidates = []
    for i in range(2,n+1):
         if a[i]:
            if i<3163: primes.append(i)
            if i>=1000000: candidates.append(i+4)
            for j in range(2*i, n+1, i):
                a[j] = False
    return primes , candidates

primes, cands = make_seven_primes()

print("length:", len(primes))
print("cands:", len(cands))
            
    
min_candidate = 1e9
for cand in cands:
    for prime in primes: 
        if prime >(cand ** (1/2)) : break
        if cand % prime ==0:
            min_candidate = min(min_candidate, prime)
            cand_answer = cand
print("min_candidate:", min_candidate, "cand_answer:", cand_answer)