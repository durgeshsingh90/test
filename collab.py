def duplicate_and_modify_sql(statements, start_end, blocked_item, search_items):
    """Duplicate affected SQL statements twice and apply specific modifications."""
    filtered_statements = parse_sql_statements(statements, search_items)

    if not filtered_statements:
        logger.info("No SQL statements matched the selected search items.")
        return [], statements

    modified_statements = []

    for start_bin, end_bin, previous_bin, neighbor_plus_1 in start_end:
        for lowbin, highbin, description, original_statement in filtered_statements:
            if int(lowbin) <= int(start_bin) <= int(highbin):
                # Create modified versions of the original SQL statements
                modified_original_statement = original_statement.replace(f"'{highbin}'", f"'{previous_bin}'")

                # Ensure both description and cardproduct fields are renamed to the blocked_item
                new_statement1 = original_statement.replace(f"'{lowbin}'", f"'{start_bin}'")\
                                                   .replace(f"'{highbin}'", f"'{end_bin}'")\
                                                   .replace(f"'{description.capitalize()}'", f"'{blocked_item}'")\
                                                   .replace(f"'{description.upper()}'", f"'{blocked_item.upper()}'")\
                                                   .replace(f"'{description}'", f"'{blocked_item.lower()}'")\
                                                   .replace(f"'{description}'", f"'{blocked_item}'")  # Replace the description
               
                # Additional replacement for cardproduct fields to blocked_item
                new_statement1 = new_statement1.replace(f"'CARDPRODUCT': '{description}'", f"'CARDPRODUCT': '{blocked_item}'")

                new_statement2 = original_statement.replace(f"'{lowbin}'", f"'{neighbor_plus_1}'")\
                                                   .replace(f"'{description.capitalize()}'", f"'{blocked_item}'")\
                                                   .replace(f"'{description.upper()}'", f"'{blocked_item.upper()}'")\
                                                   .replace(f"'{description}'", f"'{blocked_item.lower()}'")\
                                                   .replace(f"'{description}'", f"'{blocked_item}'")  # Replace the description

                modified_statements.extend([modified_original_statement, new_statement1, new_statement2])
                statements.remove(original_statement)

    return modified_statements, statements