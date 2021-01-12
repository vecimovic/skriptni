import eurostat
import sys
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import webbrowser as wb
if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk

matplotlib.use("TkAgg")

#riječnici za gumbove
nuts = {"Republika Hrvatska" : "HR0", 
          "Primorsko-goranska županija" : "HR031", 
          "Ličko-senjska županija" : "HR032", 
          "Zadarska županija" : "HR033", 
          "Šibensko-kninska županija" : "HR034", 
          "Splitsko-dalmatinska županija" : "HR035",
          "Istarska županija" : "HR036", 
          "Dubrovačko-neretvanska županija" : "HR037" ,
          "Grad Zagreb" : "HR041",
          "Zagrebačka županija" : "HR042",
          "Krapinsko-zagorska županija" : "HR043",
          "Varaždinska županija" : "HR044",
          "Koprivničko-križevačka županija" : "HR045",
          "Međimurska županija" : "HR046",
          "Bjelovarsko-bilogorska županija" : "HR047",
          "Virovitičko-podravska županija" : "HR048",
          "Požeško-slavonska županija" : "HR049",
          "Brodsko-posavska županija" : "HR04A",
          "Osječko-baranjska županija" : "HR04B",
          "Vukovarsko-srijemska županija" : "HR04C",
          "Karlovačka županija" : "HR04D",
          "Sisačko-moslavačka županija" : "HR04E"}

plots = {"Cjelokupna populacija" : 1,
         "Usporedba muške i ženske populacije" : 2,
         "Usporedba populacije po starosti": 3,
         "Usporedba populacije po bračnom statusu" : 4,
         "Usporedba populacije po obiteljskom statusu": 5
    }

#vraca kljuc rijecnka na temelju vrijednosti
def get_key(val,dict):
    for key, value in dict.items():
         if val == value:
             return key
 
    return "key doesn't exist"

#crta graf za cjelokupnu populaciju nekog područja
def population_hist(HR, nuts, geo_index, sex_index, age_index, labels, title):

    for i in range(len(HR)):
        if HR[i][geo_index] == nuts:
            if HR[i][sex_index] == 'T' and HR[i][age_index] == 'TOTAL':
                p = HR[i][4:]

    width = 0.3
    n = len(labels)
    ind = np.arange(n)
    fig = Figure(figsize=(8,8))
    ax = fig.add_subplot(111)
    ax.bar(ind,p,width,color='green')
    ax.set_xticks(ind)
    ax.set_xticklabels(labels, fontsize = 10)
    ax.set_title('Cjelokupna populacija \n\n' + title,size='15')
    ax.set_xlabel("Godine",size='13')
    ax.set_ylabel("Populacija",size='13')

    tabl = Figure(figsize=(8,8))
    axt = tabl.add_subplot(111)
    data = np.array([labels, p],np.int32)
    clust_data = np.transpose(data)
    collabel= ("Godina", "Populacija")
    axt.axis('tight')
    axt.axis('off')
    the_table = axt.table(cellText=clust_data,colLabels=collabel,loc='center')
    the_table[(0, 0)].set_facecolor("green")
    the_table[(0, 1)].set_facecolor("green")
    axt.set_title('Tablica za cjelokupnu populaciju \n\n' + title, size='15')
    
    return fig, tabl

