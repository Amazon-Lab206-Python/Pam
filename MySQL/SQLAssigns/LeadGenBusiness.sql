SELECT MONTHNAME(billing.charged_datetime), SUM(billing.amount)
FROM billing
WHERE MONTHNAME(billing.charged_datetime) = 'March' and year(billing.charged_datetime) = 2012
GROUP BY billing.charged_datetime;

SELECT billing.client_id, SUM(billing.amount)
FROM billing
WHERE billing.client_id = 2
GROUP BY billing.client_id;

SELECT sites.domain_name, sites.client_id
FROM sites
WHERE sites.client_id = 10;

SELECT COUNT(sites.site_id) AS number_of_sites, MONTHNAME(sites.created_datetime) as month_created, YEAR(sites.created_datetime) as year_created
FROM sites
WHERE sites.client_id = 20
GROUP BY sites.site_id;

SELECT sites.domain_name AS website, COUNT(leads.leads_id) AS leads, date_format(leads.registered_datetime, "%M %D, %Y") AS date
FROM sites
JOIN leads ON sites.site_id = leads.site_id
WHERE leads.registered_datetime BETWEEN CAST('2011-01-01' AS DATE) AND CAST('2011-02-15' AS DATE)
GROUP BY sites.domain_name



