
SELECT posts.id, title, users.username, users.email FROM posts INNER JOIN users ON posts.user_id = users.id;