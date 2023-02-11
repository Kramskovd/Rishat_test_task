# Rishat_test_task

Установить виртульное окружение
python3 -m pip install --user virtualenv

python3 -m venv env

source env/bin/activate

Перейти в директорию rishat_test_tak

Установить библиотеки
pip install -r requirements.txt

Далее необходимо создать файл .env в rishat_test_task/rishat_test_task
По шаблону .env.template установить значения переменных (приватный и публичный ключи API Stripe)

Чтобы запустить сервер нужно ввести команду
python3 manage.py runserver

В базе данных созданы и заполнены таблицы Item, Order, Tax, Discount

Приложение обрабатывает 4 путя
/buy/id
/item/id
/order/order_number
/buy_order/order_nubmer

где, соответсвенно, id и order_number первичные ключи записей товара и объединенных товаров 
