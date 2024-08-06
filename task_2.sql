CREATE TEMP TABLE serv_down_transp AS
SELECT id, 't1' AS time, t1 AS value FROM serv_down
UNION ALL
SELECT id, 't2' AS time, t2 AS value FROM serv_down
UNION ALL
SELECT id, 't3' AS time, t3 AS value FROM serv_down
UNION ALL
SELECT id, 't4' AS time, t4 AS value FROM serv_down;


CREATE TEMP TABLE req_down_transp AS
SELECT id, 't1' AS time, t1 AS value FROM req_down
UNION ALL
SELECT id, 't2' AS time, t2 AS value FROM req_down
UNION ALL
SELECT id, 't3' AS time, t3 AS value FROM req_down
UNION ALL
SELECT id, 't4' AS time, t4 AS value FROM req_down;


CREATE TABLE final_table AS
SELECT 
    d.id, 
    d.year, 
    t.time, 
    d.uber_3, 
    d.speed_down, 
    s.value AS serv_down, 
    r.value AS req_down
FROM 
    data d
JOIN 
    serv_down_transp s ON d.id = s.id
JOIN 
    req_down_transp r ON d.id = r.id AND s.time = r.time
JOIN 
    (SELECT DISTINCT id, time FROM serv_down_transp) t ON d.id = t.id AND s.time = t.time;