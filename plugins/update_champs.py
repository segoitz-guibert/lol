# -*- coding: utf-8 -*-

from config import *
import requests

print(Color(
    '{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  update_champs.py importado.{/cyan}'))


def static_get_champion_list(region, data_by_id, locale=None, champ_data=None, lol_api=extra['lol_api']):
    url = "https://{}.api.riotgames.com/lol/static-data/v3/champions".format(
        update_region(region))
    params = {
        "tags": champ_data,
        "dataById": "true" if data_by_id else "false",
        "locale": locale,
        "api_key": lol_api
    }
    r = requests.get(url, params)
    return r.json()


@bot.message_handler(commands=['update_champs_1'])
def command_update_champs_1(m):
    cid = m.chat.id
    uid = m.from_user.id
    try:
        send_udp('update_champs_1')
    except Exception as e:
        bot.send_message(52033876, send_exception(e), parse_mode="Markdown")
    if not is_recent(m):
        return None
    if is_admin(uid):
        lol_api = extra['lol_api'] if len(m.text.split()) == 1 else m.text.split()[1]
        msg = bot.send_message(
            cid,
            "Descargando nuevas bases de datos de campeones:\n`-Español`\n`-Inglés`\n`-Italiano`\n`-Alemán`\n`-Francés`\n`-Rumano`",
            parse_mode="Markdown")
        try:
            aux = {
                "champs_es.json": static_get_champion_list(
                    region='euw',
                    locale='es_ES',
                    champ_data=['all'],
                    data_by_id=False,
                    lol_api=lol_api)['data'],
                "champs_en.json": static_get_champion_list(
                    region='na',
                    locale='en_US',
                    champ_data=['all'],
                    data_by_id=False,
                    lol_api=lol_api)['data'],
                "champs_it.json": static_get_champion_list(
                    region='eune',
                    locale='it_IT',
                    champ_data=['all'],
                    data_by_id=False,
                    lol_api=lol_api)['data'],
                "champs_de.json": static_get_champion_list(
                    region='na',
                    locale='de_DE',
                    champ_data=['all'],
                    data_by_id=False,
                    lol_api=lol_api)['data'],
                "champs_fr.json": static_get_champion_list(
                    region='eune',
                    locale='fr_FR',
                    champ_data=['all'],
                    data_by_id=False,
                    lol_api=lol_api)['data'],
                "champs_ro.json": static_get_champion_list(
                    region='eune',
                    locale='ro_RO',
                    champ_data=['all'],
                    data_by_id=False,
                    lol_api=lol_api)['data']
            }
        except:
            # bot.send_message(cid, "Error descargando nuevas bases de datos.")
            bot.edit_message_text(
                "Error descargando nuevas bases de datos.",
                cid,
                msg.message_id)
            return
        # bot.send_message(cid, "Bases de datos descargadas.\n\n`" + '\n'.join([i for i in aux]) + "`", parse_mode="Markdown")
        bot.edit_message_text("Bases de datos descargadas.\n\n`" +
                              '\n'.join([i for i in aux]) +
                              "`", cid, msg.message_id, parse_mode="Markdown")
        # bot.send_message(cid, "Actualizando archivos...")
        bot.edit_message_text("Actualizando archivos...", cid, msg.message_id)
        try:
            for x in aux:
                with open(x, 'w') as f:
                    json.dump(aux[x], f, indent=4)
        except:
            # bot.send_message(cid, "Error actualizando archivos.")
            bot.edit_message_text(
                "Error actualizando archivos.", cid, msg.message_id)
            return

        # bot.send_message(cid, "Archivos actualizados correctamente.")
        bot.edit_message_text(
            "Archivos actualizados correctamente.",
            cid,
            msg.message_id)
        # bot.send_message(cid, "Reiniciando bot...")
        bot.edit_message_text("Reiniciando bot...", cid, msg.message_id)
        exit()


