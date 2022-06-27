class Movie:
    def __init__(self,title, year, genre) -> None:
        #private attribute begin with _
        self.__title = title
        self.__year = year
        self.__genre = genre

    #private method
    def __get_movie(self):
        print(f'title:{self.__title}\nyear:{self.__year}\ngenre:{self.__genre}')

    #เตรียมprivate
    def print_detail(self):
        self.__get_movie()