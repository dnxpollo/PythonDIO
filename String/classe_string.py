# metodos

# Maiuscula | Minuscula | Inicial Maiuscula
curso = "python"
print(curso.upper())

print(curso.lower())

print(curso.title())

# Retira espaços em branco do inicio e do fim do texto
texto = "   Olá Mundo   "

print(texto)
print(texto.strip())
print(texto.lstrip())
print(texto.rstrip())

# Centraliza,
# primeiro parametro é obrigatório indicando a largura
# segundo parametro é opcional podendo ser um caractere especial

print(curso.center(10, "#"))

# Juntaiterável 
print(".".join(curso))
