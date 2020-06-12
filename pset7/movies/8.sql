Select name
from people
Join stars on people.id = stars.person_id join movies on stars.movie_id = movies.id
where title == 'Toy Story';