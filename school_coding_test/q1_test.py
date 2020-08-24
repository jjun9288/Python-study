def square_digits(num):
    words = list(str(num)) 
    for word in words: 
        print(int(word)**2, end="") 


def test_q1():
    assert square_digits(9119) == 811181

    