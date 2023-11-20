# SpeedPortal
SpeedPortal - веб-платформа для размещения и просмотра спидранов пользователей в разных играх и категориях. Авторизованный пользователь может оставить заявку на размещение его рана в общей таблице, модератор должен будет его проверить на валидность и принять решение - публиковать его или нет
# ТЗ по БД
## Описание
### Общее описание
SpeedPortal - веб-платформа для размещения и просмотра спидранов пользователей в разных играх и категориях. Авторизованный пользователь может оставить заявку на размещение его рана в общей таблице, модератор должен будет его проверить на валидность и принять решение - публиковать его или нет
### Предметная область
Предметная область включает следующие сущности:
* Пользователь
* Игра
* Категория спидрана
* Ран (забег)
* Комментарий к рану
## Данные
### Пользователь
Должны храниться следующие данные о пользователе
* Уникальный идентификатор
* Имя пользователя (уникальное)
* Адрес электронной почты (уникальный)
* Пароль
* Изображение профиля (аватар)
* Количество набранных очков
* Биография ("о себе")
* Является ли пользователь модератором, если да, то какие имеет полномочия, например, повышать до модераторов других пользователей, одобраять или отклонять раны, банить пользователей
Модераторы имеют полномочия только в рамках своей "компетенции", то есть перечня игр, в которых они могут объективно оценивать валидность рана
* Забанен ли пользователь, если да, то причина бана
### Игра
Должны храниться следующие данные об игре
* Название (уникальное)
* Ссылка на игру в Steam (уникальная)
* Иконка
* Банер
* Описание
* Доступные категории спидранов
Для категорий в свою очередь требуется хранить их уникальное название и описание
### Раны
Должна храниться следующая информация о ране
* Игра
* Категория
* Время пробега (положительное целое число миллисекунд)
* Ссылка на видео с раном
* Статус рана - на рассмотрении, принят, отклонен, идентификатор модератора, проверявшего ран, если отклонен, то причина отказа
### Для каждого элемента данных - ограничения
### Общие ограничения целостности
## Пользовательские роли
### Рядовой пользователей
Рядовой пользователей имеет следующие возможности:
* Просмотреть таблицу ранов различных игр в различных категориях
* Подать заявку на внесение рана в общую таблицу
* Прокомментировать ран
* Пожаловаться на ран или комментарий
### Модератор
Каждый модератор имеет свою "компетенцию" - перечень игр, в отношении которых он может реализовывать свои полномочия. Подобные ограничения следуют из того, что для объективной оценки валидности спидрана по какой-либо игре, требуется глубокое знание механик и хитростей этой игры
Модератор обладает следующими возможностями в рамках своей компетенции:
* Просмотр заявок на внесение ранов в таблицу
* Одобрение/отклонение этих заявок (модератор не может одобрить свой же ран)
* Добавление категорий (при наличии полномочия)
* Повышение других пользователей до модераторов такой же или меньшей компетенции (при наличии полномочия)
* Бан пользователей при наличии жалоб (при наличии полномочия)
### Администратор
Администратор имеет все возможности модератора во всех компетенциях
## Технологии разработки
### Языки программирования
* Python Django
* JS
### СУБД
PostgreSQL
## Структура БД
https://lucid.app/lucidchart/3beae458-0ca5-4f42-a3f4-27d3898f9cbf/edit?invitationId=inv_a228f947-7b3c-4cc9-b814-717159d768d9
