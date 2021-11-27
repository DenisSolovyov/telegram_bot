from transitions import Machine

states = ['choice_of_pizza_size', 'choice_of_payment', 'order_checking', 'order_is_ready']
transitions = [
    {'trigger': 'to_payment', 'source': 'choice_of_pizza_size', 'dest': 'choice_of_payment'},
    {'trigger': 'to_check_order', 'source': 'choice_of_payment', 'dest': 'order_checking'},
    {'trigger': 'to_completion', 'source': 'order_checking', 'dest': 'order_is_ready'},
    {'trigger': 'go_to_start', 'source': 'order_is_ready', 'dest': 'choice_of_pizza_size'},
]

messages = {'choice_of_pizza_size': 'Какую вы хотите пиццу? Большую или маленькую?',
            'choice_of_payment': 'Как вы будете платить?',
            'order_checking': 'Вы хотите {} пиццу, оплата - {}?',
            'order_is_ready': 'Спасибо за заказ',
            }


class Questions(object):
    pass


test = Questions()
machine = Machine(test, states=states, initial='choice_of_pizza_size', transitions=transitions)
triggers = ['to_payment', 'to_check_order', 'to_completion', 'go_to_start']
trigger_counter = 0
