-- List all shows with their title and genre_id (NULL if no genre is linked)
SELECT tv_shows.title, COALESCE(tv_show_genres.genre_id, NULL) AS genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
ORDER BY tv_shows.title ASC, genre_id ASC;
