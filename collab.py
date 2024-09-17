def duplicate_and_modify_sql(sql_statements, bins_with_neighbors, blocked_item):
    """
    Duplicate and modify SQL statements based on processed bins and the blocked item, applying length checks and removing empty lines.
    
    Args:
    sql_statements (list): List of SQL statements to process.
    bins_with_neighbors (list): Processed bins with start and end ranges, along with their neighboring bins.
    blocked_item (str): The item to be blocked.

    Returns:
    tuple: A tuple containing the modified SQL statements and the remaining original SQL statements.
    """
    # Logging the inputs for debugging purposes
    logger.debug(f"SQL Statements to be processed: {sql_statements}")
    logger.debug(f"Bins with Neighbors: {bins_with_neighbors}")
    logger.debug(f"Blocked Item: {blocked_item}")

    modified_statements = []
    remaining_statements = []

    # Iterate over each SQL statement
    for statement in sql_statements:
        # Extract the fields from the SQL statement
        try:
            # Preserve the original format of the statement
            insert_part, values_part = statement.split("VALUES (", 1)
            values_part = values_part.rstrip("); \n").strip()

            # Split the values part and strip each value of leading/trailing whitespace and quotes
            values = [value.strip(" '") for value in values_part.split(",")]

            # Ensure there are enough values to process
            if len(values) < 7:  # Adjust this number if you have more or fewer fields in your insert statement
                logger.error(f"Unexpected number of fields in statement: {statement}. Found {len(values)} fields.")
                remaining_statements.append(statement)
                continue

            # Extract relevant fields for clarity
            lowbin = values[0]  # LOWBIN
            highbin = values[1]  # HIGHBIN
            description = values[4]  # DESCRIPTION
            card_product = values[6]  # CARDPRODUCT

            # Convert LOWBIN and HIGHBIN to integers for comparison
            lowbin_int = int(lowbin)
            highbin_int = int(highbin)
        except (IndexError, ValueError) as e:
            logger.error(f"Error parsing fields from statement: {statement}. Error: {e}")
            remaining_statements.append(statement)
            continue

        # Check if any of the bins need to be modified based on the blocked item
        statement_modified = False

        for (start_bin, end_bin, neighbor_minus_1, neighbor_plus_1) in bins_with_neighbors:
            # Convert start_bin and end_bin to integers for comparison
            try:
                start_bin_int = int(start_bin.strip())
                end_bin_int = int(end_bin.strip())
            except ValueError:
                logger.error(f"Invalid start_bin or end_bin format: {start_bin}, {end_bin}")
                continue

            # Check if start_bin falls within the range of LOWBIN and HIGHBIN
            if lowbin_int <= start_bin_int <= highbin_int:
                # Log the modification details
                logger.debug(f"Modifying SQL statement: {statement} for BIN range {start_bin} - {end_bin}")

                # Create three new SQL statements based on the split
                # Part 1: Before the blocked range (if applicable)
                if lowbin_int < start_bin_int:
                    part1_values = values.copy()
                    part1_values[0] = lowbin  # Original LOWBIN
                    part1_values[1] = neighbor_minus_1  # HIGHBIN before blocked range
                    part1_values_dict = {key: value for key, value in zip(
                        ["LOWBIN", "HIGHBIN", "O_LEVEL", "STATUS", "DESCRIPTION", "DESTINATION", "ENTITY_ID", "CARDPRODUCT", "FILE_NAME", "FILE_VERSION", "FILE_DATE"],
                        part1_values
                    )}
                    part1_values_dict = apply_length_checks(part1_values_dict)
                    part1_statement = "{}VALUES ({});".format(
                        insert_part, ', '.join(f"'{part1_values_dict[key]}'" for key in part1_values_dict if part1_values_dict[key].strip())
                    )
                    modified_statements.append(part1_statement)

                # Part 2: The blocked range
                blocked_values = values.copy()
                blocked_values[0] = start_bin  # LOWBIN for blocked range
                blocked_values[1] = end_bin  # HIGHBIN for blocked range
                blocked_values[4] = blocked_item  # DESCRIPTION changed to blocked_item
                blocked_values[6] = blocked_item  # CARDPRODUCT changed to blocked_item
                blocked_values_dict = {key: value for key, value in zip(
                    ["LOWBIN", "HIGHBIN", "O_LEVEL", "STATUS", "DESCRIPTION", "DESTINATION", "ENTITY_ID", "CARDPRODUCT", "FILE_NAME", "FILE_VERSION", "FILE_DATE"],
                    blocked_values
                )}
                blocked_values_dict = apply_length_checks(blocked_values_dict)
                blocked_statement = "{}VALUES ({});".format(
                    insert_part, ', '.join(f"'{blocked_values_dict[key]}'" for key in blocked_values_dict if blocked_values_dict[key].strip())
                )
                modified_statements.append(blocked_statement)

                # Part 3: After the blocked range (if applicable)
                if highbin_int > end_bin_int:
                    part3_values = values.copy()
                    part3_values[0] = neighbor_plus_1  # LOWBIN after blocked range
                    part3_values[1] = highbin  # Original HIGHBIN
                    part3_values_dict = {key: value for key, value in zip(
                        ["LOWBIN", "HIGHBIN", "O_LEVEL", "STATUS", "DESCRIPTION", "DESTINATION", "ENTITY_ID", "CARDPRODUCT", "FILE_NAME", "FILE_VERSION", "FILE_DATE"],
                        part3_values
                    )}
                    part3_values_dict = apply_length_checks(part3_values_dict)
                    part3_statement = "{}VALUES ({});".format(
                        insert_part, ', '.join(f"'{part3_values_dict[key]}'" for key in part3_values_dict if part3_values_dict[key].strip())
                    )
                    modified_statements.append(part3_statement)

                statement_modified = True
                break

        if not statement_modified:
            remaining_statements.append(statement)

    # Remove any empty or blank lines
    modified_statements = [stmt for stmt in modified_statements if stmt.strip()]

    # Log the results of the modification process
    logger.debug(f"Modified SQL Statements: {modified_statements}")
    logger.debug(f"Remaining SQL Statements: {remaining_statements}")

    return modified_statements, remaining_statements