#crta graf usporedbe muske i zenske populacije nekog područja
def m_f_population_hist(HR, nuts, geo_index, sex_index, age_index, labels, title):

    for i in range(len(HR)):
        if HR[i][geo_index] == nuts:
            if HR[i][sex_index] == 'F' and HR[i][age_index] == 'TOTAL':
                f = HR[i][4:]
            if HR[i][sex_index] == 'M' and HR[i][age_index] == 'TOTAL':
                m = HR[i][4:]
    width = 0.3
    n = len(labels)
    ind = np.arange(n)
    fig = Figure(figsize=(8,8))
    ax = fig.add_subplot(111)
    ax.bar(ind,f,width,label='Ž',color='red')
    ax.bar(ind + width,m,width,label='M',color='blue')
    ax.set_xticks(ind + width / 2)
    ax.set_xticklabels(labels, fontsize = 10)
    ax.set_title('Usporedba muške i ženske populacije \n\n' + title,size='15')
    ax.set_xlabel("Godine",size='13')
    ax.set_ylabel("Populacija",size='13')
    ax.legend()
    
    tabl = Figure(figsize=(8,8))
    axt = tabl.add_subplot(111)
    data = np.array([labels, f, m],np.int32)
    clust_data = np.transpose(data)
    collabel= ("Godina", "Ženska populacija", "Muška populacija")
    axt.axis('tight')
    axt.axis('off')
    axt.set_title('Tablica za usporedbu muške i ženske populacije \n\n' + title,size='15')
    the_table = axt.table(cellText=clust_data,colLabels=collabel,loc='center')
    the_table[(0, 0)].set_facecolor("#b39ddb")
    the_table[(0, 1)].set_facecolor("#ef9a9a")
    the_table[(0, 2)].set_facecolor("#90caf9")
    return fig, tabl

def make_autopct(values):
    def my_autopct(pct):
        return '{p:.1f}%'.format(p=pct)
    return my_autopct

#crta graf usporedbe starosne dobi stanovnika nekog područja
def population_age_pie_chart(HR, nuts, geo_index, sex_index, age_index, year_index, labels, title):
    
    for i in range(len(HR)):
        if HR[i][geo_index] == nuts:
            if HR[i][sex_index] == 'T' and HR[i][age_index] == 'Y_LT5':
                y_lt5 = HR[i][year_index]
            if HR[i][sex_index] == 'T' and HR[i][age_index] == 'Y5-9':
                y5_9 = HR[i][year_index]
            if HR[i][sex_index] == 'T' and HR[i][age_index] == 'Y10-14':
                y10_14 = HR[i][year_index]
            if HR[i][sex_index] == 'T' and HR[i][age_index] == 'Y15-19':
                y15_19 = HR[i][year_index]
            if HR[i][sex_index] == 'T' and HR[i][age_index] == 'Y20-24':
                y20_24 = HR[i][year_index]
            if HR[i][sex_index] == 'T' and HR[i][age_index] == 'Y25-29':
                y25_29 = HR[i][year_index]
            if HR[i][sex_index] == 'T' and HR[i][age_index] == 'Y30-34':
                y30_34 = HR[i][year_index]
            if HR[i][sex_index] == 'T' and HR[i][age_index] == 'Y35-39':
                y35_39 = HR[i][year_index]
            if HR[i][sex_index] == 'T' and HR[i][age_index] == 'Y40-44':
                y40_44 = HR[i][year_index]
            if HR[i][sex_index] == 'T' and HR[i][age_index] == 'Y45-49':
                y45_49 = HR[i][year_index]
            if HR[i][sex_index] == 'T' and HR[i][age_index] == 'Y50-54':
                y50_54 = HR[i][year_index]
            if HR[i][sex_index] == 'T' and HR[i][age_index] == 'Y55-59':
                y55_59 = HR[i][year_index]
            if HR[i][sex_index] == 'T' and HR[i][age_index] == 'Y60-64':
                y60_64 = HR[i][year_index]
            if HR[i][sex_index] == 'T' and HR[i][age_index] == 'Y65-69':
                y65_69 = HR[i][year_index]
            if HR[i][sex_index] == 'T' and HR[i][age_index] == 'Y70-74':
                y70_74 = HR[i][year_index]
            if HR[i][sex_index] == 'T' and HR[i][age_index] == 'Y75-79':
                y75_79 = HR[i][year_index]
            if HR[i][sex_index] == 'T' and HR[i][age_index] == 'Y80-84':
                y80_84 = HR[i][year_index]
            if HR[i][sex_index] == 'T' and HR[i][age_index] == 'Y85-89':
                y85_89 = HR[i][year_index]
            if HR[i][sex_index] == 'T' and HR[i][age_index] == 'Y_GE90':
                y_ge90 = HR[i][year_index]
    ages = ['0-5', '5-9', '10-14', '15-19', '20-24', '25-29', '30-34', '35-39', '40-44', '45-49',
            '50-54', '55-59', '60-64', '65-69', '70-74', '75-79', '80-84', '85-89', '>90']
    data = [y_lt5, y5_9, y10_14, y15_19, y20_24, y25_29, y30_34, y35_39, y40_44, y45_49, y50_54, 
            y55_59, y60_64, y65_69, y70_74, y75_79, y80_84, y85_89, y_ge90]
    
    fig = Figure(figsize=(8,8))
    ax = fig.add_subplot(111)
    ax.pie(data, labels = ages, autopct=make_autopct(data))
    ax.set_title('Usporedba populacije po starosti \n\n'+ title + " ({}. godina)".format(labels[year_index]),size='15')
    
    tabl = Figure(figsize=(8,8))
    axt = tabl.add_subplot(111)
    d = np.array([ages, data])
    clust_data = np.transpose(d)
    collabel= ("Raspon godina", "Populacija")
    axt.axis('tight')
    axt.axis('off')
    axt.set_title('Tablica za usporedbu populacije po starosti \n\n'+ title + " ({}. godina)".format(labels[year_index]),size='15')
    the_table = axt.table(cellText=clust_data,colLabels=collabel,loc='center')
    the_table[(0, 0)].set_facecolor("#ffee58")
    the_table[(0, 1)].set_facecolor("#ffee58")
    return fig,tabl

