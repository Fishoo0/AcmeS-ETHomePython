drop table if exists User;
create table User (
    id integer primary key autoincrement,
    time text not null,

    name text not null,
    password text not null,
    token text,

    cover text,
    sex text,
    gender integer,
    birth text,
    age text,
    location text,
    about text,

    following integer,
    following_count integer,

    followed integer,
    followed_count integer,

    post_count integer,
    rate_number integer,

    like_count integer,
    dislike_count integer

);