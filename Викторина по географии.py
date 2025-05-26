from tkinter import*
import tkinter as tk
from idlelib.tooltip import Hovertip
count = 0
p = 0
def H():# начало
    root.geometry('1550x800')
    global count
    global p
    p += 1
    d.destroy()
    c.destroy()
    IT.destroy()
    g.destroy()
    v.destroy()
    x1.grid(column = 0, row = 0)
    q1.grid(column = 0, row = 1)
    next1.grid(column = 3, row = 3)
    del1.grid(column = 1, row = 3)
    list1.grid(column = 3, row = 2)
    for i in ('Антарктида','Африка','Австралия','Арктика'):
        list1.insert(0,i)
    world.grid(column = 0, row = 2)
    
def exid():
    root.destroy()

def fo1():
    global count
    global k1
    global p
    p += 1
    k1=list1.get(ANCHOR)
    k1 = 'Ваш ответ: ' + k1
    if list1.get(ANCHOR) == 'Арктика':
        count += 1
        b1.config(text='1')
    if k1 != 'Ваш ответ: ':
      Hovertip(a1, k1, hover_delay=100)
    else:
      Hovertip(a1, 'Нет ответа', hover_delay=100)
    q1.destroy()
    next1.destroy()
    del1.destroy()
    list1.destroy()
    x1.destroy()
    x2.grid(column = 0, row = 0)
    q2.grid(column = 0, row = 1)
    next2.grid(column = 3, row = 3)
    del2.grid(column = 1, row = 3)
    list2.grid(column = 3, row = 2)
    for i in ('по четырём сторонам света','по расположению в Северном или Южном полушарии','на обитаемые и необитаемые','на тёплые и холодные'):
        list2.insert(0,i)
    
    

def fo2():
    global count
    global p
    p += 1
    k2=list2.get(ANCHOR)
    k2 = 'Ваш ответ: ' + k2
    if k2 != 'Ваш ответ: ':
      Hovertip(a2, k2, hover_delay=100)
    else:
      Hovertip(a2, 'Нет ответа', hover_delay=100)
    if list2.get(ANCHOR) == 'по расположению в Северном или Южном полушарии':
        count += 1
        b2.config(text='1')
    q2.destroy()
    x2.destroy()
    next2.destroy()
    del2.destroy()
    list2.destroy()
    x3.grid(column = 0, row = 0)
    q3.grid(column = 0, row = 1)
    next3.grid(column = 3, row = 3)
    del3.grid(column = 1, row = 3)
    list3.grid(column = 3, row = 2)
    for i in ('восемь','семь','шесть','пять'):
        list3.insert(0,i)
    


def fo3():
    global count
    global p
    p += 1
    k3=list3.get(ANCHOR)
    k3 = 'Ваш ответ: ' + k3
    if k3 != 'Ваш ответ: ':
      Hovertip(a3,k3, hover_delay=100)
    else:
      Hovertip(a3, 'Нет ответа', hover_delay=100)
    if list3.get(ANCHOR) == 'шесть':
        count += 1
        b3.config(text='1')
    q3.destroy()
    next3.destroy()
    del3.destroy()
    x3.destroy()
    list3.destroy()
    world.destroy()
    x4.grid(column = 0, row = 0)
    q4.grid(column = 0, row = 1,columnspan = 2)
    next4.grid(column = 3, row = 3)
    del4.grid(column = 1, row = 3)
    list4.grid(column = 3, row = 2)
    an.grid(column = 0, row = 2)
    for i in ('единственный, который расположен выше экватора','наименьший из всех','покрыт ледяным панцирем','во много раз крупнее других'):
        list4.insert(0,i)
    

def fo4():
    global count
    global p
    p += 1
    k4=list4.get(ANCHOR)
    k4 = 'Ваш ответ: ' + k4
    if k4 != 'Ваш ответ: ':
      Hovertip(a4,k4, hover_delay=100)
    else:
      Hovertip(a4, 'Нет ответа', hover_delay=100)
    if list4.get(ANCHOR) == 'покрыт ледяным панцирем':
        count += 1
        b4.config(text='1')
    q4.destroy()
    next4.destroy()
    del4.destroy()
    x4.destroy()
    list4.destroy()
    an.destroy()
    x5.grid(column = 0, row = 0)
    q5.grid(column = 0, row = 1,columnspan = 2)
    next5.grid(column = 3, row = 3)
    del5.grid(column = 1, row = 3)
    list5.grid(column = 3, row = 2)
    for i in ('Австралия и Антарктида','Евразия, затем Африка','Азия, а потом Америка (Северная)','Америка (Южная) и Австралия'):
        list5.insert(0,i)
    photo5.grid(column = 0, row = 2)

def fo5():
    global count
    global p
    p += 1
    k5=list5.get(ANCHOR)
    k5 = 'Ваш ответ: ' + k5
    if k5 != 'Ваш ответ: ':
      Hovertip(a5,k5, hover_delay=100)
    else:
      Hovertip(a5, 'Нет ответа', hover_delay=100)
    if list5.get(ANCHOR) == 'Евразия, затем Африка':
        count += 1
        b5.config(text='1')
    q5.destroy()
    x5.destroy()
    next5.destroy()
    del5.destroy()
    list5.destroy()
    photo5.destroy()
    x6.grid(column = 0, row = 0)
    q6.grid(column = 0, row = 1,columnspan = 2)
    next6.grid(column = 3, row = 3)
    del6.grid(column = 1, row = 3)
    list6.grid(column = 3, row = 2)
    for i in ('Америки (Южной)','Америки (Северной)','Австралии','Евразии'):
        list6.insert(0,i)
    world5.grid(column = 0, row = 2)

def fo6():
    global count
    global p
    p += 1
    k6=list6.get(ANCHOR)
    k6 = 'Ваш ответ: ' + k6
    if k6 != 'Ваш ответ: ':
      Hovertip(a6,k6, hover_delay=100)
    else:
      Hovertip(a6, 'Нет ответа', hover_delay=100)
    if list6.get(ANCHOR) == 'Австралии':
        count += 1
        b6.config(text='1')
    q6.destroy()
    next6.destroy()
    del6.destroy()
    x6.destroy()
    list6.destroy()
    world5.destroy()
    x7.grid(column = 0, row = 0)
    q7.grid(column = 0, row = 1)
    next7.grid(column = 3, row = 3)
    del7.grid(column = 1, row = 3)
    list7.grid(column = 3, row = 2)
    for i in ('Африка и Северная Америка','Антарктида и Австралия','Европа и Антарктида','Африка и Азия'):
        list7.insert(0,i)
    photo7.grid(column = 0, row = 2)

def fo7():
    global count
    global p
    p += 1
    k7=list7.get(ANCHOR)
    k7 = 'Ваш ответ: ' + k7
    if k7 != 'Ваш ответ: ':
      Hovertip(a7,k7, hover_delay=100)
    else:
      Hovertip(a7, 'Нет ответа', hover_delay=100)
    if list7.get(ANCHOR) == 'Антарктида и Австралия':
        count += 1
        b7.config(text='1')
    q7.destroy()
    next7.destroy()
    del7.destroy()
    x7.destroy()
    list7.destroy()
    photo7.destroy()
    x8.grid(column = 0, row = 0)
    q8.grid(column = 0, row = 1)
    next8.grid(column = 3, row = 3)
    del8.grid(column = 1, row = 3)
    list8.grid(column = 3, row = 2)
    for i in ('в Северном','в Западном','в Южном','в Восточном'):
        list8.insert(0,i)
    pot.grid(column = 0, row = 2)

