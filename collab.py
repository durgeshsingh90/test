def save_sql_statements_to_file(statements, file_path):
    """Save SQL INSERT statements to a file and maintain a record of file paths and their statements."""
    # Initialize a dictionary to store file paths and their corresponding statements
    if not hasattr(save_sql_statements_to_file, "file_statements"):
        save_sql_statements_to_file.file_statements = {}  # Attribute to store paths and statements

    logger.debug(f"Saving SQL statements to {file_path}")
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write("\n".join(statements))
        logger.info(f"SQL statements saved to {file_path}")
        
        # Store the statements in the dictionary under the file path key
        if file_path in save_sql_statements_to_file.file_statements:
            save_sql_statements_to_file.file_statements[file_path].extend(statements)
        else:
            save_sql_statements_to_file.file_statements[file_path] = list(statements)

    except Exception as e:
        logger.error(f"Error saving SQL statements to file {file_path}: {e}")
    logger.debug(f"Completed saving SQL statements to {file_path}")

# Example Usage
# Assume `save_sql_statements_to_file` is called multiple times like this:
save_sql_statements_to_file(["INSERT INTO ..."], "file1.sql")
save_sql_statements_to_file(["INSERT INTO ..."], "file2.sql")

# At any point, you can access the saved statements like this:
all_file_statements = save_sql_statements_to_file.file_statements
