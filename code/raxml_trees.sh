#!/bin/bash

# Directory paths
input_dir="phylip_numbered"
output_dir="trees"

# Create output directory if it doesn't exist
mkdir -p "$output_dir"

# Execute RAxML-NG for each file in the input directory
for file in "$input_dir"/*.aligned.phy; do
    # Get the file name without extension
    filename=$(basename "$file" .aligned.phy)
    
    # Run RAxML-NG command
    ./raxml-ng --msa "$file" --model JTT --tree pars{1} --bs-trees 100 --all --prefix "$output_dir/$filename"
done

