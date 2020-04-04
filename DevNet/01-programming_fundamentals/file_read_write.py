from datetime import datetime

log = "log_file.txt"
"""
when we use "with open" then we don't need to explicitly close open file , it will be atomically taken care  
"""

def read_log(log):
    with open(log, "r") as f:
        print(f.read())


def write_log(log, data):
    with open(log, "a") as f:
        f.writelines("{0} : This is line has data : {1}\n".format(current_time, data))


if __name__ == "__main__":
    current_time = str(datetime.now())
    data = input("Please provide some data : ")

    print("Writing some data to log file..")
    write_log(log, data)

    print("Reading log file..")
    read_log(log)
