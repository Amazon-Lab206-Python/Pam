SELECT countries.name, languages.language, languages.percentage
FROM languages
JOIN countries ON countries.id = languages.country_id
WHERE languages.language = 'Slovene'
ORDER BY languages.percentage DESC;

SELECT countries.name, COUNT(cities.id)
FROM countries
LEFT JOIN cities on countries.id = cities.country_id
GROUP BY countries.name
ORDER BY COUNT(cities.id) DESC;

SELECT cities.name, SUM(cities.population) AS total_pop
FROM countries
JOIN cities on countries.id = cities.country_id
WHERE countries.name = 'Mexico'
GROUP BY cities.name
HAVING SUM(cities.population) > 500000
ORDER BY SUM(cities.population) DESC;

SELECT countries.name, languages.language, languages.percentage
FROM languages
LEFT JOIN countries ON countries.id = languages.country_id
WHERE languages.percentage > 89
ORDER BY languages.percentage DESC;

SELECT countries.name, countries.surface_area, countries.population
FROM countries
WHERE countries.surface_area < 501 and countries.population > 100000;

SELECT countries.name, countries.government_form, countries.capital, countries.life_expectancy
FROM countries
WHERE countries.government_form = 'Constitutional Monarchy' and countries.capital > 200 and countries.life_expectancy > 75;

SELECT countries.name, cities.name, district, cities.population
FROM cities
LEFT JOIN countries ON countries.id = cities.country_id
WHERE cities.district = 'Buenos Aires' and cities.population > 500000;

SELECT countries.region, COUNT(countries.id) AS countries
FROM countries
GROUP BY countries.region
ORDER BY COUNT(countries.id) DESC;