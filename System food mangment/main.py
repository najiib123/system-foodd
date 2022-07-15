from tkinter import *
from tkinter import messagebox
import os
import tempfile
import time

import random

from PIL import  ImageTk

def Login():
    user=username.get()
    code=password.get()
    if user!="" and code!="":




        def bariis():
            if var1.get() == 1:
                textBariis.config(state=NORMAL)
                textBariis.delete(0, END)
                textBariis.focus()
            else:
                textBariis.config(state=DISABLED)
                e_bariis.set("0")

        def baasto():
            if var2.get() == 1:
                textbaasto.config(state=NORMAL)
                textbaasto.delete(0, END)
                textbaasto.focus()
            else:
                textbaasto.config(state=DISABLED)
                e_baasto.set("0")

        def kalaankal():
            if var3.get() == 1:
                textkalaankal.config(state=NORMAL)
                textkalaankal.delete(0, END)
                textkalaankal.focus()
            else:
                textkalaankal.config(state=DISABLED)
                e_kalaankal.set("0")

        def muufo():
            if var4.get() == 1:
                textmuufo.config(state=NORMAL)
                textmuufo.delete(0, END)
                textmuufo.focus()
            else:
                textmuufo.config(state=DISABLED)
                e_muufo.set("0")

        def oodkac():
            if var5.get() == 1:
                textoodkac.config(state=NORMAL)
                textoodkac.delete(0, END)
                textoodkac.focus()
            else:
                textoodkac.config(state=DISABLED)
                e_oodkac.set("0")

        def suqaar():
            if var6.get() == 1:
                textsuqaar.config(state=NORMAL)
                textsuqaar.delete(0, END)
                textsuqaar.focus()
            else:
                textsuqaar.config(state=DISABLED)
                e_suqaar.set("0")

        def soor():
            if var7.get() == 1:
                textsoor.config(state=NORMAL)
                textsoor.delete(0, END)
                textsoor.focus()
            else:
                textsoor.config(state=DISABLED)
                e_soor.set("0")

        def dooro():
            if var8.get() == 1:
                textdooro.config(state=NORMAL)
                textdooro.delete(0, END)
                textdooro.focus()
            else:
                textdooro.config(state=DISABLED)
                e_dooro.set("0")

        def malaay():
            if var9.get() == 1:
                textmalaay.config(state=NORMAL)
                textmalaay.delete(0, END)
                textmalaay.focus()
            else:
                textmalaay.config(state=DISABLED)
                e_malaay.set("0")

        # functons of drink
        def cambo():
            if var10.get() == 1:
                textcambo.config(state=NORMAL)
                textcambo.delete(0, END)
                textcambo.focus()
            else:
                textcambo.config(state=DISABLED)
                v_cambo.set("0")

        def qaro():
            if var11.get() == 1:
                textqaro.config(state=NORMAL)
                textqaro.delete(0, END)
                textqaro.focus()
            else:
                textqaro.config(state=DISABLED)
                v_qaro.set("0")

        def caano():
            if var12.get() == 1:
                textcaano.config(state=NORMAL)
                textcaano.delete(0, END)
                textcaano.focus()
            else:
                textcaano.config(state=DISABLED)
                v_caano.set("0")

        def fulaarto():
            if var13.get() == 1:
                textfulaarto.config(state=NORMAL)
                textfulaarto.delete(0, END)
                textfulaarto.focus()
            else:
                textfulaarto.config(state=DISABLED)
                v_fulaarto.set("0")

        def mushakal():
            if var14.get() == 1:
                textmushakal.config(state=NORMAL)
                textmushakal.delete(0, END)
                textmushakal.focus()
            else:
                textmushakal.config(state=DISABLED)
                v_mushakal.set("0")

        def liin():
            if var15.get() == 1:
                textliin.config(state=NORMAL)
                textliin.delete(0, END)
                textliin.focus()
            else:
                textliin.config(state=DISABLED)
                v_liin.set("0")

        def caanoGeel():
            if var16.get() == 1:
                textcaanogeel.config(state=NORMAL)
                textcaanogeel.delete(0, END)
                textcaanogeel.focus()
            else:
                textcaanogeel.config(state=DISABLED)
                v_caanogeel.set("0")

        def faanta():
            if var17.get() == 1:
                textfaanta.config(state=NORMAL)
                textfaanta.delete(0, END)
                textfaanta.focus()
            else:
                textfaanta.config(state=DISABLED)
                v_faanta.set("0")

        def lavitta():
            if var18.get() == 1:
                textlavitta.config(state=NORMAL)
                textlavitta.delete(0, END)
                textlavitta.focus()
            else:
                textlavitta.config(state=DISABLED)
                v_lavitta.set("0")

        # fucntion of cakes

        def angle():
            if var19.get() == 1:
                texangle.config(state=NORMAL)
                texangle.delete(0, END)
                texangle.focus()
            else:
                texangle.config(state=DISABLED)
                c_angel_cake.set("0")

        def apple():
            if var20.get() == 1:
                texapple.config(state=NORMAL)
                texapple.delete(0, END)
                texapple.focus()
            else:
                texapple.config(state=DISABLED)
                c_apple_cake.set("0")

        def beer():
            if var21.get() == 1:
                texbeer.config(state=NORMAL)
                texbeer.delete(0, END)
                texbeer.focus()
            else:
                texbeer.config(state=DISABLED)
                c_beer_cake.set("0")

        def birthday():
            if var21.get() == 1:
                texbirthday.config(state=NORMAL)
                texbirthday.delete(0, END)
                texbirthday.focus()
            else:
                texbirthday.config(state=DISABLED)
                c_birthday_cake.set("0")

        def chocolate():
            if var23.get() == 1:
                texchocolate.config(state=NORMAL)
                texchocolate.delete(0, END)
                texchocolate.focus()
            else:
                texchocolate.config(state=DISABLED)
                c_chocolate_cake.set("0")

        def banana():
            if var24.get() == 1:
                texbanan.config(state=NORMAL)
                texbanan.delete(0, END)
                texbanan.focus()
            else:
                texbanan.config(state=DISABLED)
                c_banana_cake.set("0")

        def butter():
            if var25.get() == 1:
                texbutter.config(state=NORMAL)
                texbutter.delete(0, END)
                texbutter.focus()
            else:
                texbutter.config(state=DISABLED)
                c_butter_cake.set("0")

        def battika():
            if var26.get() == 1:
                texbattika.config(state=NORMAL)
                texbattika.delete(0, END)
                texbattika.focus()
            else:
                texbattika.config(state=DISABLED)
                c_battik_cake.set("0")

        def browine():
            if var27.get() == 1:
                texbarrwine.config(state=NORMAL)
                texbarrwine.delete(0, END)
                texbarrwine.focus()
            else:
                texbarrwine.config(state=DISABLED)
                c_brwine_cake.set("0")

        def print():
            p = textreciept.get("1.0", "end-1c")
            filname = tempfile.mktemp(".txt")
            open(filname, "w").write(p)
            os.startfile(filname, "print")

        def rest():
            textreciept.delete(1.0, END)
            e_soor.set('0')
            e_malaay.set('0')
            e_baasto.set('0')
            e_kalaankal.set('0')
            e_suqaar.set('0')
            e_bariis.set('0')
            e_muufo.set('0')
            e_oodkac.set('0')
            e_dooro.set('0')

            v_qaro.set('0')
            v_caano.set('0')
            v_cambo.set('0')
            v_lavitta.set('0')
            v_faanta.set('0')
            v_caanogeel.set('0')
            v_mushakal.set('0')
            v_liin.set('0')
            v_fulaarto.set('0')

            c_apple_cake.set('0')
            c_banana_cake.set('0')
            c_butter_cake.set('0')
            c_birthday_cake.set('0')
            c_battik_cake.set('0')
            c_brwine_cake.set('0')
            c_chocolate_cake.set('0')
            c_beer_cake.set('0')
            c_angel_cake.set('0')

            textbaasto.config(state=DISABLED)
            textmuufo.config(state=DISABLED)
            textsoor.config(state=DISABLED)
            textdooro.config(state=DISABLED)
            textkalaankal.config(state=DISABLED)
            textmalaay.config(state=DISABLED)
            textBariis.config(state=DISABLED)
            textoodkac.config(state=DISABLED)
            textsuqaar.config(state=DISABLED)

            textcambo.config(state=DISABLED)
            textcaano.config(state=DISABLED)
            textcaanogeel.config(state=DISABLED)
            textfaanta.config(state=DISABLED)
            textfulaarto.config(state=DISABLED)
            textliin.config(state=DISABLED)
            textlavitta.config(state=DISABLED)
            textqaro.config(state=DISABLED)
            textmushakal.config(state=DISABLED)
            # cakes
            texangle.config(state=DISABLED)
            texapple.config(state=DISABLED)
            texbeer.config(state=DISABLED)
            texbanan.config(state=DISABLED)
            texbanan.config(state=DISABLED)
            texbutter.config(state=DISABLED)
            texbattika.config(state=DISABLED)
            texbarrwine.config(state=DISABLED)
            texchocolate.config(state=DISABLED)

            var1.set(0)
            var2.set(0)
            var3.set(0)
            var4.set(0)
            var5.set(0)
            var6.set(0)
            var7.set(0)
            var8.set(0)
            var9.set(0)
            var10.set(0)
            var11.set(0)
            var12.set(0)
            var13.set(0)
            var14.set(0)
            var15.set(0)
            var16.set(0)
            var17.set(0)
            var18.set(0)
            var19.set(0)
            var20.set(0)
            var21.set(0)
            var22.set(0)
            var23.set(0)
            var24.set(0)
            var25.set(0)
            var26.set(0)
            var27.set(0)

            costoffoodvar.set('')
            costofdrinkvar.set('')
            costofcakesvar.set('')
            subtotalvar.set('')
            servicevar.set('')
            totalcostvar.set('')

        def recipt():
            z = random.randint(100, 10000)
            billnumber = "BILL" + str(z)
            date = time.strftime('%d/%m/%Y')
            textreciept.insert(END, 'Receipt Ref:\t\t' + billnumber + '\t\t' + date + '\n')
            textreciept.insert(END, '***************************************************************\n')
            textreciept.insert(END, 'Items:\t\t Cost Of Items($)\n')
            textreciept.insert(END, '***************************************************************\n')

            if e_bariis.get() != '0':
                textreciept.insert(END, f'bariis:\t\t\t{int(e_bariis.get()) * 1}\n\n')

            if e_baasto.get() != '0':
                textreciept.insert(END, f'baasto:\t\t\t{int(e_baasto.get()) * 1}\n\n')

            if e_kalaankal.get() != '0':
                textreciept.insert(END, f'kalaanka:\t\t\t{int(e_kalaankal.get()) * 2}\n\n')

            if e_muufo.get() != '0':
                textreciept.insert(END, f'muufo:\t\t\t{int(e_muufo.get()) * 1}\n\n')

            if e_oodkac.get() != '0':
                textreciept.insert(END, f'oodkac:\t\t\t{int(e_oodkac.get()) * 1}\n\n')

            if e_suqaar.get() != '0':
                textreciept.insert(END, f'malaay:\t\t\t{int(e_suqaar.get()) * 1.5}\n\n')

            if e_soor.get() != '0':
                textreciept.insert(END, f'soor:\t\t\t{int(e_soor.get()) * 1}\n\n')

            if e_dooro.get() != '0':
                textreciept.insert(END, f'dooro:\t\t\t{int(e_dooro.get()) * 1}\n\n')

            if e_malaay.get() != '0':
                textreciept.insert(END, f'malaay:\t\t\t{int(e_malaay.get()) * 1}\n\n')

                # drinks recipt

            if v_cambo.get() != '0':
                textreciept.insert(END, f'Cambo:\t\t\t{int(v_cambo.get())  * 1}\n\n')

            if v_qaro.get() != '0':
                textreciept.insert(END, f'Qaro:\t\t\t{int(v_qaro.get()) * 1}\n\n')

            if v_liin.get() != '0':
                textreciept.insert(END, f'Liin:\t\t\t{int(v_liin.get()) * 1}\n\n')

            if v_fulaarto.get() != '0':
                textreciept.insert(END, f'fulaarto:\t\t\t{int(v_fulaarto.get()) * 1}\n\n')

            if v_mushakal.get() != '0':
                textreciept.insert(END, f'mushakal:\t\t\t{int(v_mushakal.get()) * 1}\n\n')

            if v_faanta.get() != '0':
                textreciept.insert(END, f'faanta:\t\t\t{int(v_faanta.get()) * 1}\n\n')

            if v_lavitta.get() != '0':
                textreciept.insert(END, f'lavvita:\t\t\t{int(v_lavitta.get()) * 1}\n\n')

            if v_caanogeel.get() != '0':
                textreciept.insert(END, f'caanogeel:\t\t\t{int(v_caanogeel.get()) * 1}\n\n')

            if v_caano.get() != '0':
                textreciept.insert(END, f'Caano Drinks:\t\t\t{int(v_caano.get()) * 1}\n\n')

                # recipt of cake

            if c_apple_cake.get() != '0':
                textreciept.insert(END, f'Apple Cake:\t\t\t{int(c_apple_cake.get()) * 4}\n\n')

            if c_beer_cake.get() != '0':
                textreciept.insert(END, f'beer cake:\t\t\t{int(c_beer_cake.get()) * 3}\n\n')

            if c_birthday_cake.get() != '0':
                textreciept.insert(END, f'Birthday cake:\t\t\t{int(c_birthday_cake.get()) * 5}\n\n')

            if c_chocolate_cake.get() != '0':
                textreciept.insert(END, f'chocalate cake:\t\t\t{int(c_chocolate_cake.get()) * 4}\n\n')

            if c_battik_cake.get() != '0':
                textreciept.insert(END, f'battkia cake:\t\t\t{int(c_battik_cake.get()) * 2}\n\n')

            if c_butter_cake.get() != '0':
                textreciept.insert(END, f'butter_cake:\t\t\t{int(c_butter_cake.get()) * 1}\n\n')

            if c_brwine_cake.get() != '0':
                textreciept.insert(END, f'brwine cake:\t\t\t{int(c_brwine_cake.get()) * 1}\n\n')

            if c_banana_cake.get() != '0':
                textreciept.insert(END, f'banna cake:\t\t\t{int(c_banana_cake.get()) * 1}\n\n')

            if c_angel_cake.get() != '0':
                textreciept.insert(END, f'Angle cake:\t\t\t{int(c_angel_cake.get()) * 1}\n\n')

            textreciept.insert(END, '***************************************************************\n')
            if costoffoodvar.get() != '0 $':
                textreciept.insert(END, f'Cost Of Food\t\t\t{priceoffood}$\n\n')
            if costofdrinkvar.get() != '0 $':
                textreciept.insert(END, f'Cost Of Drinks\t\t\t{priceofdrink}$\n\n')
            if costofcakesvar.get() != '0 $':
                textreciept.insert(END, f'Cost Of Cakes\t\t\t{priceofcake}$\n\n')

            textreciept.insert(END, f'Sub Total\t\t\t{subtotal_of_itms}$\n\n')
            textreciept.insert(END, f'Service Tax\t\t\t{1}$\n\n')
            textreciept.insert(END, f'Total Cost\t\t\t{subtotal_of_itms + 1}$\n\n')
            textreciept.insert(END, '***************************************************************\n')

        # function of total
        def totalofcost():
            global priceoffood, priceofdrink, priceofcake, subtotal_of_itms
            if var1.get() != 0 or var2.get() != 0 or var3.get() != 0 or var4.get() != 0 or var5.get() != 0 or \
                 var6.get() != 0 or var7.get() != 0 or var8.get() != 0 or var9.get() != 0 or var10.get() != 0 or \
                 var11.get() != 0 or var12.get() != 0 or var13.get() != 0 or var14.get() != 0 or var15.get() != 0 or \
                 var16.get() != 0 or var17.get() != 0 or var18.get() != 0 or var19.get() != 0 or var20.get() != 0 or \
                 var21.get() != 0 or var22.get() != 0 or var23.get() != 0 or var24.get() != 0 or var25.get() != 0 or \
                 var26.get() != 0 or var27.get() != 0:


            # itemes of food
                 item1 = int(e_bariis.get())
                 item2 = int(e_baasto.get())
                 item3 = int(e_kalaankal.get())
                 item4 = int(e_muufo.get())
                 item5 = int(e_soor.get())
                 item6 = int(e_suqaar.get())
                 item7 = int(e_dooro.get())
                 item8 = int(e_malaay.get())
                 item9 = int(e_oodkac.get())

                 # itemes of drink

                 item10 = int(v_cambo.get())
                 item11 = int(v_qaro.get())
                 item12 = int(v_caano.get())
                 item13 = int(v_caanogeel.get())
                 item14 = int(v_fulaarto.get())
                 item15 = int(v_mushakal.get())
                 item16 = int(v_liin.get())
                 item17 = int(v_mushakal.get())
                 item18 = int(v_lavitta.get())

                 item19 = int(c_angel_cake.get())
                 item20 = int(c_beer_cake.get())
                 item21 = int(c_banana_cake.get())
                 item22 = int(c_birthday_cake.get())
                 item23 = int(c_chocolate_cake.get())
                 item24 = int(c_apple_cake.get())
                 item25 = int(c_battik_cake.get())
                 item26 = int(c_butter_cake.get())
                 item27 = int(c_brwine_cake.get())

               # calculate of prices of food

                 priceoffood = (item1 * 1) + (item2 * 1) + (item3 * 1) + (item4 * 1) + (item5 * 1) + \
                             (item6 * 1) + (item7 * 1) + (item1 * 1) + (item9 * 1)

               # calculate of prices of drink
                 priceofdrink = (item10 * 1) + (item11 * 1) + (item12 * 1) + (item13 * 1) + (item14 * 1) + \
                              (item15 * 1) + (item16 * 1) + (item17 * 1) + (item18 * 1)

               # calculate of prices of cake
                 priceofcake = (item19 * 1) + (item20 * 1) + (item21 * 1) + (item22 * 2) + (item23 * 1) + \
                                             (item24 * 1) + (item25 * 1) + (item26 * 8) + (item27 * 1)

                 costoffoodvar.set(str(priceoffood) + "$")
                 costofdrinkvar.set(str(priceofdrink) + "$")
                 costofcakesvar.set(str(priceofcake) + "$")

               # sub totla
                 subtotal_of_itms = priceoffood + priceofdrink + priceofcake
                 subtotalvar.set(str(subtotal_of_itms) + "$")

                 servicevar.set("1 $")

                 totalcost = subtotal_of_itms + 1
                 totalcostvar.set(str(subtotal_of_itms) + "$")


    root=Toplevel(screen)
    root.geometry("1310x690+0+0")

    root.resizable(0, 0)

    root.title("haashim resturant")
    root.config(bg="#6F8FAF")

    topframe = Frame(root, bd=10, relief=RIDGE, bg="#6F8FAF")
    topframe.pack(side=TOP)

    # lebel frame
    Lebeltitle = Label(topframe, text="Resturent managment system", font=("avant-garde-medium.", 30, "bold"),
                       fg="yellow",
                       bd=10, bg="#6F8FAF", width=51)
    Lebeltitle.grid(row=0, column=0)

    # menue frame
    menuframe = Frame(root, bd=10, relief=RIDGE, bg="#6F8FAF")
    menuframe.pack(side=LEFT)

    # cost frame
    costframe = Frame(menuframe, bd=4, relief=RIDGE, bg="#6F8FAF", pady=10)
    costframe.pack(side=BOTTOM)

    # food frame
    foodFrame = LabelFrame(menuframe, text="food", font=("avant-garde-medium", "19", "bold"), bd=10, relief=RIDGE,
                           fg="#6F8FAF")
    foodFrame.pack(side=LEFT)

    # drink frame
    drinksFrame = LabelFrame(menuframe, text="drinks", font=("avant-garde-medium", "19", "bold"), bd=10, relief=RIDGE,
                             fg="#6F8FAF")
    drinksFrame.pack(side=LEFT)

    # cake frame
    cakesFrame = LabelFrame(menuframe, text="cakes", font=("avant-garde-medium", "19", "bold"), bd=10, relief=RIDGE,
                            fg="#6F8FAF")
    cakesFrame.pack(side=LEFT)

    # right frame
    rightFrame = Frame(root, bd=15, relief=RIDGE, bg='#6F8FAF')
    rightFrame.pack(side=RIGHT)
    # calculator fram
    calculatorFrame = Frame(rightFrame, bd=1, relief=RIDGE, bg="#6F8FAF")
    calculatorFrame.pack()
    # reciott frame
    reciptFrame = Frame(rightFrame, bd=4, relief=RIDGE, bg="#6F8FAF")
    reciptFrame.pack()
    # buttom frame
    buttomFrame = Frame(rightFrame, bd=3, relief=RIDGE, bg="#6F8FAF")
    buttomFrame.pack()

    # variables
    var1 = IntVar()
    var2 = IntVar()
    var3 = IntVar()
    var4 = IntVar()
    var5 = IntVar()
    var6 = IntVar()
    var7 = IntVar()
    var8 = IntVar()
    var9 = IntVar()
    var10 = IntVar()
    var11 = IntVar()
    var12 = IntVar()
    var13 = IntVar()
    var14 = IntVar()
    var15 = IntVar()
    var16 = IntVar()
    var17 = IntVar()
    var18 = IntVar()
    var19 = IntVar()
    var20 = IntVar()
    var21 = IntVar()
    var22 = IntVar()
    var23 = IntVar()
    var24 = IntVar()
    var25 = IntVar()
    var26 = IntVar()
    var27 = IntVar()

    # varibal boxes foods
    e_bariis = StringVar()
    e_baasto = StringVar()
    e_kalaankal = StringVar()
    e_muufo = StringVar()
    e_oodkac = StringVar()
    e_suqaar = StringVar()
    e_soor = StringVar()
    e_dooro = StringVar()
    e_malaay = StringVar()

    # set 0
    e_bariis.set("0")
    e_baasto.set("0")
    e_dooro.set("0")
    e_malaay.set("0")
    e_soor.set("0")
    e_suqaar.set("0")
    e_muufo.set("0")
    e_kalaankal.set("0")
    e_oodkac.set("0")

    # variables of boxes for dirnk
    v_cambo = StringVar()
    v_qaro = StringVar()
    v_caano = StringVar()
    v_fulaarto = StringVar()
    v_mushakal = StringVar()
    v_liin = StringVar()
    v_caanogeel = StringVar()
    v_faanta = StringVar()
    v_lavitta = StringVar()

    # set of dirink
    v_qaro.set("0")
    v_cambo.set("0")
    v_caano.set("0")
    v_caanogeel.set("0")
    v_fulaarto.set("0")
    v_lavitta.set("0")
    v_faanta.set("0")
    v_liin.set("0")
    v_mushakal.set("0")

    # variables boxes for cakes
    c_angel_cake = StringVar()
    c_apple_cake = StringVar()
    c_beer_cake = StringVar()
    c_battik_cake = StringVar()
    c_butter_cake = StringVar()
    c_chocolate_cake = StringVar()
    c_banana_cake = StringVar()
    c_brwine_cake = StringVar()
    c_birthday_cake = StringVar()

    # vriables of all cost
    costoffoodvar = StringVar()
    costofdrinkvar = StringVar()
    costofcakesvar = StringVar()
    subtotalvar = StringVar()
    servicevar = StringVar()
    totalcostvar = StringVar()

    # cake set of 0
    c_angel_cake.set("0")
    c_apple_cake.set("0")
    c_beer_cake.set("0")
    c_banana_cake.set("0")
    c_battik_cake.set("0")
    c_birthday_cake.set("0")
    c_brwine_cake.set("0")
    c_chocolate_cake.set("0")
    c_butter_cake.set("0")

    # foods

    Bariis = Checkbutton(foodFrame, text="Bariis", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var1,
                         command=bariis)
    Bariis.grid(row=0, column=0, sticky=W)

    baasto = Checkbutton(foodFrame, text="Baasto", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var2,
                         command=baasto)
    baasto.grid(row=1, column=0, sticky=W)

    kalaankal = Checkbutton(foodFrame, text="Kalaankal", font=("arial", 18, "bold"), onvalue=1, offvalue=0,
                            variable=var3,
                            command=kalaankal)
    kalaankal.grid(row=2, column=0, sticky=W)

    muufo = Checkbutton(foodFrame, text="Muufo", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var4,
                        command=muufo)
    muufo.grid(row=3, column=0, sticky=W)

    oodkac = Checkbutton(foodFrame, text="0odkac", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var5,
                         command=oodkac)
    oodkac.grid(row=4, column=0, sticky=W)

    suqaar = Checkbutton(foodFrame, text="Suqaar", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var6,
                         command=suqaar)
    suqaar.grid(row=5, column=0, sticky=W)

    soor = Checkbutton(foodFrame, text="Soor", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var7,
                       command=soor)
    soor.grid(row=6, column=0, sticky=W)

    dooro = Checkbutton(foodFrame, text="Dooro", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var8,
                        command=dooro)
    dooro.grid(row=7, column=0, sticky=W)

    malaay = Checkbutton(foodFrame, text="Malaay", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var9,
                         command=malaay)
    malaay.grid(row=8, column=0, sticky=W)

    # entiry text

    textBariis = Entry(foodFrame, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=e_bariis)
    textBariis.grid(row=0, column=1)

    textbaasto = Entry(foodFrame, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=e_baasto)
    textbaasto.grid(row=1, column=1)

    textkalaankal = Entry(foodFrame, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED,
                          textvariable=e_kalaankal)
    textkalaankal.grid(row=2, column=1)

    textmuufo = Entry(foodFrame, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=e_muufo)
    textmuufo.grid(row=3, column=1)

    textoodkac = Entry(foodFrame, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=e_oodkac)
    textoodkac.grid(row=4, column=1)

    textsuqaar = Entry(foodFrame, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=e_suqaar)
    textsuqaar.grid(row=5, column=1)

    textsoor = Entry(foodFrame, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=e_soor)
    textsoor.grid(row=6, column=1)

    textdooro = Entry(foodFrame, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=e_dooro)
    textdooro.grid(row=7, column=1)

    textmalaay = Entry(foodFrame, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=e_malaay)
    textmalaay.grid(row=8, column=1)

    # drink

    cambo = Checkbutton(drinksFrame, text="Cambo", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var10,
                        command=cambo)
    cambo.grid(row=0, column=0, sticky=W)

    Qaro = Checkbutton(drinksFrame, text="Qaro", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var11,
                       command=qaro)
    Qaro.grid(row=1, column=0, sticky=W)

    caano = Checkbutton(drinksFrame, text="Caano", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var12,
                        command=caano)
    caano.grid(row=2, column=0, sticky=W)

    furlaato = Checkbutton(drinksFrame, text="Fulaarto", font=("arial", 18, "bold"), onvalue=1, offvalue=0,
                           variable=var13,
                           command=fulaarto)
    furlaato.grid(row=3, column=0, sticky=W)

    mushakal = Checkbutton(drinksFrame, text="Mushakal", font=("arial", 18, "bold"), onvalue=1, offvalue=0,
                           variable=var14,
                           command=mushakal)
    mushakal.grid(row=4, column=0, sticky=W)

    liin = Checkbutton(drinksFrame, text="Liin", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var15,
                       command=liin)
    liin.grid(row=5, column=0, sticky=W)

    caanoGeel = Checkbutton(drinksFrame, text="CaanoGeel", font=("arial", 18, "bold"), onvalue=1, offvalue=0,
                            variable=var16, command=caanoGeel)
    caanoGeel.grid(row=6, column=0, sticky=W)

    faanta = Checkbutton(drinksFrame, text="Faanta", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var17,
                         command=faanta)
    faanta.grid(row=7, column=0, sticky=W)

    lavitta = Checkbutton(drinksFrame, text="Lavitta", font=("arial", 18, "bold"), onvalue=1, offvalue=0,
                          variable=var18,
                          command=lavitta)
    lavitta.grid(row=8, column=0, sticky=W)

    # entiry boxes

    textcambo = Entry(drinksFrame, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=v_cambo)
    textcambo.grid(row=0, column=1)

    textqaro = Entry(drinksFrame, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=v_qaro)
    textqaro.grid(row=1, column=1)

    textcaano = Entry(drinksFrame, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=v_caano)
    textcaano.grid(row=2, column=1)

    textfulaarto = Entry(drinksFrame, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED,
                         textvariable=v_fulaarto)
    textfulaarto.grid(row=3, column=1)

    textmushakal = Entry(drinksFrame, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED,
                         textvariable=v_mushakal)
    textmushakal.grid(row=4, column=1)

    textliin = Entry(drinksFrame, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=v_liin)
    textliin.grid(row=5, column=1)

    textcaanogeel = Entry(drinksFrame, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED,
                          textvariable=v_caanogeel)
    textcaanogeel.grid(row=6, column=1)

    textfaanta = Entry(drinksFrame, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=v_faanta)
    textfaanta.grid(row=7, column=1)

    textlavitta = Entry(drinksFrame, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=v_lavitta)
    textlavitta.grid(row=8, column=1)

    # check for cakes

    anglecake = Checkbutton(cakesFrame, text="Angel cake", font=("arial", 18, "bold"), onvalue=1, offvalue=0,
                            variable=var19, command=angle)
    anglecake.grid(row=0, column=0, sticky=W)

    applecake = Checkbutton(cakesFrame, text="Apple cake", font=("arial", 18, "bold"), onvalue=1, offvalue=0,
                            variable=var20, command=apple)
    applecake.grid(row=1, column=0, sticky=W)

    beercake = Checkbutton(cakesFrame, text="Beer cake", font=("arial", 18, "bold"), onvalue=1, offvalue=0,
                           variable=var21,
                           command=beer)
    beercake.grid(row=2, column=0, sticky=W)

    birthdaycake = Checkbutton(cakesFrame, text="Birthday cake", font=("arial", 18, "bold"), onvalue=1, offvalue=0,
                               variable=var22, command=birthday)
    birthdaycake.grid(row=3, column=0, sticky=W)

    chocolatecake = Checkbutton(cakesFrame, text="CHocolate cake", font=("arial", 18, "bold"), onvalue=1, offvalue=0,
                                variable=var23, command=chocolate)
    chocolatecake.grid(row=4, column=0, sticky=W)

    bananacake = Checkbutton(cakesFrame, text="Banana cake", font=("arial", 18, "bold"), onvalue=1, offvalue=0,
                             variable=var24, command=banana)
    bananacake.grid(row=5, column=0, sticky=W)

    buttercake = Checkbutton(cakesFrame, text="Butter cake", font=("arial", 18, "bold"), onvalue=1, offvalue=0,
                             variable=var25, command=butter)
    buttercake.grid(row=6, column=0, sticky=W)

    battikacake = Checkbutton(cakesFrame, text="Batika cake", font=("arial", 18, "bold"), onvalue=1, offvalue=0,
                              variable=var26, command=battika)
    battikacake.grid(row=7, column=0, sticky=W)

    brwinecake = Checkbutton(cakesFrame, text="Browine cake", font=("arial", 18, "bold"), onvalue=1, offvalue=0,
                             variable=var27, command=browine)
    brwinecake.grid(row=8, column=0, sticky=W)

    # ntiry cake for cakes

    texangle = Entry(cakesFrame, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=c_angel_cake)
    texangle.grid(row=0, column=1)

    texapple = Entry(cakesFrame, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=c_apple_cake)
    texapple.grid(row=1, column=1)

    texbeer = Entry(cakesFrame, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=c_beer_cake)
    texbeer.grid(row=2, column=1)

    texbirthday = Entry(cakesFrame, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED,
                        textvariable=c_birthday_cake)
    texbirthday.grid(row=3, column=1)

    texchocolate = Entry(cakesFrame, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED,
                         textvariable=c_chocolate_cake)
    texchocolate.grid(row=4, column=1)

    texbanan = Entry(cakesFrame, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=c_banana_cake)
    texbanan.grid(row=5, column=1)

    texbutter = Entry(cakesFrame, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=c_butter_cake)
    texbutter.grid(row=6, column=1)

    texbattika = Entry(cakesFrame, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED,
                       textvariable=c_battik_cake)
    texbattika.grid(row=7, column=1)

    texbarrwine = Entry(cakesFrame, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED,
                        textvariable=c_brwine_cake)
    texbarrwine.grid(row=8, column=1)

    # coslebel & entry filed

    lebelcostfood = Label(costframe, text="Cost of Food", font=("arial", 16, "bold"), bg="#6F8FAF", fg="white")
    lebelcostfood.grid(row=0, column=0)

    textcostfood = Entry(costframe, font=("arial", 16, "bold"), bd=6, width=14, state="readonly",
                         textvariable=costoffoodvar)
    textcostfood.grid(row=0, column=1, padx=55)

    lebelcostdrink = Label(costframe, text="Cost of Drink", font=("arial", 16, "bold"), bg="#6F8FAF", fg="white")
    lebelcostdrink.grid(row=1, column=0)

    textcostdrink = Entry(costframe, font=("arial", 16, "bold"), bd=6, width=14, state="readonly",
                          textvariable=costofdrinkvar)
    textcostdrink.grid(row=1, column=1, padx=55)

    lebelcostcake = Label(costframe, text="Cost of Cake", font=("arial", 16, "bold"), bg="#6F8FAF", fg="white")
    lebelcostcake.grid(row=2, column=0)

    textcostcakes = Entry(costframe, font=("arial", 16, "bold"), bd=6, width=14, state="readonly",
                          textvariable=costofcakesvar)
    textcostcakes.grid(row=2, column=1, padx=55)

    lebelsubtotal = Label(costframe, text="Sub Total", font=("arial", 16, "bold"), bg="#6F8FAF", fg="white")
    lebelsubtotal.grid(row=0, column=2)

    textsubtotal = Entry(costframe, font=("arial", 16, "bold"), bd=6, width=14, state="readonly",
                         textvariable=subtotalvar)
    textsubtotal.grid(row=0, column=3, padx=55)

    lebelservicetax = Label(costframe, text="Service Tax", font=("arial", 16, "bold"), bg="#6F8FAF", fg="white")
    lebelservicetax.grid(row=1, column=2)

    textservicetax = Entry(costframe, font=("arial", 16, "bold"), bd=6, width=14, state="readonly",
                           textvariable=servicevar)
    textservicetax.grid(row=1, column=3, padx=55)

    lebeltotalcost = Label(costframe, text="Total Cost", font=("arial", 16, "bold"), bg="#6F8FAF", fg="white")
    lebeltotalcost.grid(row=2, column=2)

    texttotalcost = Entry(costframe, font=("arial", 16, "bold"), bd=6, width=14, state="readonly",
                          textvariable=totalcostvar)
    texttotalcost.grid(row=2, column=3, padx=55)

    # buttoms of recep & total

    buttontotal = Button(buttomFrame, text="Total", font=("arial", 14, "bold"), fg="white", bg="#6F8FAF", bd=3, padx=5,
                         command=totalofcost)
    buttontotal.grid(row=0, column=0)

    buttonrecepit = Button(buttomFrame, text="Receipt", font=("arial", 14, "bold"), fg="white", bg="#6F8FAF", bd=3,
                           padx=5,
                           command=recipt)
    buttonrecepit.grid(row=0, column=1)

    buttmonclear = Button(buttomFrame, text="Reset", font=("arial", 14, "bold"), fg="white", bg="#6F8FAF", bd=3, padx=5,
                          command=rest)
    buttmonclear.grid(row=0, column=3)

    buttomprint = Button(buttomFrame, text="Print", font=("arial", 14, "bold"), fg="white", bg="#6F8FAF", bd=3, padx=5,
                         command=print)
    buttomprint.grid(row=0, column=4)

    # text area for recept

    textreciept = Text(reciptFrame, font=("arial", 12, "bold"), bd=3, width=42, height=14)
    textreciept.grid(row=0, column=0)