@bot.message_handler(commands=['update_champs_2'])
def command_update_champs_2(m):
    cid = m.chat.id
    uid = m.from_user.id
    try:
        send_udp('update_champs_2')
    except Exception as e:
        bot.send_message(52033876, send_exception(e), parse_mode="Markdown")
    if not is_recent(m):
        return None
    if is_admin(uid):
        lol_api = extra['lol_api'] if len(m.text.split()) == 1 else m.text.split()[1]
        msg = bot.send_message(
            cid,
            "Descargando nuevas bases de datos de campeones:\n`-Polaco`\n`-Portugués`\n`-Griego`\n`-Ruso`\n`-Tailandés`\n`-Turco`",
            parse_mode="Markdown")
        try:
            aux = {
                "champs_pl.json": static_get_champion_list(
                    region='na',
                    locale='pl_PL',
                    champ_data=['all'],
                    data_by_id=False,
                    lol_api=lol_api)['data'],
                "champs_pt.json": static_get_champion_list(
                    region='euw',
                    locale='pt_BR',
                    champ_data=['all'],
                    data_by_id=False,
                    lol_api=lol_api)['data'],
                "champs_el.json": static_get_champion_list(
                    region='na',
                    locale='el_GR',
                    champ_data=['all'],
                    data_by_id=False,
                    lol_api=lol_api)['data'],
                "champs_ru.json": static_get_champion_list(
                    region='na',
                    locale='ru_RU',
                    champ_data=['all'],
                    data_by_id=False,
                    lol_api=lol_api)['data'],
                "champs_th.json": static_get_champion_list(
                    region='eune',
                    locale='th_TH',
                    champ_data=['all'],
                    data_by_id=False,
                    lol_api=lol_api)['data'],
                "champs_tr.json": static_get_champion_list(
                    region='na',
                    locale='tr_TR',
                    champ_data=['all'],
                    data_by_id=False,
                    lol_api=lol_api)['data']}
        except:
            # bot.send_message(cid, "Error descargando nuevas bases de datos.")
            bot.edit_message_text(
                "Error descargando nuevas bases de datos.",
                cid,
                msg.message_id)
            return
        # bot.send_message(cid, "Bases de datos descargadas.\n\n`" + '\n'.join([i for i in aux]) + "`", parse_mode="Markdown")
        bot.edit_message_text("Bases de datos descargadas.\n\n`" +
                              '\n'.join([i for i in aux]) +
                              "`", cid, msg.message_id, parse_mode="Markdown")
        # bot.send_message(cid, "Actualizando archivos...")
        bot.edit_message_text("Actualizando archivos...", cid, msg.message_id)
        try:
            for x in aux:
                with open(x, 'w') as f:
                    json.dump(aux[x], f, indent=4)
        except:
            # bot.send_message(cid, "Error actualizando archivos.")
            bot.edit_message_text(
                "Error actualizando archivos.", cid, msg.message_id)
            return

        # bot.send_message(cid, "Archivos actualizados correctamente.")
        bot.edit_message_text(
            "Archivos actualizados correctamente.",
            cid,
            msg.message_id)
        # bot.send_message(cid, "Reiniciando bot...")
        bot.edit_message_text("Reiniciando bot...", cid, msg.message_id)
        exit()


@bot.message_handler(commands=['update_champs_keys'])
def command_update_champs_keys(m):
    cid = m.chat.id
    uid = m.from_user.id
    try:
        send_udp('update_champs_2')
    except Exception as e:
        bot.send_message(52033876, send_exception(e), parse_mode="Markdown")
    if not is_recent(m):
        return None
    if is_admin(uid):
        msg = bot.send_message(
            cid,
            "Actualizando fichero `champs_keys.json` ...",
            parse_mode="Markdown")
        try:
            req = static_get_champion_list(
                region='euw', data_by_id=True)['data']
        except:
            bot.edit_message_text(
                "Error descargando el fichero.", cid, msg.message_id)
            return
        with open('champs_keys.json', 'w') as f:
            json.dump(req, f, indent=4)
        bot.edit_message_text("Éxito. Reiniciando bot...", cid, msg.message_id)
        exit()
