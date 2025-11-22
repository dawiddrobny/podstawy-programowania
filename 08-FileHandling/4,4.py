# Read and display the CSV file in batches of 5 lines
with open("it_company.csv", "r", encoding="utf-8") as file:
    lines = file.readlines()

    # Process lines in batches of 5
    for i in range(0, len(lines), 5):
        # Display the next 5 lines (or remaining lines if less than 5)
        batch = lines[i : i + 5]
        for line in batch:
            print(line.rstrip())  # Remove trailing newline to avoid double spacing

        # Check if there are more lines to display
        if i + 5 < len(lines):
            print("Press Enter key...")
            input()  # Wait for Enter key press
