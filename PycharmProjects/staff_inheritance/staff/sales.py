from employee import Employee


class Sales(Employee):
    def __init__(self, fname, sname, no_of_years, territory):
        self.territory = territory
        super(Sales, self).__init__(fname, sname, no_of_years)


    def details(self):
        return super(Sales, self).details() + 'Territory: %s' % self.territory

    def calculate_salary(self):
        standard = super(Sales, self).calculate_salary()
        if self.territory.lower() == 'monaghan':
            bonus = standard * .05
        else:
            bonus = standard * .01

        return standard + bonus
