from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça','Gourmet')
#restaurante_mexicano = Restaurante('Mexican Food','Mexicana')
#restaurante_japones = Restaurante('Japa','Japones')
restaurante_praca.receber_avaliacao('Gui', 10)
restaurante_praca.receber_avaliacao('Lais', 8)



def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()