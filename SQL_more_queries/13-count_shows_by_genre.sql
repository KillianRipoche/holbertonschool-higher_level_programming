-- 13. Number of shows by genre
-- Lists all genres with the number of shows linked to each from the hbtn_0d_tvshows database.
-- Only genres with at least one associated TV show are displayed.
-- The output displays two columns: genre and number_of_shows, sorted in descending order by number_of_shows.

SELECT
    G.NAME AS genre,
    TS.NUMBER_OF_SHOWS AS number_of_shows
FROM
    GENRES AS G
    INNER JOIN (
        SELECT
            GENRE_ID,
            COUNT(TV_SHOW_ID) AS NUMBER_OF_SHOWS
        FROM
            TV_SHOW_GENRES
        GROUP BY
            GENRE_ID
    ) AS TS ON G.ID = TS.GENRE_ID
ORDER BY
    TS.NUMBER_OF_SHOWS DESC;
