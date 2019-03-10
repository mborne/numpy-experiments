create temporary table noisy_circle AS
	select
		( 1.0 + r * cos(theta) ) as x,
		( 2.0 + r * sin(theta) ) as y
	from (
		SELECT ( 2.0 * pi() * generate_series(0,1000) / 1000.0 ) as theta, 3.0 + random() / 10.0 as r 
	) t;

\copy noisy_circle to 'noisy-circle.csv' with CSV HEADER;
