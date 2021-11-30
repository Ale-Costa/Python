file = open("seq.fasta")

linhas = file.readlines()
multiFasta = {}

for linha in linhas:

        if linha[0] == ">":
            seq = linha.strip()
            multiFasta[seq] = ""
        else:
            multiFasta[seq] = multiFasta[seq]+linha.strip()


print(multiFasta)