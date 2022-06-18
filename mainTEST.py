from numpy import *
import calfem.core as cfc

#define топология элемента
Edof = array([
        [1,2,3,4,5,6],
        [4,5,6,7,8,9]
        ])

#define нулевые матрицы жесткости и силы
k = zeros((9,9))
f = zeros((9,1))

E = 2*pow(10,11)

#define площадь первой балки элемент и второй элемент балки
Ab = 0.105
Ab2 = Ab

#define момент первого элемента балки и второго элемента балки
Ib = 1.072*pow(10,-3)
Ib2 = 1.072*pow(10,-3)

#define свойство E,A,I для первого элемента балки и второго элемента лбалки
ep_b = array([E,Ab,Ib])
ep_b2 = array([E,Ab2,Ib2])

#define распределенная нагрузка на второй элемент балки
eq_b2 = array([0,10000])

#assign элементы
element = array([1,2])

#define позицию элемента в направлении x
ex = array([
        [0,5],      #в локальных осях, [начальная точка в направлении x, конечная точка в направлении y ]
        [0,10],
        ])

ey = array([
        [0,0],
        [0,0],
        ])

i=0
for elx,ely,eltopo in zip(ex,ey,Edof):
        #если элемент является первым балочным элементом, то будем использовать свойство первой балки для определения жесткости
        if element[i] == 1 :
                ke = cfc.beam2e(elx, ely, ep_b)
                k_global = cfc.assem(eltopo, k, ke)
        #если элемент является вторым элементом балки, то будет использоваться свойство второй балки для определения жесткости
        if element[i] == 2:
                #ke = cfc.beam2e(elx,ely,ep_b2)
                ke, fe = cfc.beam2e(elx,ely,ep_b2,eq_b2)
                k_global, f = cfc.assem(eltopo, k, ke, f, fe=fe)
        #собираем локальные матрицы жесткости в глобальную матрицу жесткости
        
        i += 1
#define граничные условия
bc = array([1,2,3,5,8])

#solve уравнение жесткости
a,r = cfc.solveq(k_global,f,bc)

reaction = array([r[1],r[2],r[4],r[7]])
displacement = array([a[5],a[8]])
print(k)
print("Смещение: ")
print(displacement)
print("Реакция: (кН)")
print(reaction/1000)