from queue import Queue

event_queue = Queue()


def enqueue(event):

    event_queue.put(event)


def dequeue():

    if not event_queue.empty():

        return event_queue.get()

    return None
