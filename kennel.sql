SELECT
    a.id,
    a.name,
    a.breed,
    a.treatment,
    a.customerId,
    a.locationId,
    l.name location_name,
    l.address location_address,
    c.name customer_name,
    c.address customer_address,
    c.email customer_email,
    c.password customer_password
FROM Animal a
JOIN Location l
    ON l.id = a.locationId
JOIN Customer c
    ON c.id = a.customerId
WHERE a.id = 2;
