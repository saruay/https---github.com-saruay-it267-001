from documentary_private import Documentary

m = Documentary('Mulan',2020,'action')
#m.__get_movie() เรียก private methodไม่ได้
#print(m._genre) เรียก attributeไม่ได้
m.print_detail()
print(f'year: {m._Movie__year}')
#obj._ClassName__privateattribute