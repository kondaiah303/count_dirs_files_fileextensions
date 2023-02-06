import os
import json
path = r'/Users/entropik/Documents/code/converz-collab'


def count_dirs_files_and_file_extensions(dir_path):
    dirs = 0
    files = 0
    file_extensions = {}
    count = 0
    for dir_root, dir_names, file_names in os.walk(dir_path):
        dirs += len(dir_names)
        for filename in file_names:
            files += 1
            extension = os.path.splitext(filename)[1]
            if extension == '':
                count += 1
                continue
            if extension in file_extensions:
                file_extensions[extension] += 1
            else:
                file_extensions[extension] = 1
    sorted_file_extensions = dict(sorted(file_extensions.items(), key=lambda value: value[1]))
    body = {
        'folders_count': dirs,
        'files_count': files,
        'extensions_count': sorted_file_extensions,
        'non_extensions_file_count': count
    }
    return json.dumps(body, indent=3)


print(count_dirs_files_and_file_extensions(path))
