def duplicate_and_modify_sql(sql_statements, bins_with_neighbors, blocked_item):
    """
    Duplicate and modify SQL statements based on processed bins and the blocked item.
    
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
        # Extract the LOWBIN and HIGHBIN from the SQL statement
        try:
            values_part = statement.split("VALUES (")[1]
            values = values_part.split(",")
            lowbin = values[0].strip(" '")  # Extract LOWBIN
            highbin = values[1].strip(" '")  # Extract HIGHBIN
            description = values[4].strip(" '")  # Extract DESCRIPTION
            card_product = values[6].strip(" '")  # Extract CARDPRODUCT

            # Ensure LOWBIN and HIGHBIN are numeric for comparison
            lowbin_int = int(lowbin)
            highbin_int = int(highbin)
        except (IndexError, ValueError):
            logger.error(f"Error parsing LOWBIN and HIGHBIN from statement: {statement}")
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
                    part1_statement = f"INSERT INTO your_table_name (LOWBIN, HIGHBIN, DESCRIPTION, CARDPRODUCT) " \
                                      f"VALUES ('{lowbin}', '{neighbor_minus_1}', '{description}', '{card_product}');"
                    modified_statements.append(part1_statement)

                # Part 2: The blocked range
                blocked_statement = f"INSERT INTO your_table_name (LOWBIN, HIGHBIN, DESCRIPTION, CARDPRODUCT) " \
                                    f"VALUES ('{start_bin}', '{end_bin}', '{blocked_item}', '{blocked_item}');"
                modified_statements.append(blocked_statement)

                # Part 3: After the blocked range (if applicable)
                if highbin_int > end_bin_int:
                    part3_statement = f"INSERT INTO your_table_name (LOWBIN, HIGHBIN, DESCRIPTION, CARDPRODUCT) " \
                                      f"VALUES ('{neighbor_plus_1}', '{highbin}', '{description}', '{card_product}');"
                    modified_statements.append(part3_statement)

                statement_modified = True
                break

        if not statement_modified:
            remaining_statements.append(statement)

    # Log the results of the modification process
    logger.debug(f"Modified SQL Statements: {modified_statements}")
    logger.debug(f"Remaining SQL Statements: {remaining_statements}")

    return modified_statements, remaining_statements
