import atexit
import grpc
import json
import logging
import os
import psycopg2

from concurrent import futures
from typing import Dict
from typing import List
from typing import Tuple


import user_pb2
import user_pb2_grpc
import sql_pb2
import sql_pb2_grpc
import sql_read_pb2
import sql_read_pb2_grpc


name: str = 'SQLRead'
v: str = 'v2'

env_json_file: str = os.path.abspath('./env.json')

conn = None
log = None

env = {}
env_list: List[str] = [
    "PORT",
    "PG_PORT",
    "PG_HOST",
    "PG_USER",
    "PG_PASS",
    "PG_DB"
]


def get(key: str) -> str:
    global env
    return env[key]


def init_sql() -> None:
    db: str = get('PG_DB')
    usr: str = get('PG_USER')
    host: str = get('PG_HOST')
    port: str = get('PG_PORT')
    pss: str = get('PG_PASS')

    global conn
    conn = psycopg2.connect(database=db,
                            user=usr,
                            password=pss,
                            host=host,
                            port=port)

    log.info('Successfully connected to db')


def init_env() -> None:
    for e in env_list:
        if e in env:
            msg: str = 'Found env var "%s" in file with default value "%s"'
            log.info(msg, e, get(e))
        else:
            env[e] = os.environ[e]
            log.info('Found env var "%s" with value "%s"', e, env[e])


def init_atexit() -> None:
    def end():
        global conn
        if conn is not None:
            log.info('Closing DB connection')
            conn.close()
        log.info('bye')

    atexit.register(end)


def init_log() -> None:
    global log
    global name
    global v

    logging.basicConfig(
        format=f'[{v}] [{name}] %(asctime)s %(levelname)-8s %(message)s',
        level=logging.DEBUG,
        datefmt='%Y-%m-%d %H:%M:%S')

    log = logging.getLogger(name)
    log.info('hi')


def init_server() -> None:
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    sql_read_pb2_grpc.add_SQLReadServicer_to_server(Server(), server)
    port = get('PORT')
    server.add_insecure_port(f'localhost:{port}')

    server.start()
    log.info('Started server at %s', port)
    server.wait_for_termination()

    log.info('Ending server')


def init_json() -> None:
    global env

    try:
        json_file = open(env_json_file, 'r')
        env = json.load(json_file)
    except FileNotFoundError as fe:
        log.warning('Did not find env json file - using env vars')


class Server(sql_read_pb2_grpc.SQLReadServicer):
    usr: str = 'SELECT username from duolingo.data.queue'
    rm: str = 'DELETE FROM duolingo.data.queue WHERE username = %s'
    refill: str = 'INSERT INTO duolingo.data.queue (SELECT username from duolingo.data.users)'
    count: str = 'SELECT COUNT(*) FROM duolingo.data.queue'

    @staticmethod
    def count() -> int:
        log.info('Counting queue table')
        curr = conn.cursor()
        curr.execute(Server.count)
        count: int = curr.fetchone()[0]
        
        log.info('Queue table has %d entries', count)
        return count

    @staticmethod
    def refill_users() -> None:
        log.info('Refilling user queue table')
        curr = conn.cursor()
        curr.execute(Server.refill)
        conn.commit()
        curr.close()
        log.info('Finished refilling user queue table')
        

    @staticmethod
    def drop_user(user: str) -> None:
        curr = conn.cursor()
        curr.execute(Server.rm, [user])
        conn.commit()
        curr.close()
        log.info('Dropped user %s', user)

        if Server.count() == 0:
            Server.refill_users()

    @staticmethod
    def get_user() -> str:
        curr = conn.cursor()
        curr.execute(Server.usr)
        user = curr.fetchone()[0]
        curr.close()

        log.info('Got random user %s', user)
        Server.drop_user(user)

        return user

    def GetUser(self, request, context):
        log.info('Received request for username')
        name = Server.get_user()

        log.info('Sending user %s', name)
        return sql_read_pb2.User(name=name)


def init() -> None:
    init_log()
    init_json()
    init_env()
    init_sql()
    init_atexit()
    init_server()


def main() -> None:
    init()


if __name__ == '__main__':
    main()
