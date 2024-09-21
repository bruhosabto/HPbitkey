
class Stocked:
    def __init__(self):
        self.__lista_chave_publica = [
            "633cbe3ec02b9401c5effa144c5b4d22f87940259634858fc7e59b1c09937852",#0 130
	        "145d2611c823a396ef6712ce0f712f09b9b4f3135e3e0aa3230fb9b6d08d1e16",#1 135
	        "1f6a332d3c5c4f2de2378c012f429cd109ba07d69690c6c701b6bb87860d6640",#2 140
	        "afdda497369e219a2c1c369954a930e4d3740968e5e4352475bcffce3140dae5",#3 145
	        "137807790ea7dc6e97901c2bc87411f45ed74a5629315c4e4b03a0a102250c49",#4 150
	        "5cd1854cae45391ca4ec428cc7e6c7d9984424b954209a8eea197b9e364c05f6",#5 155
	        "e0a8b039282faf6fe0fd769cfbc4b6b4cf8758ba68220eac420e32b91ddfa673"#6 160
        ]
        self.__lista_numeros = [ 130,135,140,145,150,155,160]
    def getPublic_key(self, valor):

        if valor in self.__lista_numeros:
                return self.__lista_chave_publica[self.__lista_numeros.index(valor)]
        else:
                return None
    def getRanger(self,valor):
        if valor in self.__lista_numeros:
            return 2**(valor-1),2**(valor) # retorna o intervalo
        else:
             return None,None
