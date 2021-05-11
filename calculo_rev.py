import pendulum

def calcular_rev_atual(data):
    if data.weekday() != 5:
        for i in range(1, 7):
            rev_atual = data.subtract(days=i)
            if rev_atual.weekday() == 5:
                break
    else:
        rev_atual = data
    return rev_atual

def calcular_rev0(rev_atual):
    rev_anterior = rev_atual
    for i in range(7, 28, 7):
        if rev_anterior.month == rev_anterior.add(days=7).month:
            print("Mesmo mês operativo. Subtraindo a semana...")
            rev_anterior = rev_atual.subtract(days=i)
        else:
            rev0 = rev_atual.subtract(days=i-7)
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