#crta graf koji uspoređuje populaciju nekog područja prema bračnom statusu 
def marsta_barh_chart(data, nuts, marsta_index, sex_index, age_index, labels, title):
    for i in range(len(data)):
        if data[i][age_index] == 'TOTAL' and data[i][sex_index] == 'T':
            if data[i][marsta_index] == 'MAR':
                mar = data1[i]
            if data[i][marsta_index] == 'DIV':
                div = data1[i]
            if data[i][marsta_index] == 'SIN':
                sin = data1[i]
            if data[i][marsta_index] == 'UNK':
                unk = data1[i]
            if data[i][marsta_index] == 'WID':
                wid = data1[i]
    
    nuts_index = labels.index(nuts)
    marstats = ['MAR', 'DIV', 'SIN', 'UNK', 'WID']
    stats = [mar[nuts_index], div[nuts_index], sin[nuts_index], unk[nuts_index], wid[nuts_index]]
    ind = np.arange(len(marstats))
    fig = Figure(figsize=(8,8))
    ax = fig.add_subplot(111)
    ax.barh(ind, stats, align='center', color='orange')
    ax.set_yticks(ind)
    ax.set_yticklabels(marstats)
    ax.set_xlabel('Populacija',size='13')
    ax.set_title('Usporedba populacije po bračnom statusu \n\n' + title,size='15')

    tabl = Figure(figsize=(8,8))
    axt = tabl.add_subplot(111)
    d = np.array([marstats, stats])
    clust_data = np.transpose(d)
    collabel= ("Bračni status", "Populacija")
    axt.axis('tight')
    axt.axis('off')
    axt.set_title('Tablica za usporedbu populacije po bračnom statusu \n\n' + title,size='15')
    the_table = axt.table(cellText=clust_data,colLabels=collabel,loc='center')
    the_table[(0, 0)].set_facecolor("orange")
    the_table[(0, 1)].set_facecolor("orange")
    return fig, tabl
    

