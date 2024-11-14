import math

a=int(input('''=====
This program allows you to solve quadratic equations

ax²+bx+c=0

Enter the value of A\n'''))
b=int(input('Enter the value of B\n'))
c=int(input('Enter the value of C\n'))

if a==0:
    x=-c/b
    input(f'''
=-=Solved!=-=

----Solution----
{a}x²+({b})x+({c})=0
a=0 => The equation took the form bx+c=0
({b})x+({c})=0
1. ({b})x=-({c})
2. x=-({c})/({b})
3. x={x}

The only value of X is {x}

---Solution check---

({b})({x})+({c})=0\n''')
else:
    d=b**2-4*a*c

    if d<0:
        input(f'''
=-=Unsolved!=-=

---Solution---
{a}x²+({b})x+({c})=0
1. D=b²-4ac=({b})²-4*{a}*{c}={d}
D<0 => X has 0 values

The discriminant value is less than 0 (The discriminant is {d})

The values of the X do not exist

---Solution check---
{a}x²+({b})x+({c})=0\n''')
    
    elif d==0:
        g=2*a
        x=-b/g
        input(f'''
=-=Solved!=-=

---Solution---
{a}x²+({b})x+({c})=0
1. D=b²-4ac=({b})²-4*{a}*{c}=0
D=0 => X has 1 value
2. X=(-b)/2a=(-({b}))/(2*{a})={x}
   
Discriminant is 0

The only value of X is {x}

---Solution check---
            
{a}({x})²+({b})({x})+({c})=0\n''')
    
    else:
        h=math.sqrt(d)
        g=2*a
        e=b+h
        x1=e/g
        f=-b-h
        x2=f/g
        input(f'''
=-=Solved!=-=

---Solution---
{a}x²+({b})x+({c})=0
1. D=b²-4ac=({b})²-4*{a}*{c}={d}
D>0 => X has 2 values
2. X₁=(-b+√d)/2a=(-({b})+{h})/(2*{a})={x1}
3. X₂=(-b-√d)/2a=(-({b})+{h})/(2*{a})={x2}

Discriminant is {d}

The 1st value of X is {x1}

---Solution check---
{a}({x1})²+({b})({x1})+({c})=0

The 2nd value of X is {x2}

---Solution check---
{a}({x2})²+({b})({x2})+({c})=0\n''')
