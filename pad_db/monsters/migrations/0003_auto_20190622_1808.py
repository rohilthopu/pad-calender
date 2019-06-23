# Generated by Django 2.0.7 on 2019-06-23 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monsters', '0002_skill_server'),
    ]

    operations = [
        migrations.RenameField(
            model_name='monster',
            old_name='activeSkillID',
            new_name='active_skill_id',
        ),
        migrations.RenameField(
            model_name='monster',
            old_name='ancestorID',
            new_name='ancestor_id',
        ),
        migrations.RenameField(
            model_name='monster',
            old_name='attributeID',
            new_name='attribute_id',
        ),
        migrations.RenameField(
            model_name='monster',
            old_name='baseID',
            new_name='base_id',
        ),
        migrations.RenameField(
            model_name='monster',
            old_name='cardID',
            new_name='card_id',
        ),
        migrations.RenameField(
            model_name='monster',
            old_name='evomat1',
            new_name='evo_mat_1',
        ),
        migrations.RenameField(
            model_name='monster',
            old_name='evomat2',
            new_name='evo_mat_2',
        ),
        migrations.RenameField(
            model_name='monster',
            old_name='evomat3',
            new_name='evo_mat_3',
        ),
        migrations.RenameField(
            model_name='monster',
            old_name='evomat4',
            new_name='evo_mat_4',
        ),
        migrations.RenameField(
            model_name='monster',
            old_name='evomat5',
            new_name='evo_mat_5',
        ),
        migrations.RenameField(
            model_name='monster',
            old_name='isCollab',
            new_name='is_collab',
        ),
        migrations.RenameField(
            model_name='monster',
            old_name='isReleased',
            new_name='is_released',
        ),
        migrations.RenameField(
            model_name='monster',
            old_name='isUlt',
            new_name='is_ult',
        ),
        migrations.RenameField(
            model_name='monster',
            old_name='leaderSkillID',
            new_name='leader_skill_id',
        ),
        migrations.RenameField(
            model_name='monster',
            old_name='maxATK',
            new_name='max_atk',
        ),
        migrations.RenameField(
            model_name='monster',
            old_name='maxHP',
            new_name='max_hp',
        ),
        migrations.RenameField(
            model_name='monster',
            old_name='maxLevel',
            new_name='max_level',
        ),
        migrations.RenameField(
            model_name='monster',
            old_name='maxRCV',
            new_name='max_rcv',
        ),
        migrations.RenameField(
            model_name='monster',
            old_name='maxXP',
            new_name='max_xp',
        ),
        migrations.RenameField(
            model_name='monster',
            old_name='minATK',
            new_name='min_atk',
        ),
        migrations.RenameField(
            model_name='monster',
            old_name='minHP',
            new_name='min_hp',
        ),
        migrations.RenameField(
            model_name='monster',
            old_name='minRCV',
            new_name='min_rcv',
        ),
        migrations.RenameField(
            model_name='monster',
            old_name='sellCoin',
            new_name='sell_coin',
        ),
        migrations.RenameField(
            model_name='monster',
            old_name='subattribute',
            new_name='sub_attribute',
        ),
        migrations.RenameField(
            model_name='monster',
            old_name='subAttributeID',
            new_name='sub_attribute_id',
        ),
        migrations.RenameField(
            model_name='monster',
            old_name='superAwakenings',
            new_name='super_awakenings',
        ),
        migrations.RenameField(
            model_name='monster',
            old_name='type1',
            new_name='type_1',
        ),
        migrations.RenameField(
            model_name='monster',
            old_name='type2',
            new_name='type_2',
        ),
        migrations.RenameField(
            model_name='monster',
            old_name='type3',
            new_name='type_3',
        ),
        migrations.RenameField(
            model_name='monster',
            old_name='unevomat1',
            new_name='unevo_mat_1',
        ),
        migrations.RenameField(
            model_name='monster',
            old_name='unevomat2',
            new_name='unevo_mat_2',
        ),
        migrations.RenameField(
            model_name='monster',
            old_name='unevomat3',
            new_name='unevo_mat_3',
        ),
        migrations.RenameField(
            model_name='monster',
            old_name='unevomat4',
            new_name='unevo_mat_4',
        ),
        migrations.RenameField(
            model_name='monster',
            old_name='unevomat5',
            new_name='unevo_mat_5',
        ),
        migrations.RemoveField(
            model_name='monster',
            name='atk99',
        ),
        migrations.RemoveField(
            model_name='monster',
            name='evos_raw',
        ),
        migrations.RemoveField(
            model_name='monster',
            name='hp99',
        ),
        migrations.RemoveField(
            model_name='monster',
            name='rcv99',
        ),
        migrations.RemoveField(
            model_name='monster',
            name='sellMP',
        ),
        migrations.RemoveField(
            model_name='monster',
            name='superAwakenings_raw',
        ),
        migrations.AddField(
            model_name='monster',
            name='sell_mp',
            field=models.IntegerField(default=0),
        ),
        migrations.RemoveField(
            model_name='monster',
            name='evolutions',
        ),
        migrations.AddField(
            model_name='monster',
            name='evolutions',
            field=models.TextField(default=''),
        ),
    ]
