subscribers = []


def subscribe(callback):

    subscribers.append(
        callback
    )


def publish(event):

    for callback in subscribers:

        callback(event)
