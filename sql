SELECT 
    SUBSTR(TO_CHAR(omni_log_dt_utc, 'DD/MM/YYYY HH:MI:SS AM'), 1, 5) AS Date_,
    SUBSTR(TO_CHAR(omni_log_dt_utc, 'YYYYMMDD HH:MI:SS AM'), 10, 2) || ' ' || SUBSTR(TO_CHAR(omni_log_dt_utc, 'YYYYMMDD HH:MI:SS AM'), -2) AS HOUR_,
    COUNT(*) AS Total_Transactions
FROM 
    oasis77.shclog
WHERE  
    omni_log_dt_utc BETWEEN TO_DATE('11-JUN-2025 11:00:00', 'DD-MON-YYYY HH24:MI:SS') AND TO_DATE('12-JUN-2025 13:00:00', 'DD-MON-YYYY HH24:MI:SS')  -- Search for a specific time
-- AND acceptorname LIKE 'SumUp%'
GROUP BY     
    SUBSTR(TO_CHAR(omni_log_dt_utc, 'YYYYMMDD HH:MI:SS AM'), 10, 2),
    SUBSTR(TO_CHAR(omni_log_dt_utc, 'DD/MM/YYYY HH:MI:SS AM'), 1, 5),
    SUBSTR(TO_CHAR(omni_log_dt_utc, 'YYYYMMDD HH:MI:SS AM'), -2),
    SUBSTR(TO_CHAR(omni_log_dt_utc, 'YYYYMMDD HH24:MI:SS'), 10, 2)
ORDER BY     
    SUBSTR(TO_CHAR(omni_log_dt_utc, 'YYYYMMDD HH24:MI:SS'), 10, 2);
