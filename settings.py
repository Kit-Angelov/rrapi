# конфиги к очередям (обьедини их с переприсваиванием если хочешь)

# конфиг к очереди заказа
order_queue_config = {
    'dev': {
        'user': 'admin',
        'password': 'itt0root',
        'host': 'localhost',
        'port': 5672,
        'queue': 'rrd_order',
        'exchange': '',
        'routing_key': 'rrd_order',
        'virtual_host': '/'
    },
    'kt': {
        'user': 'prqaihqx',
        'password': '3aMGiZ2tpYcm4ZGUzcvWEx_SfP4UCg80',
        'host': 'black-boar.rmq.cloudamqp.com',
        'port': 5672,
        'queue': 'rrd_order',
        'exchange': '',
        'routing_key': 'rrd_order',
        'virtual_host': 'prqaihqx'
    },
    'prod': {
        'user': 'prqaihqx',
        'password': '3aMGiZ2tpYcm4ZGUzcvWEx_SfP4UCg80',
        'host': 'black-boar.rmq.cloudamqp.com',
        'port': 5672,
        'queue': 'rrd_order',
        'exchange': '',
        'routing_key': 'rrd_order',
        'virtual_host': 'prqaihqx'
    }

}
order_queue_param = order_queue_config

# конфиг к очереди проверки статуса
check_queue_config = {
    'dev': {
        'user': 'admin',
        'password': 'itt0root',
        'host': 'localhost',
        'port': 5672,
        'queue': 'check_order',
        'exchange': '',
        'routing_key': 'check_order',
        'virtual_host': '/'
    },
    'kt': {
        'user': 'prqaihqx',
        'password': '3aMGiZ2tpYcm4ZGUzcvWEx_SfP4UCg80',
        'host': 'black-boar.rmq.cloudamqp.com',
        'port': 5672,
        'queue': 'check_order',
        'exchange': '',
        'routing_key': 'check_order',
        'virtual_host': 'prqaihqx'
    },
    'prod': {
        'user': 'prqaihqx',
        'password': '3aMGiZ2tpYcm4ZGUzcvWEx_SfP4UCg80',
        'host': 'black-boar.rmq.cloudamqp.com',
        'port': 5672,
        'queue': 'check_order',
        'exchange': '',
        'routing_key': 'check_order',
        'virtual_host': 'prqaihqx'
    }
}
check_queue_param = check_queue_config

# конфиг к очереди скачивания документа
download_queue_config = {
    'dev': {
        'user': 'admin',
        'password': 'itt0root',
        'host': 'localhost',
        'port': 5672,
        'queue': 'download_order',
        'exchange': '',
        'routing_key': 'download_order',
        'virtual_host': '/'
    },
    'kt': {
        'user': 'prqaihqx',
        'password': '3aMGiZ2tpYcm4ZGUzcvWEx_SfP4UCg80',
        'host': 'black-boar.rmq.cloudamqp.com',
        'port': 5672,
        'queue': 'download_order',
        'exchange': '',
        'routing_key': 'download_order',
        'virtual_host': 'prqaihqx'
    },
    'prod': {
        'user': 'prqaihqx',
        'password': '3aMGiZ2tpYcm4ZGUzcvWEx_SfP4UCg80',
        'host': 'black-boar.rmq.cloudamqp.com',
        'port': 5672,
        'queue': 'download_order',
        'exchange': '',
        'routing_key': 'download_order',
        'virtual_host': 'prqaihqx'
    }
}
download_queue_param = download_queue_config

# словарь режимов работы воркера и соответсвущих конфигов очереди
mode_dict = {
	'order': order_queue_param,
	'status': check_queue_param,
	'download': download_queue_param
}

other_param = {
    'dev': {
        'SENTRY_DSN': None
    },
    'kt': {
        'SENTRY_DSN': None
    },
    'prod': {
        'SENTRY_DSN': None
    }
}