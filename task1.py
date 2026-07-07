book_profile = {
"title": "Основи програмування",
"author": "Іван Петренко",
"year": 2023,
"publisher_info": {
"name": "Наукова думка",
"city": "Київ"
}
}

print(f'Назва книги: "{book_profile["title"]}", автор: {book_profile["author"]}')
print(f'Назва видавництва: "{book_profile["publisher_info"]["name"]}"')
print(f'Книга "{book_profile["title"]}" автора {book_profile["author"]} була видана у місті {book_profile["publisher_info"]["city"]}.')
print(f"Рік видання {book_profile.get('year', "невідомий")}")