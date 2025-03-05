-- 13. Number of shows by genre
-- Lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
-- Only genres with at least one TV show are shown.
-- The result displays two columns: genre and number_of_shows,
-- sorted in descending order by the number of shows.

SELECT
    GENRES.NAME AS genre,
    COUNT(TV_SHOW_GENRES.TV_SHOW_ID) AS number_of_shows
FROM GENRES
JOIN TV_SHOW_GENRES ON GENRES.ID = TV_SHOW_GENRES.GENRE_ID
GROUP BY GENRES.NAME
ORDER BY number_of_shows DESC;
