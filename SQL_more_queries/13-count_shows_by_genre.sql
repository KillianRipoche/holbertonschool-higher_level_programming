-- 13. Number of shows by genre
-- Lists all genres from the hbtn_0d_tvshows database with the number of associated TV shows.
-- Only genres with at least one TV show are displayed.
-- The output displays two columns: genre and number_of_shows,
-- sorted in descending order by the number of shows.
SELECT
    genres.name AS genre,
    COUNT(tv_show_genres.tv_show_id) AS number_of_shows
FROM genres
INNER JOIN tv_show_genres ON genres.id = tv_show_genres.genre_id
GROUP BY genres.id
ORDER BY number_of_shows DESC;
