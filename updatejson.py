import json
import os
import sys


# この関数は `main.py` ファイルの内容を解析して、必要なデータを抽出します。
def parse_main_py(file_path):
    if not os.path.exists(file_path):
        return None

    with open(file_path, "r") as file:
        lines = file.read().splitlines()

    # 最初の行をタイトルとして取得
    title = lines[0]

    if not title.startswith("#"):
        return None

    # ボディを構成する
    body = []
    is_paragraph = False
    paragraph = ""

    for line in lines[1:]:
        if line.startswith('"""'):  # パラグラフの開始または終了
            if is_paragraph:  # パラグラフの終了
                body.append({"tag": "p", "text": paragraph.strip()})
                paragraph = ""
            is_paragraph = not is_paragraph
            continue

        if is_paragraph:
            paragraph += line + "\n"
            continue

        if line.startswith("######"):
            body.append({"tag": "h6", "text": line[6:].strip()})
        elif line.startswith("#####"):
            body.append({"tag": "h5", "text": line[5:].strip()})
        elif line.startswith("####"):
            body.append({"tag": "h4", "text": line[4:].strip()})
        elif line.startswith("###"):
            body.append({"tag": "h3", "text": line[3:].strip()})
        elif line.startswith("##"):
            body.append({"tag": "h2", "text": line[2:].strip()})
        else:  # それ以外の行はコードとして扱う
            body.append({"tag": "code", "text": line})

    return {"title": title, "body": body}


def update_blog_json(json_path, contest_type, problem_id, content):
    if content is None:
        return

    with open(json_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    # 適切なコンテストと問題を見つけて更新
    for contest in data["dir"]:
        if contest["contestgenre"] == contest_type:
            for prob in contest["contests"]:
                if prob["name"] == problem_id:
                    prob["problems"] = content
                    break

    with open(json_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def main(file_paths):
    json_path = "docs/blog.json"  # JSONファイルのパス

    for file_path in file_paths:
        contest_type = os.path.basename(
            os.path.dirname(os.path.dirname(file_path))
        ).upper()
        problem_id = os.path.basename(os.path.dirname(file_path))

        content = parse_main_py(file_path)
        update_blog_json(json_path, contest_type, problem_id, content)


if __name__ == "__main__":
    file_paths = sys.argv[1].split(" ")
    main(file_paths)
