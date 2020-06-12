select name
from people join directors on people.id = directors.person_id
join movies on directors.movie_id = movies.id join ratings on movies.id = ratings.movie_id
where rating >= 9.0;