"""
2 - Modifique o ZipProcessor para descompactar recursivamente a pasta selecionada.
"""

import os
import sys
import shutil
import zipfile
from pathlib import Path
from PIL import Image
from abc import ABC, abstractmethod

class ZipProcessor:
    def __init__(self, nome_do_zip):
        self.nome_do_zip = nome_do_zip
        self.diretorio_temporario = Path(f"descompactado-{nome_do_zip[:-4]}")

    def processar_zip(self):
        self.descompactar_arquivos()
        self.processar_arquivos()
        self.compactar_arquivos()

    def descompactar_arquivos(self):
        self.diretorio_temporario.mkdir()
        arquivo_zip = zipfile.ZipFile(self.nome_do_zip)
        for membro in arquivo_zip.namelist():
            arquivo_zip.extract(membro, self.diretorio_temporario)
        arquivo_zip.close()

    def compactar_arquivos(self):
        arquivo_zip = zipfile.ZipFile(self.nome_do_zip, "w")
        for raiz, _, arquivos in os.walk(self.diretorio_temporario):
            for arquivo in arquivos:
                caminho_arquivo = Path(raiz) / arquivo
                nome_arquivo = caminho_arquivo.relative_to(self.diretorio_temporario)
                arquivo_zip.write(caminho_arquivo, nome_arquivo)
        arquivo_zip.close()
        shutil.rmtree(self.diretorio_temporario)

class ZipReplace(ZipProcessor):
    def __init__(self, nome_do_arquivo, string_de_busca, string_de_substituicao):
        super().__init__(nome_do_arquivo)
        self.string_de_busca = string_de_busca
        self.string_de_substituicao = string_de_substituicao

    def processar_arquivos(self):
        """realizar uma busca e substituição em todos os arquivos no
        diretório temporário"""
        for nome_arquivo in self.diretorio_temporario.iterdir():
            with nome_arquivo.open() as arquivo:
                conteudo = arquivo.read()

            conteudo = conteudo.replace(self.string_de_busca, self.string_de_substituicao)

            with nome_arquivo.open("w") as arquivo:
                arquivo.write(conteudo)

class ScaleZip(ZipProcessor):
    def processar_arquivos(self):
        """Redimensionar cada imagem no diretório para 640x480"""
        for nome_arquivo in self.diretorio_temporario.iterdir():
            im = Image.open(str(nome_arquivo))
            redimensionada = im.resize((640, 480))
            redimensionada.save(nome_arquivo)
            im.close()
            redimensionada.close()

if __name__ == "__main__":
    # Exemplo de Uso
    zip_processor = ZipProcessor("exemplo.zip")
    zip_processor.processar_zip()

    zip_replace = ZipReplace("exemplo_substituir.zip", "antiga_string", "nova_string")
    zip_replace.processar_zip()

    scale_zip = ScaleZip("exemplo_redimensionar.zip")
    scale_zip.processar_zip()
