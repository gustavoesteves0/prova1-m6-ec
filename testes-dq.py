from collections import deque

# Criação de um deque vazio
dq = deque()

# Adicionando elementos no final
dq.append('A')
dq.append('B')
dq.append('C')
print(f"Deque após append: {dq}")

# Adicionando elementos no início
dq.appendleft('X')
dq.appendleft('Y')
print(f"Deque após appendleft: {dq}")

# Removendo elementos do final
dq.pop()
print(f"Deque após pop: {dq}")

# Removendo elementos do início
dq.popleft()
print(f"Deque após popleft: {dq}")

# Rotacionando o deque
dq.rotate(-1)
print(f"Deque após rotate(-1): {dq}")

# Verificando o comprimento do deque
print(f"Tamanho do deque: {len(dq)}")