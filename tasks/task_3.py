from os import listdir

def find_need_files(directory_path, file_format):
    if "\"" in directory_path:
        directory_path = directory_path.replace("\"", "")

    if "\\" in directory_path:
        directory_path = directory_path.replace("\\", "/")

    if directory_path[-1] != "/":
        directory_path += "/"

    match_files = list()

    for file in listdir(directory_path):
        if file.endswith(f".{file_format}"):
            match_files.append(directory_path + file)

    return match_files

def determine_info_for_file(directory_to_file):
    with(open(directory_to_file, 'r', encoding="utf-8") as f):
        file_data = f.read().splitlines()

    file_name = directory_to_file.split('/')[-1]
    file_length = len(file_data)

    return {"file_name": file_name, "row_quantity": file_length,"info_from_file": file_data}

def make_export_file(info_from_all_files):
    info_from_all_files = sorted(info_from_all_files,
                                 key=lambda x: x["row_quantity"],
                                 reverse=False)
    with(open("export_data_for_task_3.txt", 'w', encoding="utf-8") as f):
        for file in info_from_all_files:
            f.write(str(file["file_name"]) + "\n")
            f.write(str(file["row_quantity"]) + "\n")
            f.write("\n".join(file["info_from_file"]) + "\n")