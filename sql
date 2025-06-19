SELECT 
    TO_CHAR(omni_log_dt_utc, 'DD/MM/YYYY') || '           ' || TO_CHAR(omni_log_dt_utc, 'HH12 AM') AS DATE______HOUR,

    COUNT(*) AS Total_Transactions,
    SUM(DECODE(respcode, '0', 1, 0)) AS Approvals,
    SUM(DECODE(respcode, '8', 1, 0)) AS Timeouts,
    SUM(DECODE(respcode, '68', 1, 0)) AS Response_rec_late,

    (SUM(DECODE(respcode, '0', 0, 1)) 
     - SUM(DECODE(respcode, '8', 1, 0)) 
     - SUM(DECODE(respcode, '68', 1, 0))) AS Other_Declines,

    ROUND(
        SUM(DECODE(respcode, '0', 1, 0)) / 
        (SUM(DECODE(respcode, '0', 0, 1)) + SUM(DECODE(respcode, '0', 1, 0))), 4
    ) * 100 || '%' AS Percentage

FROM 
    oasis77.shclog

WHERE 
    omni_log_dt_utc BETWEEN TO_DATE('11-JUN-2025 12:00:00', 'DD-MON-YYYY HH24:MI:SS') 
                        AND TO_DATE('12-JUN-2025 15:00:00', 'DD-MON-YYYY HH24:MI:SS')

-- AND acceptorname LIKE 'SumUp%'

GROUP BY 
    TO_CHAR(omni_log_dt_utc, 'DD/MM/YYYY'),
    TO_CHAR(omni_log_dt_utc, 'HH12 AM'),
    TO_CHAR(omni_log_dt_utc, 'YYYYMMDDHH24')  -- used only for ordering

ORDER BY 
    TO_CHAR(omni_log_dt_utc, 'YYYYMMDDHH24');