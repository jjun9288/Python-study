def get_count(input_str):
    words = 'aeiou'
    count = 0
    for char in input_str:
        if char in words:
            count+=1
    return count


# tester provided
def test_sample():
    assert get_count("abracadabra") == 5
    assert get_count("") == 0
    assert get_count("bcd,! ?") == 0
    assert get_count("pear tree") == 4
    assert get_count("o a kak ushakov lil vo kashu kakao") == 13
    
