"""
3 - O método process_files da classe ScaleZip chumbou no código uma resolução fixa de 640x480, o que não é tão interessante. Proponha uma solução em que os novos valores de resolução não estejam chumbados.
"""

import sys
import shutil
import zipfile
from pathlib import Path
from PIL import Image
from abc import ABC, abstractmethod

class ProcessadorZip:
    def __init__(self, nome_zip):
        self.nome_zip = nome_zip
        self.diretorio_temporario = Path(f"descompactado-{nome_zip[:-4]}")

    def processar_zip(self):
        self.descompactar_arquivos()
        self.processar_arquivos()
        self.compactar_arquivos()

    def descompactar_arquivos(self):
        self.diretorio_temporario.mkdir()
        arquivo_zip = zipfile.ZipFile(self.nome_zip)
        arquivo_zip.extractall(self.diretorio_temporario)
        arquivo_zip.close()

    def compactar_arquivos(self):
        arquivo_zip = zipfile.ZipFile(self.nome_zip, "w")
        for nome_arquivo in self.diretorio_temporario.iterdir():
            arquivo_zip.write(nome_arquivo, nome_arquivo.name)
        arquivo_zip.close()
        shutil.rmtree(self.diretorio_temporario)

class SubstituirZip(ProcessadorZip):
    def __init__(self, nome_arquivo, string_busca, string_substituir):
        super().__init__(nome_arquivo)
        self.string_busca = string_busca
        self.string_substituir = string_substituir

    def processar_arquivos(self):
        """Realizar busca e substituição em todos os arquivos no
        diretório temporário"""
        for nome_arquivo in self.diretorio_temporario.iterdir():
            with nome_arquivo.open() as arquivo:
                conteudo = arquivo.read()

            conteudo = conteudo.replace(self.string_busca, self.string_substituir)

            with nome_arquivo.open("w") as arquivo:
                arquivo.write(conteudo)

class RedimensionarZip(ProcessadorZip):
    def processar_arquivos(self, largura, altura):
        """Redimensionar cada imagem no diretório para as dimensões especificadas"""
        for nome_arquivo in self.diretorio_temporario.iterdir():
            im = Image.open(str(nome_arquivo))
            redimensionada = im.resize((largura, altura))
            redimensionada.save(nome_arquivo)
            im.close()
            redimensionada.close()

if __name__ == "__main__":
    # Exemplo de Uso
    processador_zip = ProcessadorZip("exemplo.zip")
    processador_zip.processar_zip()

    substituir_zip = SubstituirZip("exemplo_substituir.zip", "string_antiga", "string_nova")
    substituir_zip.processar_zip()

    redimensionar_zip = RedimensionarZip("exemplo_redimensionar.zip")
    redimensionar_zip.processar_arquivos(800, 600)  # Especificando largura e altura desejadas