import os
import shutil


def criar_pasta(nome):
	if not os.path.exists(nome):
		os.makedirs(nome)
		print(f"📁 Pasta '{nome}' criada.")
	else:
		print(f"ℹ️ Pasta '{nome}' já existe.")

def mover_verilog(origem='.', destino='src'):
	arquivos = [f for f in os.listdir(origem) if f.endswith('.v')]
	if not arquivos:
		print("⚠️ Nenhum arquivo .v encontrado.")
	for arquivo in arquivos:
		shutil.move(os.path.join(origem, arquivo), os.path.join(destino, arquivo))
		print(f"✅ {arquivo} movido para {destino}/")

print("🚀 Iniciando configuração do ambiente...")

criar_pasta('src')
criar_pasta('sim')
mover_verilog()

print("🎉 Ambiente pronto!")
