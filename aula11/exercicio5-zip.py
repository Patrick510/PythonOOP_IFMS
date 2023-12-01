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
    processador_zip = ProcessadorZip("exemplo.zip")
    processador_zip.processar_zip()

    substituir_zip = SubstituirZip("exemplo_substituir.zip", "string_antiga", "string_nova")
    substituir_zip.processar_zip()

    redimensionar_zip = RedimensionarZip("exemplo_redimensionar.zip")
    redimensionar_zip.processar_zip()

"""
5 - Resolvemos o problema de duplicação de código em ZipProcessor através de herança. Também é possível usar composição em vez de herança. Em vez de estender a classe nas classes ZipReplace e ScaleZip, você poderia passar instâncias dessas classes para o construtor do ZipProcessor e chamá-las para realizar a parte do processamento. Implemente isso.

Qual versão você acha mais fácil de usar? Qual é mais elegante? Qual é mais fácil de ler? Essas são perguntas subjetivas; a resposta varia para cada um de nós. No entanto, saber a resposta é importante. Se você perceber que prefere herança em vez de composição, é necessário prestar atenção para não abusar da herança em sua programação diária. Se você preferir composição, certifique-se de não perder oportunidades de criar uma solução elegante baseada em herança.
"""

class ZipProcessor(ABC):
    def __init__(self, zipname, *processors):
        self.zipname = zipname
        self.temp_directory = Path(f"unzipped-{zipname[:-4]}")
        self.processors = processors

    @abstractmethod
    def process_files(self):
        pass

    def process_zip(self):
        self.unzip_files()
        for processor in self.processors:
            processor.process_files()
        self.zip_files()

    # ... rest of the code ...

if __name__ == "__main__":
    # Example Usage with composition
    zip_processor = ZipProcessor("example.zip", ZipReplace("old_string", "new_string"), ScaleZip((800, 600)))
    zip_processor.process_zip()
