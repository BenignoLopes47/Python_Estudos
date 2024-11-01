class Filme():
    def __init__(self, valor_do_titulo, descricao, arquivo_video):
        self.titulo = valor_do_titulo
        self.arquivo_video = arquivo_video
        self.descricao = descricao
        
    def assistir_filme(self):
        duracao = self.calcular_duracao_filme()
        print("Dar play no arquivo de video", self.arquivo_video, "do filme", self.titulo, "que tem", duracao, "minutos de duração")

    def calcular_duracao_filme(self):
        # varios comandos para calcular a duração do filme
        return 130

filme1 = Filme("Não olhe para cima","Filme de meteoros e fim do mundo", "nao_olhe_para_cima.mp4")
filme1.assistir_filme()
print(filme1.titulo)
print(filme1.descricao)