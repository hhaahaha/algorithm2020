# https://juhee-maeng.tistory.com/32

def rotation(key):
    """시계방향으로 90도씩 돌린다"""
    new_key = []
    for n in zip(*key):
        n = list(reversed(n))
        new_key.append(list(n))
    return new_key


def padding(key, lock):
    """2로 패딩한다"""
    key_n = len(key[-1])
    lock_n = len(lock)
    padding = (2 * (key_n - 1) + lock_n)

    pad_top = [[2 for _ in range(padding)] for _ in range(key_n - 1)]
    pad_side = [2 for _ in range(key_n - 1)]
    expand_lock = pad_top[::]

    for row in lock:
        new_row = pad_side + row + pad_side
        expand_lock.append(new_row)

    expand_lock.extend(pad_top)

    return expand_lock

def check_key(key, lock):
    key_n = len(key)
    lock_n = len(lock)
    slot_num = (lock_n * lock_n) -  sum(list(map(lambda x: sum(x) , lock)))

    key90 = rotation(key)
    key180 = rotation(key90)
    key270 = rotation(key180)

    expand_lock = padding(key, lock)
    is_match = False

    for x_start in range(lock_n + key_n - 1):
        for y_start in range(lock_n + key_n - 1):
            # 해당 위치에 자물쇠의 0이 모두 존재하는가?
            cnt = 0
            for i in range(key_n):
                for j in range(key_n):
                    if expand_lock[x_start+i][y_start+j] == 0:
                        cnt +=1
            if cnt == slot_num:
                keys = [key, key90, key180, key270]
                for k in keys:
                    another_key = False
                    check_slots = slot_num
                    for i in range(key_n):
                        for j in range(key_n):
                            if expand_lock[x_start+i][y_start+j] == 0 and k[i][j] == 1:
                                check_slots -= 1
                            elif expand_lock[x_start+i][y_start+j] == 1 and k[i][j] == 1:
                                another_key = True
                                break
                        if another_key: break

                    if check_slots == 0:
                        is_match = True
                        return True
            else: continue
    return is_match


def solution(key, lock):
    answer = True

    if check_key(key, lock) == False:
        answer = False

    return answer

