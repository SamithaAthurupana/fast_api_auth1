from fastapi import FastAPI # import

myapp =FastAPI()  #instance
# we can easily start API using import, instance, decorate function

@myapp.get("/")  # decorate function
def index():
    return {"data": "blog list"}


@myapp.get("/blog/{id}")
def show(id : int):
    #fletch blog with id = id
    return {"data": id}

@myapp.get("/blog/{id}/comments")
def comments(id):
    #fletch comments of blogs with id = id
    return {"data":{"1", "2"}}
