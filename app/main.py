#!/usr/bin/env python3

class NewCalendar :

    def __init__(self, days_in_year, days_in_month, days_in_week) :
        self.days_in_year = int(days_in_year)
        self.days_in_month = int(days_in_month)
        self.days_in_week = int(days_in_week)

        #ASCIIコード
        self.A = 65

    def is_valid_Date(self, year, month, day) :
        return (day < self.days_in_month and ((month - 1)*self.days_in_month)+ day < self.days_in_year)

    def getDate(self, fullyear) :
        year, month, day = list(map(int, fullyear.split('-')))
        if(self.is_valid_Date(year, month, day)) :
            number_of_days_from_00010101 = self._calculate_at_year(year) +self._calculate_at_month(month) +self._calculate_at_day(day)
            return chr((number_of_days_from_00010101 % self.days_in_week) + self.A)
        else :
            return ('-1')

    def _calculate_at_year(self, year) :
        return (year - 1) * self.days_in_year


    def _calculate_at_month(self, month) :
        return (month - 1) * self.days_in_month


    def _calculate_at_day(self, day) :
        return (day - 1)





def main(argv):
    days_in_year = argv[0]
    days_in_month = argv[1]
    days_in_week = argv[2]
    date = argv[3]

    calendar = NewCalendar(days_in_year, days_in_month, days_in_week)
    print(calendar.getDate(argv[3]))
