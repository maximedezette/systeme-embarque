class Info:

    __first_line = ""
    __second_line = ""
    __level = "INFO"
    __telegram_message = "Une erreur est survenue!"


    def set_first_line(self,line):
        self.__first_line = line

    def set_second_line(self,line):
        self.__second_line = line

    def set_level(self,level):
        self.__level = level  

    def set_telegram_message(self,telegram_message):
        self.__telegram_message = telegram_message   

    def get_first_line(self):
        return self.__first_line

    def get_second_line(self):
        return self.__second_line

    def get_level(self):
        return self.__level

    def get_telegram_message(self):
        return self.__telegram_message