def fo8():
    global count
    global p
    p += 1
    k8=list8.get(ANCHOR)
    k8 = 'Ваш ответ: ' + k8
    if k8 != 'Ваш ответ: ':
      Hovertip(a8,k8, hover_delay=100)
    else:
      Hovertip(a8, 'Нет ответа', hover_delay=100)
    if list8.get(ANCHOR) == 'в Южном':
        count += 1
        b8.config(text='1')
    q8.destroy()
    next8.destroy()
    del8.destroy()
    x8.destroy()
    list8.destroy()
    x9.grid(column = 0, row = 0)
    q9.grid(column = 0, row = 1)
    next9.grid(column = 3, row = 3)
    del9.grid(column = 1, row = 3)
    list9.grid(column = 3, row = 2)
    for i in ('Африка','Евразия','Антарктида','Австралия'):
        list9.insert(0,i)

def fo9():
    global count
    global p
    p += 1
    k9=list9.get(ANCHOR)
    k9 = 'Ваш ответ: ' + k9
    if k9 != 'Ваш ответ: ':
      Hovertip(a9,k9, hover_delay=100)
    else:
      Hovertip(a9, 'Нет ответа', hover_delay=100)
    if list9.get(ANCHOR) == 'Евразия':
        count += 1
        b9.config(text='1')
    q9.destroy()
    next9.destroy()
    del9.destroy()
    x9.destroy()
    list9.destroy()
    x10.grid(column = 0, row = 0)
    q10.grid(column = 0, row = 1)
    next10.grid(column = 3, row = 3)
    del10.grid(column = 1, row = 3)
    list10.grid(column = 3, row = 2)
    for i in ('Австралию, Азию и Америку (Южную)','Северную Америку','Африку и Южную Америку','Африку'):
        list10.insert(0,i)        

def fo10():
    global count
    global p
    p += 1
    k10=list10.get(ANCHOR)
    k10 = 'Ваш ответ: ' + k10
    if k10 != 'Ваш ответ: ':
      Hovertip(a10,k10, hover_delay=100)
    else:
      Hovertip(a10, 'Нет ответа', hover_delay=100)
    if list10.get(ANCHOR) == 'Африку и Южную Америку':
        count += 1
        b10.config(text='1')
    q10.destroy()
    x10.destroy()
    next10.destroy()
    del10.destroy()
    list10.destroy()
    x11.grid(column = 0, row = 0)
    q11.grid(column = 0, row = 1)
    next11.grid(column = 3, row = 3)
    del11.grid(column = 1, row = 3)
    list11.grid(column = 3, row = 2)
    for i in ('Евразия и Австралия','Европа и Антарктида','Азия и Америка (Южная)','Северная Америка и Евразия'):
        list11.insert(0,i)

def fo11():
    global count
    global p
    p += 1
    k11=list11.get(ANCHOR)
    k11 = 'Ваш ответ: ' + k11
    if k11 != 'Ваш ответ: ':
      Hovertip(a11,k11, hover_delay=100)
    else:
      Hovertip(a11, 'Нет ответа', hover_delay=100)
    if list11.get(ANCHOR) == 'Северная Америка и Евразия':
        count += 1
        b11.config(text='1')
    q11.destroy()
    next11.destroy()
    del11.destroy()
    list11.destroy()
    x11.destroy()
    pot.destroy()
    x12.grid(column = 0, row = 0)
    q12.grid(column = 0, row = 1)
    next12.grid(column = 3, row = 3)
    del12.grid(column = 1, row = 3)
    list12.grid(column = 3, row = 2)
    for i in ('древний материк на месте нынешней Антарктиды','обозначение всех материков на Земле','устаревшее название южного материка','единый северный материк в прошлом, на месте нынешних Евразии и Северной Америки'):
        list12.insert(0,i)
    log.grid(column = 0, row = 2)

def fo12():
    global count
    global p
    p += 1
    k12=list12.get(ANCHOR)
    k12 = 'Ваш ответ: ' + k12
    if k12 != 'Ваш ответ: ':
      Hovertip(a12,k12, hover_delay=100)
    else:
      Hovertip(a12, 'Нет ответа', hover_delay=100)
    if list12.get(ANCHOR) == 'единый северный материк в прошлом, на месте нынешних Евразии и Северной Америки':
        count += 1
        b12.config(text='1')
    q12.destroy()
    next12.destroy()
    del12.destroy()
    list12.destroy()
    x12.destroy()
    x13.grid(column = 0, row = 0)
    q13.grid(column = 0, row = 1)
    next13.grid(column = 3, row = 3)
    del13.grid(column = 1, row = 3)
    list13.grid(column = 3, row = 2)
    for i in ('единственный материк на Земле, существовавший более 20 тысяч лет назад','обозначение всех северных материков в прошлом','название единого древнего материка в южном полушарии','древнее название Америки (Северной)'):
        list13.insert(0,i)
    
def fo13():
    global count
    global p
    p += 1
    k13=list13.get(ANCHOR)
    k13 = 'Ваш ответ: ' + k13
    if k13 != 'Ваш ответ: ':
      Hovertip(a13,k13, hover_delay=100)
    else:
      Hovertip(a13, 'Нет ответа', hover_delay=100)
    if list13.get(ANCHOR) == 'название единого древнего материка в южном полушарии':
        count += 1
        b13.config(text='1')
    q13.destroy()
    next13.destroy()
    del13.destroy()
    list13.destroy()
    x13.destroy()
    x14.grid(column = 0, row = 0)
    q14.grid(column = 0, row = 1,columnspan = 2)
    next14.grid(column = 3, row = 3)
    del14.grid(column = 1, row = 3)
    list14.grid(column = 3, row = 2)
    for i in ('Америка (Южная)','Австралия','Евразия','Африка'):
        list14.insert(0,i)
    
def fo14():
    global count
    global p
    p += 1
    k14=list14.get(ANCHOR)
    k14 = 'Ваш ответ: ' + k14
    if k14 != 'Ваш ответ: ':
      Hovertip(a14,k14, hover_delay=100)
    else:
      Hovertip(a14, 'Нет ответа', hover_delay=100)
    if list14.get(ANCHOR) == 'Евразия':
        count += 1
        b14.config(text='1')
    q14.destroy()
    log.destroy()
    next14.destroy()
    del14.destroy()
    list14.destroy()
    x14.destroy()
    x15.grid(column = 0, row = 0)
    q15.grid(column = 0, row = 1)
    next15.grid(column = 3, row = 3)
    del15.grid(column = 2, row = 3)
    list15.grid(column = 3, row = 2)
    top.grid(column = 0, row = 2)
    for i in ('Южная Америка','Австралия','Африка','Антарктида'):
        list15.insert(0,i)
    
def fo15():
    global count
    global p
    p += 1
    k15=list15.get(ANCHOR)
    k15 = 'Ваш ответ: ' + k15
    if k15 != 'Ваш ответ: ':
      Hovertip(a15,k15, hover_delay=100)
    else:
      Hovertip(a15, 'Нет ответа', hover_delay=100)
    if list15.get(ANCHOR) == 'Африка':
        count += 1
        b15.config(text='1')
    q15.destroy()
    next15.destroy()
    del15.destroy()
    list15.destroy()
    x15.destroy()
    top.destroy()
    x16.grid(column = 0, row = 0)
    q16.grid(column = 0, row = 1)
    next16.grid(column = 3, row = 3)
    del16.grid(column = 2, row = 3)
    list16.grid(column = 3, row = 2)
    war.grid(column = 0, row = 2)
    for i in ('Антарктида','Африка','Австралия','Южная Америка'):
        list16.insert(0,i)
    
def fo16():
    global count
    global p
    p += 1
    k16=list16.get(ANCHOR)
    k16 = 'Ваш ответ: ' + k16
    if k16 != 'Ваш ответ: ':
      Hovertip(a16,k16, hover_delay=100)
    else:
      Hovertip(a16, 'Нет ответа', hover_delay=100)
    if list16.get(ANCHOR) == 'Антарктида':
        count += 1
        b16.config(text='1')
    q16.destroy()
    next16.destroy()
    del16.destroy()
    list16.destroy()
    x16.destroy()
    war.destroy()
    x17.grid(column = 0, row = 0)
    q17.grid(column = 0, row = 1)
    next17.grid(column = 3, row = 3)
    del17.grid(column = 2, row = 3)
    list17.grid(column = 3, row = 2)
    tep.grid(column = 0, row = 2)
    for i in ('в холодном и жарком','только в умеренном','полностью в жарком','в холодном и умеренном'):
        list17.insert(0,i)

