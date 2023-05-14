import csv
import os
import glob

counterA = 1
folder = r'D:\AERMOD_Core_01\UnzippedFiles'
csv_files=glob.glob(os.path.join(folder, '*.csv'))
for fpath in csv_files:
    print(fpath)

with open(r'D:\AERMOD_Core_01\UnzippedFiles\micro2020_{i}_core01.csv', newline='') as f:
    with open(r'D:\AERMOD_Core_01\AERMOD_UIDS\micro2020_{i}_core01_UniqID.csv', 'w', newline='') as o:
        writer = csv.writer(o)
        reader = csv.reader(f)
        counter=1
        for row in reader:
            if row[0] != '14':
                continue
            id=(int(row[1]) + 3000) * 100000 + int(row[2])
            row.append(str(id))

            writer.writerow(row)
            del row
            counter=counter + 1
            if counter % 1000 == 0:
                print(counter)