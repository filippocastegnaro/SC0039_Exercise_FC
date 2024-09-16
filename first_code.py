import csv
#old file
old_file = 'brca_cnvs_tcga-1-2.csv' 

#new file
new_file = 'brca_cnvs_tcga-1-2_NEW.csv'    

#reading the old file
with open(old_file, mode='r', newline='') as file:
    reader = csv.reader(file)

    #converting the reader into a list
    data = list(reader)

#create the 'lenght' to the header and ' ' values
new_column_header = 'lenght'

#add 'lenght' to the header
data[0].append(new_column_header)

#define the indices for the columns i want to subtract
column_a_index = 3 #loc.end
column_b_index = 2 #loc.start

#skip the header and run a for loop to add the difference between the row 3 and 2
for row in data[1:]:
    
    # convert the values to floats and make the difference
    value_a = float(row[column_a_index])
    value_b = float(row[column_b_index])
    difference = value_a - value_b

    # add the difference in the last spot of the row
    row.append(difference)

#print data to check if changes are correct
print(data)

#save the updated data in a new file in the same folder
with open(new_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