def fo17():
    global count
    global p
    p += 1
    k17=list17.get(ANCHOR)
    k17 = 'Ваш ответ: ' + k17
    if k17 != 'Ваш ответ: ':
      Hovertip(a17,k17, hover_delay=100)
    else:
      Hovertip(a17, 'Нет ответа', hover_delay=100)
    if list17.get(ANCHOR) == 'в холодном и умеренном':
        count += 1
        b17.config(text='1')
    q17.destroy()
    next17.destroy()
    del17.destroy()
    list17.destroy()
    x17.destroy()
    tep.destroy()
    x18.grid(column = 0, row = 0)
    q18.grid(column = 0, row = 1)
    next18.grid(column = 3, row = 3)
    del18.grid(column = 2, row = 3)
    list18.grid(column = 3, row = 2)
    ward.grid(column = 0, row = 2)
    for i in ('Азия','Евразия','Европа','Африка'):
        list18.insert(0,i)

def fo18():
    global count
    global p
    p += 1
    k18=list18.get(ANCHOR)
    k18 = 'Ваш ответ: ' + k18
    if k18 != 'Ваш ответ: ':
      Hovertip(a18,k18, hover_delay=100)
    else:
      Hovertip(a18, 'Нет ответа', hover_delay=100)
    if list18.get(ANCHOR) == 'Евразия':
        count += 1
        b18.config(text='1')
    q18.destroy()
    next18.destroy()
    del18.destroy()
    list18.destroy()
    x18.destroy()
    x19.grid(column = 0, row = 0)
    q19.grid(column = 0, row = 1)
    next19.grid(column = 3, row = 3)
    del19.grid(column = 2, row = 3)
    list19.grid(column = 3, row = 2)
    for i in ('реками, болотами и озёрами','океанами и морями','горами','лесами'):
        list19.insert(0,i)

def fo19():
    global count
    global p
    p += 1
    k19=list19.get(ANCHOR)
    k19 = 'Ваш ответ: ' + k19
    if k19 != 'Ваш ответ: ':
      Hovertip(a19,k19, hover_delay=100)
    else:
      Hovertip(a19, 'Нет ответа', hover_delay=100)
    if list19.get(ANCHOR) == 'океанами и морями':
        count += 1
        b19.config(text='1')
    q19.destroy()
    next19.destroy()
    del19.destroy()
    list19.destroy()
    x19.destroy()
    x20.grid(column = 0, row = 0)
    q20.grid(column = 0, row = 1)
    next20.grid(column = 3, row = 3)
    del20.grid(column = 2, row = 3)
    list20.grid(column = 3, row = 2)
    for i in ('Африка','Антарктида','Южная Америка','Азия'):
        list20.insert(0,i)

def end():
    root.geometry('1200x700')
    global count
    global k1
    global p
    k20=list20.get(ANCHOR)
    k20 = 'Ваш ответ: ' + k20
    if k20 != 'Ваш ответ: ':
      Hovertip(a20,k20, hover_delay=100)
    else:
      Hovertip(a20, 'Нет ответа', hover_delay=100)
    if list20.get(ANCHOR) == 'Азия':
        count += 1
        b20.config(text='1')
    q20.destroy()
    resy.config(text=str(count))
    next20.destroy()
    del20.destroy()
    list20.destroy()
    x20.destroy()
    ward.destroy()
    resl.grid(column = 3, row = 0)
    num.grid(column = 0, row = 0)
    resy.grid(column = 3, row = 21)
    d1.grid(column = 0, row = 1)
    a1.grid(column = 1, row = 1)
    b1.grid(column = 3, row = 1)

    d2.grid(column = 0, row = 2)
    a2.grid(column = 1, row = 2)
    b2.grid(column = 3, row = 2)

    d3.grid(column = 0, row = 3)
    a3.grid(column = 1, row = 3)
    b3.grid(column = 3, row = 3)

    d4.grid(column = 0, row = 4)
    a4.grid(column = 1, row = 4)
    b4.grid(column = 3, row = 4)

    d5.grid(column = 0, row = 5)
    a5.grid(column = 1, row = 5)
    b5.grid(column = 3, row = 5)

    d6.grid(column = 0, row = 6)
    a6.grid(column = 1, row = 6)
    b6.grid(column = 3, row = 6)

    d7.grid(column = 0, row = 7)
    a7.grid(column = 1, row = 7)
    b7.grid(column = 3, row = 7)

    d8.grid(column = 0, row = 8)
    a8.grid(column = 1, row = 8)
    b8.grid(column = 3, row = 8)

    d9.grid(column = 0, row = 9)
    a9.grid(column = 1, row = 9)
    b9.grid(column = 3, row = 9)

    d10.grid(column = 0, row = 10)
    a10.grid(column = 1, row = 10)
    b10.grid(column = 3, row = 10)

    d11.grid(column = 0, row = 11)
    a11.grid(column = 1, row = 11)
    b11.grid(column = 3, row = 11)

    d12.grid(column = 0, row = 12)
    a12.grid(column = 1, row = 12)
    b12.grid(column = 3, row = 12)

    d13.grid(column = 0, row = 13)
    a13.grid(column = 1, row = 13)
    b13.grid(column = 3, row = 13)

    d14.grid(column = 0, row = 14)
    a14.grid(column = 1, row = 14)
    b14.grid(column = 3, row = 14)

    d15.grid(column = 0, row = 15)
    a15.grid(column = 1, row = 15)
    b15.grid(column = 3, row = 15)

    d16.grid(column = 0, row = 16)
    a16.grid(column = 1, row = 16)
    b16.grid(column = 3, row = 16)

    d17.grid(column = 0, row = 17)
    a17.grid(column = 1, row = 17)
    b17.grid(column = 3, row = 17)

    d18.grid(column = 0, row = 18)
    a18.grid(column = 1, row = 18)
    b18.grid(column = 3, row = 18)

    d19.grid(column = 0, row = 19)
    a19.grid(column = 1, row = 19)
    b19.grid(column = 3, row = 19)

    d20.grid(column = 0, row = 20)
    a20.grid(column = 1, row = 20)
    b20.grid(column = 3, row = 20)

    it.grid(column = 0, row = 21)
    tru.grid(column = 1, row = 0)

