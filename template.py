from genericpath import exists
import os


dirs = [
    os.path.join("data", "raw"),
    os.path.join("data", "processed"),
    "notebooks",
    "saved_models",
    "src"
]

files = [
    "dvc.yaml",
    "param.yaml",
    ".gitignore",
    os.path.join("src", "__init__py"),

]


for dir_ in dirs:
    os.makedirs(dir_, exist_ok=True)
    # with open(os.path.join(dir_, ".gitkeep")) as f:
    #     pass

for file_ in files:
    with open(file_, "w") as f:
        pass