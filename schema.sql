drop table if exists user;
create table user (
  id integer primary key autoincrement,
  username text not null,
  email text not null,
  passwordHash text not null,
  passwordSalt text not null,
  timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
  accessLevel int DEFAULT 1
);