def end2():
    global count
    global list2
    global list19
    global p
    if p == 1:
        k1=list1.get(ANCHOR)
    if p == 2:
        k2=list2.get(ANCHOR)
    if p == 3:
        k3=list3.get(ANCHOR)
    if p == 4:
        k4=list4.get(ANCHOR)
    if p == 5:
        k5=list5.get(ANCHOR)
    if p == 6:
        k6=list6.get(ANCHOR)
    if p == 7:
        k7=list7.get(ANCHOR)
    if p == 8:
        k8=list8.get(ANCHOR)
    if p == 9:
        k9=list9.get(ANCHOR)
    if p == 10:
        k10=list10.get(ANCHOR)
    if p == 11:
        k11=list11.get(ANCHOR)
    if p == 12:
        k12=list12.get(ANCHOR)
    if p == 13:
        k13=list13.get(ANCHOR)
    if p == 14:
        k14=list14.get(ANCHOR)
    if p == 15:
        k15=list15.get(ANCHOR)
    if p == 16:
        k16=list16.get(ANCHOR)
    if p == 17:
        k17=list17.get(ANCHOR)
    if p == 18:
        k18=list18.get(ANCHOR)
    if p == 19:
        k19=list19.get(ANCHOR)
    if p == 20:
        k20=list20.get(ANCHOR)
    #1
    if p == 1:
        q1.destroy()
        next1.destroy()
        del1.destroy()
        list1.destroy()
        x1.destroy()
        world.destroy()
        k1 = 'Ваш ответ: ' + k1
        if k1 == 'Ваш ответ: Арктика':
            count += 1
            b1.config(text='1')
        if k1 != 'Ваш ответ: ':
          Hovertip(a1, k1, hover_delay=100)
        else:
          Hovertip(a1, 'Нет ответа', hover_delay=100)
        end()
        Hovertip(a2, 'Нет ответа', hover_delay=100)
        Hovertip(a3, 'Нет ответа', hover_delay=100)
        Hovertip(a4, 'Нет ответа', hover_delay=100)
        Hovertip(a5, 'Нет ответа', hover_delay=100)
        Hovertip(a6, 'Нет ответа', hover_delay=100)
        Hovertip(a7, 'Нет ответа', hover_delay=100)
        Hovertip(a8, 'Нет ответа', hover_delay=100)
        Hovertip(a9, 'Нет ответа', hover_delay=100)
        Hovertip(a10, 'Нет ответа', hover_delay=100)
        Hovertip(a11, 'Нет ответа', hover_delay=100)
        Hovertip(a12, 'Нет ответа', hover_delay=100)
        Hovertip(a13, 'Нет ответа', hover_delay=100)
        Hovertip(a14, 'Нет ответа', hover_delay=100)
        Hovertip(a15, 'Нет ответа', hover_delay=100)
        Hovertip(a16, 'Нет ответа', hover_delay=100)
        Hovertip(a17, 'Нет ответа', hover_delay=100)
        Hovertip(a18, 'Нет ответа', hover_delay=100)
        Hovertip(a19, 'Нет ответа', hover_delay=100)
        Hovertip(a20, 'Нет ответа', hover_delay=100)
    #2
    if p == 2:
        q2.destroy()
        next2.destroy()
        del2.destroy()
        list2.destroy()
        x2.destroy()
        world.destroy()
        k2 = 'Ваш ответ: ' + k2
        if k2 != 'Ваш ответ: ':
          Hovertip(a2, k2, hover_delay=100)
        else:
          Hovertip(a2, 'Нет ответа', hover_delay=100)
        if k2 == 'Ваш ответ: по расположению в Северном или Южном полушарии':
            count += 1
            b2.config(text='1')
        Hovertip(a3, 'Нет ответа', hover_delay=100)
        Hovertip(a4, 'Нет ответа', hover_delay=100)
        Hovertip(a5, 'Нет ответа', hover_delay=100)
        Hovertip(a6, 'Нет ответа', hover_delay=100)
        Hovertip(a7, 'Нет ответа', hover_delay=100)
        Hovertip(a8, 'Нет ответа', hover_delay=100)
        Hovertip(a9, 'Нет ответа', hover_delay=100)
        Hovertip(a10, 'Нет ответа', hover_delay=100)
        Hovertip(a11, 'Нет ответа', hover_delay=100)
        Hovertip(a12, 'Нет ответа', hover_delay=100)
        Hovertip(a13, 'Нет ответа', hover_delay=100)
        Hovertip(a14, 'Нет ответа', hover_delay=100)
        Hovertip(a15, 'Нет ответа', hover_delay=100)
        Hovertip(a16, 'Нет ответа', hover_delay=100)
        Hovertip(a17, 'Нет ответа', hover_delay=100)
        Hovertip(a18, 'Нет ответа', hover_delay=100)
        Hovertip(a19, 'Нет ответа', hover_delay=100)
        Hovertip(a20, 'Нет ответа', hover_delay=100)
        end()
    #3
    elif p == 3:
        q3.destroy()
        next3.destroy()
        del3.destroy()
        list3.destroy()
        x3.destroy()
        world.destroy()
        k3 = 'Ваш ответ: ' + k3
        if k3 != 'Ваш ответ: ':
          Hovertip(a3,k3, hover_delay=100)
        else:
          Hovertip(a3, 'Нет ответа', hover_delay=100)
        if k3 == 'Ваш ответ: шесть':
            count += 1
            b3.config(text='1')
        Hovertip(a4, 'Нет ответа', hover_delay=100)
        Hovertip(a5, 'Нет ответа', hover_delay=100)
        Hovertip(a6, 'Нет ответа', hover_delay=100)
        Hovertip(a7, 'Нет ответа', hover_delay=100)
        Hovertip(a8, 'Нет ответа', hover_delay=100)
        Hovertip(a9, 'Нет ответа', hover_delay=100)
        Hovertip(a10, 'Нет ответа', hover_delay=100)
        Hovertip(a11, 'Нет ответа', hover_delay=100)
        Hovertip(a12, 'Нет ответа', hover_delay=100)
        Hovertip(a13, 'Нет ответа', hover_delay=100)
        Hovertip(a14, 'Нет ответа', hover_delay=100)
        Hovertip(a15, 'Нет ответа', hover_delay=100)
        Hovertip(a16, 'Нет ответа', hover_delay=100)
        Hovertip(a17, 'Нет ответа', hover_delay=100)
        Hovertip(a18, 'Нет ответа', hover_delay=100)
        Hovertip(a19, 'Нет ответа', hover_delay=100)
        Hovertip(a20, 'Нет ответа', hover_delay=100)
        end()
    #4
    elif p == 4:
        q4.destroy()
        next4.destroy()
        del4.destroy()
        list4.destroy()
        x4.destroy()
        an.destroy()
        k4 = 'Ваш ответ: ' + k4
        if k4 != 'Ваш ответ: ':
          Hovertip(a4,k4, hover_delay=100)
        else:
          Hovertip(a4, 'Нет ответа', hover_delay=100)
        if k4 == 'Ваш ответ: покрыт ледяным панцирем':
            count += 1
            b4.config(text='1')
        Hovertip(a5, 'Нет ответа', hover_delay=100)
        Hovertip(a6, 'Нет ответа', hover_delay=100)
        Hovertip(a7, 'Нет ответа', hover_delay=100)
        Hovertip(a8, 'Нет ответа', hover_delay=100)
        Hovertip(a9, 'Нет ответа', hover_delay=100)
        Hovertip(a10, 'Нет ответа', hover_delay=100)
        Hovertip(a11, 'Нет ответа', hover_delay=100)
        Hovertip(a12, 'Нет ответа', hover_delay=100)
        Hovertip(a13, 'Нет ответа', hover_delay=100)
        Hovertip(a14, 'Нет ответа', hover_delay=100)
        Hovertip(a15, 'Нет ответа', hover_delay=100)
        Hovertip(a16, 'Нет ответа', hover_delay=100)
        Hovertip(a17, 'Нет ответа', hover_delay=100)
        Hovertip(a18, 'Нет ответа', hover_delay=100)
        Hovertip(a19, 'Нет ответа', hover_delay=100)
        Hovertip(a20, 'Нет ответа', hover_delay=100)
        end()
    #5
    elif p == 5:
        q5.destroy()
        x5.destroy()
        next5.destroy()
        del5.destroy()
        list5.destroy()
        photo5.destroy()
        k5 = 'Ваш ответ: ' + k5
        if k5 != 'Ваш ответ: ':
          Hovertip(a5,k5, hover_delay=100)
        else:
          Hovertip(a5, 'Нет ответа', hover_delay=100)
        if k5 == 'Ваш ответ: Евразия, затем Африка':
            count += 1
            b5.config(text='1')
        Hovertip(a6, 'Нет ответа', hover_delay=100)
        Hovertip(a7, 'Нет ответа', hover_delay=100)
        Hovertip(a8, 'Нет ответа', hover_delay=100)
        Hovertip(a9, 'Нет ответа', hover_delay=100)
        Hovertip(a10, 'Нет ответа', hover_delay=100)
        Hovertip(a11, 'Нет ответа', hover_delay=100)
        Hovertip(a12, 'Нет ответа', hover_delay=100)
        Hovertip(a13, 'Нет ответа', hover_delay=100)
        Hovertip(a14, 'Нет ответа', hover_delay=100)
        Hovertip(a15, 'Нет ответа', hover_delay=100)
        Hovertip(a16, 'Нет ответа', hover_delay=100)
        Hovertip(a17, 'Нет ответа', hover_delay=100)
        Hovertip(a18, 'Нет ответа', hover_delay=100)
        Hovertip(a19, 'Нет ответа', hover_delay=100)
        Hovertip(a20, 'Нет ответа', hover_delay=100)
        end()
    #6
    elif p == 6:
        q6.destroy()
        x6.destroy()
        next6.destroy()
        del6.destroy()
        list6.destroy()
        world5.destroy()
        k6 = 'Ваш ответ: ' + k6
        if k6 != 'Ваш ответ: ':
          Hovertip(a6,k6, hover_delay=100)
        else:
          Hovertip(a6, 'Нет ответа', hover_delay=100)
        if k6 == 'Ваш ответ: Австралии':
            count += 1
            b6.config(text='1')
        Hovertip(a7, 'Нет ответа', hover_delay=100)
        Hovertip(a8, 'Нет ответа', hover_delay=100)
        Hovertip(a9, 'Нет ответа', hover_delay=100)
        Hovertip(a10, 'Нет ответа', hover_delay=100)
        Hovertip(a11, 'Нет ответа', hover_delay=100)
        Hovertip(a12, 'Нет ответа', hover_delay=100)
        Hovertip(a13, 'Нет ответа', hover_delay=100)
        Hovertip(a14, 'Нет ответа', hover_delay=100)
        Hovertip(a15, 'Нет ответа', hover_delay=100)
        Hovertip(a16, 'Нет ответа', hover_delay=100)
        Hovertip(a17, 'Нет ответа', hover_delay=100)
        Hovertip(a18, 'Нет ответа', hover_delay=100)
        Hovertip(a19, 'Нет ответа', hover_delay=100)
        Hovertip(a20, 'Нет ответа', hover_delay=100)
        end()
    #7
    elif p == 7:
        q7.destroy()
        x7.destroy()
        next7.destroy()
        del7.destroy()
        list7.destroy()
        photo7.destroy()
        k7 = 'Ваш ответ: ' + k7
        if k7 != 'Ваш ответ: ':
          Hovertip(a7,k7, hover_delay=100)
        else:
          Hovertip(a7, 'Нет ответа', hover_delay=100)
        if k7 == 'Ваш ответ: Антарктида и Австралия':
            count += 1
            b7.config(text='1')
        Hovertip(a8, 'Нет ответа', hover_delay=100)
        Hovertip(a9, 'Нет ответа', hover_delay=100)
        Hovertip(a10, 'Нет ответа', hover_delay=100)
        Hovertip(a11, 'Нет ответа', hover_delay=100)
        Hovertip(a12, 'Нет ответа', hover_delay=100)
        Hovertip(a13, 'Нет ответа', hover_delay=100)
        Hovertip(a14, 'Нет ответа', hover_delay=100)
        Hovertip(a15, 'Нет ответа', hover_delay=100)
        Hovertip(a16, 'Нет ответа', hover_delay=100)
        Hovertip(a17, 'Нет ответа', hover_delay=100)
        Hovertip(a18, 'Нет ответа', hover_delay=100)
        Hovertip(a19, 'Нет ответа', hover_delay=100)
        Hovertip(a20, 'Нет ответа', hover_delay=100)
        end()
    #8
    elif p == 8:
        q8.destroy()
        next8.destroy()
        del8.destroy()
        list8.destroy()
        x8.destroy()
        pot.destroy()
        if k8 != 'Ваш ответ: ':
          Hovertip(a8,k8, hover_delay=100)
        else:
          Hovertip(a8, 'Нет ответа', hover_delay=100)
        if k8 == 'Ваш ответ: в Южном':
            count += 1
            b8.config(text='1')
        Hovertip(a9, 'Нет ответа', hover_delay=100)
        Hovertip(a10, 'Нет ответа', hover_delay=100)
        Hovertip(a11, 'Нет ответа', hover_delay=100)
        Hovertip(a12, 'Нет ответа', hover_delay=100)
        Hovertip(a13, 'Нет ответа', hover_delay=100)
        Hovertip(a14, 'Нет ответа', hover_delay=100)
        Hovertip(a15, 'Нет ответа', hover_delay=100)
        Hovertip(a16, 'Нет ответа', hover_delay=100)
        Hovertip(a17, 'Нет ответа', hover_delay=100)
        Hovertip(a18, 'Нет ответа', hover_delay=100)
        Hovertip(a19, 'Нет ответа', hover_delay=100)
        Hovertip(a20, 'Нет ответа', hover_delay=100)
        end()
    #9
    elif p == 9:
        q9.destroy()
        next9.destroy()
        del9.destroy()
        list9.destroy()
        x9.destroy()
        pot.destroy()
        k9 = 'Ваш ответ: ' + k9
        if k9 != 'Ваш ответ: ':
          Hovertip(a9,k9, hover_delay=100)
        else:
          Hovertip(a9, 'Нет ответа', hover_delay=100)
        if k9 == 'Ваш ответ: Евразия':
            count += 1
            b9.config(text='1')
        Hovertip(a10, 'Нет ответа', hover_delay=100)
        Hovertip(a11, 'Нет ответа', hover_delay=100)
        Hovertip(a12, 'Нет ответа', hover_delay=100)
        Hovertip(a13, 'Нет ответа', hover_delay=100)
        Hovertip(a14, 'Нет ответа', hover_delay=100)
        Hovertip(a15, 'Нет ответа', hover_delay=100)
        Hovertip(a16, 'Нет ответа', hover_delay=100)
        Hovertip(a17, 'Нет ответа', hover_delay=100)
        Hovertip(a18, 'Нет ответа', hover_delay=100)
        Hovertip(a19, 'Нет ответа', hover_delay=100)
        Hovertip(a20, 'Нет ответа', hover_delay=100)
        end()
    #10
    elif p == 10:
        q10.destroy()
        next10.destroy()
        del10.destroy()
        list10.destroy()
        x10.destroy()
        pot.destroy()
        k10 = 'Ваш ответ: ' + k10
        if k10 != 'Ваш ответ: ':
          Hovertip(a10,k10, hover_delay=100)
        else:
          Hovertip(a10, 'Нет ответа', hover_delay=100)
        if k10 == 'Ваш ответ: Африку и Южную Америку':
            count += 1
            b10.config(text='1')
        Hovertip(a11, 'Нет ответа', hover_delay=100)
        Hovertip(a12, 'Нет ответа', hover_delay=100)
        Hovertip(a13, 'Нет ответа', hover_delay=100)
        Hovertip(a14, 'Нет ответа', hover_delay=100)
        Hovertip(a15, 'Нет ответа', hover_delay=100)
        Hovertip(a16, 'Нет ответа', hover_delay=100)
        Hovertip(a17, 'Нет ответа', hover_delay=100)
        Hovertip(a18, 'Нет ответа', hover_delay=100)
        Hovertip(a19, 'Нет ответа', hover_delay=100)
        Hovertip(a20, 'Нет ответа', hover_delay=100)
        end()
    #11
    elif p == 11:
        q11.destroy()
        next11.destroy()
        del11.destroy()
        list11.destroy()
        x11.destroy()
        pot.destroy()
        k11 = 'Ваш ответ: ' + k11
        if k11 != 'Ваш ответ: ':
          Hovertip(a11,k11, hover_delay=100)
        else:
          Hovertip(a11, 'Нет ответа', hover_delay=100)
        if k11 == 'Ваш ответ: Северная Америка и Евразия':
            count += 1
            b11.config(text='1')
        Hovertip(a12, 'Нет ответа', hover_delay=100)
        Hovertip(a13, 'Нет ответа', hover_delay=100)
        Hovertip(a14, 'Нет ответа', hover_delay=100)
        Hovertip(a15, 'Нет ответа', hover_delay=100)
        Hovertip(a16, 'Нет ответа', hover_delay=100)
        Hovertip(a17, 'Нет ответа', hover_delay=100)
        Hovertip(a18, 'Нет ответа', hover_delay=100)
        Hovertip(a19, 'Нет ответа', hover_delay=100)
        Hovertip(a20, 'Нет ответа', hover_delay=100)
        end()
    #12
    elif p == 12:
        q12.destroy()
        next12.destroy()
        del12.destroy()
        list12.destroy()
        x12.destroy()
        log.destroy()
        k12 = 'Ваш ответ: ' + k12
        if k12 != 'Ваш ответ: ':
          Hovertip(a12,k12, hover_delay=100)
        else:
          Hovertip(a12, 'Нет ответа', hover_delay=100)
        if k12 == 'Ваш ответ: единый северный материк в прошлом, на месте нынешних Евразии и Северной Америки':
            count += 1
            b12.config(text='1')
        Hovertip(a13, 'Нет ответа', hover_delay=100)
        Hovertip(a14, 'Нет ответа', hover_delay=100)
        Hovertip(a15, 'Нет ответа', hover_delay=100)
        Hovertip(a16, 'Нет ответа', hover_delay=100)
        Hovertip(a17, 'Нет ответа', hover_delay=100)
        Hovertip(a18, 'Нет ответа', hover_delay=100)
        Hovertip(a19, 'Нет ответа', hover_delay=100)
        Hovertip(a20, 'Нет ответа', hover_delay=100)
        end()
    #13
    elif p == 13:
        q13.destroy()
        next13.destroy()
        del13.destroy()
        list13.destroy()
        x13.destroy()
        log.destroy()
        k13 = 'Ваш ответ: ' + k13
        if k13 != 'Ваш ответ: ':
          Hovertip(a13,k13, hover_delay=100)
        else:
          Hovertip(a13, 'Нет ответа', hover_delay=100)
        if k13 == 'Ваш ответ: название единого древнего материка в южном полушарии':
            count += 1
            b13.config(text='1')
        Hovertip(a14, 'Нет ответа', hover_delay=100)
        Hovertip(a15, 'Нет ответа', hover_delay=100)
        Hovertip(a16, 'Нет ответа', hover_delay=100)
        Hovertip(a17, 'Нет ответа', hover_delay=100)
        Hovertip(a18, 'Нет ответа', hover_delay=100)
        Hovertip(a19, 'Нет ответа', hover_delay=100)
        Hovertip(a20, 'Нет ответа', hover_delay=100)
        end()
    #14
    elif p == 14:
        q14.destroy()
        next14.destroy()
        del14.destroy()
        list14.destroy()
        x14.destroy()
        log.destroy()
        k14 = 'Ваш ответ: ' + k14
        if k14 != 'Ваш ответ: ':
            Hovertip(a14,k14, hover_delay=100)
        else:
          Hovertip(a14, 'Нет ответа', hover_delay=100)
        if k14 == 'Ваш ответ: Евразия':
            count += 1
            b14.config(text='1')
        Hovertip(a15, 'Нет ответа', hover_delay=100)
        Hovertip(a16, 'Нет ответа', hover_delay=100)
        Hovertip(a17, 'Нет ответа', hover_delay=100)
        Hovertip(a18, 'Нет ответа', hover_delay=100)
        Hovertip(a19, 'Нет ответа', hover_delay=100)
        Hovertip(a20, 'Нет ответа', hover_delay=100)
        end()
    #15
    elif p == 15:
        q15.destroy()
        next15.destroy()
        del15.destroy()
        list15.destroy()
        x15.destroy()
        top.destroy()
        k15 = 'Ваш ответ: ' + k15
        if k15 != 'Ваш ответ: ':
          Hovertip(a15,k15, hover_delay=100)
        else:
          Hovertip(a15, 'Нет ответа', hover_delay=100)
        if k15 == 'Ваш ответ: Африка':
            count += 1
            b15.config(text='1')
        Hovertip(a16, 'Нет ответа', hover_delay=100)
        Hovertip(a17, 'Нет ответа', hover_delay=100)
        Hovertip(a18, 'Нет ответа', hover_delay=100)
        Hovertip(a19, 'Нет ответа', hover_delay=100)
        Hovertip(a20, 'Нет ответа', hover_delay=100)
        end()
    #16
    elif p == 16:
        q16.destroy()
        next16.destroy()
        del16.destroy()
        list16.destroy()
        x16.destroy()
        war.destroy()
        k16 = 'Ваш ответ: ' + k16
        if k16 != 'Ваш ответ: ':
          Hovertip(a16,k16, hover_delay=100)
        else:
          Hovertip(a16, 'Нет ответа', hover_delay=100)
        if k16 == 'Ваш ответ: Антарктида':
            count += 1
            b16.config(text='1')
        Hovertip(a17, 'Нет ответа', hover_delay=100)
        Hovertip(a18, 'Нет ответа', hover_delay=100)
        Hovertip(a19, 'Нет ответа', hover_delay=100)
        Hovertip(a20, 'Нет ответа', hover_delay=100)
        end()
    #17
    elif p == 17:
        q17.destroy()
        next17.destroy()
        del17.destroy()
        list17.destroy()
        x17.destroy()
        tep.destroy()
        k17 = 'Ваш ответ: ' + k17
        if k17 != 'Ваш ответ: ':
          Hovertip(a17,k17, hover_delay=100)
        else:
          Hovertip(a17, 'Нет ответа', hover_delay=100)
        if k17 == 'Ваш ответ: в холодном и умеренном':
            count += 1
            b17.config(text='1')
        Hovertip(a18, 'Нет ответа', hover_delay=100)
        Hovertip(a19, 'Нет ответа', hover_delay=100)
        Hovertip(a20, 'Нет ответа', hover_delay=100)
        end()
    #18
    elif p == 18:
        q18.destroy()
        next18.destroy()
        del18.destroy()
        list18.destroy()
        x18.destroy()
        ward.destroy()
        k18 = 'Ваш ответ: ' + k18
        if k18 != 'Ваш ответ: ':
          Hovertip(a18,k18, hover_delay=100)
        else:
          Hovertip(a18, 'Нет ответа', hover_delay=100)
        if k18 == 'Ваш ответ: Евразия':
            count += 1
            b18.config(text='1')
        Hovertip(a19, 'Нет ответа', hover_delay=100)
        Hovertip(a20, 'Нет ответа', hover_delay=100)
        end()
    #19
    elif p == 19:
        q19.destroy()
        next19.destroy()
        del19.destroy()
        list19.destroy()
        x19.destroy()
        ward.destroy()
        k19 = 'Ваш ответ: ' + k19
        if k19 != 'Ваш ответ: ':
          Hovertip(a19,k19, hover_delay=100)
        else:
          Hovertip(a19, 'Нет ответа', hover_delay=100)
        if k19 == 'Ваш ответ: океанами и морями':
            count += 1
            b19.config(text='1')
        Hovertip(a20, 'Нет ответа', hover_delay=100)
        end()
    #20
    elif p == 20:
        q20.destroy()
        next20.destroy()
        del20.destroy()
        list20.destroy()
        x20.destroy()
        ward.destroy()
        k20 = 'Ваш ответ: ' + k20
        if k20 != 'Ваш ответ: ':
            Hovertip(a20,k20, hover_delay=100)
        else:
          Hovertip(a20, 'Нет ответа', hover_delay=100)
        if k20 == 'Ваш ответ: Азия':
            count += 1
            b20.config(text='1')
        end()

    
    



