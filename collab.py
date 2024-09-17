nblock\urls.py", line 2, in <module>
    from .views import bin_blocking_editor
  File "C:\Durgesh\Office\Automation\AutoMate\AutoMate\binblock\views.py", line 389
    part1_statement = f"INSERT INTO your_table_name VALUES ({', '.join(f'\'{v}\'' for v in part1_values)});"      
                                                         
                                                   ^     
SyntaxError: f-string expression part cannot include a backslash
