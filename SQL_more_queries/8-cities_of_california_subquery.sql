-- sql
select  id ,name from cities where state_id in (select id from states were name = "california") order by id ;
