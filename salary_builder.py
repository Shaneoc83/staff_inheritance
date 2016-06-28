
from staff.developer import Developer
from staff.sales import Sales

emp1 = Developer('tom', 'bombadil', 4, 'Python')
emp2 = Developer('Martha', 'Wainright', 4, 'Java')
emp3 = Sales('Dom', 'Tombadil', 4, 'Monaghan')

print emp1.details()

print emp2.details()

print emp3.details()
