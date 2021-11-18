import ciag_arytmetyczny

# print("Obliczymy n-ty wyraz ciagu arytmetycznego \n")
a1= input("Podaj pierwszy wyraz ciagu arytmetycznego: ")
a1 = int(a1)
n = input("Podaj, ktory wyraz chcesz obliczyc :")
n = int(n)
r = input("Podaj roznice ciagu arytmetycznego: ")
r = int(r)

print(ciag_arytmetyczny.wyraz_ciagu1(a1, n, r))