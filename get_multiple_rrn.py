SELECT JSON_OBJECT(
  'refnum' VALUE refnum,
  'Mask_pan' VALUE Mask_pan,
  'amount' VALUE amount,
  'OMNI_LOG_DT_UTC' VALUE OMNI_LOG_DT_UTC
) AS json_output
FROM oasis77.shclog
WHERE TRIM(refnum) = '425611726410'
AND UPPER(acquirer) LIKE '%000054%'
ORDER BY OMNI_LOG_DT_UTC DESC;