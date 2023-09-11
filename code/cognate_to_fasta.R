                          #### CRÉATION FICHIER FASTA ####


# Create the paths for input and output folders 
input_dir <- "/Users/wasmi/Stage/r_linguisitic/word_table"
output_dir <- "/Users/wasmi/Stage/r_linguisitic/word_fasta"

if (!dir.exists(output_dir)) {
  dir.create(output_dir)
}

# list all the files in the input folder

input_files <- list.files(input_dir, full.names = TRUE)



# Function to transform text files to fast format (the right fast structure)
write_fasta <- function(data, output_file) {
  
  file_conn <- file(output_file, "w")

  for (i in 1:nrow(data)) {
    language <- data[i, 1]
    word <- data[i, 2]
    # Entête (similaire à "> organisme" mais avec le nom mot/cognat)
    writeLines(paste0(">", language), con=file_conn)
    # Le mot en seconde ligne (au lieu d'une séquence biologique)
    writeLines(word, con=file_conn)
  }
  close(file_conn)
}


for (input_file in input_files) {
  data <- read.table(input_file, sep="\t", header=FALSE, stringsAsFactors=FALSE)
 
  #retirer l'extention du nom du fichier
  file_name <- tools::file_path_sans_ext(basename(input_file))
  
 #créer les fichiers fasta
  output_file <- file.path(output_dir, paste0(file_name, ".fasta"))
  write_fasta(data, output_file)
}




