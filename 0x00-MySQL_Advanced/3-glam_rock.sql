-- 3 glam rock

-- return bands with glam rock as main style order by lifespan
SELECT band_name, (IFNULL(split, 2022) - formed) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
