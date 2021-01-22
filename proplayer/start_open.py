try:
    with open ("data.txt","r") as aa:print ("".join ([chr (int (ff)-1) for ff in aa.read ().strip ("\n").split ("\n")]));
except (FileNotFoundError):exit ("file data.txt mungkin sudah dihapus");

