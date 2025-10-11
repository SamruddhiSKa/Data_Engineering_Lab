CREATE TABLE IF NOT EXISTS state_climate (
    id SERIAL PRIMARY KEY,
    state_ut VARCHAR(100),
    district VARCHAR(100),
    temperature_c REAL,
    condition VARCHAR(50),
    humidity_percent REAL,
    wind_speed_kmh REAL,
    last_updated TIMESTAMP
);

SELECT * FROM state_climate LIMIT 10;

SELECT district, temperature_c, humidity_percent, wind_speed_kmh, last_updated
FROM state_climate
WHERE state_ut = 'Maharashtra'
ORDER BY district, last_updated;
