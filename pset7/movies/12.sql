select title
from movies join stars on movies.id = stars.movie_id
join people on stars.person_id = people.id
where name in ("Johnny Depp","Helena Bonham Carter")
group by title
having count(title)>1;