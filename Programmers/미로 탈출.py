def solution(n, start, end, roads, traps):
    answer = 100000000000000

    def move(s, reverse, time):
        if s == end:
            print(time)
            return time
        else:
            if reverse:
                for road in roads:
                    if road[1] == s:
                        if road[0] in traps:
                            if time+road[2] >= answer:
                                break
                            move(road[0], False, time + road[2])
                        else:
                            move(road[0], True, time + road[2])
            else:
                for road in roads:
                    if road[0] == s:
                        if road[1] in traps:
                            if time+road[2] >= answer:
                                break
                            move(road[1], True, time + road[2])
                        else:
                            move(road[1], False, time + road[2])
    move(start, False, 0)
    return answer


solution(4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3])
