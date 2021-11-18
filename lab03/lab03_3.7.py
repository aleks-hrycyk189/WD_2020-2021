def iloczyn_ciagu(* liczby):
    if len(liczby) == 0:
        return 0
    else:
        iloczyn = 1
        for a in liczby:
            iloczyn *= a
        return iloczyn
print(iloczyn_ciagu())
print(iloczyn_ciagu(4,8,12,3))