#crta graf koji uspoređuje populaciju nekog područja prema obiteljskom statusu 
def hhstatus_barh_chart(data, nuts, hhstatus_index, sex_index, age_index, labels, title):

    for i in range(len(data)):
        if data[i][age_index] == 'TOTAL' and data[i][sex_index] == 'T':
            if data[i][hhstatus_index] == 'CPL':
                cpl = data1[i]
            if data[i][hhstatus_index] == 'MAR':
                mar = data1[i]
            if data[i][hhstatus_index] == 'PAR1':
                par1 = data1[i]
            if data[i][hhstatus_index] == 'REP':
                rep = data1[i]
            if data[i][hhstatus_index] == 'UNK':
                unk = data1[i]
            
    nuts_index = labels.index(nuts)
    hhstatuses = ['CPL','MAR','PAR1', 'REP', 'UNK']
    stats = [cpl[nuts_index], mar[nuts_index], par1[nuts_index], rep[nuts_index], unk[nuts_index]]        
    ind = np.arange(len(hhstatuses))
    fig = Figure(figsize=(8,8))
    ax = fig.add_subplot(111)
    ax.barh(ind, stats, align='center', color='purple')
    ax.set_yticks(ind)
    ax.set_yticklabels(hhstatuses)
    ax.set_xlabel('Populacija',size='13')
    ax.set_title('Usporedba populacije po obiteljskom statusu \n\n' + title,size='15')
    
    tabl = Figure(figsize=(8,8))
    axt = tabl.add_subplot(111)
    d = np.array([hhstatuses, stats])
    clust_data = np.transpose(d)
    collabel= ("Obiteljski status", "Populacija")
    axt.axis('tight')
    axt.axis('off')
    axt.set_title('Tablica za usporedbu populacije po obiteljskom statusu \n\n' + title,size='15')
    the_table = axt.table(cellText=clust_data,colLabels=collabel,loc='center')
    the_table[(0, 0)].set_facecolor("#b39ddb")
    the_table[(0, 1)].set_facecolor("#b39ddb")
    return fig, tabl


#funkcija koja se poziva kada se neki od radio gumbova(ili dropdown za godine) promijeni
def callback(*args):

    for widget in plotPane.winfo_children():
        widget.destroy()
    if (p.get() == 1):
        fig,tabl = population_hist(HR, v.get(), geo_index, sex_index, age_index, labels[4:], get_key(v.get(), nuts))  
    elif (p.get() == 2):
        fig,tabl = m_f_population_hist(HR, v.get(), geo_index, sex_index, age_index, labels[4:], get_key(v.get(), nuts))
    elif (p.get() == 3):
        year_index = labels.index(y.get())
        fig,tabl = population_age_pie_chart(HR, v.get(), geo_index, sex_index, age_index, year_index, labels, get_key(v.get(), nuts))
    elif (p.get() == 4):
        fig,tabl=  marsta_barh_chart(data1, v.get(), marsta_index, sex_index1, age_index1, labels1, get_key(v.get(), nuts))
    elif (p.get() == 5):
        fig,tabl = hhstatus_barh_chart(data2, v.get(), hhstatus_index, sex_index2, age_index2, labels2, get_key(v.get(), nuts))
    global graf
    global tablica
    
    graf = fig
    tablica = tabl
    canvas = FigureCanvasTkAgg(fig, master=plotPane)
    canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)


def save():
    pdf.savefig(graf)
    pdf.savefig(tablica)

def close():
    pdf.close()
    wb.open_new('podaci.pdf')
#toc = eurostat.get_toc()

#toc_df = eurostat.get_toc_df()
global graf
global tablica 

#population_dataset = eurostat.subset_toc_df(toc_df, 'population')
pdf = PdfPages('podaci.pdf')
#Populacija 1. siječnja po dobnoj skupini, spolu i NUTS 3 regijama(županije)
data = eurostat.get_data('demo_r_pjangrp3')
#Populacija prema bračnom statusu i NUTS 3 regijama za 2011. g(županije)
data1 = eurostat.get_data('cens_11ms_r3')
#Populacija prema obiteljskom statusu i NUTS 3 regijama za 2011. g(županije)
data2 = eurostat.get_data('cens_11fs_r3')


#oznake podataka
#za data
labels = data[0]
geo_index = labels.index('geo\\time')
sex_index = labels.index('sex')
age_index = labels.index('age')
#za data1
labels1 = data1[0]
sex_index1 = labels1.index('sex')
age_index1 = labels1.index('age')
marsta_index = labels1.index('marsta')
#za data2
labels2 = data2[0]
sex_index2 = labels2.index('sex')
age_index2 = labels2.index('age')
hhstatus_index = labels2.index('hhstatus')

