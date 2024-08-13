import json
from pathlib import Path
from django.db import migrations


def load_items_from_json(apps, schema_editor):
    Item = apps.get_model('ProPlanner', 'Item')
    json_path = Path(__file__).resolve().parent / "items.json"

    with open(json_path, 'r') as file:
        data = json.load(file)

        for category, items in data.items():
            for title in items:
                Item.objects.create(title=title, score=0, category=category)


class Migration(migrations.Migration):

    dependencies = [
        # Change this to your last migration if necessary
        ('ProPlanner', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_items_from_json),
    ]
