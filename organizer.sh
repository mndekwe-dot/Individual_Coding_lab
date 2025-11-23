#!/bin/bash

# organizer.sh - In charge of archiving CSV files with timestamps

# ✅ REQUIREMENT 1: To check/create Archive
if [ ! -d "archive" ]; then
    mkdir archive
    echo "Created archive directory"
fi

# ✅ REQUIREMENT 2: Find and Process CSVs
csv_files=$(find . -maxdepth 1 -name "*.csv" -type f)

# Check if any CSV files exist
if [ -z "$csv_files" ]; then
    echo "No CSV files found to archive."
    exit 0
fi

# ✅ REQUIREMENT 3: Loop, Log, and Archive
for csv_file in $csv_files; do
    # Get just the filename without path
    filename=$(basename "$csv_file")
    
    # ✅ Generate Timestamp (format: YYYYMMDD-HHMMSS)
    timestamp=$(date +"%Y%m%d-%H%M%S")
    
    # Extract filename without extension
    name="${filename%.csv}"
    
    # ✅ Define New Name with timestamp before extension
    new_filename="${name}-${timestamp}.csv"
    
    # ✅ Log Action: Append archiving details and file content
    echo "========================================" >> organizer.log
    echo "Archive Date: $(date '+%Y-%m-%d %H:%M:%S')" >> organizer.log
    echo "Original File: $filename" >> organizer.log
    echo "New File: $new_filename" >> organizer.log
    echo "Contents:" >> organizer.log
    cat "$csv_file" >> organizer.log
    echo "" >> organizer.log
    
    # ✅ Move & Rename to archive directory
    mv "$csv_file" "archive/$new_filename"
    
    echo "Archived: $filename -> archive/$new_filename"
done

echo "All CSV files have been archived successfully!"