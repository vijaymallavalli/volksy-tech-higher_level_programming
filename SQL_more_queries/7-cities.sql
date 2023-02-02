-- sql 
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(
	id INT auto_increment not null primary key,
	state_id INT not null,
	name VARCHAR(256) not null,
	foreign key(state_id) references hbtn_0d_usa.states(id));
