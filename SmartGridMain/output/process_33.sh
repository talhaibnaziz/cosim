#!/bin/bash

output_file="combined_results_33.md"

# Initialize output file with header
echo "# Combined Results" > "$output_file"

# Loop through all files starting with "ieee13"
for file in ./ieee33_*; do
    if [[ -f "$file" ]]; then
        filename=$(basename "$file")
        
        # Add Heading 1 for the current file
        echo "## $filename" >> "$output_file"

        # Find lines following "Simulation finished successfully."
        grep_lines=$(grep -A 9 'Simulation finished successfully.' "$file")

        # Initialize line counter and result number
        line_counter=0
        result_number=1

        while IFS= read -r line; do
            if [[ $line =~ Simulation\ finished\ successfully\. ]]; then
                echo "### Result $result_number" >> "$output_file"

                ((result_number++))
                continue
            fi

            echo "$line" >> "$output_file"
        done <<< "$grep_lines"
    fi
done

echo "Combined results saved to $output_file"
