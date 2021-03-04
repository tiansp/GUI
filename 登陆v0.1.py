import tkinter as tk
import tkinter.messagebox

def check():
    pass

def denglu():
    user = en1.get()
    password = en2.get()

    if user == "123" and password == '123':
        tk.messagebox.showinfo(title='welcome!',message='success login in ')
    else:
        tk.messagebox.showinfo(title='error!', message='your password is wrong, try again. ')
def zhuce_show():
    root2 = tk.Toplevel(root)
    root2.title('注册')

    v3 = tk.StringVar()
    v4 = tk.StringVar()
    v5 = tk.StringVar()

    fram1 = tk.Frame(root2)
    l1 = tk.Label(fram1, text='账号:')
    en1 = tk.Entry(fram1, textvariable=v3)
    fram1.grid(row=0, column=0)
    l1.grid(row=0, column=0, padx=5, pady=5)
    en1.grid(row=0, column=1, padx=5)

    fram2 = tk.Frame(root2)
    l2 = tk.Label(fram2, text='密码:')
    en2 = tk.Entry(fram2, textvariable=v4, show='*')
    fram2.grid(row=1, column=0)
    l2.grid(row=1, column=0, padx=5, pady=5)
    en2.grid(row=1, column=1, padx=5)

    fram3 = tk.Frame(root2)
    fram3.grid(row=3, column=0)
    bn1 = tk.Button(fram3, text='确认', command=check).grid(row=3, column=0, padx=57, pady=5)


root = tk.Tk()
root.title("登陆")
# root.geometry("400x300")

v1 = tk.StringVar()
v2 = tk.StringVar()

fram1 = tk.Frame(root)
l1 = tk.Label(fram1,text = '账号:')
en1 = tk.Entry(fram1,textvariable = v1)
fram1.grid(row = 0,column = 0)
l1.grid(row = 0 ,column = 0,padx = 5,pady = 5)
en1.grid(row = 0,column = 1,padx = 5)

fram2 = tk.Frame(root)
l2 = tk.Label(fram2,text = '密码:')
en2 = tk.Entry(fram2,textvariable = v2,show = '*')
fram2.grid(row = 1,column = 0)
l2.grid(row = 1 ,column = 0,padx = 5,pady = 5)
en2.grid(row = 1,column = 1,padx = 5)

fram3 = tk.Frame(root)

fram3.grid(row = 2,column = 0)
bn1 = tk.Button(fram3,text = '登陆',command = denglu).grid(row  = 0,column = 0,padx = 57,pady = 5)
bn2 = tk.Button(fram3,text = '注册',command = zhuce_show).grid(row = 0,column = 1,padx = 18,pady = 5)


root.mainloop()

