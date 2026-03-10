from datetime import datetime
import json
from files import *



def register_movement(entity_type, obj_id, action, new_value):
    event = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "type": entity_type,
        "id": obj_id,
        "action": action,
        "new_value": new_value
    }

    all_movements = view_datas("movements.json")
    path = verify("movements.json")

    all_movements.append(event)

    with open(path,"w",encoding="utf-8") as f:
        json.dump(all_movements, f, indent=4, ensure_ascii=False)