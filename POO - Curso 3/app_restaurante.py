from modelos.mod_restaurante import Restaurante
from modelos.cardapio.bebidas import Bebida
from modelos.cardapio.pratos import Prato

restaurante1 = Restaurante('Padoquinha', 'padaria')
bebida_suco = Bebida('Suco de Melancia', 5.00, '500 ml')
prato_salgado = Prato('Pão de queijo', 4.00,'Direto de minas')

prato_salgado.aplicar_desconto(5)

restaurante1.add_item_cardapio(prato_salgado)
restaurante1.add_item_cardapio(bebida_suco)

def main():
    restaurante1.show
    

if __name__ == '__main__':
    main()