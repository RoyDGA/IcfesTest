import pandas as pd

listest = [1,2,3,4,5,6]
estrato = 4
excel = pd.read_excel('data.xlsx')

if estrato in listest:
    print(f'Estrato dentro del rango({listest[estrato-1]})')
    excel = excel.sort_values('PUNT_GLOBAL', ascending=False) #Tabla descendente

    # excel[(excel['GENERO'] & (excel['Estrato']))]
    filterEst = excel['ESTRATO']==f'Estrato {estrato}'
    filterby = excel[filterEst] #Filtro por estrato

    countGen = filterby['GENERO'].value_counts() #Conteo por Genero
    depbypoint = excel[['DEPARTAMENTO', 'PUNT_GLOBAL']].head(10)
    depbypoint2 = excel['DEPARTAMENTO'].head(10)
    # print(excel[['DEPARTAMENTO', 'PUNT_GLOBAL']].head(10)) #Departamentos con mejor puntaje
    countGen = pd.DataFrame(countGen)
    print('Genero por estrato: ')
    print(countGen)
    print('____________________________________________________________________________________')
    depbypoint = pd.DataFrame(depbypoint)
    print('Mejores departamentos por puntaje: ')
    print(depbypoint)
    print('____________________________________________________________________________________')
    
    print("Diccionario final: ")
    print(f'{countGen.T.to_dict()},{depbypoint2.T.to_dict()}')
else:
    print(f'Estrato fuera de rango({estrato})')
    





    


          


