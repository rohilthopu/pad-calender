from django.core.management.base import BaseCommand, CommandError
from monsters.models import Monster, Evolution
from dataversions.models import Version
import json
import time
import os

from .maps import TYPE_MAP, AWAKENING_MAP
from Utils.progress import progress
from django.conf import settings

class Command(BaseCommand):
    help = 'Runs an update on the models to add to the database.'

    def handle(self, *args, **options):

        def makeMonster(rawCard, server):
            monster = Monster()
            monster.save()
            monster.active_skill_id = rawCard['active_skill_id']
            monster.ancestorID = rawCard['ancestor_id']
            monster.attributeID = rawCard['attr_id']

            awakenings = []
            awakenings_raw = []
            for a in rawCard['awakenings']:
                awakenings_raw.append(int(a))
                awakening = AWAKENING_MAP[a]
                if awakening != "":
                    awakenings.append(awakening)

            jsonDump = json.dumps(awakenings)
            jsonDump2 = json.dumps(awakenings_raw)

            monster.awakenings = jsonDump
            monster.awakenings_raw = jsonDump2
            monster.baseID = rawCard['base_id']
            monster.cardID = rawCard['card_id']
            monster.cost = rawCard['cost']
            monster.inheritable = "Yes" if rawCard['inheritable'] else "No"
            monster.isCollab = "Yes" if rawCard['is_collab'] else "No"
            monster.isReleased = "Yes" if rawCard['released_status'] else "No"
            monster.isUlt = rawCard['is_ult']
            monster.leaderSkillID = rawCard['leader_skill_id']
            monster.maxATK = rawCard['max_atk']
            monster.maxHP = rawCard['max_hp']
            monster.maxLevel = rawCard['max_level']
            monster.maxRCV = rawCard['max_rcv']
            monster.minATK = rawCard['min_atk']
            monster.minHP = rawCard['min_hp']
            monster.minRCV = rawCard['min_rcv']
            monster.maxXP = rawCard['xp_max']

            monster.name = rawCard['name']
            if monster.cardID >= 100000:
                if "alt." not in rawCard['name'].lower():
                    name = rawCard['name']
                    altname = "Alt. " + name
                    monster.name = altname

            monster.rarity = rawCard['rarity']
            monster.subAttributeID = rawCard['sub_attr_id']
            monster.evomat1 = rawCard['evo_mat_id_1']
            monster.evomat2 = rawCard['evo_mat_id_2']
            monster.evomat3 = rawCard['evo_mat_id_3']
            monster.evomat4 = rawCard['evo_mat_id_4']
            monster.evomat5 = rawCard['evo_mat_id_5']

            if monster.ancestorID != 0:
                monster.unevomat1 = rawCard['un_evo_mat_1']
                monster.unevomat2 = rawCard['un_evo_mat_2']
                monster.unevomat3 = rawCard['un_evo_mat_3']
                monster.unevomat4 = rawCard['un_evo_mat_4']
                monster.unevomat5 = rawCard['un_evo_mat_5']

            monster.hp99 = monster.maxHP + 990
            monster.atk99 = monster.maxATK + 495
            monster.rcv99 = monster.maxRCV + 495

            monster.type1 = TYPE_MAP[rawCard['type_1_id']]
            monster.type2 = TYPE_MAP[rawCard['type_2_id']]
            monster.type3 = TYPE_MAP[rawCard['type_3_id']]

            sawakenings = []
            sawakenings_raw = []
            for sa in rawCard['super_awakenings']:
                awakening = AWAKENING_MAP[sa]
                sawakenings_raw.append(int(sa))
                if awakening != "":
                    sawakenings.append(awakening)
            sadump = json.dumps(sawakenings)
            monster.superAwakenings = sadump
            monster.superAwakenings_raw = json.dumps(sawakenings_raw)

            monster.sellMP = rawCard['sell_mp']
            monster.sellCoin = rawCard['sell_price_at_lvl_10']

            monster.server = server

            enemy_skills = []

            for skill in rawCard['enemy_skill_refs']:
                enemy_skills.append(skill['enemy_skill_id'])

            monster.enemy_skills = json.dumps(enemy_skills)

            monster.save()

        m = Monster.objects.all()
        prevSize = m.count()
        m.delete()
        Evolution.objects.all().delete()

        if settings.DEBUG:
            self.stdout.write('\tDebug option enabled')
            self.stdout.write('\tGrabbing files from alternative locations')
            location = '/Users/rohil/projects/personal/data_files/processed/na_cards.json'
            location2 = '/Users/rohil/projects/personal/data_files/processed/jp_cards.json'

        else:
            self.stdout.write('\tUsing standard file path')
            location = '/home/rohil/data/pad_data/processed_data/na_cards.json'
            location2 = '/home/rohil/data/pad_data/processed_data/jp_cards.json'

        self.stdout.write('\tLocation 1, NA: {}'.format(location))
        self.stdout.write('\tLocation 2, JP: {}'.format(location2))

        with open(os.path.abspath(location), 'r') as jsonPull:

            self.stdout.write('')
            self.stdout.write(self.style.SUCCESS('Starting NA MONSTER DB update.'))

            cards = json.load(jsonPull)
            start_time = time.time()
            self.stdout.write('')
            self.stdout.write(self.style.SUCCESS('Adding new NA Cards.'))


            total = len(cards)
            for i in range(0, total):
                card = cards[i]
                released = card['card']['released_status']
                cardName = card['card']['name']
                if released and cardName is not '' and '*' not in cardName:
                    rawCard = card['card']
                    if not isinstance(rawCard, type(None)):
                        progress(i, total)
                        makeMonster(rawCard, 'na')
                        self.stdout.flush()

        self.stdout.write('')
        monsters = Monster.objects.all()

        # merge in JP monsters
        with open(os.path.abspath(location2), 'r') as jsonPull:
            cards = json.load(jsonPull)

            self.stdout.write('Merging in JP monsters')
            total = len(cards)
            for i in range(0, total):
                card = cards[i]
                name = card['card']['name']
                if name != '':
                    rawCard = card['card']
                    cardID = rawCard['card_id']
                    if not monsters.filter(cardID=cardID).exists():
                        progress(i, total)
                        makeMonster(rawCard, 'jp')
                        self.stdout.flush()

        monsters = Monster.objects.all()

        self.stdout.write('')
        self.stdout.write(self.style.SUCCESS('NA Monster List Updated.'))
        self.stdout.write('')
        self.stdout.write(self.style.SUCCESS('Updating forward evolutions and relevant dungeons.'))


        total = monsters.count()

        for i in range(0, total):
            monster = monsters[i]
            progress(i, total)
            if monster.ancestorID != monster.cardID:
                if monster.ancestorID != 0:
                    ancestor = monsters.get(cardID=monster.ancestorID)
                    evo = Evolution(evo=monster.cardID)
                    evo.save()
                    ancestor.evolutions.add(evo)
                    ancestor.save()
            self.stdout.flush()

        self.stdout.write('')
        self.stdout.write('Adding in raw evolution IDs')
        for i in range(0, total):
            monster = monsters[i]
            progress(i, total)
            parsedEvos = monster.evolutions.all()
            evos = []
            for evo in parsedEvos:
                evos.append(evo.evo)
            monster.evos_raw = json.dumps(evos)
            monster.save()
            self.stdout.flush()



        end_time = time.time()

        self.stdout.write('')

        self.stdout.write(self.style.SUCCESS('Monster update complete.'))

        self.stdout.write('')
        self.stdout.write("Updating version")

        ver = Version.objects.all()

        if len(ver) == 0:
            v = Version()
            v.monster = 1
            v.save()
        else:
            v = ver.first()
            if prevSize < monsters.count():
                v.monster += 1
            v.save()

        self.stdout.write("Elapsed time : {}".format(end_time - start_time))
        self.stdout.write('')
