import platform          # Library to obtain system information (OS, CPU, architecture, etc.)
import os                # Library to interact with the operating system (variables, commands, etc.)
import subprocess        # Library to execute terminal commands and capture output
import psutil

os.system("clear")       # Clears the terminal (equivalent to the 'clear' command in Linux)

# Gets the current Desktop Environment from environment variables (XFCE, Cinnamon, KDE, etc.)
desktop_env = os.environ.get("XDG_CURRENT_DESKTOP")  

# Opens the file containing Linux system information
with open("/etc/os-release", "r") as system_file:   
    for line in system_file:                     # Read line by line
        if "PRETTY_NAME" in line:                # Find the line with the full system name
            system_name = line.replace('"', "")  # Remove quotes
            system_name = system_name.replace("PRETTY_NAME=", "")  # Remove prefix to keep only the name
        if "VERSION_CODENAME" in line:           # Find the version codename
            codename = line.replace("VERSION_CODENAME=", "")  # Remove prefix to keep only the codename

print("Generic OS Name:", platform.system(), platform.release())
# Displays generic OS name (Linux) and kernel version

print(f"System: {system_name}", end="")  
# Displays full system name (e.g., Linux Mint 21.3)
# end="" avoids an unnecessary newline here

print(f"Desktop Environment: {desktop_env}")  
# Displays the current graphical environment (XFCE, Cinnamon, etc.)

print(f"CodeName Version: {codename.capitalize()}")  
# Displays version codename (e.g., 'virginia') with the first letter capitalized

print("CPU Architecture:", platform.processor())  
# Displays CPU architecture (e.g., x86_64 or processor name)

occurrence_count = 0     # Variable used to ensure only the first occurrence of cache size is captured
cpu_model_placeholder = "" # Unused variable, left as a placeholder

# Opens the file with detailed CPU information
with open("/proc/cpuinfo", "r") as cpu_specs_file:   
    for line in cpu_specs_file:                  # Read line by line

        if "model name" in line:                 # Find the line with the CPU model
            part_model, part_freq = line.split("@")  
            # Split the line into two parts: before @ (model) and after @ (frequency)

            part_model = part_model.replace("model name", "").replace(":", "").replace("(R)", "").replace("CPU", "")
            # Clean up text: remove 'model name:', ':', '(R)', and 'CPU'

            part_model = part_model.strip().split()
            # Remove extra spaces and split into separate words

            part_model = " ".join(part_model)
            # Rejoin with a single space between words for a cleaner output

        if "cache size" in line:                 # Find the cache size line
            if occurrence_count == 0:            # Only capture the first occurrence
                cpu_cache = line                 # Save the whole line
                cpu_cache = cpu_cache.split(":") # Split into ['cache size', ' value']
            else:
                pass
            occurrence_count += 1                # Mark that the first occurrence was captured

        occurrence_count = 0                     # Reset counter

        if "cpu cores" in line:                  # Find the line with the number of cores
            if occurrence_count == 0:            # Capture only the first occurrence
                cpu_cores = line                 # Save the line
                cpu_cores = cpu_cores.split(":") # Split into ['cpu cores', ' value']
            else:
                pass

print(f"Processor Model (CPU): {part_model}")  
# Displays cleaned CPU model

print(f"CPU Frequency: {part_freq.strip()}")  
# Displays CPU frequency (part after the @)

print(f"CPU Cache: {cpu_cache[-1].strip()}")  
# Displays cache value (last element of the list)

print(f"CPU Cores: {cpu_cores[-1].strip()}")  
# Displays number of cores (last element of the list)

print("CPU usage (%):", psutil.cpu_percent(interval=1))

# Execute 'lspci' filtered by 'vga' and capture output
gpu_info = subprocess.run("lspci | grep -i vga", shell=True, capture_output=True)

# Decode captured bytes to a standard string
gpu_info = gpu_info.stdout.decode("utf-8")

# Split string at the last ':' -> returns a list with 2 parts
gpu_info = gpu_info.rsplit(":", 1)

# Keep the right part (where the GPU name is)
gpu_name = gpu_info[1]

# Split at '(' and take the part before to remove revisions like '(rev 0e)'
gpu_name = gpu_name.split("(")[0]

# Clean specific strings and remove extra spaces
gpu_name = gpu_name.replace("Graphics & Display", "").strip()

print("")
print(f"Graphics Card (GPU): {gpu_name}")
# Displays final cleaned GPU name

print("")
ram = psutil.virtual_memory()
print("Total Memory:", round(ram.total / 1e9, 2), "GB")
print("Used Memory:", round(ram.used / 1e9, 2), "GB")
print("Available Memory:", round(ram.available / 1e9, 2), "GB")
print("Free Memory:", round(ram.free / 1e9, 2), "GB")
print("RAM usage:", ram.percent, "%")
