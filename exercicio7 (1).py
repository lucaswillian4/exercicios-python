nome_disciplina = input("Digite o nome da disciplina: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 7:
    condicao = "Aprovado"
else:
    condicao = "Reprovado"

print(f"A média na disciplina {nome_disciplina} é: {media:.2f}")
print(f"O aluno está {condicao}.")