root = Tk()
root.title("Викторина по географии")
root.geometry('1000x400')
root.iconbitmap('pic/map.ico')
root.resizable(width=False, height=False)

# начало
pr = Label(root, text=" ", font=("Arial", 20))
pr.grid(column = 0, row = 0)
r = Label(root, text="                      ", font=("Arial",25))
r.grid(column = 4, row = 3)
d = Button(root, text= "Начать", command = H, font=("Arial",16))
d.grid(column = 5, row = 3)
g = Label(root, text="Викторина по географии", font=("Arial",25))
g.grid(column = 3, row = 2)
IT2 = PhotoImage(file = 'pic/emblem.gif')
IT = Label(root,image = IT2)
IT.grid(column = 3, row = 1)
c = Label(root,text= "                                                                                                   ")
c.grid(column = 2, row = 2)
v = Button(root, text= "Выйти", command = exid, font=("Arial",16))
v.grid(column = 2, row = 3)

# 1
x1 = Label(root, text="Вопрос номер 1", font=("Arial",15))
q1 = Label(root, text="К материкам не относится:", font=("Arial",15))
next1 = Button(root, text= "Далее", command = fo1, font=("Arial",16))
del1 = Button(root, text= "Завершить сейчас", command = end2, font=("Arial",16))
list1 = Listbox(width = 90, height = 4)
wor11 = PhotoImage(file = 'pic/мир1.png')
world = Label(root,image = wor11)

