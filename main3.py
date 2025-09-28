from fastapi import FastAPI # import

app =FastAPI()  #instance
# we can easily start API using import, instance, decorate function

@app.get("/")  # decorate function
def index():
    return {"data":{"name": "samitha"}}
@app.get("/about")
def about():
    return {"data":"about page"}

