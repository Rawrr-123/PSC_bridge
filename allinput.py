import pandas as pd
import tkinter as tk
from PIL import Image,ImageTk


    

def allinput():
    def quit():
        main_root.quit()

    main_root=tk.Tk()
    main_canvas=tk.Canvas(main_root,width=300,height=300)
    main_canvas.pack()
    main_root.title("Bridge Inputs")
    logo=ImageTk.PhotoImage(file="Images\logo.png")
    main_root.iconphoto(False,logo)

    ############Buttons######################

    button1 = tk.Button(text='Permanent Cross Section Inputs', command=tkinput)    
    button2 = tk.Button(text='Span and Number of Sections Input', command=spaninput)
    button3 = tk.Button(text='Discharge Input', command=dischargeinput)

    button_quit = tk.Button(text='Exit',command=quit)
    main_canvas.create_window(150, 50, window=button1)
    main_canvas.create_window(150, 100, window=button2)
    main_canvas.create_window(150, 150, window=button3)

    main_canvas.create_window(150, 250, window=button_quit)
    main_root.mainloop()

    
def tkinput():
    length=[]
    height=[]

    root = tk.Toplevel()

    canvas1 = tk.Canvas(root, width=1000, height=500)
    canvas1.pack()
    root.title("Section Input")

    img=tk.PhotoImage(file="Images/Section.png")
    # logo=ImageTk.PhotoImage(file="Images\logo.png")
    # root.iconphoto(False,logo)

    canvas1.create_image(700,250,image=img)

    l1 = tk.Label(root, text='Width(m)→')
    canvas1.create_window(160, 75, window=l1)
    l2 = tk.Label(root, text='Length(m)↑')
    canvas1.create_window(300, 75, window=l2)



    l3 = tk.Label(root, text='Section 1')
    canvas1.create_window(50, 100, window=l3)
    e1 = tk.Entry(root)
    canvas1.create_window(160, 100, window=e1)
    e2 = tk.Entry(root)
    canvas1.create_window(300, 100, window=e2)

    l4 = tk.Label(root, text='Section 2')
    canvas1.create_window(50, 125, window=l4)
    e3 = tk.Entry(root)
    canvas1.create_window(160, 125, window=e3)
    e4 = tk.Entry(root)
    canvas1.create_window(300, 125, window=e4)


    l5 = tk.Label(root, text='Section 3')
    canvas1.create_window(50, 150, window=l5)
    e5 = tk.Entry(root)
    canvas1.create_window(160, 150, window=e5)
    e6 = tk.Entry(root)
    canvas1.create_window(300, 150, window=e6)


    l6 = tk.Label(root, text='Section 4')
    canvas1.create_window(50, 175, window=l6)
    e7 = tk.Entry(root)
    canvas1.create_window(160, 175, window=e7)
    e8 = tk.Entry(root)
    canvas1.create_window(300, 175, window=e8)


    l7 = tk.Label(root, text='Section 5')
    canvas1.create_window(50, 200, window=l7)
    e9 = tk.Entry(root)
    canvas1.create_window(160, 200, window=e9)
    e10 = tk.Entry(root)
    canvas1.create_window(300, 200, window=e10)

    l8 = tk.Label(root, text='Section 6')
    canvas1.create_window(50, 225, window=l8)
    e11 = tk.Entry(root)
    canvas1.create_window(160, 225, window=e11)
    e12 = tk.Entry(root)
    canvas1.create_window(300, 225, window=e12)

    l9 = tk.Label(root, text='Section 7')
    canvas1.create_window(50, 250, window=l9)
    e13 = tk.Entry(root)
    canvas1.create_window(160, 250, window=e13)
    e14 = tk.Entry(root)
    canvas1.create_window(300, 250, window=e14)


    l10 = tk.Label(root, text='Section 8')
    canvas1.create_window(50, 275, window=l10)
    e15 = tk.Entry(root)
    canvas1.create_window(160, 275, window=e15)
    e16 = tk.Entry(root)
    canvas1.create_window(300, 275, window=e16)


    l11 = tk.Label(root, text='Section 9')
    canvas1.create_window(50, 300, window=l11)
    e17 = tk.Entry(root)
    canvas1.create_window(160, 300, window=e17)
    e18 = tk.Entry(root)
    canvas1.create_window(300, 300, window=e18)

    l12 = tk.Label(root, text='Section 10')
    canvas1.create_window(50, 325, window=l12)
    e19 = tk.Entry(root)
    canvas1.create_window(160, 325, window=e19)
    e20 = tk.Entry(root)
    canvas1.create_window(300, 325, window=e20)


    # l13 = tk.Label(root, text='Section 11')
    # canvas1.create_window(50, 350, window=l13)
    # e21 = tk.Entry(root)
    # canvas1.create_window(160, 350, window=e21)
    # e22 = tk.Entry(root)
    # canvas1.create_window(300, 350, window=e22)


    l14 = tk.Label(root, text='Section 11')
    canvas1.create_window(50, 350, window=l14)
    e23 = tk.Entry(root)
    canvas1.create_window(160, 350, window=e23)
    e24 = tk.Entry(root)
    canvas1.create_window(300, 350, window=e24)


    l15 = tk.Label(root, text='Section 12')
    canvas1.create_window(50, 375, window=l15)
    e25 = tk.Entry(root)
    canvas1.create_window(160, 375, window=e25)
    e26 = tk.Entry(root)
    canvas1.create_window(300, 375, window=e26)


    # l16 = tk.Label(root, text='Section 14')
    # canvas1.create_window(50, 425, window=l16)
    # e27 = tk.Entry(root)
    # canvas1.create_window(160, 425, window=e27)
    # e28 = tk.Entry(root)
    # canvas1.create_window(300, 425, window=e28)


    def entry():
        w1=float(e1.get())
        l1=float(e2.get())
        w2=float(e3.get())
        l2=float(e4.get())
        w3=float(e5.get())
        l3=float(e6.get())
        w4=float(e7.get())
        l4=float(e8.get())
        w5=float(e9.get())
        l5=float(e10.get())
        w6=float(e11.get())
        l6=float(e12.get())
        w7=float(e13.get())
        l7=float(e14.get())
        w8=float(e15.get())
        l8=float(e16.get())
        w9=float(e17.get())
        l9=float(e18.get())
        w10=float(e19.get())
        l10=float(e20.get())
        # w11=float(e21.get())
        # l11=float(e22.get())
        w12=float(e23.get())
        l12=float(e24.get())
        w13=float(e25.get())
        l13=float(e26.get())
        # w14=float(e27.get())
        # l14=float(e28.get())
        length.extend([w1,w2,w3,w4,w10,w13,w9,w12,w5,w6,w7,w8])
        height.extend([l1,l2,l3,l4,l10,l13,l9,l12,l5,l6,l7,l8])
        root.quit()
    button4 = tk.Button(root,text='Input', command=entry)
    canvas1.create_window(225, 475, window=button4)

    root.mainloop()
    df=pd.DataFrame(length,height).T
    df.to_excel('Saved Inputs/box.xlsx',encoding='utf-8',index_label='Columns',index=False)

