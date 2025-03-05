-- Write a script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.

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
