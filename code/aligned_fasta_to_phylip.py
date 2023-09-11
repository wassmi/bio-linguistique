# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.5
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

import os
from Bio import SeqIO
from Bio.Align.Applications import MuscleCommandline
from Bio import AlignIO

# +
"""This part is to convert the fast files to aligned fasta format"""

input_folder = "./word_fasta"
output_folder = "./aligned_fasta_1"


# -

def align_sequences(input_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    # Get list of input files in the input folder
    input_files = os.listdir(input_folder)
    input_files = [file for file in input_files if file.endswith(".fasta")]

    for file_name in input_files:
        input_path = os.path.join(input_folder, file_name)
        output_path = os.path.join(output_folder, file_name.replace(".fasta", ".aligned.fasta"))

        input_sequences = list(SeqIO.parse(input_path, "fasta"))

        if len(input_sequences) < 2:
            print(f"Skipping file '{file_name}' - at least two sequences required for alignment.")
            continue

        # command line for MUSCLE alignment
        muscle_cline = MuscleCommandline(input=input_path)

        # Perform the alignment
        stdout, stderr = muscle_cline()

        # Save the aligned sequences to the output file
        with open(output_path, "w") as handle:
            handle.write(stdout)

        print(f"Alignment saved to '{output_path}'.")
align_sequences(input_folder, output_folder)

# +
"""This part is to convert the fasta files to phylip format"""

input_fasta = "./aligned_fasta_1"
output_phylip = "./phylip_files"
# -

# Create the output folder if it doesn't exist
if not os.path.exists(output_phylip):
    os.makedirs(output_phylip)

# +
# Iterate over each file in the input folder
for file_name in os.listdir(input_fasta):
    if file_name.endswith(".fasta"):
        # Construct the input and output file paths
        input_path = os.path.join(input_fasta, file_name)
        output_path = os.path.join(output_phylip, file_name.replace(".fasta", ".phy"))

        # Read the input fasta file
        alignment = AlignIO.read(input_path, "fasta")

        # Retrieve the original sequence names
        sequence_names = [record.id for record in alignment]

        # Get the maximum length of sequence names
        max_name_length = max(len(name) for name in sequence_names)

        # Write the alignment to Phylip format with sequence names on the left
        with open(output_path, "w") as output_file:
            output_file.write(f"{len(sequence_names)} {alignment.get_alignment_length()}\n")
            for i, record in enumerate(alignment):
                name = sequence_names[i]
                output_file.write(f"{name:<{max_name_length}} {record.seq}\n")

        print(f"Converted {file_name} to Phylip format.")

print("Conversion complete!")






# -


