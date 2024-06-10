Query:

`[GET] http://127.0.0.1:8000/movies/list/?p=3&s=2`

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
Query:

`[GET] http://127.0.0.1:8000/movies/reviews/list/?username=mohammad`

Response:

```
[
    {
        "id": 5,
        "movie": 1,
        "review_user": "mohammad",
        "rating": 2,
        "description": "Review 1 - Updated 3",
        "created": "2024-06-02T07:40:05.327466Z",
        "update": "2024-06-02T07:40:05.327466Z"
    }
]
```
Query:

`[PUT] http://127.0.0.1:8000/movies/reviews/5/`

Response:

```
{
    "id": 5,
    "movie": 1,
    "review_user": "mohammad",
    "rating": 4,
    "description": "Review 1 - Updated 4",
    "created": "2024-06-02T07:40:05.327466Z",
    "update": "2024-06-10T08:28:34.792551Z"
}
```

