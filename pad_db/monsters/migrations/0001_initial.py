# Generated by Django 2.0.7 on 2019-06-23 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EnemySkill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default='')),
                ('effect', models.TextField(default='')),
                ('enemy_skill_id', models.IntegerField(default=-1)),
            ],
        ),
        migrations.CreateModel(
            name='Evolution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('evo', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Monster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active_skill_id', models.IntegerField(blank=True, default=0)),
                ('ancestor_id', models.IntegerField(default=0)),
                ('attribute_id', models.IntegerField(default=0)),
                ('attribute', models.CharField(default='', max_length=100)),
                ('awakenings', models.TextField(default='')),
                ('awakenings_raw', models.TextField(default='')),
                ('base_id', models.IntegerField(default=0)),
                ('card_id', models.IntegerField(default=0)),
                ('cost', models.IntegerField(default=0)),
                ('inheritable', models.CharField(default='', max_length=5)),
                ('is_collab', models.CharField(default='', max_length=5)),
                ('is_released', models.CharField(default='', max_length=5)),
                ('is_ult', models.CharField(default='', max_length=5)),
                ('leader_skill_id', models.IntegerField(blank=True, default=0)),
                ('max_atk', models.IntegerField(default=0)),
                ('max_hp', models.IntegerField(default=0)),
                ('max_level', models.IntegerField(default=0)),
                ('max_rcv', models.IntegerField(default=0)),
                ('min_atk', models.IntegerField(default=0)),
                ('min_hp', models.IntegerField(default=0)),
                ('min_rcv', models.IntegerField(default=0)),
                ('max_xp', models.IntegerField(default=0)),
                ('name', models.CharField(default='', max_length=200)),
                ('rarity', models.IntegerField(default=0)),
                ('sub_attribute_id', models.IntegerField(default=0)),
                ('sub_attribute', models.CharField(default='', max_length=100)),
                ('super_awakenings', models.TextField(default='')),
                ('evolutions', models.TextField(default='')),
                ('evo_mat_1', models.IntegerField(default=0)),
                ('evo_mat_2', models.IntegerField(default=0)),
                ('evo_mat_3', models.IntegerField(default=0)),
                ('evo_mat_4', models.IntegerField(default=0)),
                ('evo_mat_5', models.IntegerField(default=0)),
                ('unevo_mat_1', models.IntegerField(default=0)),
                ('unevo_mat_2', models.IntegerField(default=0)),
                ('unevo_mat_3', models.IntegerField(default=0)),
                ('unevo_mat_4', models.IntegerField(default=0)),
                ('unevo_mat_5', models.IntegerField(default=0)),
                ('type_1', models.CharField(default='', max_length=100)),
                ('type_2', models.CharField(default='', max_length=100)),
                ('type_3', models.CharField(default='', max_length=100)),
                ('sell_mp', models.IntegerField(default=0)),
                ('sell_coin', models.IntegerField(default=0)),
                ('enemy_skills', models.TextField(default='')),
                ('server', models.CharField(default='', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=200)),
                ('description', models.TextField(blank=True, default='')),
                ('skillID', models.IntegerField(default=-1)),
                ('skill_type', models.CharField(default='', max_length=50)),
                ('hp_mult', models.FloatField(default=1)),
                ('atk_mult', models.FloatField(default=1)),
                ('rcv_mult', models.FloatField(default=1)),
                ('dmg_reduction', models.FloatField(default=0)),
                ('c_skill_1', models.IntegerField(default=-1)),
                ('c_skill_2', models.IntegerField(default=-1)),
                ('c_skill_3', models.IntegerField(default=-1)),
                ('skill_class', models.CharField(default='', max_length=100)),
                ('levels', models.IntegerField(default=0)),
                ('maxTurns', models.IntegerField(blank=True, default=0)),
                ('minTurns', models.IntegerField(blank=True, default=0)),
                ('server', models.CharField(default='', max_length=2)),
            ],
        ),
    ]
