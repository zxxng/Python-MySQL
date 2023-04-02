from tkinter import *

window = Tk()
# window.title("윈도창 연습")
# window.geometry("400x100")
# window.resizable(width=FALSE, height=FALSE)

## 레이블(Label) : 문자를 표현할 수 있는 위젯

# 레이블에 글자 넣기
label1 = Label(window, text = "cookbook~~python을")
label2 = Label(window, text = "열심히", font = ("궁서체",30), fg = "blue")
label3 = Label(window, text = "공부 중입니다.", bg = "magenta", width = 20, height = 5, anchor = SE)

label1.pack()
label2.pack()
label3.pack()

# 레이블에 이미지 넣기
photo = PhotoImage(file = "gif/dog.gif")
label1 = Label(window, image = photo)

label1.pack()

## 버튼(Button) : 마우스로 클릭하면 눌리는 효과와 함께 지정한 작업 실행
button1 = Button(window, text = "파이썬 종료", fg = "red", command =quit)

button1.pack()

# 이미지 버튼을 누르면 간단한 메시지창이 나오는 코드
from tkinter import messagebox

def myFunc():
    messegebox.showinfo("강아지버튼", "강아지가 귀엽죠?^^")

photo = PhotoImage(file = 'gif/dog2.gif')
button2 = Button(window, image = photo, command = myFunc)

button2.pack()

# 체크버튼
def myFunc2():
    if chk.get() == 0:
        messegebox.showinfo("", "체크버튼이 꺼졌어요.")
    else :
        messegebox.showinfo("", "체크버튼이 켜졌어요.")

chk = IntVar()
cb1 = Checkbutton(window, text = "클릭하세요", variable = chk, commend = myFunc2())

cb1.pack()

## 라디오버튼(Radiobutton) : 여러 개 중 하나를 선택하기 위한 위젯
def myFunc3():
    if var.get() == 1:
        label1.configure(text = "파이썬")
    elif var.get() == 2:
        label1.configure(text="C++")
    else : 
        label1.configure(text = "Java")

var = IntVar()
rb1 = Radiobutton(window, text = "파이썬", variable = var, value = 1, command = myFunc3)
rb2 = Radiobutton(window, text = "C++", variable = var, value = 2, command = myFunc3)
rb3 = Radiobutton(window, text = "Java", variable = var, value = 3, command = myFunc3)

label4 = Label*window, text = "선택한 언어 : ", fg = "red")

rb1.pack()
rb2.pack()
rb3.pack()
label4.pack()

# 마우스
def clickLeft(event):
    messagebox.showinfo("마우스, "마우스 왼쪽 버튼이 클림됨")

window.bind("<Button-1>", clickLeft)

# 마우스 시발
def clickMouse(event):
    txt = ""
    if event.num == 1:
        txt += "마우스 왼쪽 버튼이 ("
    elif event.num == 3:
        txt += "마우스 오른쪽 버튼이 ("

    txt += str(event.y) + "," + str(event.x) + ")에서 클릭됨"
    label.configure(text = txt)


window.mainloop()

