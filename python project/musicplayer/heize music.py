import random
from pygame import *
from pygame import mixer
from tkinter import *
from tkinter import messagebox
from tkinter.font import *

# 함수 정의
def rdoplay():
    path='music/'
    if var.get()==1:
        path+=mplay[0]
        label.config(image=photo[0])
    elif var.get()==2:
        path+=mplay[1]
        label.config(image=photo[1])
    elif var.get()==3:
        path+=mplay[2]
        label.config(image=photo[2])
    elif var.get()==4:
        path+=mplay[3]
        label.config(image=photo[3])
    else:
        path+=mplay[4]
        label.config(image=photo[4])

    path+='.mp3'
    mixer.init()
    mixer.music.load(path)
    mixer.music.play()

def play():
    rdoplay()

def stop():
    mixer.music.stop()

def lyric():
    path='lyric/'
    if var.get()==1:
        path+=mplay[0]
    elif var.get()==2:
        path+=mplay[1]
    elif var.get()==3:
        path+=mplay[2]
    elif var.get()==4:
        path+=mplay[3]
    else:
        path+=mplay[4]

    path+='.txt'
    f = open(path,'r',encoding='UTF8')
    line = f.read()
    # 텍스트위젯 출력
    result1.insert('1.0',line)

def randomchic(): # 함수정의
    m=random.choice(mplay)
    while True:
        path=('music/' + m + '.mp3')
        if var.get()==1:
            path+=mplay[0]
            label.config(image=photo[0])
        elif var.get()==2:
            path+=mplay[1]
            label.config(image=photo[1])
        elif var.get()==3:
            path+=mplay[2]
            label.config(image=photo[2])
        elif var.get()==4:
            path+=mplay[3]
            label.config(image=photo[3])
        else:
            path+=mplay[4]
            label.config(image=photo[4])

        mixer.init()
        mixer.music.load(path)
        mixer.music.play()

def endless():
    path='music/'
    if var.get()==1:
        path+=mplay[0]
        label.config(image=photo[0])
    elif var.get()==2:
        path+=mplay[1]
        label.config(image=photo[1])
    elif var.get()==3:
        path+=mplay[2]
        label.config(image=photo[2])
    elif var.get()==4:
        path+=mplay[3]
        label.config(image=photo[3])
    else:
        path+=mplay[4]
        label.config(image=photo[4])

    path+='.mp3'
    mixer.init()
    mixer.music.load(path)
    mixer.music.play()


# 윈도우w 생성
w = Tk()
w.geometry('500x600')
w.title('Heize - Lyricist')
f=Font(family='DX하얀토끼B',size=20)
mplay=['작사가','일이 너무 잘 돼','너의 이름은 (Feat. ASH ISLAND)','1_1440 (Feat. 지샤넬)','Not to see you again.']
photo=[None]*5


for i in range(5):
    path=('photo/'+ mplay[i] +'.png')
    photo[i]=PhotoImage(file=path)

label=Label(w,image=None)
var=IntVar()
rb1=Radiobutton(w,text=mplay[0],font=f,variable=var, value=1,command=rdoplay)
rb2=Radiobutton(w,text=mplay[1],font=f,variable=var, value=2,command=rdoplay)
rb3=Radiobutton(w,text=mplay[2],font=f,variable=var, value=3,command=rdoplay)
rb4=Radiobutton(w,text=mplay[3],font=f,variable=var, value=4,command=rdoplay)
rb5=Radiobutton(w,text=mplay[4],font=f,variable=var, value=5,command=rdoplay)
btn1 = Button(w, text='재생 ▶',fg='sky blue', font=f, command=play)
btn2 = Button(w, text='멈추기 ⏸',fg='sky blue', font=f, command=stop)
btn3 = Button(w, text='랜덤재생',fg='sky blue', font=f, command=randomchic)
btn4 = Button(w, text='가사 보기',fg='gray', font=f, command=lyric)
btn5 = Button(w, text='무한반복',fg='sky blue', font=f, command=endless)

result1 = Text(w, width=30, height=15, font=f, bg='sky blue')
label.pack()
rb1.pack()
rb2.pack()
rb3.pack()
rb4.pack()
rb5.pack()
btn1.pack()
btn2.pack()
btn3.pack()
btn4.pack()
btn5.pack()
result1.pack()

