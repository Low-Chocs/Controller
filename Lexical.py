list_of_words = ['Hola', 'pana', 'Juan', 'Guillermo', ';']
variable = 'Hola pana Juan Guillermo Antonio\n;'
list_of_tokens = []
error_list = []

#Less efficient way but it is approved in the class
def controller(list: list, string: str, row: int, column: int):
    for element_in_list in list:
        for char_in_element in range(len(element_in_list)):

            if element_in_list[char_in_element] == string[char_in_element]:
                if char_in_element != len(string)-1:
                    continue
                else:
                    return 'Word: {}, in row: {} and in column: {}'.format(element_in_list, row, column)
            else:
                break
    return None

#Satisfying the problem solution
row = 1 
column = 1
new_word = ''
variable += ' '

for string in variable:

    if string == '\n':
        if len(new_word) != 0:
            if controller(list_of_words, new_word, row, column) != None:
                list_of_tokens.append(controller(list_of_words, new_word, row, column))
            else:
                error_list.append('Word: {}, was not recognized in row {} and in column {}'.format(new_word, row, column))
        new_word = ''
        row += 1
        column = 0
        continue

    if string == '\t':
        column += 4
        if len(new_word) != 0:
            if controller(list_of_words, new_word, row, column) != None:
                list_of_tokens.append(controller(list_of_words, new_word, row, column))
            else:
                error_list.append('Word: {}, was not recognized in row {} and in column {}'.format(new_word, row, column))
        new_word = ''
        continue

    if string == ' ':
        if controller(list_of_words, new_word, row, column) != None:
            list_of_tokens.append(controller(list_of_words, new_word, row, column))
        else:
            error_list.append('Word: {}, was not recognized in row {} and in column {}'.format(new_word, row, column))
        new_word = ''
        continue
    else:
        column += 1
        new_word += string

for i in list_of_tokens:
    print(i)

for i in error_list:
    print(i)


    