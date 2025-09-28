from fastapi import FastAPI # import

myapp =FastAPI()  #instance
# we can easily start API using import, instance, decorate function

@myapp.get("/blog")  # decorate function
def index(limit = 10, published:bool = True):

    if published:
        return {"data": f"{limit} published blogs from the db"}
    else:
        return {"data": f"{limit} blogs from the db"}

@myapp.get("/blog/unpublished")
def unpublished():
    return {"data": "all unpublished blogs"}

@myapp.get("/blog/{id}")
def show(id : int):
    #fletch blog with id = id
    return {"data": id}

@myapp.get("/blog/{id}/comments")
def comments(id):
    #fletch comments of blogs with id = id
    return {"data":{"1", "2"}}

