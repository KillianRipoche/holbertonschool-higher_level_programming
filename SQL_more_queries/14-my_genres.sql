-- List all genres of the show Dexter, displaying tv_genres.name
SELECT g.name
FROM tv_genres g
JOIN tv_show_genres tsg ON g.id = tsg.genre_id
JOIN tv_shows ts ON tsg.show_id = ts.id
WHERE ts.title = 'Dexter'
ORDER BY g.name ASC;
