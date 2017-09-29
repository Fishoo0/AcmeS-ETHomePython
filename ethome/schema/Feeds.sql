drop table if exists Feed;
create table Feed(
    id integer primary key autoincrement,
    time text not null,

    title text not null,
    des text,
    media_list text,

    comment_list text,
    like_count integer,
    report_count integer

);