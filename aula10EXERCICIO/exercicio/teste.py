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
        if self._ultimo_carregamento is None:
            return True  # O cache é considerado expirado se nunca foi carregado
        tempo_atual = time.time()
        tempo_decorrido = tempo_atual - self._ultimo_carregamento
        tempo_expiracao_cache_segundos = 60  # Você pode definir o tempo de expiração do cache aqui (em segundos)
        return tempo_decorrido > tempo_expiracao_cache_segundos

    def diferenca_tempo(self):
        if self._ultimo_carregamento is None:
            return "Nenhum conteúdo carregado ainda."
        tempo_atual = time.time()
        tempo_decorrido = tempo_atual - self._ultimo_carregamento
        return f"Diferença de tempo: {tempo_decorrido} segundos."

# Exemplo de Uso:
url = "https://ead.ifms.edu.br/course/view.php?id=34005"
pagina_web = PaginaWeb(url)

# Solicite o conteúdo da página várias vezes e observe o recarregamento após o período de expiração
for _ in range(5):
    print(pagina_web.conteudo)

# Calcule e imprima a diferença entre as datas (timestamps)
print(pagina_web.diferenca_tempo())
