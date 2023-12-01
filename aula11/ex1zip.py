"""
1 - Torne ZipProcessor abstrata.
"""

import shutil
import zipfile
from pathlib import Path
from PIL import Image
from abc import ABC, abstractmethod

class ProcessadorZip(ABC):
    def __init__(self, nome_zip):
        self.nome_zip = nome_zip
        self.diretorio_temporario = Path(f"descompactado-{nome_zip[:-4]}")

    @abstractmethod
    def processar_arquivos(self):
        pass

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
        for nome_arquivo in self.diretorio_temporario.rglob('*'):
            arquivo_zip.write(nome_arquivo, nome_arquivo.relative_to(self.diretorio_temporario))
        arquivo_zip.close()
        shutil.rmtree(self.diretorio_temporario)