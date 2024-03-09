import queue

queue = queue.Queue()


class Request:
    static_id_counter = 0

    def __init__(self, id):
        Request.static_id_counter += 1
        self.id = Request.static_id_counter


def generate_request():
    queue.put(Request(id))


def process_request():
    if queue.empty():
        print('No requests to process')
        return
    while not queue.empty():
        item = queue.get()
        print('Processing request with id', item.id)


while True:
    print('Press:\n\t"g" to generate new request\n\t"p" to process requests\n\t"q" to exit')
    user_input = input()
    if user_input == 'q':
        break
    elif user_input == 'p':
        process_request()
    elif user_input == 'g':
        generate_request()
    else:
        print('Invalid input')
