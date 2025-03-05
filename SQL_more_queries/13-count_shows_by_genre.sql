-- 13. Number of shows by genre
-- Lists all genres from the hbtn_0d_tvshows database with the number of associated TV shows.
-- Only genres with at least one TV show are displayed.
-- The output displays two columns: genre and number_of_shows,
-- sorted in descending order by the number of shows.
SELECT g.name AS genre, COUNT(g.id) AS number_of_shows
FROM tv_genres g
JOIN tv_show_genres tsg ON g.id = tsg.genre_id
GROUP BY g.id
ORDER BY number_of_shows DESC;

