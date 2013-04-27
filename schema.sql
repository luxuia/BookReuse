drop table if exists bookinfo;
create table bookinfo(
    id integer primary key autoincrement,
    small_title string,
    main_title string not null,
    img_url string,
    short_info string,
    rating_num integer,
    rating_man integer
);


drop table if exists booktag;
create table booktag(
    id integer primary key autoincrement,
    tag string not null,
    book_id integer not null
);
