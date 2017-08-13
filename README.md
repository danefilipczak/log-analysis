

This is a program that does some analysis of a postgreSQL database. 



# Setup 

Connect to the 'news' database with `psql -d news` . 

If the 'news' database hasn't been initialized, execute the content of newsdata.sql with the command ` psql -d news -f newsdata.sql `


This project requires two additional views, which can be created by entering the following commands in the psql console:


```
create view toparticles as 
	select articles.title, articles.author, sub.num from articles 
	join (select path, 
	count(*) as num 
	from log 
	where status='200 OK' 
	group by path
	order by num desc) as sub
	on '/article/' || articles.slug = sub.path;
```




```
create view errors as 
	select time::date as date, 
	count(CASE WHEN status = '404 NOT FOUND' THEN 1 END)::float 
	/ count(*)::float * 100 as percent 
	from log group by time::date;
```

# Execution 

Run dbproj.py using python3