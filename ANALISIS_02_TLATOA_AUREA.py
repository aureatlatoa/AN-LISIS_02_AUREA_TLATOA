#Importación de la base de datos
from csv import reader
#Lista donde se guardan los datos
list_master = []

#Dividir y separar filas y columnas:
def Convert(string):
    li = list(string.split("\t"))
    return li

def SumarExportacionesPorPais(pais, lista):
    ##print("Iniciando funcion:")
    ##print("\n")
    #saber si mi fila es del pais que quiero
    fila = 0
    suma = 0
    while fila < (len(lista) - 1):
        fila = fila + 1
        #texto_consultado=lista[fila][2]
        #print(texto_consultado)
        #print("\n")
        if lista[fila][2] == pais:
            total_value_indice = 9
            ##print(lista[fila][total_value_indice])
            ##print("\n")
            total_value = lista[fila][total_value_indice]
            total_value_tipo_entero = int(total_value)
            ##print(total_value_tipo_entero)
            ##print("\n")
            suma = suma + total_value_tipo_entero
            ##print(suma)
    return suma

##### IMPORTACIONES ######
def SumarImortsPorPais(pais, lista):
    ##print("Iniciando funcion:")
    ##print("\n")
    #saber si mi fila es del pais que quiero
    fila = 0
    suma_imp = 0
    while fila < (len(lista) - 1):
        fila = fila + 1
        #texto_consultado=lista[fila][3]
        #print(texto_consultado)
        #print("\n")
        if lista[fila][3] == pais:
            total_value_indice = 9
            ##print(lista[fila][total_value_indice])
            ##print("\n")
            total_value = lista[fila][total_value_indice]
            total_value_tipo_entero = int(total_value)
            ##print(total_value_tipo_entero)
            ##print("\n")
            suma_imp = suma_imp + total_value_tipo_entero
            ##print(suma)
    return suma_imp

