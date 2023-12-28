"""
Independent Alleles

URL: https://rosalind.info/problems/lia/

Given: Two positive integers k
 (k≤7
) and N
 (N≤2k
). In this problem, we begin with Tom, who in the 0th generation has genotype Aa Bb. Tom has two children in the 1st generation, each of whom has two children, and so on. Each organism always mates with an organism having genotype Aa Bb.

Return: The probability that at least N
 Aa Bb organisms will belong to the k
-th generation of Tom's family tree (don't count the Aa Bb mates at each level). Assume that Mendel's second law holds for the factors.
"""
import math   

def prob(k, n):
                                                                            
    P = 2**k                                                                       
    probability = 0                                                                
    for i in range(n, P + 1):                                                      
        prob = (math.factorial(P) /                                                
                (math.factorial(i) * math.factorial(P - i))) * (0.25**i) * (0.75**(
                    P - i))                                                        
        probability += prob                                                        
    return probability

if __name__ == "__main__":
    k = 6                                                                          
    n = 18
    print(prob(k, n))
