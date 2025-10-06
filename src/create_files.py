import os 
from pathlib import Path


def new_file():
    log_dir = Path("logs/")
    log_dir.mkdir(exist_ok=True)

    id_file_path = log_dir / "id.txt"

    try:
        with open(id_file_path, "r") as ide:
            g = ide.read().strip() 
            if not g.isdigit():
                g = "0"
    except FileNotFoundError:
        with open(id_file_path, "w") as ide:
            ide.write("0")
        g = "0"
    ide.close()
    ide = open(id_file_path,"w")

    ide.write(str(int(g)+1))
    ide.close()
    f =  open(log_dir / f"{g}.csv","a")
    f.write("food_count,robots_count,avg_speed,avg_rot_vel,avg_vision,avg_fail_rot\n")

    return f