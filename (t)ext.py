func_choice = input('Welcome to (t)ext! Choose the operation you wanna do: (1)Write in a New File > ')
if func_choice == '1':
    extension = input('What exentsion should your file have? > ')
    file_name = input('What name should your file have? > ')
    file = open(f'{file_name}.{extension}', 'w')
    content_of_file = input('> ')
    print(content_of_file, file=file)