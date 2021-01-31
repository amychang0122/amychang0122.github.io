from os import listdir
import os, time
import shutil

print('????')
files = listdir("./Music")
f = open("./music_list.txt", "w", encoding="utf-8")
for i in range(len(files)):
    f.write("\"" + os.path.splitext(files[i])[0] + "\"")
    if i!=len(files)-1:
        f.write(",")
    #print(os.path.splitext(files[i])[0])
print(len(files))
f.close()

# backup file
localtime = time.asctime( time.localtime(time.time()) )
web = "./index.html"
backup = "./Backup/index_" + time.strftime("%m%d", time.localtime()) + ".html"
if not os.path.isfile(backup):
    shutil.copyfile(web, backup)
    shutil.copyfile(web, "./index_backup.html")

f = open("./music_list.txt", "r", encoding="utf-8")
read = open(backup, "r", encoding="utf-8")
write = open(web, "w", encoding="utf-8")
content = read.readlines()
for each in content:
    if "var songs" in each:
        write.write(each.split("song")[0] + "songs = [" + f.read() + "];\n")
    else:
        write.write(each)
f.close()
read.close()
write.close()
