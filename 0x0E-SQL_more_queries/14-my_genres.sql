-- script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter

SELECT
    genres.name AS name
FROM
    genres
JOIN
    tv_show_genres
ON
    genres.id = tv_show_genres.genre_id
WHERE
    tv_show_genres.show_id = (
        SELECT
            id
        FROM
            tv_shows
        WHERE
            title = 'Dexter'
    )
ORDER BY
    genres.name ASC;
