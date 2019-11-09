from pprint import pprint as pp
sunday=[12,14,15,15,17,21,22,22]
monday=[13,14,14,16,15,20,21,19]
tuesday=[10,11,12,13,14,15,16,17]
daily=[sunday, monday, tuesday]
pp(daily)

transposed=list(zip(*daily))
pp(transposed)