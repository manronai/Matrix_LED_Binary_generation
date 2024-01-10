
def buttonprint():
    for y in range(1, 8):
        for i in range(1, 6):
            print(f'ttk.Button(win, text= "o", width=5, command=show_msg{y}{i}).place(x={i * 50}, y={y * 50})')


def functionprint():

    for y in range(1, 8):
        for i in range(1, 6):
            s = f"""def show_msg{y}{i}():
        l.append("{8-y-1},{i-1}")
        global c
        c += 1
        ct = str(c)
        label.config(text=ct)"""
            print(s)



def t():
    s = """6,4
6,3
6,2
6,1
5,0
4,0
3,1
3,2
3,3
2,4
1,4
0,3
0,2
0,1 
0,0"""
    print(s.replace("\n", " "))

functionprint()
