drop table if exists Setting;
create table Setting (
    id integer primary key autoincrement,
    time text not null,

    user_id text not null,
    setting_01 integer
);