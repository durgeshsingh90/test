select  
refnum,Mask_pan,amount,OMNI_LOG_DT_UTC
from oasis77.shclog 
where refnum in ('425611726410')
and acquirer LIKE '%000054%'
order by omni_log_dt_utc desc

