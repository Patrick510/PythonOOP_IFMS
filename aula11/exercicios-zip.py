import sys
import shutil
import zipfile
from pathlib import Path
from PIL import Image
from abc import ABC, abstractmethod

class ZipProcessor:
    def __init__(self, zipname):
        self.zipname = zipname
        self.temp_directory = Path(f"unzipped-{zipname[:-4]}")

    def process_zip(self):
        self.unzip_files()
        self.process_files()
        self.zip_files()

    def unzip_files(self):
        self.temp_directory.mkdir()
        zip_file = zipfile.ZipFile(self.zipname)
        zip_file.extractall(self.temp_directory)
        zip_file.close()

    def zip_files(self):
        zip_file = zipfile.ZipFile(self.zipname, "w")
        for filename in self.temp_directory.iterdir():
            zip_file.write(filename, filename.name)
        zip_file.close()
        shutil.rmtree(self.temp_directory)

class ZipReplace(ZipProcessor):
    def __init__(self, filename, search_string, replace_string):
        super().__init__(filename)
        self.search_string = search_string
        self.replace_string = replace_string

    def process_files(self):
        """perform a search and replace on all files in the
        temporary directory"""
        for filename in self.temp_directory.iterdir():
            with filename.open() as file:
                contents = file.read()

            contents = contents.replace(self.search_string, self.replace_string)

            with filename.open("w") as file:
                file.write(contents)

class ScaleZip(ZipProcessor):
    def process_files(self):
        """Scale each image in the directory to 640x480"""
        for filename in self.temp_directory.iterdir():
            im = Image.open(str(filename))
            scaled = im.resize((640, 480))
            scaled.save(filename)
            im.close()
            scaled.close()

if __name__ == "__main__":
    # Example Usage
    zip_processor = ZipProcessor("example.zip")
    zip_processor.process_zip()

    zip_replace = ZipReplace("example_replace.zip", "old_string", "new_string")
    zip_replace.process_zip()

    scale_zip = ScaleZip("example_scale.zip")
    scale_zip.process_zip()

"""
6 - Qual versão você acha mais fácil de usar? Qual é mais elegante? Qual é mais fácil de ler? Essas são perguntas subjetivas; a resposta varia para cada um de nós. No entanto, saber a resposta é importante. Se você perceber que prefere herança em vez de composição, é necessário prestar atenção para não abusar da herança em sua programação diária. Se você preferir composição, certifique-se de não perder oportunidades de criar uma solução elegante baseada em herança.
"""

class ScaleZip:
    def __init__(self, resolution):
        self.resolution = resolution

    def process_files(self, temp_directory):
        """Scale each image in the directory to the specified resolution"""
        for filename in temp_directory.iterdir():
            im = Image.open(str(filename))
            scaled = im.resize(self.resolution)
            scaled.save(filename)
            im.close()
            scaled.close()

class ZipProcessor:
    def __init__(self, zipname, *processors):
        self.zipname = zipname
        self.temp_directory = Path(f"unzipped-{zipname[:-4]}")
        self.processors = processors

    def process_zip(self):
        self.unzip_files()
        for processor in self.processors:
            processor.process_files(self.temp_directory)
        self.zip_files()
