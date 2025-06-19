select substr(to_char(omni_log_dt_utc, 'DD/MM/YYYY HH:MI:SS AM'),1,9)|| '             '||substr(to_char(omni_log_dt_utc, 'YYYYMMDD HH:MI:SS AM'),10,5) || ' '|| substr(to_char(omni_log_dt_utc, 'YYYYMMDD HH:MI:SS AM'),-2) AS DATE______HOUR_MIN,

count(*) as Total_Transactions,SUM (DECODE (respcode, '0', 1, 0)) AS approvals,

SUM (DECODE (respcode, '8', 1, 0)) Timeouts,   

SUM (DECODE (respcode, '68', 1, 0)) Response_rec_late,  

           (SUM (DECODE (respcode, '0', 0, 1))-SUM (DECODE (respcode, '8', 1, 0))-SUM (DECODE (respcode, '68', 1, 0))) Other_Declines,

       (Round(SUM (DECODE (respcode, '0', 1, 0))/(SUM (DECODE (respcode, '0', 0, 1)) + SUM (DECODE (respcode, '0', 1, 0))),4)*100)  || '%' AS Percentage
 
from         oasis77.shclog

--where OMNI_LOG_DT_UTC >= (sysdate-1/24)-5/1440 -- past 15 mins BST

--WHERE OMNI_LOG_DT_UTC >= sysdate -15/1440 -- Winter Time GMT

where   omni_log_dt_utc between to_date('11-JUN-2025 12:00:00', 'dd-mon-yyyy hh24:mi:ss')and 

                              to_date('12-JUN-2025 15:00:00', 'dd-mon-yyyy hh24:mi:ss')  --Search for a specific time

--and acceptorname like 'SumUp%'
 
group by     substr(to_char(omni_log_dt_utc, 'YYYYMMDD HH:MI:SS AM'),10,5),

            substr(to_char(omni_log_dt_utc, 'DD/MM/YYYY HH:MI:SS AM'),1,9), 

            substr(to_char(omni_log_dt_utc, 'YYYYMMDD HH:MI:SS AM'),-2), 

            substr(to_char(omni_log_dt_utc, 'YYYYMMDD HH24:MI:SS'),10,2)

order by    substr(to_char(omni_log_dt_utc, 'YYYYMMDD HH:MI:SS AM'),10,5)desc;
 
