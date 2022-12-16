responses = {"gif":"image/gif", "jpg":"image/jpg","jpeg":"image/jpeg","png":"image/png","pdf":"application/pdf","txt":"application/txt","zip":"application/zip"}
fname = input("Filename: ")
fname = fname.split(".")
try:
    print(responses[fname[1]])
except IndexError:
    print("application/octet-stream")
except KeyError:
    print("application/octet-stream")