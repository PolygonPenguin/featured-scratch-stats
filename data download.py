import scratchattach as sa
import json
import math
from tqdm import tqdm

studio = sa.get_studio(25080442)
def get_if_project(number):
    return len(studio.projects(1, number))>0

last = 0
projects = 1
while last!=projects:
    
    if get_if_project(projects):
        last = projects
        projects*=2
    else:
        l=projects
        projects = (projects-last)//2+last
        last = l
print(projects)
chunks = []
for i in tqdm(range(math.ceil(projects/40))):
    for project in studio.projects(offset=i*40):
        project.update()
        try:
            chunks.append({
                "title": project.title,
                "creator": project.author_name,
                "id": project.id,
                "date": project.share_date,
                "instructions": project.instructions,
                "notes": project.notes,
                "loves": project.loves,
                "favorites": project.favorites,
                "views": project.views,
                "remixes": project.remix_count
            })
        except:
            pass
with open("data.json", 'w') as f:
    json.dump(chunks, f)
