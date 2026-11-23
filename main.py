import os
LINE = "I did not miss that spot. My lidar classified it as a rug, the rug filed a complaint, and we are still in mediation."
os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
