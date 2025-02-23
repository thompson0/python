from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato


restaurante_praca = Restaurante('praça','Gourmet')
bebida_suco = Bebida('suco de melancia', 5.0 , 'grande')
bebida_suco.aplicar_desconto()
prato_paozinho = Prato('Paozinho', 2.0 , 'O melhor da cidade')
prato_paozinho.aplicar_desconto()
restaurante_praca.adiconar_no_cardapio(bebida_suco)
restaurante_praca.adiconar_no_cardapio(prato_paozinho)

def main():
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()