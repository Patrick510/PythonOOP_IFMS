
import time
from urllib.request import urlopen

class PaginaWeb:
  def __init__(self, url, chache_timeout = 60):
    self.url = url
    self._conteudo = None
    self._cache_timeout = chache_timeout
    self._ultimo_carregamento = None

  @property
  def conteudo(self):
    if not self._conteudo or self._cache_expirado():
      print("Obtendo nova página...")
      self._conteudo = urlopen(self.url).read()
      self._ultimo_carregamento = time.time()
    return self._conteudo

  def _cache_expirado(self):
    if self._ultimo_carregamento is None:
      return True
    tempo_atual = time.time()
    tempo_decorrido = tempo_atual - self._ultimo_carregamento
    return tempo_decorrido > self._cache_timeout

url = "https://google.com/"
pagina = PaginaWeb(url, chache_timeout=60)

print(pagina.conteudo)
print(pagina._ultimo_carregamento)