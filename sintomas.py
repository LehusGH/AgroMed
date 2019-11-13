#En este diccionario se guardan los sintomas necesarios para
#predecir alguna enfermedad o sacar la probabilidad de 
#tener alguna a partir de un conjunto de enfermedades
sintomas = {
	1: 'hojas con manchas amarillas/naranjas',
	2: 'caída de hojas',
	3: 'hongos en los suelos',
	4: 'manchas circulares color pardo claro',
	5: 'manchas circulares color marrón rojizo',
	6: 'amarillez de las hojas viejas',
	7: 'rajaduras en la base del pseudotallo',
	8: 'frutos de baja calidad',
	9: 'racimos de color negro',
	10: 'punta podrida de los platanos inmaduros',
	11: 'marchitamiento',
	12: 'amarillamiento de las plantas',
	13: 'hojas secas en los bordes',
	14: 'vasos conductores necrosados',
	15: 'venas color amarillo brillante',
	16: 'patrón moteado en hojas',
	17: 'hojas enrolladas',
	18: 'vainas no se expanden o se enrollan',
	19: 'baja producción de semillas',
	20: 'semillas de baja calidad',
	21: 'lesiones llenas de agua en la base del tallo',
	22: 'se marchita y pudre la parte superior de la planta',
	23: 'crece hongo blanco y algodonoso en las lesiones',
	24: 'se marchitan vainas, tallos y ramas',
	25: 'esporas de color rojizo',
	26: 'puntos negros ligeramente elevados en las hojas',
	27: 'granos chupados, flácidos y flojos en la mazorca',
	28: 'grandes áreas necróticas',
	29: 'color pajizo en las hojas',
	30: 'presencia de plantas con cogollos amarillos',
	31: 'cogollo con base blanda, color crema y de mal olor',
	32: 'hoja seca y erecta cerca a la mazorca',
	33: 'pudrición acuosa del capacho',
	34: 'granos color perla, acuosos y de mal olor',
	35: 'granos con coloración blanca o rosada',
	36: 'hongo de color rosado o blanco sobre o entre los granos',
	37: 'aparecen exudaciones de goma',
	38: 'planta color verde pálido en el follaje',
	39: 'nervaduras amarillas',
	40: 'brotes escasos',
	41: 'planta con aspecto decaído',
	42: 'lesiones necróticas de color oscuro en botones florales y frutos',
	43: 'caída prematura de frutos',
	44: 'manchas irregulares en las hojas',
	45: 'defoliaciones intensas',
	46: 'masas blandas de color rosado',
	47: 'pudriciones a nivel de la base del tronco de los árboles',
	48: 'decaimiento de los árboles',
	49: 'amarillamiento progresivo',
	50: 'pérdida de hojas',
	51: 'muerte de árboles',
	52: 'lesiones en forma de llaga en la base de los troncos',
	53: 'crecimiento del hongo en forma radial y de color blanco'
}

#Este diccionario guarda las enfermedades como llave
#y una lista de sintomas como valor
#util para operar con enfermedades
#para cada cultivo hay un diccionario llamado enfermedad_<nombre_de_cultivo>
#de la misma manera con las plagas
enfermedades = {
	'roya': [1,2],
  	'llagas del cafeto': [3],
  	'mancha de hierro': [4,5],
	'mal de panamá': [6,7,8,14],
	'negrilla': [9],
	'ahongado': [10],
	'moko': [11,12,13],
	'mosaico dorado': [15,16,17,18,19,20],
	'moho blanco': [21,22,23,24],
	'mancha de asfalto': [26,27,28,29],
	'pudrición acuosa del tallo': [30,31,32,33,34],
	'pudrición rosada por fusarium': [35,36],
	'gomosis de los cítricos': [37,38,39,40,41],
	'antracnosis de los cítricos': [42,43,44,45,46],
	'llagas radicales': [47,48,49,50,51,52,53],
}

#identificadores para las enfermedades
id_enfermedades = {
    0: 'roya', 1: 'llagas del cafeto', 2: 'mancha de hierro', 3: 'mal de panamá', 
    4: 'negrilla', 5: 'ahongado', 6: 'moko', 7: 'mosaico dorado', 
    8: 'moho blanco', 9: 'mancha de asfalto', 10: 'pudrición acuosa del tallo',
	11: 'pudrición rosada por fusarium', 
    12: 'gomosis de los cítricos', 13: 'antracnosis de los cítricos', 14: 'llagas radicales'
}

cantidad_enfermedades = 15

#Esta funcion saca la enfermedad que es mas probable sea pedecida por 
#el cultivo
def calcularMayor(enfermedades):
	posp = 0
	maxp = 0
	for i in range(len(enfermedades)):
		if enfermedades[i][1] > maxp:
			maxp = enfermedades[i][1]
			posp = i
	return enfermedades[posp]

#Una funcion que debe recibir una lista de enfermedades entregadas por el usuario
#Devuelve una lista de numeros que sirven para detectar la probabillidad
#de padecer alguna enfermedad
def convSintomas(l_sintomas, pos):
	lista_sintomas = enfermedades[id_enfermedades[pos]]
	l_aux = []
	for s in lista_sintomas:
		l_aux.append(sintomas[s])

	#la cantidad de sintomas sirve para medir la probabilidad de encontrar
	#una enfermedad a partir de unos sintomas
	#la probabilidad P esta dada por
	#P = sintomas acertados / total sintomas enfermedad
	total_sintomas = len(l_aux)
	aciertos = 0
	for s in l_sintomas:
		if l_aux.count(s):
			aciertos += 1
	p = (aciertos / total_sintomas) * 100
	return [id_enfermedades[pos], p]

def consultarEnfermedad(l_sintomas):
	probabilidades = []
	for i in range(cantidad_enfermedades):
		probabilidades.append(convSintomas(l_sintomas, i))
	return calcularMayor(probabilidades)