#2
x2 = Label(root, text="Вопрос номер 2", font=("Arial",15))
q2 = Label(root, text="Как принято подразделять материки?", font=("Arial",15))
next2 = Button(root, text= "Далее", command = fo2, font=("Arial",16))
del2 = Button(root, text= "Завершить сейчас", command = end2, font=("Arial",16))
list2 = Listbox(width = 90, height = 4)

#3
x3 = Label(root, text="Вопрос номер 3", font=("Arial",15))
q3 = Label(root, text="Сколько всего насчитывается их на нашей планете?", font=("Arial",15))
next3 = Button(root, text= "Далее", command = fo3, font=("Arial",16))
del3 = Button(root, text= "Завершить сейчас", command = end2, font=("Arial",16))
list3 = Listbox(width = 90, height = 4)

#4
x4 = Label(root, text="Вопрос номер 4", font=("Arial",15))
q4 = Label(root, text="Особенностью материка под названием «Антарктида» является то, что он …", font=("Arial",15))
next4 = Button(root, text= "Далее", command = fo4, font=("Arial",16))
del4 = Button(root, text= "Завершить сейчас", command = end2, font=("Arial",16))
list4 = Listbox(width = 90, height = 4)
an11 = PhotoImage(file = 'pic/ан.png')
an = Label(root,image = an11)


