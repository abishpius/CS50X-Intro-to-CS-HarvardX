select title
from movies join stars on movies.id = stars.movie_id
join ratings on movies.id = ratings.movie_id
join people on stars.person_id = people.id
where name == "Chadwick Boseman"
order by rating DESC
Limit 5;