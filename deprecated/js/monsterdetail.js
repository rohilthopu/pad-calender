function showSkill() {

    document.getElementById('monsterdata').style.display = 'none';
    document.getElementById('evomaterials').style.display = 'none';
    document.getElementById('unevomaterials').style.display = 'none';
    document.getElementById('dungeondata').style.display = 'none';


    var actives = document.getElementsByClassName('is-active');
    for (i = 0; i < actives.length; i++) {
        if (actives[i].classList.contains('is-active')) {
            actives[i].classList.remove('is-active');
        }
    }
    document.getElementById('leadertab').classList.add('is-active');

    document.getElementById('leaderskill').style.display = '';
    document.getElementById('activeskill').style.display = '';

}


function showMonsterData() {

    document.getElementById('leaderskill').style.display = 'none';
    document.getElementById('activeskill').style.display = 'none';
    document.getElementById('evomaterials').style.display = 'none';
    document.getElementById('unevomaterials').style.display = 'none';

    var actives = document.getElementsByClassName('is-active');
    for (i = 0; i < actives.length; i++) {
        if (actives[i].classList.contains('is-active')) {
            actives[i].classList.remove('is-active');
        }
    }
    document.getElementById('monstertab').classList.add('is-active');

    document.getElementById('monsterdata').style.display = '';
    document.getElementById('dungeondata').style.display = '';


}


function showEvoData() {

    document.getElementById('leaderskill').style.display = 'none';
    document.getElementById('activeskill').style.display = 'none';
    document.getElementById('monsterdata').style.display = 'none';
    document.getElementById('dungeondata').style.display = 'none';

    var actives = document.getElementsByClassName('is-active');
    for (i = 0; i < actives.length; i++) {
        if (actives[i].classList.contains('is-active')) {
            actives[i].classList.remove('is-active');
        }
    }

    document.getElementById('evotab').classList.add('is-active');
    document.getElementById('evomaterials').style.display = '';
    document.getElementById('unevomaterials').style.display = '';


}

function hamburgerHelper() {
    var nav = document.getElementsByClassName('navbar-menu')[0];
    if (nav.classList.contains('is-active')) {
        nav.classList.remove('is-active');
    } else {
        nav.classList.add('is-active');
    }
}




