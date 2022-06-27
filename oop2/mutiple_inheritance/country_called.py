from country import Country

#create countries
#thailand lat = 13.7649136, long = 100.5360959
#population = 70,078,203
#area = 513,120
#temp = 32C

c1 = Country('Thailand',513120,70078203)
c1.setcordinate(13.7649136,100.5360959)
c1.setcelcius(32)
c1.showdetail()

#create 2 countries
c2 = Country('United States',9834000,329500000)
c2.setcordinate(39.2554791,102.2531752)
c2.setcelcius(26)
c2.showdetail()

c3 = Country('Singapore',728.6,5686800)
c3.setcordinate(1.3781448,103.8069525)
c3.setcelcius(31)
c3.showdetail()
