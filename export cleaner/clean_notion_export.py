import os
import re

def clean_name(name):
    # Remove trailing UUIDs (32 hex digits) and extra spaces before extension or folder
    return re.sub(r"\s[a-f0-9]{32}(\.md)?$", r"\1", name)

for root, dirs, files in os.walk(".", topdown=False):
    # Clean files
    for file in files:
        new_name = clean_name(file)
        if file != new_name:
            os.rename(os.path.join(root, file), os.path.join(root, new_name))
    # Clean folders
    for dir in dirs:
        new_name = clean_name(dir)
        if dir != new_name:
            os.rename(os.path.join(root, dir), os.path.join(root, new_name))
