# Onyx.Taxi
#
# Для вашей продуктовой команды пришло задание на создание веб-приложения. PO поставил цель до конца спринта  реализовать сервис заказа такси.
#
# Вам успели предоставить краткое текстовое описание требований к сервису. Описание приложено к этому документу.
#
# Также, для вашей команды подготовили примерную целевую документацию к сервису: описание api в формате openapi 3 и схема БД в нотации dbml.
#
#
#
#
# Краткое описание:
#
# Необходим централизованный сервис для хранения данных о заказах такси.
# Пользователи сервиса — мобильные приложения пассажира и водителя.
#
#
# Клиентов можно создавать, искать, удалять. Изменять данные клиента нельзя, лучше удалить и создать нового.
#
#
# Данные водителей тоже  только создавать, искать и удалять. Вместо изменения также удалить и создать нового.
#
#
# Заказы только создаются, ищутся и изменяются.
#
# Удалить заказ не должно быть позволено. В случае если заказ отменён — поставить в колонку статус о том что он отменён.
#
# Последовательности смены статусов заказа допускаются только такие:
#
# 1) not_accepted → in_progress → done
#
# 2) not_accepted → in_progress → cancelled
#
# 3) not_accepted → cancelled
#
#
# Менять дату создания , id водителя и  id клиента можно только в случае если статус заказа - not_accepted
#
#
# Требуется реализовать веб-приложение в соответствии с приложенной документацией.
#
# В случае недостатка требований допускается коллективное решение по изменениям и дополнениям.
#
#
# Требования:
# Используйте Flask
#
# Используйте ORM
#
# Напишите программу удовлетворяющую описанным документам
#
# Используйте подключение к бд postgres