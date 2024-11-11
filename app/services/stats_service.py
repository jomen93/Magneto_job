

def get_stats():
    number_mutant_dna = 40
    number_human_dna = 100
    ratio = number_mutant_dna / number_mutant_dna
    return {
        "count_mutant_dna": number_mutant_dna,
        "count_human_dna": number_human_dna,
        "ratio": ratio
    }
