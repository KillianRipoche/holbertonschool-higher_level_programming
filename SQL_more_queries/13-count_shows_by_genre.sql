-- 13. Number of shows by genre
-- Lists all genres from hbtn_0d_tvshows with the number of TV shows linked to each.
-- Only genres with at least one associated TV show are displayed.
-- The output displays two columns: genre and number_of_shows.
-- Results are sorted in descending order by number_of_shows,
-- and in case of tie, by the genre ID in ascending order.

SELECT
    g.name AS genre,
    COUNT(tg.tv_show_id) AS number_of_shows
FROM genres AS g
INNER JOIN tv_show_genres AS tg ON g.id = tg.genre_id
GROUP BY g.id
HAVING COUNT(tg.tv_show_id) > 0
ORDER BY number_of_shows DESC, g.id ASC;
