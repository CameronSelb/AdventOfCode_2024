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

rules = []
books = []

rules, books = split_input(rules, books)
mid_count = 0

for book in books:
    for num in book:
        valid_book = check_rules(book, num, rules)
        if valid_book is False:
            break
    
    if valid_book:
        mid_count += book[int((len(book)-1)/2)]
    
print(mid_count)