#5
x5 = Label(root, text="Вопрос номер 5", font=("Arial",15))
q5 = Label(root, text="По площади самые масштабные — это … (смотри подсказку на рисунке)", font=("Arial",15))
next5 = Button(root, text= "Далее", command = fo5, font=("Arial",16))
del5 = Button(root, text= "Завершить сейчас", command = end2, font=("Arial",16))
list5 = Listbox(width = 90, height = 4)
photo55 = PhotoImage(file = 'pic/5.png')
photo5 = Label(root,image = photo55)

#6
x6 = Label(root, text="Вопрос номер 6", font=("Arial",15))
q6 = Label(root, text="К нижнему своему краю сужаются все, кроме Антарктиды и …", font=("Arial",15))
next6 = Button(root, text= "Далее", command = fo6, font=("Arial",16))
del6 = Button(root, text= "Завершить сейчас", command = end2, font=("Arial",16))
list6 = Listbox(width = 90, height = 4)
wr = PhotoImage(file = 'pic/мир1.png')
world5 = Label(root,image = wr)

#7
x7 = Label(root, text="Вопрос номер 7", font=("Arial",15))
q7 = Label(root, text="Наименьшую площадь (представлены на рисунке) имеют:", font=("Arial",15))
next7 = Button(root, text= "Далее", command = fo7, font=("Arial",16))
del7 = Button(root, text= "Завершить сейчас", command = end2, font=("Arial",16))
list7 = Listbox(width = 90, height = 4)
photo77 = PhotoImage(file = 'pic/7.png')
photo7 = Label(root,image = photo77)

#8
x8 = Label(root, text="Вопрос номер 8", font=("Arial",15))
q8 = Label(root, text="В этом полушарии суша занимает меньшее пространство", font=("Arial",15))
next8 = Button(root, text= "Далее", command = fo8, font=("Arial",16))
del8 = Button(root, text= "Завершить сейчас", command = end2, font=("Arial",16))
list8 = Listbox(width = 90, height = 4)
po = PhotoImage(file = 'pic/пол1.png')
pot = Label(root,image = po)

#9
x9 = Label(root, text="Вопрос номер 9", font=("Arial",15))
q9 = Label(root, text="К южным не относится материк под названием:", font=("Arial",15))
next9 = Button(root, text= "Далее", command = fo9, font=("Arial",16))
del9 = Button(root, text= "Завершить сейчас", command = end2, font=("Arial",16))
list9 = Listbox(width = 90, height = 4)

#10
x10 = Label(root, text="Вопрос номер 10", font=("Arial",15))
q10 = Label(root, text="Экватор проходит через ...", font=("Arial",15))
next10 = Button(root, text= "Далее", command = fo10, font=("Arial",16))
del10 = Button(root, text= "Завершить сейчас", command = end2, font=("Arial",16))
list10 = Listbox(width = 90, height = 4)

#11
x11 = Label(root, text="Вопрос номер 11", font=("Arial",15))
q11 = Label(root, text="Полностью расположены в Северном полушарии:", font=("Arial",15))
next11 = Button(root, text= "Далее", command = fo11, font=("Arial",16))
del11 = Button(root, text= "Завершить сейчас", command = end2, font=("Arial",16))
list11 = Listbox(width = 90, height = 4)

#12
x12 = Label(root, text="Вопрос номер 12", font=("Arial",15))
q12 = Label(root, text="Лавразия — это:", font=("Arial",15))
next12 = Button(root, text= "Далее", command = fo12, font=("Arial",16))
del12 = Button(root, text= "Завершить сейчас", command = end2, font=("Arial",16))
list12 = Listbox(width = 90, height = 4)
lg = PhotoImage(file = 'pic/лг.png')
log = Label(root,image = lg)

#13
x13 = Label(root, text="Вопрос номер 13", font=("Arial",15))
q13 = Label(root, text="Что такое Гондвана? Это ..", font=("Arial",15))
next13 = Button(root, text= "Далее", command = fo13, font=("Arial",16))
del13 = Button(root, text= "Завершить сейчас", command = end2, font=("Arial",16))
list13 = Listbox(width = 90, height = 4)

#14
x14 = Label(root, text="Вопрос номер 14", font=("Arial",15))
q14 = Label(root, text="Какой материк, по мнению учёных, в палеозойскую эру НЕ был покрыт ледниками?", font=("Arial",15))
next14 = Button(root, text= "Далее", command = fo14, font=("Arial",16))
del14 = Button(root, text= "Завершить сейчас", command = end2, font=("Arial",16))
list14 = Listbox(width = 90, height = 4)
tp = PhotoImage(file = 'pic/тп.png')
top = Label(root,image = tp)

#15
x15 = Label(root, text="Вопрос номер 15", font=("Arial",15))
q15 = Label(root, text="По карте тепловых поясов самой жаркой является:", font=("Arial",15))
next15 = Button(root, text= "Далее", command = fo15, font=("Arial",16))
del15 = Button(root, text= "Завершить сейчас", command = end2, font=("Arial",16))
list15 = Listbox(width = 90, height = 4)

