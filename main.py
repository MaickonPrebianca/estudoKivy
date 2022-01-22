from kivy.app import App
from kivy.lang import Builder


GUI = Builder.load_file("tela.kv")


class CotacaoMoedas(App):
    def build(self):
        return GUI

    def on_start(self):
        self.root.isd['moeda1'].text = f'Dólar para R${self.pegar_cotacao("USD")}'
        self.root.isd['moeda2'].text = f'Euro para R${self.pegar_cotacao("EUR")}'
        self.root.isd['moeda3'].text = f'Bitcoin para R${self.pegar_cotacao("BTC")}'
        self.root.isd['moeda4'].text = f'Ethereum para R${self.pegar_cotacao("ETH")}'

        #return super().on_start()
    
    def pegar_cotacao(self, moeda):
        link = f'https://economia.awesomeapi.com.br/last/{moeda}-BRL'
        requisicao = requests.get(link)
        dic_requisicao = requisicao.json()
        cotacao = dic_requisicao[f'{moeda}BRL']['bid']
        return cotacao
        
CotacaoMoedas().run()