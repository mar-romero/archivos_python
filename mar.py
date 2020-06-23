def menu():
    print('Categorias analizar')
    print('1) MPRO')
    print('2) M45-49')
    print('3) M25-29')
    print('4) M18-24')
    
    while True: 
        try: 
            cat = int(input('Ingrese la categoria analizar: '))
            if cat == 1 :
                categoria = "MPRO"
                print('Eligio categoria: ', cat,') MPRO',sep="")
                return categoria
                break
            elif cat == 2 :
                categoria = 'M45-49'
                print('Eligio categoria: ', cat,') M45-49',sep="")
                return categoria
                break
            elif cat == 3 :
                categoria = 'M25-29'
                print('Eligio categoria: ', cat,') M25-29',sep="")
                return categoria
                break
            elif cat == 4 :
                categoria = 'M18-24'
                print('Eligio categoria: ', cat,') M18-24',sep="")
                return categoria
                break
            else:
                print(cat,'No es una categoria')
        except ValueError:
            print('No es una categoria')
