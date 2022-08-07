import os, argparse

ap = argparse.ArgumentParser()
ap.add_argument("-n", "--file_name", required=True, help="File name to generate")
ap.add_argument("-p", "--path", required=True, help="Path to image folder")
ap.add_argument("-t", "--type", required=True, help="File type to generate csv or txt")
ap.add_argument("-i", "--include", type=bool, default=False, help="Include path to files")
args = vars(ap.parse_args())

file_name = str(args["file_name"])
path = str(args["path"])
file_type = str(args["type"])
inclusion = args["include"]

myfile = open(str(file_name + "." + file_type), 'w')

for path, subdirs, files in os.walk(path):
        for filename in files:
            f = "{}/{}".format(path, filename)
            ext = filename.split(".")
            g = filename.replace(ext[1], "")
            z = g.replace(".", "")

            if file_type == "csv" and inclusion == False:
                myfile.write(str(g + ext[1] + "," + z + '\n'))
            if file_type == "txt" and inclusion == False:
                myfile.write(str(g + ext[1] + " " + z + '\n'))
            if file_type == "csv" and inclusion == True:
                myfile.write(str(f + "," + z + '\n'))
            if file_type == "txt" and inclusion == True:
                myfile.write(str(f + " " + z + '\n'))
myfile.close()
