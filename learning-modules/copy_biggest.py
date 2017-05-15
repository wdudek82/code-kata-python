import os
import shutil


def copy_biggest_files(source, destination, number):
    """
    This function copies n biggest files from source to destination folders.
    First draft.
    """

    os.chdir(source)

    files = tuple(
        (os.path.abspath(file), os.stat(file).st_size, os.path.isfile(file)) for file in os.listdir(source)
    )
    sorted_files = sorted(files, key=lambda f: f[1], reverse=True)

    count = 0
    number = number if number < len(sorted_files) else len(sorted_files)
    while count < number:
        file, size, is_file = sorted_files[count]

        if is_file:
            position = str(count).zfill(3)
            print("[{}] Copying file: {}".format(position, file))
            shutil.copy(file, destination)

        count += 1


source = "/home/neevor/"
destination = os.path.join(os.getcwd(), "dest")

copy_biggest_files(source, destination, 5)

