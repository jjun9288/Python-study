def queue_time(customers, n):
    time = [0]*n
    for i in customers:
        time[0] += i
        time.sort()
        return max(time)

queue_time([],1)

def test_q2():
    assert queue_time([], 1)== 0
    assert queue_time([5], 1) == 5
    assert queue_time([2], 5) == 2
    assert queue_time([1,2,3,4,5], 1) == 15
    assert queue_time([1,2,3,4,5], 100) == 5
    assert queue_time([2,2,3,3,4,4], 2) == 9


