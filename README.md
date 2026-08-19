# FastAPI Path Parameters Practice

This repository contains my hands-on practice with **FastAPI Path Parameters**, completed through three progressively harder coding challenges.

## Concepts Practiced

* Basic GET endpoints
* Single path parameters
* Multiple path parameters
* Using path parameters with lists and dictionaries
* Searching data using a path parameter
* Conditional logic based on retrieved data
* Dynamic responses using f-strings

## Challenges Completed

### Question 1 — Basic Path Parameter

Created a product endpoint using a single path parameter.

`/products/{product_id}`

Example:

`/products/101`

Returns:

`Product ID is 101`

### Question 2 — Multiple Path Parameters

Created a books and chapters endpoint using two path parameters.

`/books/{book_id}/chapters/{chapter_id}`

Example:

`/books/12/chapters/4`

Returns:

`Book 12, Chapter 4`

### Question 3 — Path Parameter + Data + Logic

Created a student endpoint that:

* Receives a student ID through the URL.
* Finds the matching student from a list.
* Retrieves the student's name and marks.
* Determines whether the student is Premium or Regular.
* Returns a dynamic response.

`/students/{id}`

Example:

`/students/2`

Returns:

`Student Priya has 18 marks and is a Premium student`

## Difficulty Progression

* Question 1 → Single Path Parameter
* Question 2 → Multiple Path Parameters
* Question 3 → Path Parameter + Data Lookup + Conditional Logic

## Tools

* Python
* FastAPI
* Swagger UI

## Learning Approach

These exercises were completed as hands-on coding challenges rather than simply copying solutions. Each challenge increased in difficulty to strengthen practical understanding of FastAPI Path Parameters.
