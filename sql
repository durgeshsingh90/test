SELECT 
    TO_CHAR(omni_log_dt_utc, 'DD/MM') AS DATE_,
    TO_CHAR(omni_log_dt_utc, 'HH12 AM') AS HOUR_,
    COUNT(*) AS TOTAL_TRANSACTIONS
FROM 
    oasis77.shclog
WHERE  
    omni_log_dt_utc BETWEEN TO_TIMESTAMP('2025-06-11 11:00:00', 'YYYY-MM-DD HH24:MI:SS')
    AND TO_TIMESTAMP('2025-06-12 13:00:00', 'YYYY-MM-DD HH24:MI:SS')
    -- AND acceptorname LIKE 'SumUp%'
GROUP BY     
    TO_CHAR(omni_log_dt_utc, 'DD/MM'),
    TO_CHAR(omni_log_dt_utc, 'HH12 AM'),
    TO_CHAR(omni_log_dt_utc, 'YYYYMMDDHH24')  -- used only for correct ordering
ORDER BY     
    TO_CHAR(omni_log_dt_utc, 'YYYYMMDDHH24');