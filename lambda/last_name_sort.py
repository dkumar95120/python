scientists = ['Marie Curie', 'Albert Einstien', 'Niels Bohr', 'Issac Newton', \
              'Dmitri Mendeleev', 'Antoine Lavoisier', 'Carl Linnaeus', \
              'Alfred Wegner', 'Charles Darwin']

last_name_sort = sorted(scientists, key=lambda name: name.split()[-1])
print(last_name_sort)