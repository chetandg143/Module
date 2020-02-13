import  File
try:
  File f = open("/home/tibil/Desktop\demofile.txt")
  f.write("Lorum Ipsum")
except:
  print("Something went wrong when writing to the file")
finally:
  f.close()