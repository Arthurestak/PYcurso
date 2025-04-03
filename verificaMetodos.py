def verificaAtributo(item,metodo):
    if hasattr(item, metodo):
        print(f'{type(item)} possui o metodo {metodo}!')
        
        try:
            print(getattr(item, metodo)())
        except:
            print('Não é possível prosseguir, mas existe este atributo!')
    
    else:
        print(f'{type(item)} não possui o metodo {metodo}!')




verificaAtributo('', 'upper')