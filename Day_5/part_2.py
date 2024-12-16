def split_input(r : list, b : list) -> list[list] | list[int]:
    rules = True
    with open('Day_5/puzzle_input.txt', 'r') as input_file:
        for line in input_file:
            line = line.replace('\n', '')
            if line == '':
                rules = False
                continue

            if rules:
                r.append([int(n) for n in line.split('|')])
            else:
                b.append([int(n) for n in line.split(',')])
    
    return r, b

def check_rules(current_book : list, book_page : int, rules: list[list]) -> bool:
    
    book_page_index = current_book.index(book_page)
    
    for rule in rules:
        if book_page not in rule:
            continue

        page_index = rule.index(book_page)
        if page_index == 0:
            check_index = 1
            pos =  'X'  
        else: 
            check_index = 0
            pos = 'Y'

        if rule[check_index] not in current_book:
            continue
        
        compare_index = current_book.index(rule[check_index])
        
        if pos == 'Y' and compare_index > book_page_index:
            return False
        
        if pos == 'X' and compare_index < book_page_index:
            return False
        
    return True

def check_correct_pos(num, book, rules):
    for rule in rules:
        if num not in rule:
            continue

        num_index = rule.index(num)
        other_index = 1 if num_index == 0 else 0

        if rule[other_index] not in book:
            continue

        if  num_index == 1:
            return False
        
    return True

def reorder_updates(book : list[int], rules : list[list]):
    new_order = []
    book_copy = book.copy()
    while len(book) > 1:
        for num in book_copy:
            if check_correct_pos(num, book, rules) and num not in new_order:
                new_order.append(num)
                book.pop(book.index(num))

    if len(book) == 1:
        new_order.append(book[0])

    return new_order

rules = []
books = []

rules, books = split_input(rules, books)
mid_count = 0

for book in books:
    for num in book:
        valid_book = check_rules(book, num, rules)
        if valid_book is False:
            break
    
    if valid_book is False:
        book = reorder_updates(book, rules)
        mid_count += book[int((len(book)-1)/2)]
    
print(mid_count)