def main_screen():
    global screen
    global username
    global password



    screen=Tk()
    screen.geometry("1310x690+0+0")
    screen.bg = ImageTk.PhotoImage(file="images/login.jpg")
    screen.bg_imge = Label(screen, image=screen.bg).place(x=0, y=0, relwidth=1, relheight=1, )

    lblTitle=Label(text="Login Here",font=("arial",50,'bold'),fg="black",bg="#d7dae2")
    lblTitle.pack(pady=50)

    mainframe=Frame(bg="#d7dae2",width=800,height=400)
    mainframe.pack(padx=20,pady=20)
    #user login

    Label(mainframe, text="Username", font=("arial", 30, "bold"), bg="#d7dae2").place(x=100, y=50)
    Label(mainframe, text="Password", font = ("arial", 30, "bold"), bg="#d7dae2").place(x=100, y=150)
    username = StringVar()
    password = StringVar()

    entry_username = Entry(mainframe, textvariable=username, width=12, bd=2, font = ("arial", 30))
    entry_username.place(x=400, y=50)

    entry_password = Entry(mainframe, textvariable=password, width=12, bd=2, font=("arial", 30),show="*")
    entry_password.place(x= 400, y=150)

    def rest():
        entry_username.delete(0, END)
        entry_password.delete(0, END)

    Button(mainframe, text="Login", height="2", width=23, bg="#ed3833", fg="white", bd=0,command=Login).place(x=100, y=250)
    Button(mainframe, text="Reset", height="2", width=23, bg="#1089ff", fg="white", bd=0,command=rest).place(x=300, y=250)
    Button(mainframe, text="Exit", height="2", width=23, bg="#00bd56", fg="white", bd=0,command=screen.destroy).place(x=500, y=250)


    screen.mainloop()

main_screen()