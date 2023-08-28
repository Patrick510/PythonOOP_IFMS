last_id = 0

class Tarefa:

  def __init__(self,id ,titulo ,prioridade ,descricao ,concluida = None):

    self.id = id
    self.titulo = titulo
    self.prioridade = prioridade
    self.concluida = concluida
    self.descricao = descricao
    global last_id
    last_id += 1
    self.id = last_id

  def simples(self):
    return f"{self.id} : {self.titulo}"

  def detalhada(self):
    return self.id+self.titulo+self.descricao+self.prioridade+self.concluida

  def __lt__(self,other):
    if self.prioridade<other.prioridade:
      return True


class Lista:
  def __init__(self):
    self.tarefas = []

  def adicionar_tarefa(self,tarefa):
    self.tarefa.append(tarefa)

  def remover_tarefa(self,id):
    self.tarefas = [t for t in self.tarefas if t.id != id]

  def editar_tarefa(self, id, titulo, descricao, prioridade, concluida = None):
    for t in self.tarefas:
        if t.id==id:
          if self.titulo != None:
            t.titulo = None

  def obter_tarefa(self, filtro=None, nao_concluidas=None):
    self.tarefas = sorted(self.tarefas,reverse=True)

    if nao_concluidas == True: 
      tarefas=[t for t in tarefas if t.concluida !=True]