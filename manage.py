#! ./luxenv/bin/python
import sys
import uvicorn


def execute(options):
    host = "0.0.0.0"
    port = 8000
    uvicorn.run("app.app:app", host=host, port=port, reload=False, )


action_map = {
    "serve": execute,
}

if __name__ == "__main__":
    args = sys.argv[1:]
    action = args[0]
    options = args[1:]
    try:
        action_map[action](options)
    except Exception as exc:
        print(exc)
        raise exc
