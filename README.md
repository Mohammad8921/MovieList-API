Query:

`http://127.0.0.1:8000/movies/list/?p=3&s=2`

Response:

```
{
    "count": 7,
    "next": "http://127.0.0.1:8000/movies/list/?p=4&s=2",
    "previous": "http://127.0.0.1:8000/movies/list/?p=2&s=2",
    "results": [
        {
            "id": 5,
            "reviews": [],
            "title": "Toy Story 2",
            "storyline": "Toy Story 2",
            "active": true,
            "created": "2024-06-04T08:13:00.349341Z",
            "ave_rating": 0.0,
            "rating_number": 0,
            "platform": 1
        },
        {
            "id": 6,
            "reviews": [],
            "title": "Toy Story 3",
            "storyline": "Toy Story 3",
            "active": true,
            "created": "2024-06-04T08:14:03.729667Z",
            "ave_rating": 0.0,
            "rating_number": 0,
            "platform": 1
        }
    ]
}
```
