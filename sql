SELECT
  TO_CHAR(omni_log_dt_utc, 'DD/MM') AS DATE,
  TO_CHAR(omni_log_dt_utc, 'HH12 AM') AS HOUR,
  COUNT(*) AS TOTAL_TRANSACTIONS
FROM
  oasis77.schlog
WHERE
  omni_log_dt_utc BETWEEN TO_DATE('11-JUN-2025 11:00:00', 'DD-MON-YYYY HH24:MI:SS')
  AND TO_DATE('12-JUN-2025 13:00:00', 'DD-MON-YYYY HH24:MI:SS')
  AND acceptorname LIKE 'SumUp%'
GROUP BY
  TO_CHAR(omni_log_dt_utc, 'DD/MM'),
  TO_CHAR(omni_log_dt_utc, 'HH12 AM'),
  TO_CHAR(omni_log_dt_utc, 'YYYYMMDDHH24') -- for proper sorting
ORDER BY
  TO_CHAR(omni_log_dt_utc, 'YYYYMMDDHH24');