"""
Introduction to Mendelian Inheritance

URL: https://rosalind.info/problems/iprb/

Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.

Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.
"""

def probability_dom(k, m, n):
    total = k + m + n
    # recessive_parents_prob = ((n/total)) * ((n-1/(total-1)))
    first_recessive = n/total
    second_recessive = (n-1)/(total-1)
    recessive_parents_prob = first_recessive * second_recessive
    # print(recessive_parents_prob)
    first_het = m/total
    second_het = (m-1)/(total-1)
    heterozygous_prob = first_het * second_het
    heterozygous_recessive_prob = first_het * (n/(total-1)) + first_recessive * (m/(total-1))

    probability_recessive = recessive_parents_prob + (heterozygous_prob * 1/4) + (heterozygous_recessive_prob * 1/2)
    probability_dominant = 1 - probability_recessive

    return probability_dominant

if __name__ == "__main__":
    print(probability_dom(21, 21, 30))