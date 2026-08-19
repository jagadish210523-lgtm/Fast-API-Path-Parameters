from fastapi import FastAPI
jaga = FastAPI()
@jaga.get("/book/{book_id}/chapters/{chapter_id}")
async def book(book_id,chapter_id):
    return f"Book {book_id}, Chapter {chapter_id}"