
class Arithematic:
    def add(self):
        a=15
        b=75
        print(a+b)

    def sub(self):
        a=45
        b=15
        print(a-b)

    
    def mul(self):
        a=15
        b=5
        print(a*b)

    def div(self):
        a=45
        b=15
        print(a/b)

obj=Arithematic()
obj.add()
obj.sub()
obj.mul()
obj.div()


class area:
    def area_of_rectangle(self):
        l=40
        b=20
        print(l*b)

    def area_of_triangle(self):
        b=40
        h=20
        print(0.5*b*h)

    def area_of_square(self):
        s=40
        print(s*s)

    def area_of_circle(self):
        r=8
        print(3.14*r*r)

obj1=area()
obj1.area_of_rectangle()
obj1.area_of_triangle()
obj1.area_of_square()
obj1.area_of_circle()

class volume:
    def volume_of_cuboid(self):
        l=60
        h=40
        b=30
        print(l*h*b)

    def volume_cube(self):
        a=60
        print(a*a*a)

    def volume_cone(self):
        h=80
        r=25
        print(1/3*h*3.14*r*r)

    def volume_cylinder(self):
        r=30
        h=40
        print(3.14*r*r*h)

obj2=volume()
obj2.volume_of_cuboid()
obj2.volume_cube()
obj2.volume_cone()
obj2.volume_cylinder()

class swap:
    def swap_num(self):
        a=10
        b=20
        c=a
        a=b
        b=c
        print(a,b)
obj3=swap()
obj3.swap_num()


class reverse:
    def reverse(self):
        num=123
        rem1=num%10
        num=num//10
        rem2=num%10
        num=num//10
        rem3=num%10
        print(rem1*100+rem2*10+rem3*1)
obj4=reverse()
obj4.reverse()


class km_m:
    def km_m(self):
        km=1
        print(km*1000)

obj5=km_m()
obj5.km_m()


class temperature:
    def cel_fah(self):
        cel=2
        print(cel*1.8+32)

obj6=temperature()
obj6.cel_fah()


class formula:
    def f1(self):
        x=12
        y=14
        print(x*x+2*(x*y)+y*y)
    def f2(self):
        x=12
        y=14
        print(x*x+2*(x*y)-y*y)

obj7=formula()
obj7.f1()
obj7.f2()


