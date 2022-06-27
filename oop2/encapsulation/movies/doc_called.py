from documentary import Documentary
m = Documentary()
m._add_movie('My Octopus Teacher',2020,'Documentary')
m.add_channel('NetFlix')
m._get_movie()

#access protected attribute from super class(Movie)
print(f'Title:{m._title}')