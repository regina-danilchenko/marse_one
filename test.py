from requests import get, post, delete, put
import datetime

# получение всех колонистов
# print(get('http://localhost:5000/api/v2/users').json())

# получение 1 колониста по id
# print(get('http://localhost:5000/api/v2/users/3').json())

# получение 1 колониста по id котрого нет
# print(get('http://localhost:5000/api/v2/users/55').json())

# добавлнеие колониста
# print(post('http://localhost:5000/api/v2/users',
#            json={
#                'surname': 'колонист',
#                'name': 'колонист',
#                'age': 27,
#                'position': 'повар',
#                'speciality': 'кулинария',
#                'address': 'марс',
#                'email': 'м@bk.com',
#                'modified_date': datetime.date(2025, 3, 25).isoformat()
#            }).json())

# добавлнеие колониста где указаны не все поля
# print(post('http://localhost:5000/api/v2/users',
#            json={
#                'surname': 'колонист',
#                'name': 'колонист',
#                'age': 27,
#                'position': 'повар',
#                'speciality': 'кулинария',
#            }).json())

# добавление колониста с пустым json
# print(post('http://localhost:5000/api/v2/users', json={}).json())

# удаление колониста по id
# print(delete('http://localhost:5000/api/v2/users/1').json())

# удаление колониста где не указан id
# print(delete('http://localhost:5000/api/v2/users').json())

# удаление колониста по id которого нет
# print(delete('http://localhost:5000/api/v2/users/45').json())

# все работы
# print(get('http://localhost:5000/api/v2/jobs').json())

# работа по id
# print(get('http://localhost:5000/api/v2/jobs/3').json())

# работа по id (id нет в базе данных)
# print(get('http://localhost:5000/api/v2/jobs/999').json())

# в теле запроса json, с нужными полями
# print(post('http://localhost:5000/api/v2/jobs',
#            json={'team_leader': 1,
#                  'job': 'Распределить всех по каютам',
#                  'work_size': 2,
#                  'collaborators': '1',
#                  'start_date': datetime.date(2025, 3, 25).isoformat(),
#                  'end_date': datetime.date(2025, 3, 30).isoformat(),
#                  'is_finished': True}).json())

# в теле запроса пустой json
# print(post('http://localhost:5000/api/v2/jobs', json={}).json())

# в теле запроса json, в котором есть не все поля
# print(post('http://localhost:5000/api/v2/jobs',
#            json={'team_leader': 1}).json())

# в теле запроса json есть все поля, но значения не нужного типа
# print(post('http://localhost:5000/api/v2/jobs',
#            json={'team_leader': 'p',
#                  'job': 'Распределить всех по каютам',
#                  'work_size': 2,
#                  'collaborators': '1',
#                  'start_date': datetime.date(2025, 3, 25).isoformat(),
#                  'end_date': datetime.date(2025, 3, 30).isoformat(),
#                  'is_finished': 1}).json())

# проверка, что post-запрос добавил новую работу
# print(get('http://localhost:5000/api/v2/jobs').json())

# удаление работы по id
# print(delete('http://localhost:5000/api/v2/jobs/5').json())

# удаление работы по id (id нет в базе данных)
# print(delete('http://localhost:5000/api/v2/jobs/999').json())

# удаление работы по id (id не число)
# print(delete('http://localhost:5000/api/v2/jobs/not_int'))

# проверка, что delete-запрос удалил работу
# print(get('http://localhost:5000/api/v2/jobs').json())

# изменение работы
# print(put('http://localhost:5000/api/v2/jobs/3',
#            json={'team_leader': 1,
#                  'job': 'Распределить по каютам',
#                  'work_size': 78,
#                  'collaborators': '1',
#                  'start_date': datetime.date(2025, 3, 25).isoformat(),
#                  'end_date': datetime.date(2025, 3, 30).isoformat(),
#                  'is_finished': True}))

# изменение работы по id (id нет в базе данных)
# print(put('http://localhost:5000/api/v2/jobs/888', json={'team_leader': 1,
#                  'job': 'Распределить всех по каютам',
#                  'work_size': 78,
#                  'collaborators': '1',
#                  'start_date': datetime.date(2025, 3, 25).isoformat(),
#                  'end_date': datetime.date(2025, 3, 30).isoformat(),
#                  'is_finished': True}))

# изменение работы в теле запроса пустой json
# print(put('http://localhost:5000/api/v2/jobs/3', json={}))

# изменение работы в теле запроса json, в котором есть не все поля
# print(put('http://localhost:5000/api/v2/jobs/5',
#            json={'team_leader': 1}))

# изменение работы в теле запроса json есть все поля, но значения не нужного типа
# print(put('http://localhost:5000/api/v2/jobs/5',
#            json={'team_leader': 'p',
#                  'job': 'Распределить всех по каютам',
#                  'work_size': 2,
#                  'collaborators': '1',
#                  'start_date': datetime.date(2025, 3, 25).isoformat(),
#                  'end_date': datetime.date(2025, 3, 30).isoformat(),
#                  'is_finished': 1}))


# получение всех колонистов
# print(get('http://localhost:5000/api/v2/users').json())

# получение 1 колониста по id
# print(get('http://localhost:5000/api/v2/users/3').json())

# получение 1 колониста по id котрого нет
# print(get('http://localhost:5000/api/v2/users/55').json())

# добавлнеие колониста
# print(post('http://localhost:5000/api/v2/users',
#            json={
#                'surname': 'колонист',
#                'name': 'колонист',
#                'age': 27,
#                'position': 'повар',
#                'speciality': 'кулинария',
#                'address': 'марс',
#                'email': 'м@bk.com',
#                'modified_date': datetime.date(2025, 3, 25).isoformat()
#            }).json())

# добавлнеие колониста где указаны не все поля
# print(post('http://localhost:5000/api/v2/users',
#            json={
#                'surname': 'колонист',
#                'name': 'колонист',
#                'age': 27,
#                'position': 'повар',
#                'speciality': 'кулинария',
#            }).json())

# добавление колониста с пустым json
# print(post('http://localhost:5000/ap/i/v2/users', json={}).json())

# удаление колониста по id
# print(delete('http://localhost:5000/api/v2/users/1').json())

# удаление колониста где не указан id
# print(delete('http://localhost:5000/api/v2/users').json())

# удаление колониста по id которого нет
# print(delete('http://localhost:5000/api/v2/users/45').json())
