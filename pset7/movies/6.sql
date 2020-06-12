Select AVG(rating)
From ratings
where movie_id in (
Select id from movies where year == 2012);