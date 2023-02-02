-- sql
SELECT tv_shows.title , tv_show_genres.genre_id FROM tv_shows INNER JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id
order by tv_shows.title,tv_shows_genre_id;
