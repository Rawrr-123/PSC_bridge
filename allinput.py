import pandas as pd
import tkinter as tk
from PIL import Image,ImageTk

def all_input():    

    def ss_design():

        def ss_output():
            def quit_des_super():
                ss_out_root.destroy()

            ss_out_root = tk.Toplevel(ssd_root)
            ss_out_canvas = tk.Canvas(ss_out_root, width=425, height=500)
            ss_out_canvas.pack()
            ss_out_root.title("Superstructure Outputs")

        def ss_input():

            def boxinput():
                length=[]
                height=[]

                root = tk.Toplevel(ss_root)

                canvas1 = tk.Canvas(root, width=1000, height=500)
                canvas1.pack()
                root.title("Box Input")

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
                    df=pd.DataFrame(length,height).T
                    df.to_excel('data/box.xlsx',encoding='utf-8',index_label='Columns',index=False)
                    root.destroy()
                button4 = tk.Button(root,text='Input', command=entry)
                canvas1.create_window(225, 475, window=button4)

                root.mainloop()
                

            def quit11():
                ss_root.destroy()

            ss_root = tk.Toplevel(ssd_root)
            ss_canvas = tk.Canvas(ss_root, width=800, height=500)
            ss_canvas.pack()
            ss_root.title("Superstructure Inputs")


            #######################Extra Inputs####################################
            span_lab=tk.Label(ss_root,text='Span Inputs',font='Calibri')
            ss_canvas.create_window(75, 50, window=span_lab)

            ss_canvas.create_rectangle(15,50,400,100)

            label_span = tk.Label(ss_root, text='Span(m)')
            ss_canvas.create_window(100, 75, window=label_span)

            e_span = tk.Entry(ss_root)
            ss_canvas.create_window(190, 75, window=e_span)


            bearing_label=tk.Label(ss_root,text='Bearing Inputs',font='Calibri')
            ss_canvas.create_window(100,125,window=bearing_label)

            l_bear_len = tk.Label(ss_root, text='Length(m)')
            ss_canvas.create_window(75, 150, window=l_bear_len)

            ss_canvas.create_rectangle(15,125,400,225)

            e_bear_len = tk.Entry(ss_root)
            ss_canvas.create_window(190, 150, window=e_bear_len)

            l_bear_wid = tk.Label(ss_root, text='Width(m)')
            ss_canvas.create_window(75, 175, window=l_bear_wid)
            
            e_bear_wid = tk.Entry(ss_root)
            ss_canvas.create_window(190, 175, window=e_bear_wid)

            l_bear_dist = tk.Label(ss_root, text='C/C distance(m)')
            ss_canvas.create_window(75, 200, window=l_bear_dist)
            
            e_bear_dist = tk.Entry(ss_root)
            ss_canvas.create_window(190, 200, window=e_bear_dist)

            ss_canvas.create_rectangle(15,250,400,325)


            mat_label=tk.Label(ss_root,text='Material Inputs',font='Calibri')
            ss_canvas.create_window(100,250,window=mat_label)


            l1_mat = tk.Label(ss_root, text='fck(MPa)')
            ss_canvas.create_window(75, 275, window=l1_mat)

            e1_mat = tk.Entry(ss_root)
            ss_canvas.create_window(190, 275, window=e1_mat)

            l2_mat = tk.Label(ss_root, text='fy(MPa)')
            ss_canvas.create_window(75, 300, window=l2_mat)

            e2_mat = tk.Entry(ss_root)
            ss_canvas.create_window(190, 300, window=e2_mat)

            ss_canvas.create_rectangle(15,350,400,400)
            ss_canvas.create_line(425,75,425,375)


            dis_label=tk.Label(ss_root,text='Discharge Inputs',font='Calibri')
            ss_canvas.create_window(100,350,window=dis_label)

        
            l_discharge = tk.Label(ss_root, text='Discharge(m³/s)')
            ss_canvas.create_window(75, 375, window=l_discharge)

            e_dis = tk.Entry(ss_root)
            ss_canvas.create_window(190, 375, window=e_dis)

            cable_label=tk.Label(ss_root,text='Cable Inputs',font='Calibri')
            ss_canvas.create_window(500,50,window=cable_label)

            ss_canvas.create_rectangle(450,50,775,200)


            
            l1_cable = tk.Label(ss_root, text='No of Cables')
            ss_canvas.create_window(500, 75, window=l1_cable)

            e1_cable = tk.Entry(ss_root)
            ss_canvas.create_window(615, 75, window=e1_cable)      

            l2_cable = tk.Label(ss_root, text='Cable Type')
            ss_canvas.create_window(500, 125, window=l2_cable)    

           
            def entry_dis():
                s1=float(e1_mat.get())
                s2=float(e2_mat.get())
                df=pd.DataFrame({s1,s2})
                df.to_excel('data/discharge.xlsx',encoding='utf-8',index_label='Columns',index=False)

            def entry_bearing():
                s1=float(e_bear_len.get())
                s2=float(e_bear_wid.get())
                s3=float(e_bear_dist.get())
                df=pd.DataFrame({s1,s2,s3})
                df.to_excel('data/bearing.xlsx',encoding='utf-8',index_label='Columns',index=False)

            def entry_span():
                s1=float(e_span.get())
                df=pd.DataFrame({s1})
                df.to_excel('data/span.xlsx',encoding='utf-8',index_label='Columns',index=False)

            def entry_mat():
                s1=float(e1_mat.get())
                s2=float(e1_mat.get())
                df=pd.DataFrame({s1,s2})
                df.to_excel('data/material.xlsx',encoding='utf-8',index_label='Columns',index=False)

            
            def entry_cable():
                s1=float(e1_mat.get())
                s2=float(e1_mat.get())
                df=pd.DataFrame({s1,s2})
                df.to_excel('data/cable_nos.xlsx',encoding='utf-8',index_label='Columns',index=False)

            
            def entry_cable2():
                s1=clicked.get()
                
                df=pd.DataFrame({s1})
                df.to_excel('data/cable_type.xlsx',encoding='utf-8',index_label='Columns',index=False)



            #########################################################################3

            button_quit11 = tk.Button(ss_root,text='Exit',command=quit11)
            button11 = tk.Button(ss_root,text='Permanent Cross Section Inputs', command=boxinput)    
            button22 = tk.Button(ss_root,text='Input', command=entry_dis)
            button33 = tk.Button(ss_root,text='Input', command=entry_bearing)
            button44 = tk.Button(ss_root,text='Input', command=entry_span)
            button55= tk.Button(ss_root,text='Input',command=entry_mat)
            button66= tk.Button(ss_root,text='Input',command=entry_cable)
            button77= tk.Button(ss_root,text='Input',command=entry_cable2)

            clicked=tk.StringVar(ss_root)
            clicked.set('9K13')
            dropdn=tk.OptionMenu(ss_root,clicked,*['4K13','4K15','7K13','7K15','12K13','12K15','19K13','19K15','27K13','27K15','37K13','37K15','55K13'])
            ss_canvas.create_window(175, 425, window=button11)
            ss_canvas.create_window(325, 75, window=button22)
            ss_canvas.create_window(325, 175, window=button33)
            ss_canvas.create_window(325, 275, window=button44)
            ss_canvas.create_window(325, 375, window=button55)
            ss_canvas.create_window(725, 75, window=button66)
            ss_canvas.create_window(725, 125, window=button77)
            ss_canvas.create_window(600,125,window=dropdn)
            ss_canvas.create_window(325, 425, window=button_quit11)
        


        def quit111():
            ssd_root.destroy()


        ssd_root = tk.Toplevel(main_root)
        ssd_canvas = tk.Canvas(ssd_root, width=200, height=200)
        ssd_canvas.pack()
        ssd_root.title("Superstructure Design")

        button_quit111 = tk.Button(ssd_root,text='Exit',command=quit111)
        button111 = tk.Button(ssd_root,text='Superstructure Inputs', command=ss_input)    
        button222 = tk.Button(ssd_root,text='Superstructure Outputs', command=ss_output)

        ssd_canvas.create_window(100, 50, window=button111)
        ssd_canvas.create_window(100, 100, window=button222)

        ssd_canvas.create_window(100, 150, window=button_quit111)

    def sub_input():



        def abutmentdesign():
            

            def abutmentinput():
                length=[]
                height=[]

                abut_root = tk.Toplevel(abutment_root)

                canvas_abut = tk.Canvas(abut_root, width=1000, height=500)
                canvas_abut.pack()
                abut_root.title("Abutment Input")

                img=tk.PhotoImage(file="Images/Abutment.png")
                # logo=ImageTk.PhotoImage(file="Images\logo.png")
                # root.iconphoto(False,logo)

                canvas_abut.create_image(700,250,image=img)

                l1 = tk.Label(abut_root, text='Width(m)→')
                canvas_abut.create_window(160, 75, window=l1)
                l2 = tk.Label(abut_root, text='Length(m)↑')
                canvas_abut.create_window(300, 75, window=l2)



                l3 = tk.Label(abut_root, text='Section 1')
                canvas_abut.create_window(50, 100, window=l3)
                e1 = tk.Entry(abut_root)
                canvas_abut.create_window(160, 100, window=e1)
                e2 = tk.Entry(abut_root)
                canvas_abut.create_window(300, 100, window=e2)

                l4 = tk.Label(abut_root, text='Section 2')
                canvas_abut.create_window(50, 125, window=l4)
                e3 = tk.Entry(abut_root)
                canvas_abut.create_window(160, 125, window=e3)
                e4 = tk.Entry(abut_root)
                canvas_abut.create_window(300, 125, window=e4)


                l5 = tk.Label(abut_root, text='Section 3')
                canvas_abut.create_window(50, 150, window=l5)
                e5 = tk.Entry(abut_root)
                canvas_abut.create_window(160, 150, window=e5)
                e6 = tk.Entry(abut_root)
                canvas_abut.create_window(300, 150, window=e6)


                l6 = tk.Label(abut_root, text='Section 4')
                canvas_abut.create_window(50, 175, window=l6)
                e7 = tk.Entry(abut_root)
                canvas_abut.create_window(160, 175, window=e7)
                e8 = tk.Entry(abut_root)
                canvas_abut.create_window(300, 175, window=e8)


                l7 = tk.Label(abut_root, text='Section 5')
                canvas_abut.create_window(50, 200, window=l7)
                e9 = tk.Entry(abut_root)
                canvas_abut.create_window(160, 200, window=e9)
                e10 = tk.Entry(abut_root)
                canvas_abut.create_window(300, 200, window=e10)

                l8 = tk.Label(abut_root, text='Section 6')
                canvas_abut.create_window(50, 225, window=l8)
                e11 = tk.Entry(abut_root)
                canvas_abut.create_window(160, 225, window=e11)
                e12 = tk.Entry(abut_root)
                canvas_abut.create_window(300, 225, window=e12)

                l9 = tk.Label(abut_root, text='Section 7')
                canvas_abut.create_window(50, 250, window=l9)
                e13 = tk.Entry(abut_root)
                canvas_abut.create_window(160, 250, window=e13)
                e14 = tk.Entry(abut_root)
                canvas_abut.create_window(300, 250, window=e14)


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
                
                    length.extend([w1,w2,w3,w4,w5,w6,w7])
                    height.extend([l1,l2,l3,l4,l9,l5,l6,l7])
                    abut_root.quit()
                button4 = tk.Button(abut_root,text='Input', command=entry)
                canvas_abut.create_window(225, 300, window=button4)

                abut_root.mainloop()
                df=pd.DataFrame(length,height).T
                df.to_excel('data/abutment.xlsx',encoding='utf-8',index_label='Columns',index=False)


            def quit_abut():
                abutment_root.destroy()

            abutment_root = tk.Toplevel(sub_root)
            abutment_canvas = tk.Canvas(abutment_root, width=200, height=200)
            abutment_canvas.pack()
            abutment_root.title("Substructure Design")

            button_quit_abut = tk.Button(abutment_root,text='Exit',command=quit_abut)
            button1_abut = tk.Button(abutment_root,text='Abutment Inputs', command=abutmentinput)    
            # button2 = tk.Button(sub_root,text='Span and Number of Sections Input', command=spaninput)
            # button3 = tk.Button(sub_root,text='Discharge Input', command=dischargeinput)
            # button4 = tk.Button(sub_root,text='Bearing Input', command=bearinginput)

            abutment_canvas.create_window(100, 50, window=button1_abut)
            # sub_canvas.create_window(150, 100, window=button2)
            # sub_canvas.create_window(150, 150, window=button3)
            # sub_canvas.create_window(150, 200, window=button4)
            abutment_canvas.create_window(100, 100, window=button_quit_abut)






             

    
        # def pierdesign():
            

        #     def pierinput():
        #         length=[]
        #         height=[]

        #         pier_root = tk.Toplevel(sub_root)

        #         canvas_pier = tk.Canvas(pier_root, width=1000, height=500)
        #         canvas_pier.pack()
        #         pier_root.title("Abutment Input")

        #         img=tk.PhotoImage(file="Images/Abutment.png")
        #         # logo=ImageTk.PhotoImage(file="Images\logo.png")
        #         # root.iconphoto(False,logo)

        #         canvas_pier.create_image(700,250,image=img)

        #         l1 = tk.Label(pier_root, text='Width(m)→')
        #         canvas_pier.create_window(160, 75, window=l1)
        #         l2 = tk.Label(pier_root, text='Length(m)↑')
        #         canvas_pier.create_window(300, 75, window=l2)



        #         l3 = tk.Label(pier_root, text='Section 1')
        #         canvas_pier.create_window(50, 100, window=l3)
        #         e1 = tk.Entry(pier_root)
        #         canvas_pier.create_window(160, 100, window=e1)
        #         e2 = tk.Entry(pier_root)
        #         canvas_pier.create_window(300, 100, window=e2)

        #         l4 = tk.Label(pier_root, text='Section 2')
        #         canvas_pier.create_window(50, 125, window=l4)
        #         e3 = tk.Entry(pier_root)
        #         canvas_pier.create_window(160, 125, window=e3)
        #         e4 = tk.Entry(pier_root)
        #         canvas_pier.create_window(300, 125, window=e4)


                # l5 = tk.Label(abut_root, text='Section 3')
                # canvas_abut.create_window(50, 150, window=l5)
                # e5 = tk.Entry(abut_root)
                # canvas_abut.create_window(160, 150, window=e5)
                # e6 = tk.Entry(abut_root)
                # canvas_abut.create_window(300, 150, window=e6)


                # l6 = tk.Label(abut_root, text='Section 4')
                # canvas_abut.create_window(50, 175, window=l6)
                # e7 = tk.Entry(abut_root)
                # canvas_abut.create_window(160, 175, window=e7)
                # e8 = tk.Entry(abut_root)
                # canvas_abut.create_window(300, 175, window=e8)


                # l7 = tk.Label(abut_root, text='Section 5')
                # canvas_abut.create_window(50, 200, window=l7)
                # e9 = tk.Entry(abut_root)
                # canvas_abut.create_window(160, 200, window=e9)
                # e10 = tk.Entry(abut_root)
                # canvas_abut.create_window(300, 200, window=e10)

                # l8 = tk.Label(abut_root, text='Section 6')
                # canvas_abut.create_window(50, 225, window=l8)
                # e11 = tk.Entry(abut_root)
                # canvas_abut.create_window(160, 225, window=e11)
                # e12 = tk.Entry(abut_root)
                # canvas_abut.create_window(300, 225, window=e12)

                # l9 = tk.Label(abut_root, text='Section 7')
                # canvas_abut.create_window(50, 250, window=l9)
                # e13 = tk.Entry(abut_root)
                # canvas_abut.create_window(160, 250, window=e13)
                # e14 = tk.Entry(abut_root)
                # canvas_abut.create_window(300, 250, window=e14)


                # def entry():
                #     w1=float(e1.get())
                #     l1=float(e2.get())
                #     w2=float(e3.get())
                #     l2=float(e4.get())
                #     w3=float(e5.get())
                #     l3=float(e6.get())
                #     w4=float(e7.get())
                #     l4=float(e8.get())
                #     w5=float(e9.get())
                #     l5=float(e10.get())
                #     w6=float(e11.get())
                #     l6=float(e12.get())
                #     w7=float(e13.get())
                #     l7=float(e14.get())
                
                #     length.extend([w1,w2,w3,w4,w5,w6,w7])
                #     height.extend([l1,l2,l3,l4,l9,l5,l6,l7])
                #     abut_root.quit()
                # button4 = tk.Button(abut_root,text='Input', command=entry)
                # canvas_abut.create_window(225, 300, window=button4)

                # abut_root.mainloop()
                # df=pd.DataFrame(length,height).T
                # df.to_excel('data/abutment.xlsx',encoding='utf-8',index_label='Columns',index=False)


            # def quit1111():
            #     sub_root.destroy()

            # abut_root = tk.Toplevel(sub_root)
            # abut_canvas = tk.Canvas(abut_root, width=200, height=200)
            # abut_canvas.pack()
            # abut_root.title("Substructure Design")

            # button_quit1111 = tk.Button(abut_root,text='Exit',command=quit1111)
            # button1111 = tk.Button(abut_root,text='Abutment Inputs', command=abutmentinput)    
            # # button2 = tk.Button(sub_root,text='Span and Number of Sections Input', command=spaninput)
            # # button3 = tk.Button(sub_root,text='Discharge Input', command=dischargeinput)
            # # button4 = tk.Button(sub_root,text='Bearing Input', command=bearinginput)

            # abut_canvas.create_window(100, 50, window=button1111)
            # # sub_canvas.create_window(150, 100, window=button2)
            # # sub_canvas.create_window(150, 150, window=button3)
            # # sub_canvas.create_window(150, 200, window=button4)
            # abut_canvas.create_window(100, 100, window=button_quit1111)
    
        def quit_sub():
            sub_root.destroy()

        sub_root = tk.Toplevel(main_root)
        sub_canvas = tk.Canvas(sub_root, width=200, height=200)
        sub_canvas.pack()
        sub_root.title("Substructure Design")

        button_quit_sub = tk.Button(sub_root,text='Exit',command=quit_sub)
        button1_sub = tk.Button(sub_root,text='Abutment Design', command=abutmentdesign)    
        # button2 = tk.Button(sub_root,text='Span and Number of Sections Input', command=spaninput)
        # button3 = tk.Button(sub_root,text='Discharge Input', command=dischargeinput)
        # button4 = tk.Button(sub_root,text='Bearing Input', command=bearinginput)

        sub_canvas.create_window(100, 50, window=button1_sub)
        # sub_canvas.create_window(150, 100, window=button2)
        # sub_canvas.create_window(150, 150, window=button3)
        # sub_canvas.create_window(150, 200, window=button4)
        sub_canvas.create_window(100, 100, window=button_quit_sub)  







    def main_quit():
        main_root.quit()

    main_root=tk.Tk()
    main_canvas=tk.Canvas(main_root,width=250,height=200)
    main_canvas.pack()
    main_root.title("Bridge Design")
    logo=ImageTk.PhotoImage(file="Images\logo.png")
    main_root.iconphoto(False,logo)

    ############Buttons######################


    button1 = tk.Button(text='Superstructure Design', command=ss_design)
    button2 = tk.Button(text='Substructure Design', command=sub_input)

  
    # main_canvas.create_rectangle(25,25,225,175)

    button_quit_main = tk.Button(text='Exit',command=main_quit)
    main_canvas.create_window(125, 50, window=button1)
    main_canvas.create_window(125, 100, window=button2)
    # main_canvas.create_window(150, 150, window=button3)
    # main_canvas.create_window(150, 200, window=button4)
    # main_canvas.create_window(150, 250, window=button5)

    main_canvas.create_window(125, 150, window=button_quit_main)
    main_root.mainloop()
    



all_input()


