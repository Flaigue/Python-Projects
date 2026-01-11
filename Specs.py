import platform
import os

os.system("clear")

DE = os.environ.get("XDG_CURRENT_DESKTOP")
with open("/etc/os-release", "r") as ficheiro:
    for line in ficheiro:
        if "PRETTY_NAME" in line:
            system = line.replace('"', "")
            system = system.replace("PRETTY_NAME=", "")
        if "VERSION_CODENAME" in line:
            codename = line.replace("VERSION_CODENAME=", "")
print("Generic OS Name:",platform.system(),platform.release())
print(f"System: {system}", end="")
print(f"Desktop Environment: {DE}")
print(f"CodeName Version: {codename.capitalize()}")
print("CPU Arquitecture:",platform.processor())

modelcpu = ""
with open("/proc/cpuinfo", "r") as specs_cpu:
    for line in specs_cpu:
        if "model name" in line:
            part_model, part_freq = line.split("@")
            part_model = part_model.replace("model name	:", "").replace("(R)", "").replace("CPU", "")
            part_model = part_model.split().strip()
            part_model = " ".join(part_model)
print(f"CPU Model: {part_model}")
print(f"CPU Frequency: {part_freq.strip()}")

#Colocar Specs CPU, GPU, RAM e Armazenamento como as specs principais dos PC
#Specs do OS, CPU mais especificamente o modelo da CPU, arquitetura e Frequencia foi concluido
