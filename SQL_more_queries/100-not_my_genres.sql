-- list all genres 
-- USING ONLY ONE JOIN :p 
SELECT tv_genres.name
FROM tv_genres WHERE tv_genres.names NOT IN(
SELECT tv_genres.name
FROM tv_genres
LEFT OUTER JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
LEFT OUTER JOIN tv_shows
ON tv_show_genres.show_id = tv_show.id WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name)
ORDER BY tv_genres.name;
