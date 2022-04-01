from models import engine, Base, Driver, Client, Order
from flask import Flask, request, Response
from sqlalchemy.orm import sessionmaker, scoped_session
from contextlib import contextmanager
from typing import Generator


app = Flask(__name__)
Base.metadata.create_all(engine)
Session = scoped_session(sessionmaker(autoflush=True, autocommit=False, bind=engine))


@contextmanager
def session_scope() -> Generator:
    """Создание сессий для осуществления запросов к БД.."""
    session = Session()
    try:
        yield session
        session.commit()
    except:
        print("Роллбэк")
        session.rollback()
        raise
    finally:
        session.close()


@app.route('/api/v1/drivers', methods=['POST'])
# @dec_valid(schema)   #try exapt decor в нем валидация, если ошибеа, реторн ошибки, если норм - ретурн функции
def post_driver() -> Response:
    with session_scope() as session:
        data = request.get_json()
        new_inp = Driver(name=data["name"], car=data["car"])
        session.add(new_inp)
        return Response("created!", status=201)


@app.route('/api/v1/drivers', methods=['GET'])
def get_driver() -> Response:
    with session_scope() as session:
        driver_id = request.args.get("driverId")
        o = session.query(Order).get(driver_id)
        return Response(str(o), status=200)


@app.route('/api/v1/drivers', methods=['DELETE'])
def delete_driver() -> Response:
    with session_scope() as session:
        driver_id = request.args.get("driverId")
        session.query(Driver).filter(Driver.id == int(driver_id)).delete()
        return Response("delete", status=204)


"----------------------------------"


@app.route('/api/v1/clients', methods=['POST'])
def post_clients() -> Response:
    with session_scope() as session:
        data = request.get_json()
        new_client = Client(name=data["name"], is_vip=data["is_vip"])
        session.add(new_client)
        return Response("created!", status=201)


@app.route('/api/v1/clients', methods=['GET'])
def get_clients() -> Response:
    with session_scope() as session:
        client_Id = request.args.get("clientId")
        o = session.query(Order).get(client_Id)
        return Response(str(o), status=200)


@app.route('/api/v1/clients', methods=['DELETE'])
def delete_clients() -> Response:
    with session_scope() as session:
        data = request.args.get("clientId")
        session.query(Client).filter(Client.id == int(data)).delete()
        return Response("delete", status=204)


"----------------------------------"


@app.route('/api/v1/orders', methods=['POST'])
def post_orders() -> Response:
    data = request.get_json()
    print(data)
    print(type(data["date_created"]))
    with session_scope() as session:
        new_order = Order(
            client_id=data["client_id"],
            driver_id=data["driver_id"],
            date_created=data["date_created"],
            status=data["status"],
            address_from=data["address_from"],
            address_to=data["address_to"]
        )
        session.add(new_order)
        return Response('created!', status=201)


@app.route('/api/v1/orders', methods=['GET'])
def get_orders() -> Response:
    with session_scope() as session:
        data = request.args.get("orderId")
        print(data, type(data))
        order_info = session.query(Order).filter(Order.id == int(data)).all()
        return Response(str(order_info), status=200)


@app.route('/api/v1/orders', methods=['PUT'])
def change_orders() -> Response:
    order_id = request.args.get("orderId")
    statuses = {"not_accepted": ("in_progress", "cancelled"),
                "in_progress": ("cancelled", "done")
                }
    with session_scope() as session:
        try:
            o = session.query(Order).get(order_id)                          # Как надо
            # session.query(Order).filter(Order.id == int(data)).all()      # Как было
        except:
            return Response("Объект в базе не найден", status=404)
        data_json = request.get_json()
        if data_json["status"] in statuses[o.status]:
            o.status = data_json["status"]                                                                  # Как надо
            o.date_created = data_json["date_created"]
            # session.query(Order).filter(Order.id == int(order_id)).update({"status": data_json["status"]})  # Как было
            return Response("Заказ изменен", status=200)
        else:
            return Response("Неправильный запрос", status=400)


app.run(host='127.0.0.1', port=5000) # запуск приложения локально на 5000 порту
