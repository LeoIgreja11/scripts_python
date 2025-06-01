# Library
import os


# Variables
base_dir = "home/leolinux/projetos/rt1"
verilog_files = []

# Walk the files in the actual directory
for root, dir, files in os.walk(base_dir):
	for file in files:
		if file.endswith(".v"):
			verilog_files.append(os.path.join(root,files))

# Write files in the list
with open("verilog_list.txt", "w") as f:
	for filepath in verilog_files:
		f.write(filepath + "\n")

# Write the number of files in the Linux terminal
print(f"Total de arquivos encontrados: {len(verilog_files)}")
for f in verilog_files:
	print(f)
