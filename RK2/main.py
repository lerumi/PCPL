from operator import itemgetter
class Cond:
    # Дерижер
    def __init__(self, id, fio, sal, orc_id):
        self.id = id
        self.fio = fio
        self.sal = sal
        self.orc_id = orc_id


class Orc:
    # Оркестр
    def __init__(self, id, name):
        self.id = id
        self.name = name


class CondOrc:
    # Оркестр
    def __init__(self, orc_id, cond_id):
        self.orc_id = orc_id
        self.cond_id = cond_id

print(Orc(1, 'Duhovie'))
orcs = [
    Orc(1, 'Симфонический оркестр'),
    Orc(2, 'Духовой оркестр'),
    Orc(3, 'Струнный оркестр'),
    Orc(4, 'Эстрадный оркестр'),
    Orc(5, 'Джазовый оркестр'),
    Orc(6, 'Военный оркестр')
]
conds = [
    Cond(1, 'Чичиков', 25000, 1),
    Cond(2, 'Иванов', 35000, 1),
    Cond(3, 'Артамонов', 25000, 2),
    Cond(4, 'Петров', 45000, 3),
    Cond(5, 'Ванин', 55000, 3),
    Cond(6, 'Семенов', 45000, 3),
    Cond(7, 'Герасимов', 25000, 4),
    Cond(8, 'Бирюков', 35000, 5),
    Cond(9, 'Абачков', 25000, 6)
]
conds_orcs = [
    CondOrc(1, 1),
    CondOrc(1, 2),
    CondOrc(2, 3),
    CondOrc(3, 4),
    CondOrc(3, 5),
    CondOrc(3, 6),
    CondOrc(4, 7),
    CondOrc(5, 8),
    CondOrc(6, 9),
]


def main():
    one_to_many = [(c.fio, c.sal, o.name)
                   for o in orcs
                   for c in conds
                   if c.orc_id == o.id]
    many_to_many_temp = [(o.name, co.orc_id, co.cond_id)
                         for o in orcs
                         for co in conds_orcs
                         if o.id == co.orc_id]
    many_to_many = [(c.fio, c.sal, orc_name)
                    for orc_name, orc_id, cond_id in many_to_many_temp
                    for c in conds if c.id == cond_id]

    print('Задание Е1')
    print(list(filter(lambda i: i[2].find('Струнный') != -1, one_to_many)))

    print('Задание Е2')
    res_12_unsorted = []
    for o in orcs:
        orc_conds = list(filter(lambda i: i[2] == o.name, one_to_many))
        if len(orc_conds) > 0:
            o_sals = [sal for _, sal, _ in orc_conds]
            o_sals_sum = round(sum(o_sals) / len(orc_conds), 2)
            res_12_unsorted.append((o.name, o_sals_sum))

    res_12 = sorted(res_12_unsorted, key=itemgetter(1), reverse=True)
    print(res_12)

    print('Задание Е3')
    print(list(filter(lambda i: i[0].find('А') != -1, many_to_many)))


if __name__ == '__main__':
    main()