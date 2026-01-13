import platform          # Biblioteca para obter informações do sistema (OS, CPU, arquitetura, etc.)
import os                # Biblioteca para interagir com o sistema operativo (variáveis, comandos, etc.)
import subprocess        # Biblioteca para executar comandos do terminal e capturar a saída

os.system("clear")       # Limpa o terminal (equivalente ao comando 'clear' no Linux)

DE = os.environ.get("XDG_CURRENT_DESKTOP")  
# Pega da variável de ambiente de qual é o Desktop Environment atual (XFCE, Cinnamon, KDE, etc.)

with open("/etc/os-release", "r") as ficheiro:   # Abre o ficheiro que contém informações do sistema Linux
    for line in ficheiro:                        # Lê linha por linha
        if "PRETTY_NAME" in line:                # Quando encontrar a linha com o nome completo do sistema
            system = line.replace('"', "")       # Remove aspas
            system = system.replace("PRETTY_NAME=", "")  # Remove o prefixo e deixa só o nome do sistema
        if "VERSION_CODENAME" in line:           # Quando encontrar o codename da versão
            codename = line.replace("VERSION_CODENAME=", "")  # Remove o prefixo e deixa só o codename

print("Generic OS Name:", platform.system(), platform.release())
# Mostra o nome genérico do OS (Linux) e a versão do kernel

print(f"System: {system}", end="")  
# Mostra o nome completo do sistema (ex: Linux Mint 21.3)
# end="" evita quebrar a linha aqui

print(f"Desktop Environment: {DE}")  
# Mostra o ambiente gráfico atual (XFCE, Cinnamon, etc.)

print(f"CodeName Version: {codename.capitalize()}")  
# Mostra o codename da versão (ex: 'virginia'), com a primeira letra maiúscula

print("CPU Arquitecture:", platform.processor())  
# Mostra a arquitetura da CPU (ex: x86_64 ou o nome do processador)

count = 0               # Variável usada para garantir que só apanhas a primeira ocorrência de cache size
modelcpu = ""           # Variável não usada, mas deixada aqui (não faz mal)

with open("/proc/cpuinfo", "r") as specs_cpu:   # Abre o ficheiro com informações detalhadas da CPU
    for line in specs_cpu:                      # Lê linha por linha

        if "model name" in line:                # Quando encontrar a linha com o modelo da CPU
            part_model, part_freq = line.split("@")  
            # Divide a linha em duas partes: antes do @ (modelo) e depois do @ (frequência)

            part_model = part_model.replace("model name :", "").replace("(R)", "").replace("CPU", "")
            # Limpa texto inútil: remove 'model name:', remove '(R)', remove 'CPU'

            part_model = part_model.strip().split()
            # Remove espaços extras e divide em palavras separadas

            part_model = " ".join(part_model)
            # Junta tudo de novo com um único espaço entre palavras (fica mais limpo)

        if "cache size" in line:                # Quando encontrar a linha do cache
            if count == 0:                      # Só apanha a primeira vez que aparece
                cache_cpu = line                # Guarda a linha inteira
                cache_cpu = cache_cpu.split(":")  # Divide em ['cache size', ' valor']
            else:
                pass
            count += 1                          # Marca que já apanhaste uma vez

        count = 0                               # Reinicia o contador (faz com que apanhes sempre a primeira linha)

        if "cpu cores" in line:                 # Quando encontrar a linha com o número de cores
            if count == 0:                      # Só apanha a primeira ocorrência
                cpu_cores = line                # Guarda a linha
                cpu_cores = cpu_cores.split(":")  # Divide em ['cpu cores', ' valor']
            else:
                pass

print(f"Processor Model (CPU): {part_model}")  
# Mostra o modelo da CPU já limpo

print(f"CPU Frequency: {part_freq.strip()}")  
# Mostra a frequência da CPU (parte depois do @)

print(f"CPU Cache: {cache_cpu[-1].strip()}")  
# Mostra o valor do cache (último elemento da lista)

print(f"CPU Cores: {cpu_cores[-1].strip()}")  
# Mostra o número de cores (último elemento da lista)

gpu = subprocess.run("lspci | grep -i vga", shell=True, capture_output=True)
# Executa o comando 'lspci' filtrado por 'vga' e captura a saída

gpu = gpu.stdout.decode("utf-8")
# Converte os bytes capturados para string normal

gpu = gpu.rsplit(":", 1)
# Divide a string no último ':' → devolve lista com 2 partes

gpu = gpu[1]
# Fica só com a parte da direita (onde está o nome da GPU)

gpu = gpu.split("(")[0].strip()
# Divide no '(' e apanha só a parte antes → remove '(rev 0e)' ou qualquer revisão
# strip() remove espaços extras

print(f"Grafics Card Model (GPU): {gpu}")
# Mostra o nome final da GPU já limpo

#Colocar Specs CPU, GPU, RAM e Armazenamento como as specs principais dos PC
#Specs do OS, CPU mais especificamente o modelo da CPU, arquitetura e Frequencia foi concluido
