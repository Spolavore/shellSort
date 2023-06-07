teste = [[{'AACATGAAGG\n'}, 10], [{'TTTTGGCCAA\n'}, 36], [{'TTTGGCCAAA\n'}, 37], [{'GGGGGGGGGG\n'}, 0], [{'GATCAGATTT\n'}, 11], [{'CCCGGGGGGA\n'}, 9], [{'TTTTTTTTTT\n'}, 0], [{'ATCGATGCAT\n'}, 17], [{'AAAAAAAAAA\n'}, 0], [{'CCCCCCCCCC\n'}, 0], [{'ACGTACGTAC\n'}, 16], [{'CGTACGTACG\n'}, 18], [{'TGCATGCATG\n'}, 21]]
menor = [{'GGGGGGGGGG\n'}, 0]
alo = teste.index(menor)
teste.pop(alo)
print(teste)
