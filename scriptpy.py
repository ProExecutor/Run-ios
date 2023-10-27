import plistlib

def read_plist(plist_path):
    with open(plist_path, 'rb') as fp:
        pl = plistlib.load(fp)
    return pl

# replace 'my_file.plist' with your plist file path
plist_data = read_plist('my_file.plist')
print(plist_data)
