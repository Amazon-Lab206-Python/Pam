SELECT city.city_id, city.city, customer.first_name, customer.last_name, customer.email, address.address
FROM city
JOIN address ON city.city_id = address.city_id
JOIN customer ON address.address_id = customer.address_id
WHERE city.city_id = 312;

SELECT film.film_id, film.title, film.description, film.release_year, film.rating, film.special_features, category.name AS genre
FROM film
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON film_category.category_id = category.category_id
WHERE category.name = 'Comedy';

SELECT actor.actor_id, CONCAT(actor.first_name, ' ', actor.last_name) AS actor_name, film.film_id, film.title, film.description, film.release_year
FROM film
JOIN film_actor ON film.film_id = film_actor.film_id
JOIN actor ON film_actor.actor_id = actor.actor_id
WHERE actor.actor_id = 5;

SELECT customer.first_name, customer.last_name, customer.email, address.address
FROM customer
JOIN address ON customer.address_id = address.address_id
JOIN city ON address.city_id = city.city_id
WHERE customer.store_id = 1 and city.city_id IN (1, 42, 312, 459);

SELECT film.title, film.description, film.release_year, film.rating, film.special_features
FROM film
LEFT JOIN film_actor ON film.film_id = film_actor.film_id
WHERE film.rating = 'G' and film.special_features LIKE '%Behind the Scenes%' and film_actor.actor_id = 15;

SELECT CONCAT(actor.first_name,' ', actor.last_name) AS actor_name, actor.last_update
FROM actor 
JOIN film_actor ON actor.actor_id = film_actor.actor_id
WHERE film_actor.film_id = 369;

SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name AS genre
FROM film
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON film_category.category_id = category.category_id
WHERE film.rental_rate = 2.99 and category.name = 'Drama';

SELECT CONCAT(actor.first_name,' ', actor.last_name) AS actor_name, film.title, film.description, film.release_year, film.rating, film.special_features, category.name AS genre
FROM film
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON film_category.category_id = category.category_id
JOIN film_actor ON film.film_id = film_actor.film_id
JOIN actor ON film_actor.actor_id = actor.actor_id
WHERE actor.first_name = 'SANDRA' and actor.last_name = 'KILMER' and category.name = 'Action'


