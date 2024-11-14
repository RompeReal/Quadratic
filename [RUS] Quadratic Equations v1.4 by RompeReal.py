import math

a=int(input('''=====
Эта программа позволяет решать квадартные уравнения

ax²+bx+c=0

Введите значение A\n'''))
b=int(input('Введите значение B\n'))
c=int(input('Введите значение C\n'))

if a==0:
    x=-c/b
    input(f'''
=-=Решено!=-=

----Решение----
{a}x²+({b})x+({c})=0
a=0 => Уравнение приняло вид bx+c=0
({b})x+({c})=0
1. ({b})x=-({c})
2. x=-({c})/({b})
3. x={x}

Единственный корень уравнения равен {x}

---Проверка решения---

({b})({x})+({c})=0\n''')
else:
    d=b**2-4*a*c

    if d<0:
        input(f'''
=-=Ошибка!=-=

---Решение---
{a}x²+({b})x+({c})=0
1. D=b²-4ac=({b})²-4*{a}*{c}={d}
D<0 => X имеет 0 корней

Значение дискриминанта меньше 0 (Дискриминант равен {d})

Корней уравнения не существует

---Проверка решения---
{a}x²+({b})x+({c})=0\n''')
    
    elif d==0:
        g=2*a
        x=-b/g
        input(f'''
=-=Решено!=-=

---Решение---
{a}x²+({b})x+({c})=0
1. D=b²-4ac=({b})²-4*{a}*{c}=0
D=0 => X имеет 1 корень
2. X=(-b)/2a=(-({b}))/(2*{a})={x}
   
Дискриминант равен 0

Единственный корень уравнения равен {x}

---Проверка решения---
            
{a}({x})²+({b})({x})+({c})=0\n''')
    
    else:
        h=math.sqrt(d)
        g=2*a
        e=b+h
        x1=e/g
        f=-b-h
        x2=f/g
        input(f'''
=-=Решено!=-=

---Решение---
{a}x²+({b})x+({c})=0
1. D=b²-4ac=({b})²-4*{a}*{c}={d}
D>0 => X имеет 2 корня
2. X₁=(-b+√d)/2a=(-({b})+{h})/(2*{a})={x1}
3. X₂=(-b-√d)/2a=(-({b})+{h})/(2*{a})={x2}

Дискриминант равен {d}

Первый корень уравнения равен {x1}

---Проверка решения---
{a}({x1})²+({b})({x1})+({c})=0

Второй корень уравнения равен {x2}

---Проверка решения---
{a}({x2})²+({b})({x2})+({c})=0\n''')
