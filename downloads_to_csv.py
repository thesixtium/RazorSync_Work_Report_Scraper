import glob
import os

def main():
    directory = r"C:\Users\Sixtium\Downloads"
    # file_string = "* Work Report.pdf"
    file_string = "*1).mp4"
    write_file_name = "work_reports.txt"

    open(write_file_name, "w+")
    write_file = open(write_file_name, "w")

    os.chdir(directory)
    for file in glob.glob(file_string):
        write_file.write(file + "\n")
        print(file)

if __name__ == '__main__':
    main()