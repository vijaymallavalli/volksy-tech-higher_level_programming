-- SQL
SELECT ID ,NAME FROM CITIES WHERE state_id IN (SELECT ID FROM states where name ='califorina') ORDER BY ID;
