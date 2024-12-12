# Generated by Django 5.1.3 on 2024-12-04 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pc", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="submissionbin",
            name="description",
        ),
        migrations.AddField(
            model_name="submissionbin",
            name="category",
            field=models.CharField(
                choices=[
                    ("Personal Data Sheet", "Personal Data Sheet"),
                    ("Syllabi", "Syllabi"),
                    ("Class Records", "Class Records"),
                    ("Grading Sheets", "Grading Sheets"),
                    ("Accomplishment Report", "Accomplishment Report"),
                    ("Exams", "Exams"),
                    ("Quizzes/Tests", "Quizzes/Tests"),
                    ("Table of Specifications", "Table of Specifications"),
                    ("Rubrics", "Rubrics"),
                    ("Sample Student Project", "Sample Student Project"),
                    ("Instructional Materials", "Instructional Materials"),
                    ("PRC License", "PRC License"),
                    ("Trainings/Seminars", "Trainings/Seminars"),
                    ("Research Projects", "Research Projects"),
                    ("Extension Projects", "Extension Projects"),
                    ("Documentation", "Documentation"),
                    ("Membership in Organization", "Membership in Organization"),
                ],
                max_length=100,
                null=True,
            ),
        ),
    ]
