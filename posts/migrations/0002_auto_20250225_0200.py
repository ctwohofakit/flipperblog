from django.db import migrations

def populate_status(apps, schema_editor):
    entries = {
        "published": "A post that is visible to all",
        "draft": "A post not yet ready to be published",
        "archived": "An older post, for logged in users"
    }
    Status = apps.get_model("posts", "Status")
    for key, value in entries.items():
        status_obj = Status(name=key, description=value)
        status_obj.save()

class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_status)
    ]