# read csv file as a list of lists
with open('synergy_logistics_database.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    # Pass reader object to list() to get a list of lists
    list_of_rows = list(csv_reader)

#print("Lista de filas: ", list_of_rows)

#print("\n")

for línea in list_of_rows:
    nueva_lista = Convert(línea[0])
    list_master.append(nueva_lista)

i=0
while i< (len(list_master) -1 ):
    i=i+1
    print("\n")
    print (list_master[i])

fila=0
while fila< (len(list_master) -1):
    fila=fila+1
    columna=0
    while columna<9:
        columna=columna+1
        print("\n")
        print (list_master[fila][columna])
### Sumas por país ####

suma_austria = SumarExportacionesPorPais("Austria", list_master)
suma_australia = SumarExportacionesPorPais("Australia", list_master)
suma_belg = SumarExportacionesPorPais("Belgium", list_master)
suma_brasil = SumarExportacionesPorPais("Brazil", list_master)
suma_canada = SumarExportacionesPorPais("Canada", list_master)
suma_china = SumarExportacionesPorPais("China", list_master)
suma_francia = SumarExportacionesPorPais("France", list_master)
suma_alema = SumarExportacionesPorPais("Germany", list_master)
suma_india = SumarExportacionesPorPais("India", list_master)
suma_italia = SumarExportacionesPorPais("Italy", list_master)
suma_japon = SumarExportacionesPorPais("Japan", list_master)
suma_paibaj = SumarExportacionesPorPais("Netherlands", list_master)
suma_rusia = SumarExportacionesPorPais("Russia", list_master)
suma_singapur = SumarExportacionesPorPais("Singapore", list_master)
suma_corea_del_sur = SumarExportacionesPorPais("South Korea", list_master)
suma_españa = SumarExportacionesPorPais("Spain", list_master)
suma_suiza = SumarExportacionesPorPais("Switzerland", list_master)
suma_reinounid = SumarExportacionesPorPais("United Kingdom", list_master)
suma_eu = SumarExportacionesPorPais("USA", list_master)
"""
print(suma_japon)
print(suma_austria)
print(suma_australia)
print(suma_belg)
print(suma_brasil)
print(suma_canada)
print(suma_china)
print(suma_francia)
print(suma_alema)
print(suma_india)
print(suma_italia)
print(suma_paibaj)
print(suma_rusia)
print(suma_singapur)
print(suma_corea_del_sur)
print(suma_españa)
print(suma_suiza)
print(suma_reinounid)
print(suma_eu)
"""
#### importaciones ####

suma_imp_can = SumarImortsPorPais("Canada", list_master)
suma_imp_chin = SumarImortsPorPais("China", list_master)
suma_imp_alem = SumarImortsPorPais("Germany", list_master)
suma_imp_india = SumarImortsPorPais("India", list_master)
suma_imp_jap = SumarImortsPorPais("Japan", list_master)
suma_imp_mex = SumarImortsPorPais("Mexico", list_master)
suma_imp_poland = SumarImortsPorPais("Poland", list_master)
suma_imp_singapur = SumarImortsPorPais("Singapore", list_master)
suma_imp_tailand = SumarImortsPorPais("Thailand", list_master)
suma_imp_emirates = SumarImortsPorPais("United Arab Emirates", list_master)
suma_imp_usa = SumarImortsPorPais("USA", list_master)
"""
print(suma_imp_can)
print(suma_imp_chin)
print(suma_imp_alem)
print(suma_imp_india)
print(suma_imp_jap)
print(suma_imp_mex)
print(suma_imp_poland)
print(suma_imp_singapur)
print(suma_imp_tailand)
print(suma_imp_emirates)
print(suma_imp_usa)
"""
print("esto termino :v")

Total_expo= 160163298000

##############################
#Porcentajes_exportaciones


porcentaje_paísjap= round(suma_japon/Total_expo, 3)
porcentaje_paísaustria= round(suma_austria/Total_expo, 3)
porcentaje_paísaustralia= round(suma_australia/Total_expo, 3)
porcentaje_paísbel= round(suma_belg/Total_expo, 3)
porcentaje_paísbrasil= round(suma_brasil/Total_expo, 3)
porcentaje_paíscanada= round(suma_canada/Total_expo, 3)
porcentaje_paíschina= round(suma_china/Total_expo, 3)
porcentaje_paísfrancia= round(suma_francia/Total_expo, 3)
porcentaje_paísalema= round(suma_alema/Total_expo, 3)
porcentaje_paísindia= round(suma_india/Total_expo, 3)
porcentaje_paísitalia= round(suma_italia/Total_expo, 3)
porcentaje_paísbaj= round(suma_paibaj/Total_expo, 3)
porcentaje_paísrusia= round(suma_rusia/Total_expo, 3)
porcentaje_paíssingapur= round(suma_singapur/Total_expo, 3)
porcentaje_paíscorea= round(suma_corea_del_sur/Total_expo, 3)
porcentaje_paísespaña= round(suma_españa/Total_expo, 3)
porcentaje_paíssuiza= round(suma_suiza/Total_expo, 3)
porcentaje_paísreinouni= round(suma_reinounid/Total_expo, 3)
porcentaje_paíseu= round(suma_eu/Total_expo, 3)

print("Exportaciones de EU: ", porcentaje_paíseu)
print("Exportaciones de Reino Unido: ", porcentaje_paísreinouni)
print("Exportaciones de Suiza: ",porcentaje_paíssuiza)
print("Exportaciones de España: ", porcentaje_paísespaña)
print("Exportaciones de Corea: ", porcentaje_paíscorea)
print("Exportaciones de Singapur: ", porcentaje_paíssingapur)
print("Exportaciones de Rusia: ", porcentaje_paísrusia)
print("Exportaciones de Paises Bajos: ", porcentaje_paísbaj)
print("Exportaciones de Italia: ", porcentaje_paísitalia)
print("Exportaciones de India: ", porcentaje_paísindia)
print("Exportaciones de Alemania: ", porcentaje_paísalema)
print("Exportaciones de Francia: ", porcentaje_paísfrancia)
print("Exportaciones de China",porcentaje_paíschina)
print("Exportaciones de Canadá: ", porcentaje_paíscanada)
print("Exportaciones de Brasil: ",porcentaje_paísbrasil)
print("Exportaciones de Belgica: ", porcentaje_paísbel)
print("Exportaciones de Austraia: ", porcentaje_paísaustralia)
print("Exportaciones de Austria: ",porcentaje_paísaustria)
print("Exportaciones de japon: ", porcentaje_paísjap)

##############################
#Porcentajes_importaciones
Total_impo= 55528000000



porcentaje_imp_paíscan= round(suma_imp_can/Total_impo, 3)
porcentaje_imp_paíschina= round(suma_imp_chin/Total_impo, 3)
porcentaje_imp_paísaleman= round(suma_imp_alem/Total_impo, 3)
porcentaje_imp_paísindia= round(suma_imp_india/Total_impo, 3)
porcentaje_imp_paísJapon= round(suma_imp_jap/Total_impo, 3)
porcentaje_imp_paísMexico= round(suma_imp_mex/Total_impo, 3)
porcentaje_imp_paísPoland= round(suma_imp_poland/Total_impo, 3)
porcentaje_imp_paísSingapur= round(suma_imp_singapur/Total_impo, 3)
porcentaje_imp_paísTailand= round(suma_imp_tailand/Total_impo, 3)
porcentaje_imp_paísEmiratos= round(suma_imp_emirates/Total_impo, 3)
porcentaje_imp_paísUsa= round(suma_imp_usa/Total_impo, 3)

print("El porcentaje de importacion en canadá es: ",porcentaje_imp_paíscan)
print("El porcentaje de imp en china es: ", porcentaje_imp_paíschina)
print("El porcentaje de imp en Alemania es: ", porcentaje_imp_paísaleman)
print("El porcentaje de imp en India es: ", porcentaje_imp_paísindia)
print("El porcntaje de imp en Japón es: ", porcentaje_imp_paísJapon)
print("El porcentaje de imp en México es: ", porcentaje_imp_paísMexico)
print("El porcentaje de imp en Polonia es: ", porcentaje_imp_paísPoland)
print("El porcentaje de imp en Singapur es: ", porcentaje_imp_paísSingapur)
print("El porcentaje de imp en Tailandia es: ", porcentaje_imp_paísTailand)
print("El porcentaje de imp en Emiratos es: ", porcentaje_imp_paísEmiratos)
print("El porcentaje de imp en Usa es: ", porcentaje_imp_paísUsa)