import pendulum

def rev_atual(data):
    if data.weekday() != 5:
        for i in range(1, 7):
            rev_atual = data.subtract(days=i)
            if rev_atual.weekday() == 5:
                break
    else:
        rev_atual = data
    return rev_atual

def calcular_rev0(data_rev):
    for i in range(7, 42, 7):
        rev_anterior = data_rev.subtract(days=i)
        if rev_anterior.month == rev_anterior.add(days=7).month:
            print("Mesmo mês operativo. Subtraindo a semana...")
        else:
            if rev_anterior.month == rev_anterior.add(days=6).month:
                rev0 = rev_anterior.add(days=7)
            else:
                rev0 = rev_anterior
            print(f"Rev0 encontrada: {rev0.format('DD/MM/YYYY')}")
            break
    return rev0

def calcular_mes_operativo(rev0):
    rev = 0
    revs = {"rev" + str(rev): rev0}
    for i in range(7, 42, 7):
        proxima_rev = rev0.add(days=i)
        if proxima_rev.add(days=7).month == rev0.add(days=7).month:
            rev += 1
            revs.update({"rev" + str(rev): proxima_rev})
        else:
            break
    return revs