#16
x16 = Label(root, text="Вопрос номер 16", font=("Arial",15))
q16 = Label(root, text="Как называется самый южный материк?", font=("Arial",15))
next16 = Button(root, text= "Далее", command = fo16, font=("Arial",16))
del16 = Button(root, text= "Завершить сейчас", command = end2, font=("Arial",16))
list16 = Listbox(width = 90, height = 4)
war = Label(root,image = wor11)

#17
x17 = Label(root, text="Вопрос номер 17", font=("Arial",15))
q17 = Label(root, text="В каких тепловых поясах расположены широкие части Евразии?", font=("Arial",15))
next17 = Button(root, text= "Далее", command = fo17, font=("Arial",16))
del17 = Button(root, text= "Завершить сейчас", command = end2, font=("Arial",16))
list17 = Listbox(width = 90, height = 4)
tep = Label(root,image = tp)

#18
x18 = Label(root, text="Вопрос номер 18", font=("Arial",15))
q18 = Label(root, text="На каком материке находится столица России?", font=("Arial",15))
next18 = Button(root, text= "Далее", command = fo18, font=("Arial",16))
del18 = Button(root, text= "Завершить сейчас", command = end2, font=("Arial",16))
list18 = Listbox(width = 90, height = 4)

#19
x19 = Label(root, text="Вопрос номер 19", font=("Arial",15))
q19 = Label(root, text="Материком является участок суши, со всех сторон окружённый:", font=("Arial",15))
next19 = Button(root, text= "Далее", command = fo19, font=("Arial",16))
del19 = Button(root, text= "Завершить сейчас", command = end2, font=("Arial",16))
list19 = Listbox(width = 90, height = 4)
ward = Label(root,image = wor11)

#20
x20 = Label(root, text="Вопрос номер 20", font=("Arial",15))
q20 = Label(root, text="Материком не является:", font=("Arial",15))
next20 = Button(root, text= "Завершить викторину", command = end, font=("Arial",16))
del20 = Button(root, text= "Выйти", command = exid, font=("Arial",16))
list20 = Listbox(width = 90, height = 4)

#end

resy = Label(root, text=str(count), bg='#afeeee',font=("Arial"))
d1 = Label(root,bg='#afeeee', text="1", font=("Arial"))
a1 = Label(root,bg='#afeeee',text="Арктика                                                                                                                                             ", font=("Arial"))
k1 = 'Нет ответа'
b1 = Label(root, bg='#afeeee',text='0', font=("Arial"))

  

d2 = Label(root, text="2", font=("Arial"))
a2 = Label(root, text="по расположению в Северном или Южном полушарии                                                           ", font=("Arial"))
k2 = 'Нет ответа'
b2 = Label(root, text='0', font=("Arial"))
  

d3 = Label(root, bg='#afeeee',text="3", font=("Arial"))
a3 = Label(root,bg='#afeeee', text="шесть                                                                                                                                                 ", font=("Arial"))
k3 = 'Нет ответа'
b3 = Label(root, bg='#afeeee',text='0', font=("Arial"))
  

d4 = Label(root, text="4", font=("Arial"))
a4 = Label(root, text="покрыт ледяным панцирем                                                                                                            ", font=("Arial"))
k4 = 'Нет ответа'
b4 = Label(root, text='0', font=("Arial"))
  

d5 = Label(root, bg='#afeeee',text="5", font=("Arial"))
a5 = Label(root, bg='#afeeee',text="Евразия, затем Африка                                                                                                                 ", font=("Arial"))
k5 = 'Нет ответа'
b5 = Label(root, bg='#afeeee',text='0', font=("Arial"))
  

d6 = Label(root, text="6", font=("Arial"))
a6 = Label(root, text="Австралии                                                                                                                                         ", font=("Arial"))
k6 = 'Нет ответа'
b6 = Label(root, text='0', font=("Arial"))
  

d7 = Label(root, bg='#afeeee',text="7", font=("Arial"))
a7 = Label(root,bg='#afeeee', text="Антарктида и Австралия                                                                                                               ", font=("Arial"))
k7 = 'Нет ответа'
b7 = Label(root,bg='#afeeee', text='0', font=("Arial"))


d8 = Label(root, text="8", font=("Arial"))
a8 = Label(root, text="в Южном                                                                                                                                           ", font=("Arial"))
k8 = 'Нет ответа'
b8 = Label(root, text='0', font=("Arial"))


d9 = Label(root, bg='#afeeee',text="9", font=("Arial"))
a9 = Label(root,bg='#afeeee', text="Евразия                                                                                                                                            ", font=("Arial"))
k9 = 'Нет ответа'
b9 = Label(root,bg='#afeeee', text='0', font=("Arial"))


d10 = Label(root, text="10", font=("Arial"))
a10 = Label(root, text="Африку и Южную Америку                                                                                                            ", font=("Arial"))
k10 = 'Нет ответа'
b10 = Label(root, text='0', font=("Arial"))


d11 = Label(root,bg='#afeeee', text="11", font=("Arial"))
a11 = Label(root,bg='#afeeee', text="Северная Америка и Евразия                                                                                                   ", font=("Arial"))
k11 = 'Нет ответа'
b11 = Label(root,bg='#afeeee', text='0', font=("Arial"))


d12 = Label(root, text="12", font=("Arial"))
a12 = Label(root, text="единый северный материк в прошлом, на месте нынешних Евразии и Северной Америки ", font=("Arial"))
k12 = 'Нет ответа'
b12 = Label(root, text='0', font=("Arial"))


d13 = Label(root,bg='#afeeee', text="13", font=("Arial"))
a13 = Label(root,bg='#afeeee', text="название единого древнего материка в южном полушарии                                                    ", font=("Arial"))
k13 = 'Нет ответа'
b13 = Label(root,bg='#afeeee', text='0', font=("Arial"))


d14 = Label(root, text="14", font=("Arial"))
a14 = Label(root, text="Евразия                                                                                                                                             ", font=("Arial"))
k14 = 'Нет ответа'
b14 = Label(root, text='0', font=("Arial"))


d15 = Label(root,bg='#afeeee', text="15", font=("Arial"))
a15 = Label(root,bg='#afeeee', text="Африка                                                                                                                                            ", font=("Arial"))
k15 = 'Нет ответа'
b15 = Label(root,bg='#afeeee', text='0', font=("Arial"))


d16 = Label(root, text="16", font=("Arial"))
a16 = Label(root, text="Антарктида                                                                                                                                      ", font=("Arial"))
k16 = 'Нет ответа'
b16 = Label(root, text='0', font=("Arial"))


d17 = Label(root,bg='#afeeee', text="17", font=("Arial"))
a17 = Label(root,bg='#afeeee', text="в холодном и умеренном                                                                                                            ", font=("Arial"))
k17 = 'Нет ответа'
b17 = Label(root,bg='#afeeee', text='0', font=("Arial"))

  
d18 = Label(root, text="18", font=("Arial"))
a18 = Label(root, text="Евразия                                                                                                                                           ", font=("Arial"))
k18 = 'Нет ответа'
b18 = Label(root, text='0', font=("Arial"))


d19 = Label(root,bg='#afeeee', text="19", font=("Arial"))
a19 = Label(root,bg='#afeeee', text="океанами и морями                                                                                                                      ", font=("Arial"))
k19 = 'Нет ответа'
b19 = Label(root,bg='#afeeee', text='0', font=("Arial"))

  
d20 = Label(root, text="20", font=("Arial"))
a20 = Label(root, text="Азия                                                                                                                                                   ", font=("Arial"))
k20 = 'Нет ответа'
b20 = Label(root, text='0', font=("Arial"))

  
num = Label(root, text="Номер вопроса", font=("Arial"))
it = Label(root,bg='#afeeee', text="Итог", font=("Arial"))
tru = Label(root, text="Правильный ответ", font=("Arial"))
yan = Label(root, text="Ваш ответ", font=("Arial"))
resl = Label(root, text="Балл", font=("Arial"))


root.mainloop()
