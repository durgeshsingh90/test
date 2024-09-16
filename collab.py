def duplicate_and_modify_sql(statements, start_end, blocked_item, search_items):
    """Duplicate affected SQL statements twice and apply specific modifications."""
    filtered_statements = parse_sql_statements(statements, search_items)

    if not filtered_statements:
        logger.info("No SQL statements matched the selected search items.")
        return [], statements

    modified_statements = []

    # Ensure the blocked_item is exactly 15 characters long, padded with spaces if necessary
    blocked_item_padded = blocked_item.ljust(15)

    for start_bin, end_bin, previous_bin, neighbor_plus_1 in start_end:
        for lowbin, highbin, description, original_statement in filtered_statements:
            if int(lowbin) <= int(start_bin) <= int(highbin):
                # Create modified versions of the original SQL statements
                modified_original_statement = original_statement.replace(f"'{highbin}'", f"'{previous_bin}'")

                # Adjust description replacement to maintain a fixed length of 15 characters
                new_statement1 = original_statement.replace(f"'{lowbin}'", f"'{start_bin}'")\
                                                   .replace(f"'{highbin}'", f"'{end_bin}'")\
                                                   .replace(f"'{description.capitalize().ljust(15)}'", f"'{blocked_item_padded}'")\
                                                   .replace(f"'{description.upper().ljust(15)}'", f"'{blocked_item_padded.upper()}'")\
                                                   .replace(f"'{description.ljust(15)}'", f"'{blocked_item_padded.lower()}'")\
                                                   .replace(f"'{description}'", f"'{blocked_item_padded}'")  # Replace the description with padded value

                # Replace cardproduct field with blocked_item padded to 15 characters
                new_statement1 = new_statement1.replace(f"'CARDPRODUCT': '{description.ljust(15)}'", f"'CARDPRODUCT': '{blocked_item_padded}'")

                # Adjust neighbor for new statement
                new_statement2 = original_statement.replace(f"'{lowbin}'", f"'{neighbor_plus_1}'")\
                                                   .replace(f"'{description.capitalize().ljust(15)}'", f"'{blocked_item_padded}'")\
                                                   .replace(f"'{description.upper().ljust(15)}'", f"'{blocked_item_padded.upper()}'")\
                                                   .replace(f"'{description.ljust(15)}'", f"'{blocked_item_padded.lower()}'")\
                                                   .replace(f"'{description}'", f"'{blocked_item_padded}'")  # Replace the description with padded value

                modified_statements.extend([modified_original_statement, new_statement1, new_statement2])
                statements.remove(original_statement)

    return modified_statements, statements
