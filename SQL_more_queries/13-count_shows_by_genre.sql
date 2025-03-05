-- 13. Number of shows by genre
-- Affiche chaque genre avec le nombre de shows associés (excluant ceux sans show),
-- trié par ordre décroissant du nombre de shows.
SELECT
    g.name AS genre,
    (SELECT COUNT(*) FROM tv_show_genres WHERE genre_id = g.id) AS number_of_shows
FROM genres AS g
WHERE (SELECT COUNT(*) FROM tv_show_genres WHERE genre_id = g.id) > 0
ORDER BY number_of_shows DESC;
