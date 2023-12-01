from urllib.request import urlopen
import time

class PaginaWeb:
    def __init__(self, url):
        self.url = url
        self._conteudo = None
        self._ultimo_carregamento = None

    @property
    def conteudo(self):
        if not self._conteudo or self._cache_expirado():
            print("Obtendo Nova Página...")
            self._conteudo = urlopen(self.url).read()
            self._ultimo_carregamento = time.time()
        return self._conteudo

    def _cache_expirado(self):  
        return self._ultimo_carregamento is None or time.time() - self._ultimo_carregamento > 60

    def diferenca_tempo(self):
        if self._ultimo_carregamento is None:
            return "Nenhum conteúdo carregado ainda."
        return f"Diferença de tempo: {time.time() - self._ultimo_carregamento} segundos."

url = "https://ead.ifms.edu.br/course/view.php?id=34005"
pagina_web = PaginaWeb(url)

for _ in range(5):
    print(pagina_web.conteudo)

print(pagina_web.diferenca_tempo())
