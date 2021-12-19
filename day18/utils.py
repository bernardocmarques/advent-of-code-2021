def addiction(l1, l2):
    l1 = [l1, l2]
    return l1


def traverse(lst):
    if isinstance(lst, list):
        traverse(lst[0])
        traverse(lst[1])
    else:
        print(lst)


found = False


def substitute_explosion(lst, to_add):
    global found
    found = False
    substitute_explosion_a(lst, to_add[0])
    found = False
    substitute_explosion_b(lst, to_add[1])


def substitute_explosion_a(lst, to_add):
    global found

    if isinstance(lst, list):
        lst[1] = substitute_explosion_a(lst[1], to_add)
        lst[0] = substitute_explosion_a(lst[0], to_add)
    else:
        if lst == 'X':
            found = True
            return lst

        if found:
            found = False
            return lst + to_add
    return lst


def substitute_explosion_b(lst, to_add):
    global found
    if isinstance(lst, list):
        lst[0] = substitute_explosion_b(lst[0], to_add)
        lst[1] = substitute_explosion_b(lst[1], to_add)
    else:
        if lst == 'X':
            found = True
            return 0

        if found:
            found = False
            return lst + to_add
    return lst


def explode(lst):
    _, to_add = explode_aux(lst)
    if to_add:
        substitute_explosion(lst, to_add)
    return bool(to_add)


def explode_aux(lst, level=0):
    if isinstance(lst[0], list):
        lst[0], to_add = explode_aux(lst[0], level + 1)
        if to_add:
            return lst, to_add

    if isinstance(lst[1], list):
        lst[1], to_add = explode_aux(lst[1], level + 1)
        if to_add:
            return lst, to_add

    if not isinstance(lst[0], list) and not isinstance(lst[1], list):
        if level >= 4:
            return 'X', [lst[0], lst[1]]

    return lst, []


def split(e, level=0):
    if isinstance(e, list):
        e[0], exploded, splitted = split(e[0], level + 1)
        if exploded or splitted:
            return e, exploded, splitted
        e[1], exploded, splitted = split(e[1], level + 1)
        if exploded:
            return e, exploded, splitted
    elif e >= 10:
        v = int(e / 2)
        e = [v, e - v]

        if level >= 4:
            return e, True, True
        else:
            return e, True, True
    else:
        return e, False, False

    return e, False, False


def magnitude(lst):
    if isinstance(lst, list):
        return 3 * magnitude(lst[0]) + 2 * magnitude(lst[1])
    else:
        return lst