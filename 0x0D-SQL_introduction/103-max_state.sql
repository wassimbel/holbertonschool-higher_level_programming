-- script that displays the max temperature of each state (ordered by State name)
SELECT state, MAX(value) AS max_temp from temperatures
GROUP BY state;