#skup svih podataka(demo_r_pjangrp3) za hrvatsku
HR = []
for i in range(len(data)):
    if data[i][geo_index].find('HR') != -1:
        HR.append(data[i])


#početak gui prozora
root = Tk.Tk()
root.title("Grafički prikaz podataka hrvatske populacije")
screen_width  = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f'{screen_width}x{screen_height}')


#lijevi frame(za gumbe)
dataPane = Tk.Frame(root,bg="grey")
#1 podframe lijevog framea(za gumbe od zupanije)
dataPane1 = Tk.Frame(dataPane,bg="#ede7f6")
#2 podframe lijevog framea(za gumbe od vrsta grafa)
dataPane2 = Tk.Frame(dataPane,bg="#ede7f6")
#3 podframe lijevog framea(za dropdown za godine, to sluzi samo za graf di se usporeduju starosne dobi populacije)
dataPane3 = Tk.Frame(dataPane,bg="#ede7f6")
#frame za graf
plotPane = Tk.Frame(root)
dataPane.grid(row=0,column=0,sticky="nsew")
plotPane.grid(row=0,column=1,sticky="nsew")
dataPane1.grid(row=0,column=0,sticky="nsew")
dataPane2.grid(row=0,column=1,sticky="nsew")
dataPane3.grid(row=0,column=2,sticky="nsew")


root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

dataPane.rowconfigure(0, weight=1)
dataPane.columnconfigure(0, weight=1)
dataPane.columnconfigure(1, weight=1)
dataPane.columnconfigure(2, weight=1)



#varijable u koje se spremaju vrijednosti radio gumba i dropdowna
#teritorij(zupanije)
v = Tk.StringVar(root, "HR0")
#vrsta grafa
p = Tk.IntVar(root, 1) 
#godina
y = Tk.IntVar(root, 2019)
  
#zupanije
nuts_var =Tk.StringVar()
nuts_label = Tk.Label( dataPane1, textvariable=nuts_var, font="11", background="#ede7f6")
nuts_var.set("ODABIR \nTERITORIJALNOG PODRUČJA")
nuts_label.pack() 
for (text, value) in nuts.items(): 
    Tk.Radiobutton(dataPane1, text = text, variable = v,  
                value = value, indicator = 0, 
                background = "#ff8a80").pack(fill = Tk.X,ipady = 4)  

#vrste grafa
plots_var =Tk.StringVar()
plots_label = Tk.Label( dataPane2, textvariable=plots_var, font="11", background="#ede7f6")
plots_var.set("ODABIR \nVRSTE GRAFA")
plots_label.pack() 
for (text, value) in plots.items(): 
    Tk.Radiobutton(dataPane2, text = text, variable = p,  
                value = value, indicator = 0, 
                background = "light blue").pack(fill = Tk.X, ipady = 4) 

#dropdown za godine
years = Tk.OptionMenu(dataPane3, y, 2019, 2018, 2017,2016,2015,2014)
years.config(bg = "light blue")
years["menu"].config(bg="light blue")
years.pack()
years.place(y = 110)

#gumb za spremanje grafa i tablice u pdf
button_tk = Tk.Button(dataPane2, text="Spremi graf i pripadajuću\n tablicu podataka u zajednički pdf", command=save) 
button_tk.config(bg = "yellow")
button_tk.pack()
button_tk.place(x = 40, y= 400)
#gumb za zatvaranje pdf-a i otvaranje istog na racunalu
button_tk = Tk.Button(dataPane2, text="Zatvori spremanje u pdf", command=close) 
button_tk.config(bg = "yellow")
button_tk.pack(fill = Tk.X)
button_tk.place(x = 40, y= 500)

fig,tabl = population_hist(HR, "HR0", geo_index, sex_index, age_index, labels[4:], get_key("HR0", nuts))
graf = fig
tablica = tabl
canvas = FigureCanvasTkAgg(fig, master=plotPane)
canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

#poziva se funkcija callback svaki put kada se nesto promijeni
v.trace("w",callback)
p.trace("w",callback)
y.trace("w",callback)

root.mainloop()