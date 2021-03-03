import sys
# basic log printer
def load_log(filename, process_check):
    file = open(filename, "r")
    line = ""
    while True:
        # read line
        line = file.readline()
        if not line:
            break
        # split log info string away from actual log
        line_info = line[:line.find("]: ")+2]
        line_log = line[line.find("]: ")+2:]
        line_info = line_info.split(" ")
        # remove host name 
        del line_info[3]
        # combine dates and times
        date_time = " ".join([line_info[i] for i in [0, 1, 2]])
        # process names could potentially contain spaces which is why we combine
        # instead of just reading index 3
        process_name = " ".join([line_info[i] for i in range(3, len(line_info))])
        if(process_check in process_name):
            print(date_time, line_log, sep="", end="")
    print("\n")


if len(sys.argv) - 1 != 2:
    print("Usage: python3 log.py [log_file] [process_name]")
else:
    load_log(sys.argv[1], sys.argv[2])