def spaninput():
    span_root = tk.Toplevel()
    span_canvas = tk.Canvas(span_root,width=300,height=250)
    span_canvas.pack()
    span_root.title("Span and Number of Section")


    l1 = tk.Label(span_root, text='Span(m)')
    span_canvas.create_window(75, 75, window=l1)

    l2 = tk.Label(span_root, text='No of sections')
    span_canvas.create_window(75, 125, window=l2)

    e1 = tk.Entry(span_root)
    span_canvas.create_window(190, 75, window=e1)

    e2 = tk.Entry(span_root)
    span_canvas.create_window(190, 125, window=e2)

   
    def entry():
        s1=float(e1.get())
        s2=float(e2.get())
        span_root.destroy()
        df=pd.DataFrame({s1,s2})
        df.to_excel('Saved Inputs/span.xlsx',encoding='utf-8',index_label='Columns',index=False)

    button4 = tk.Button(span_root,text='Input', command=entry)
    span_canvas.create_window(150, 175, window=button4)

def dischargeinput():
    discharge_root = tk.Toplevel()
    discharge_canvas = tk.Canvas(discharge_root,width=300,height=250)
    discharge_canvas.pack()
    discharge_root.title("Discharge")


    l1 = tk.Label(discharge_root, text='Discharge(m³/s)')
    discharge_canvas.create_window(75, 75, window=l1)

    e1 = tk.Entry(discharge_root)
    discharge_canvas.create_window(190, 75, window=e1)

   
    def entry():
        s1=float(e1.get())
        discharge_root.destroy()
        discharge_root.quit()
        df=pd.DataFrame({s1})
        df.to_excel('Saved Inputs/discharge.xlsx',encoding='utf-8',index_label='Columns',index=False)

    button4 = tk.Button(discharge_root,text='Input', command=entry)
    discharge_canvas.create_window(150, 175, window=button4)

allinput()