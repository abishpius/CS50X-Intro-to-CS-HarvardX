select distinct(name)
from people join stars on people.id = stars.person_id
join movies on stars.movie_id = movies.id
where movie_id IN (
select movie_id
from stars join people on stars.person_id = people.id
where name =="Kevin Bacon" and birth == 1958
)
Except
    select name
    from people
    where name == "Kevin Bacon"
;

