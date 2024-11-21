-- Lists all Comedy shows from the database hbtn_0d_tvshows.

SELECT 
    tv_shows.title
FROM 
    tv_shows, tv_show_genres, genres
WHERE 
    tv_shows.id = tv_show_genres.show_id
    AND tv_show_genres.genre_id = genres.id
    AND genres.name = 'Comedy'
ORDER BY 
    tv_shows.title ASC;
