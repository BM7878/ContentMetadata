import glob 
import json 
import os
import ast 

fps1 = glob.glob("blog-posts/*")

for fp in fps1:
    os.remove(fp)

fps2 = glob.glob("../pennylane.ai-react/apps/pennylane-website/content/blog/*/*/*.md")

for fp in fps2:
    print(fp)

print(len(fps2))

for fp in fps2:

    folderPath, fileName = os.path.split(fp)
    metadata = {}

    with open(fp, "r", encoding="utf-8") as fo:
        lines = fo.readlines()[0:8]
        lines = [line.strip() for line in lines if line.strip() != "---"]

        t = "{" + ",".join(lines) + "}"

        for an in ["title", "date", "authors", "name", "nameSuffix", "category", "tags", "description", "thumbnailImage"]:
            t = t.replace(an + ": ", "'" + an + "': ")

        metadata = ast.literal_eval(t)

    fn = os.path.join("blog-posts", fileName[:-3] + ".json")

    with open(fn, "w", encoding="utf-8") as fo:
        json.dump(metadata, fo, indent=4)

        