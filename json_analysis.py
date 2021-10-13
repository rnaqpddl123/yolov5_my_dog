import json
import math


def move_dog():
    with open('log/image_log.json', 'r', encoding='UTF-8-sig') as f:
        json_data = json.load(f)

    pre_x = json_data["frames"][0]["frame"][0]["center_x"]
    pre_y = json_data["frames"][0]["frame"][0]["center_y"]
    standard = 50

    outlier = 200
    count = 0

    for i in json_data["frames"] :

        if i["frame"] != []:
            for j in i["frame"]:
                move_x = abs(j["center_x"] - pre_x)
                move_y = abs(j["center_y"] - pre_y)
                pre_x = j["center_x"]
                pre_y = j["center_y"]
                compare_move = pow(move_x,2) + pow(move_y,2)
                if compare_move > standard and compare_move < outlier:
                    distance = math.sqrt(compare_move)
                    print("이동거리 x,y", move_x, move_y, "이동한거리 : ", distance)
                    count +=1
        else:
            pass
    print(count)

        
if __name__== '__main__':
    move_dog()

