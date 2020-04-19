import shutil,glob,os,datetime
from pathlib import Path

print("place which folder you want to backup")
src_dir = input()
print("to wich folder do you want to place the backup")
dst_dir = input()

curent_date = datetime.datetime.now()
file_name = str(curent_date.strftime("%d-%m-%Y"))+ ".txt"

#make a folder
folder_name = str(curent_date.strftime("%d-%m-%Y")) + "_"+ str(curent_date.strftime("%H:%M"))
new_folder = dst_dir+folder_name
path = Path(str(new_folder))
    
if path.is_dir():
    print("file already exist")
else:
    folder = os.mkdir(new_folder)

os.chdir(src_dir)
total = 0 

for file in os.listdir(src_dir):
    # type of file you want a copy of 
    if file.endswith(".xlsx"):
        file = os.path.join(src_dir, file)
        shutil.copy(file,new_folder)
        total += 1

file = open(file_name,"w+")
file.write("Amount of Files \r\n")
file.write(str(total))
file.close
shutil.move(file_name,new_folder)
