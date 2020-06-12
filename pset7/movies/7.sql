Select title, rating
from ratings
Join movies on ratings.movie_id = movies.id
where year == 2010
order by rating DESC, title;