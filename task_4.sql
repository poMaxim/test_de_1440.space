SELECT
    month,
    category,
    SUM(traffic_gb) OVER (PARTITION BY month, category) AS total_traffic,
    SUM(EXTRACT(EPOCH FROM time)) OVER (PARTITION BY month, category) AS total_time_sec
FROM
    your_table
GROUP BY
    month,
    category;
