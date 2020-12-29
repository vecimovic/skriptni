import eurostat
import sys
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
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

plots = {"Cijelokupna populacija" : 1,
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

#crta graf za cijelokupnu populaciju nekog područja
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
    ax.set_title(title,size='15')
    ax.set_xlabel("Godine")
    ax.set_ylabel("Populacija")


    return fig

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
    ax.set_title(title,size='15')
    ax.set_xlabel("Godine")
    ax.set_ylabel("Populacija")
    ax.legend()

    return fig

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
    ax.set_title(title + " ({}. godina)".format(labels[year_index]),size='15')
    
    return fig

#crta graf koji uspoređuje populaciju nekog područja prema bračnom statusu 
def marsta_barh_chart(data, nuts, marsta_index, sex_index, age_index, labels, title):
    for i in range(len(data)):
        if data[i][age_index] == 'TOTAL' and data[i][sex_index] == 'T':
            if data[i][marsta_index] == 'MAR':
                mar = data1[i]
            if data[i][marsta_index] == 'DISREP':
                disrep = data1[i]
            if data[i][marsta_index] == 'DIV':
                div = data1[i]
            if data[i][marsta_index] == 'DTHREP':
                dthrep = data1[i]
            if data[i][marsta_index] == 'REP':
                rep = data1[i]
            if data[i][marsta_index] == 'SIN':
                sin = data1[i]
            if data[i][marsta_index] == 'UNK':
                unk = data1[i]
            if data[i][marsta_index] == 'WID':
                wid = data1[i]
    
    nuts_index = labels.index(nuts)
    marstats = ['MAR', 'DISREP', 'DIV', 'DTHREP', 'REP', 'SIN', 'UNK', 'WID']
    '''
    MAR - u braku
    DISREP - Persons whose registered partnership was legally dissolved
    DIV - rastavljeni
    DTHREP - Persons whose registered partnership ended with the death of the partner
    REP - Persons in registered partnership
    SIN - samci
    UNK - nepoznato
    WID - Widowed persons
    '''
    stats = [mar[nuts_index], disrep[nuts_index], div[nuts_index], dthrep[nuts_index], rep[nuts_index],
            sin[nuts_index], unk[nuts_index], wid[nuts_index]]
    ind = np.arange(len(marstats))
    fig = Figure(figsize=(8,8))
    ax = fig.add_subplot(111)
    ax.barh(ind, stats, align='center', color='orange')
    ax.set_yticks(ind)
    ax.set_yticklabels(marstats)
    ax.set_xlabel('Populacija')
    ax.set_title(title)
    
    
    return fig

#crta graf koji uspoređuje populaciju nekog područja prema obiteljskom statusu 
def hhstatus_barh_chart(data, nuts, hhstatus_index, sex_index, age_index, labels, title):

    for i in range(len(data)):
        if data[i][age_index] == 'TOTAL' and data[i][sex_index] == 'T':
            if data[i][hhstatus_index] == 'CH_PAR':
                ch_par = data1[i]
            if data[i][hhstatus_index] == 'CPL':
                cpl = data1[i]
            if data[i][hhstatus_index] == 'CSU':
                csu = data1[i]
            if data[i][hhstatus_index] == 'MAR':
                mar = data1[i]
            if data[i][hhstatus_index] == 'NAP':
                nap = data1[i]
            if data[i][hhstatus_index] == 'PAR1':
                par1 = data1[i]
            if data[i][hhstatus_index] == 'REP':
                rep = data1[i]
            if data[i][hhstatus_index] == 'UNK':
                unk = data1[i]
            
    nuts_index = labels.index(nuts)
    hhstatuses = ['CH_PAR', 'CPL', 'CSU', 'MAR', 'NAP', 'PAR1', 'REP', 'UNK']
    '''
    CH_PAR - Child living with at least one parent
    CPL - Person in a couple
    CSU - Person in a consensual union
    MAR-Person in a married couple
    NAP- Not applicable
    PAR1 - Lone parent living with at least one child
    REP - Persons in a registered partnership
    UNK - ne zna se
    '''
    stats = [ch_par[nuts_index], cpl[nuts_index], csu[nuts_index], mar[nuts_index], nap[nuts_index],
    par1[nuts_index], rep[nuts_index], unk[nuts_index]]        
    ind = np.arange(len(hhstatuses))
    fig = Figure(figsize=(8,8))
    ax = fig.add_subplot(111)
    ax.barh(ind, stats, align='center', color='purple')
    ax.set_yticks(ind)
    ax.set_yticklabels(hhstatuses)
    ax.set_xlabel('Populacija')
    ax.set_title(title)
    
    
    return fig

#funckija koja se poziva kada se neki od radio gumbova(ili dropdown za godine) promijeni
def callback(*args):
    #za sada crta samo jedan graf(nisam stigla napravit da se na temelju varijabli crta ono kaj treba to prepustam tebi)
    fig = hhstatus_barh_chart(data2, 'HR031', hhstatus_index, sex_index2, age_index2, labels2, 'Primorsko-goranska županija')
    #trebali bi nekako napravit da se pobrise sadrzaj canvasa i da se ponovo nacrta nes na njemu
    canvas = FigureCanvasTkAgg(fig, master=plotPane)
    canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
    
    
#toc = eurostat.get_toc()

toc_df = eurostat.get_toc_df()

population_dataset = eurostat.subset_toc_df(toc_df, 'population')

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

#bilo bi korisno napravit naslove za vrste gumbova
#lijevi frame(za gumbe)
dataPane = Tk.Frame(root,bg="grey")
#1 podframe lijevog framea(za gumbe od zupanije)
dataPane1 = Tk.Frame(dataPane,bg="grey")
#2 podframe lijevog framea(za gumbe od vrsta grafa)
dataPane2 = Tk.Frame(dataPane,bg="grey")
#3 podframe lijevog framea(za dropdown za godine, to sluzi samo za graf di se usporeduju starosne dobi populacije)
dataPane3 = Tk.Frame(dataPane,bg="grey")
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
for (text, value) in nuts.items(): 
    Tk.Radiobutton(dataPane1, text = text, variable = v,  
                value = value, indicator = 0, 
                background = "light blue").pack(fill = Tk.X, ipady = 5)  

#vrste grafa
for (text, value) in plots.items(): 
    Tk.Radiobutton(dataPane2, text = text, variable = p,  
                value = value, indicator = 0, 
                background = "light blue").pack(fill = Tk.X, ipady = 5) 

#dropdown za godine(trebalo bi pozicionirat ga pored ili ispod gumba za graf koji uspoređuje starosne dobi)
years = Tk.OptionMenu(dataPane3, y, 2019, 2018, 2017,2016,2015,2014)
years.pack()
    

#poziva se funkcija callback svaki put kada se nesto promijeni
v.trace("w",callback)
p.trace("w",callback)
y.trace("w",callback)

root.mainloop()


#ako odkomentiram stvaranje pdfa crasha se jer se rade stalno novi prozori od gui-a, nez zas to radi,al mislim da se napravi pdf 
'''
#stvaranje pdf-a i naslovne stranice
pp = PdfPages('pop.pdf')
titlePage = plt.figure(figsize=(11.69,8.27))
titlePage.clf()
txt = 'Grafički prikaz podataka\n hrvatske populacije'
titlePage.text(0.5,0.5,txt, transform=titlePage.transFigure, size=24, ha="center")
pp.savefig(titlePage)

#prikaz usporedbe muske i zenske populacije 
subtitlePage1 = plt.figure(figsize=(11.69,8.27))
subtitlePage1.clf()
txt = 'Grafički prikaz usporedbe\n muške i ženske populacije\n po županijama'
subtitlePage1.text(0.5,0.5,txt, transform=subtitlePage1.transFigure, size=20, ha="center")
pp.savefig(subtitlePage1)

pgz = m_f_population_hist(HR, 'HR031', geo_index, sex_index, age_index, labels[4:],title="Primorsko-goranska županija")
lsz = m_f_population_hist(HR, 'HR032', geo_index, sex_index, age_index, labels[4:],title="Ličko-senjska županija")
zz = m_f_population_hist(HR, 'HR033', geo_index, sex_index, age_index, labels[4:],title="Zadarska županija")
skz = m_f_population_hist(HR, 'HR034', geo_index, sex_index, age_index, labels[4:],title="Šibensko-kninska županija")
sdz = m_f_population_hist(HR, 'HR035', geo_index, sex_index, age_index, labels[4:],title="Splitsko-dalmatinska županija")
iz = m_f_population_hist(HR, 'HR036', geo_index, sex_index, age_index, labels[4:],title="Istarska županija")
dnz = m_f_population_hist(HR, 'HR037', geo_index, sex_index, age_index, labels[4:],title="Dubrovačko-neretvanska županija")
gzg = m_f_population_hist(HR, 'HR041', geo_index, sex_index, age_index, labels[4:],title="Grad Zagreb")
zgz = m_f_population_hist(HR, 'HR042', geo_index, sex_index, age_index, labels[4:],title="Zagrebačka županija")
kzz = m_f_population_hist(HR, 'HR043', geo_index, sex_index, age_index, labels[4:],title="Krapinsko-zagorska županija")
vz = m_f_population_hist(HR, 'HR044', geo_index, sex_index, age_index, labels[4:],title="Varaždinska županija")
kkz = m_f_population_hist(HR, 'HR045', geo_index, sex_index, age_index, labels[4:],title="Koprivničko-križevačka županija")
mz = m_f_population_hist(HR, 'HR046', geo_index, sex_index, age_index, labels[4:],title="Međimurska županija")
bbz = m_f_population_hist(HR, 'HR047', geo_index, sex_index, age_index, labels[4:],title="Bjelovarsko-bilogorska županija")
vpz = m_f_population_hist(HR, 'HR048', geo_index, sex_index, age_index, labels[4:],title="Virovitičko-podravska županija")
psz = m_f_population_hist(HR, 'HR049', geo_index, sex_index, age_index, labels[4:],title="Požeško-slavonska županija")
bpz = m_f_population_hist(HR, 'HR04A', geo_index, sex_index, age_index, labels[4:],title="Brodsko-posavska županija")
obz = m_f_population_hist(HR, 'HR04B', geo_index, sex_index, age_index, labels[4:],title="Osječko-baranjska županija")
vsz = m_f_population_hist(HR, 'HR04C', geo_index, sex_index, age_index, labels[4:],title="Vukovarsko-srijemska županija")
kz = m_f_population_hist(HR, 'HR04D', geo_index, sex_index, age_index, labels[4:],title="Karlovačka županija")
smz = m_f_population_hist(HR, 'HR04E', geo_index, sex_index, age_index, labels[4:],title="Sisačko-moslavačka županija")

pp.savefig(pgz)
pp.savefig(lsz)
pp.savefig(zz)
pp.savefig(skz)
pp.savefig(sdz)
pp.savefig(iz)
pp.savefig(dnz)
pp.savefig(gzg)
pp.savefig(zgz)
pp.savefig(kzz)
pp.savefig(vz)
pp.savefig(kkz)
pp.savefig(mz)
pp.savefig(bbz)
pp.savefig(vpz)
pp.savefig(psz)
pp.savefig(bpz)
pp.savefig(obz)
pp.savefig(vsz)
pp.savefig(kz)
pp.savefig(smz)


subtitlePage2 = plt.figure(figsize=(11.69,8.27))
subtitlePage2.clf()
txt = 'Grafički prikaz usporedbe\n muške i ženske populacije\n cijele hrvatske'
subtitlePage2.text(0.5,0.5,txt, transform=subtitlePage2.transFigure, size=20, ha="center")
pp.savefig(subtitlePage2)

hr = m_f_population_hist(HR, 'HR0', geo_index, sex_index, age_index, labels[4:],title="Republika Hrvatska")
pp.savefig(hr)


#prikaz usporedbe populacije po starosti
year_index = labels.index(2019)

subtitlePage3 = plt.figure(figsize=(11.69,8.27))
subtitlePage3.clf()
txt = 'Grafički prikaz usporedbe\n populacije po starosti \n po županijama'
subtitlePage3.text(0.5,0.5,txt, transform=subtitlePage3.transFigure, size=20, ha="center")
pp.savefig(subtitlePage3)

pgz = population_age_pie_chart(HR, 'HR031', geo_index, sex_index, age_index, year_index, labels, 'Primorsko-goranska županija')
lsz = population_age_pie_chart(HR, 'HR032', geo_index, sex_index, age_index, year_index,labels,title="Ličko-senjska županija")
zz = population_age_pie_chart(HR, 'HR033', geo_index, sex_index, age_index, year_index, labels,title="Zadarska županija")
skz = population_age_pie_chart(HR, 'HR034', geo_index, sex_index, age_index, year_index, labels,title="Šibensko-kninska županija")
sdz = population_age_pie_chart(HR, 'HR035', geo_index, sex_index, age_index, year_index, labels,title="Splitsko-dalmatinska županija")
iz = population_age_pie_chart(HR, 'HR036', geo_index, sex_index, age_index, year_index, labels,title="Istarska županija")
dnz = population_age_pie_chart(HR, 'HR037', geo_index, sex_index, age_index, year_index, labels,title="Dubrovačko-neretvanska županija")
gzg = population_age_pie_chart(HR, 'HR041', geo_index, sex_index, age_index, year_index, labels,title="Grad Zagreb")
zgz = population_age_pie_chart(HR, 'HR042', geo_index, sex_index, age_index, year_index, labels,title="Zagrebačka županija")
kzz = population_age_pie_chart(HR, 'HR043', geo_index, sex_index, age_index, year_index, labels,title="Krapinsko-zagorska županija")
vz = population_age_pie_chart(HR, 'HR044', geo_index, sex_index, age_index, year_index, labels,title="Varaždinska županija")
kkz = population_age_pie_chart(HR, 'HR045', geo_index, sex_index, age_index, year_index, labels,title="Koprivničko-križevačka županija")
mz = population_age_pie_chart(HR, 'HR046', geo_index, sex_index, age_index, year_index, labels,title="Međimurska županija")
bbz = population_age_pie_chart(HR, 'HR047', geo_index, sex_index, age_index, year_index, labels,title="Bjelovarsko-bilogorska županija")
vpz = population_age_pie_chart(HR, 'HR048', geo_index, sex_index, age_index, year_index, labels,title="Virovitičko-podravska županija")
psz = population_age_pie_chart(HR, 'HR049', geo_index, sex_index, age_index, year_index, labels,title="Požeško-slavonska županija")
bpz = population_age_pie_chart(HR, 'HR04A', geo_index, sex_index, age_index, year_index, labels,title="Brodsko-posavska županija")
obz = population_age_pie_chart(HR, 'HR04B', geo_index, sex_index, age_index, year_index, labels,title="Osječko-baranjska županija")
vsz = population_age_pie_chart(HR, 'HR04C', geo_index, sex_index, age_index, year_index, labels,title="Vukovarsko-srijemska županija")
kz = population_age_pie_chart(HR, 'HR04D', geo_index, sex_index, age_index, year_index, labels,title="Karlovačka županija")
smz = population_age_pie_chart(HR, 'HR04E', geo_index, sex_index, age_index, year_index, labels,title="Sisačko-moslavačka županija")

pp.savefig(pgz)
pp.savefig(lsz)
pp.savefig(zz)
pp.savefig(skz)
pp.savefig(sdz)
pp.savefig(iz)
pp.savefig(dnz)
pp.savefig(gzg)
pp.savefig(zgz)
pp.savefig(kzz)
pp.savefig(vz)
pp.savefig(kkz)
pp.savefig(mz)
pp.savefig(bbz)
pp.savefig(vpz)
pp.savefig(psz)
pp.savefig(bpz)
pp.savefig(obz)
pp.savefig(vsz)
pp.savefig(kz)
pp.savefig(smz)

subtitlePage4 = plt.figure(figsize=(11.69,8.27))
subtitlePage4.clf()
txt = 'Grafički prikaz usporedbe\n populacije po starosti\n cijele hrvatske'
subtitlePage4.text(0.5,0.5,txt, transform=subtitlePage4.transFigure, size=20, ha="center")
pp.savefig(subtitlePage4)

hr = population_age_pie_chart(HR, 'HR0', geo_index, sex_index, age_index, year_index, labels,title="Republika Hrvatska")

pp.savefig(hr)

pp.close()
'''





        

        

   