drop table if exists bookinfo;
create table bookinfo(
    id integer primary key autoincrement,
    title string not null,
    text string not null
);
