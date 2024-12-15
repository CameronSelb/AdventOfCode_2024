def check_mul(mul_str : str):
    if mul_str.count('mul') > 1:
        mul_str = mul_str[3:]
        mul_str = mul_str[mul_str.index('mul'):]
    mul_str = mul_str.replace('mul', '')
    if mul_str[0] == '(' and mul_str[len(mul_str)-1] == ')':
        mul_str = mul_str.replace('(','').replace(')','').split(',')
    else:
        return False

    for num in mul_str:
        if not (num.isdigit()):
            return False
        
    mul_str = [int(num) for num in mul_str]

    return mul_str[0] * mul_str[1]


def get_mul(text : str):
    valid = []

    while True:
        #print('\n\n\n',text)
        if 'mul' not in text or ')' not in text:
            break

        start_index = text.index('mul')
        end_index = text.find(')')
        
        if end_index < start_index:
            text = text[end_index + 1 :]
            continue

        word = text[start_index : end_index + 1]
        num = check_mul(word)

        if num is False:
            text = text[end_index + 1 :]
            continue
        
        valid.append(num)
        text = text[end_index + 1 :]
        
    return valid



def main():
    total = 0

    with open('Day_3/puzzle_input.txt', 'r') as data_file:
        data = data_file.read()

    results = get_mul(data) 
    for num in results:
        total += num

    print(total)

if __name__ == '__main__':
    main()