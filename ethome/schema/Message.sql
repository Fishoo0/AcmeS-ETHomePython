drop table if exists Message;
create table Message (
    id integer primary key autoincrement,
    time text not null,

    user text not null,
    content text not null
);