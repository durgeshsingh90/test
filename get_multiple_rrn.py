C:\Durgesh\Office\Automation\Python\RRN_List>python get_multiple_rrn.py
sqlplus f94gdos/Pune24!@A5PCDO8001.EQU.IST <<EOF
SELECT JSON_OBJECT('refnum' VALUE refnum, 'Mask_pan' VALUE Mask_pan, 'amount' VALUE amount, 'OMNI_LOG_DT_UTC' VALUE OMNI_LOG_DT_UTC) AS json_output FROM oasis77.shclog WHERE refnum = '425611726410' AND acquirer LIKE '%000054%';
EXIT;
EOF
<Popen: returncode: None args: "sqlplus f94gdos/Pune24!@A5PCDO8001.EQU.IST <...>
Process completed. Output saved to output_results.txt.
