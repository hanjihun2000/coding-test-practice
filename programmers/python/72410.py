# 2021 KAKAO BLIND RECRUITMENT 신규 아이디 추천
import re
def solution(new_id):
    # Step 1
    new_id = new_id.lower()
    # Step 2
    for c in "~!@#$%^&*()=+[{]}:?,<>/":
        new_id = new_id.replace(str(c), "")
    # Step 3
    new_id = re.sub("\.\.+", ".", new_id)
    # Step 4
    if new_id.startswith("."):
        new_id = new_id.replace(new_id[0], "", 1)
    if new_id.endswith("."):
        new_id = new_id[:len(new_id)-1]
    # Step 5
    if new_id == "":
        new_id = "a"
    # Step 6:
    if len(new_id) > 15:
        new_id = new_id[:15]
        if new_id.endswith("."):
            new_id = new_id[:len(new_id)-1]
    # Step 7
    while len(new_id) < 3:
        new_id = new_id + new_id[len(new_id)-1]
    return new_id