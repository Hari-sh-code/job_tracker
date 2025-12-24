from fastapi import FastAPI

app = FastAPI()

Books = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'maths'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'commerce'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'history'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'science'},
]

@app.get("/")
async def first_api():
    return Books