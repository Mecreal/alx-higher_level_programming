# 📚 SQL More Queries Tasks

This README documents a collection of SQL scripts for advanced database operations. These scripts belong to the `alx-higher_level_programming` GitHub repository, under the `0x0E-SQL_more_queries` directory.

## 📌 Table of Contents
1. [🔑 My Privileges!](#my-privileges)
2. [👤 Root User](#root-user)
3. [👀 Read User](#read-user)
4. [📛 Always a Name](#always-a-name)
5. [🔒 ID Can't Be Null](#id-cant-be-null)
6. [🆔 Unique ID](#unique-id)
7. [🗺️ States Table](#states-table)
8. [🏙️ Cities Table](#cities-table)
9. [🌅 Cities of California](#cities-of-california)
10. [🌆 Cities by States](#cities-by-states)
11. [📺 Genre ID by Show](#genre-id-by-show)
12. [🎭 Genre ID for All Shows](#genre-id-for-all-shows)
13. [🚫 No Genre](#no-genre)
14. [📊 Number of Shows by Genre](#number-of-shows-by-genre)
15. [🎥 My Genres](#my-genres)
16. [🤣 Only Comedy](#only-comedy)
17. [🎬 List Shows and Genres](#list-shows-and-genres)
18. [🚷 Not My Genre](#not-my-genre)
19. [🚫 No Comedy Tonight!](#no-comedy-tonight)
20. [🍅 Rotten Tomatoes](#rotten-tomatoes)
21. [🏆 Best Genre](#best-genre)

### 🔑 My Privileges!
- **Script:** `0-privileges.sql`
- **Description:** Lists all privileges of MySQL users `user_0d_1` and `user_0d_2`.

### 👤 Root User
- **Script:** `1-create_user.sql`
- **Description:** Creates the MySQL server user `user_0d_1` with full privileges.

### 👀 Read User
- **Script:** `2-create_read_user.sql`
- **Description:** Creates the database `hbtn_0d_2` and the user `user_0d_2` with only SELECT privileges.

### 📛 Always a Name
- **Script:** `3-force_name.sql`
- **Description:** Creates the table `force_name` with `id INT` and `name VARCHAR(256)` not null.

### 🔒 ID Can't Be Null
- **Script:** `4-never_empty.sql`
- **Description:** Creates the table `id_not_null` with `id INT` default 1 and `name VARCHAR(256)`.

### 🆔 Unique ID
- **Script:** `5-unique_id.sql`
- **Description:** Creates the table `unique_id` with a unique `id INT` and `name VARCHAR(256)`.

### 🗺️ States Table
- **Script:** `6-states.sql`
- **Description:** Creates the database `hbtn_0d_usa` and the table `states` with unique, auto-generated `id INT` and `name VARCHAR(256)` not null.

### 🏙️ Cities Table
- **Script:** `7-cities.sql`
- **Description:** Creates the table `cities` with unique, auto-generated `id INT`, `state_id INT` as a foreign key, and `name VARCHAR(256)` not null.

### 🌅 Cities of California
- **Script:** `8-cities_of_california_subquery.sql`
- **Description:** Lists all cities of California in the `hbtn_0d_usa` database.

### 🌆 Cities by States
- **Script:** `9-cities_by_state_join.sql`
- **Description:** Lists all cities in `hbtn_0d_usa` database, displaying cities.id, cities.name, and states.name.

### 📺 Genre ID by Show
- **Script:** `10-genre_id_by_show.sql`
- **Description:** Lists all shows in `hbtn_0d_tvshows` with at least one genre linked, displaying tv_shows.title and tv_show_genres.genre_id.

### 🎭 Genre ID for All Shows
- **Script:** `11-genre_id_all_shows.sql`
- **Description:** Lists all shows in `hbtn_0d_tvshows`, displaying tv_shows.title and tv_show_genres.genre_id, including shows with no genre.

### 🚫 No Genre
- **Script:** `12-no_genre.sql`
- **Description:** Lists all shows in `hbtn_0d_tvshows` without a genre, displaying tv_shows.title and tv_show_genres.genre_id.

### 📊 Number of Shows by Genre
- **Script:** `13-count_shows_by_genre.sql`
- **Description:** Lists genres and number of shows linked to each in `hbtn_0d_tvshows`.

### 🎥 My Genres
- **Script:** `14-my_genres.sql`
- **Description:** Lists all genres of the show Dexter in `hbtn_0d_tvshows`.

### 🤣 Only Comedy
- **Script:** `15-comedy_only.sql`
- **Description:** Lists all Comedy shows in `hbtn_0d_tvshows`.

### 🎬 List Shows and Genres
- **Script:** `16-shows_by_genre.sql`
- **Description:** Lists all shows and their linked genres in `hbtn_0d_tvshows`.

### 🚷 Not My Genre
- **Script:** `100-not_my_genres.sql`
- **Advanced**
- **Description:** Lists all genres not linked to the show Dexter in `hbtn_0d_tvshows`.

### 🚫 No Comedy Tonight!
- **Script:** `101-not_a_comedy.sql`
- **Advanced**
- **Description:** Lists all shows without the genre Comedy in `hbtn_0d_tvshows`.

### 🍅 Rotten Tomatoes
- **Script:** `102-rating_shows.sql`
- **Advanced**
- **Description:** Lists all shows from `hbtn_0d_tvshows_rate` by their rating.

### 🏆 Best Genre
- **Script:** `103-rating_genres.sql`
- **Advanced**
- **Description:** Lists all genres in `hbtn_0d_tvshows_rate` by their rating.
