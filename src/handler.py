import os, shutil



def copy_static(src_path, dest_path):
    # first delete all contents
    if os.path.exists(dest_path):
        shutil.rmtree(dest_path)
    os.mkdir(dest_path)

    # loop through contents of src
    for entry in os.listdir(src_path):
        original = os.path.join(src_path, entry)
        new_path = os.path.join(dest_path, entry)

        if os.path.isfile(original):
            shutil.copy(original, new_path)
        else:
            copy_static(original, new_path)