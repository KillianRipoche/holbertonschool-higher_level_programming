-- Write a script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT g.name AS genre,
(SELECT COUNT(*) FROM tv_show_genres WHERE genre_id = g.id) AS number_of_shows
FROM genres AS g
WHERE (SELECT COUNT(*) FROM tv_show_genres WHERE genre_id = g.id) > 0
ORDER BY number_of_shows DESC;
