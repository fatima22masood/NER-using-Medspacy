import spacy
import medspacy

nlp=spacy.load("en_info_3700_i2b2_2012")



# File paths
input_dat_file = 'train.dat'  # Replace with your .dat file path
output_dat_file = 'xtrain.dat'  # Replace with your output file path


## Open the input file and read word by word
i=0
with open(input_dat_file, 'r') as infile, open(output_dat_file, 'w') as outfile:
    for line in infile:
        # Split each line into words
        doc = nlp(line)
        medical_entities = [ ent.text for ent in doc.ents]

        for token in doc:


            if token.text in medical_entities:
                doc1 = nlp(token.text)
                for i in doc1.ents:
                    outfile.write('['+ i.text + ':'+ i.label_ + '] ')
            else:
                outfile.write(token.text + ' ')

        print("working...")
