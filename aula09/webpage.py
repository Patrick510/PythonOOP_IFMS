from urllib.request import urlopen
import time

class PaginaWeb:
    def __init__(self, url, cache_timeout=60):
        self.url = url
        self._conteudo = None
        self._cache_timeout = cache_timeout
        self._ultimo_carregamento = None

    @property
    def conteudo(self):
        if not self._conteudo or self._cache_expirado():
            print("Obtendo Nova Página...")
            self._conteudo = urlopen(self.url).read()
            self._ultimo_carregamento = time.time()
        return self._conteudo

    def _cache_expirado(self):  
        if self._ultimo_carregamento is None:
            return True
        tempo_atual = time.time()
        tempo_decorrido = tempo_atual - self._ultimo_carregamento
        return tempo_decorrido > self._cache_timeout

url = "https://sqliteonline.com/"
pagina_web = PaginaWeb(url, cache_timeout=60)

print(pagina_web.conteudo)
print(pagina_web._ultimo_carregamento)
