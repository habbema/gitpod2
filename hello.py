import os
#comentário de uma linha
"""Comentário de várias linhas"""

msg ="Hello world"

linguagem_atual = os.getenv("LANG")[:5]
print(linguagem_atual)

if linguagem_atual == "pt_BR":
    msg = "Olá mundo"
else:
    msg = "Hello world"
print(msg)
