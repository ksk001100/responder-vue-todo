import responder

def create_api() -> responder.API:
    api = responder.API(cors=True, allowed_hosts=['*'])
    return api

api = create_api()
