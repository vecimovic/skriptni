import eurostat
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import numpy as np

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
    fig = plt.figure(figsize=(11.69,8.27))
    plt.bar(ind,f,width,label='Ž',color='red')
    plt.bar(ind + width,m,width,label='M',color='blue')
    plt.xticks(ind + width / 2,labels)
    plt.title(title,size='15')
    plt.xlabel("Godine")
    plt.ylabel("Populacija")
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
    return fig

def make_autopct(values):
    def my_autopct(pct):
        return '{p:.1f}%'.format(p=pct)
    return my_autopct

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
    
    fig = plt.figure(figsize=(11.69,8.27))
    plt.pie(data, labels = ages, autopct=make_autopct(data))
    plt.title(title + " ({}. godina)".format(labels[year_index]),size='15')
    
    return fig
    

#toc = eurostat.get_toc()

toc_df = eurostat.get_toc_df()

population_dataset = eurostat.subset_toc_df(toc_df, 'population')

#Populacija 1. siječnja po dobnoj skupini, spolu i NUTS 3 regijama(županije)
data = eurostat.get_data('demo_r_pjangrp3')

#oznake podataka
labels = data[0]
geo_index = labels.index('geo\\time')
sex_index = labels.index('sex')
age_index = labels.index('age')

#skup svih podataka(demo_r_pjangrp3) za hrvatsku
HR = []
for i in range(len(data)):
    if data[i][geo_index].find('HR') != -1:
        HR.append(data[i])
        


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






        

        

   