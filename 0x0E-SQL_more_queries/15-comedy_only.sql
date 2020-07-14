-- man
SELECT tv_shows FROM tv_genres, tv_shows_genres, tv_shows WHERE tv_genres.id = tv_shows_genres.genre_id AND tv_shows_genres.show_id = tv_shows.id and tv_genres.name = "Comedy" ORDER BY tv_shows.title ASC;
