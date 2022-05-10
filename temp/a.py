raw = '''
{{
  picture:
    '../img/logo.png',
  name: \'{}\',
  type: \'{}\',
}},
'''


d = {"list": [{"model": "hydrogen.artists", "pk": 28, "fields": {"name": "Czech"}}, {"model": "hydrogen.artists", "pk": 25, "fields": {"name": "Czech Philharmonic Orchestra"}}, {"model": "hydrogen.artists", "pk": 29, "fields": {"name": "Czech/Gavin/Lindsey"}}, {"model": "hydrogen.artists", "pk": 30, "fields": {"name": "DJ Project"}}, {"model": "hydrogen.artists", "pk": 34, "fields": {"name": "DJ Project/Giulia/Huiban Gabriel"}}, {"model": "hydrogen.artists", "pk": 35, "fields": {"name": "Feint"}}, {"model": "hydrogen.artists", "pk": 38, "fields": {"name": "Feint/Leah Rye/Rameses B"}}, {"model": "hydrogen.artists", "pk": 39, "fields": {"name": "Flipsyde"}}, {"model": "hydrogen.artists", "pk": 40, "fields": {"name": "Flipsyde/t.A.T.u."}}, {"model": "hydrogen.artists", "pk": 13, "fields": {"name": "Flo Rida"}}, {"model": "hydrogen.artists", "pk": 16, "fields": {"name": "Flo Rida/Robin Thicke/Verdine White"}}, {"model": "hydrogen.artists", "pk": 18, "fields": {"name": "Flo Rida/Sage the Gemini"}}, {"model": "hydrogen.artists", "pk": 20, "fields": {"name": "Flo Rida/Wynter Gordon"}}, {"model": "hydrogen.artists", "pk": 27, "fields": {"name": "Gavin"}}, {"model": "hydrogen.artists", "pk": 24, "fields": {"name": "Gavin Greenaway"}}, {"model": "hydrogen.artists", "pk": 32, "fields": {"name": "Giulia"}}, {"model": "hydrogen.artists", "pk": 23, "fields": {"name": "Greyson Chance"}}, {"model": "hydrogen.artists", "pk": 33, "fields": {"name": "Huiban Gabriel"}}, {"model": "hydrogen.artists", "pk": 37, "fields": {"name": "Leah Rye"}}, {"model": "hydrogen.artists", "pk": 26, "fields": {"name": "Lindsey"}}, {"model": "hydrogen.artists", "pk": 22, "fields": {"name": "Lindsey Stirling"}}, {"model": "hydrogen.artists", "pk": 36, "fields": {"name": "Rameses B"}}, {"model": "hydrogen.artists", "pk": 15, "fields": {"name": "Robin Thicke"}}, {"model": "hydrogen.artists", "pk": 17, "fields": {"name": "Sage the Gemini"}}, {"model": "hydrogen.artists", "pk": 12, "fields": {"name": "Selena Gomez & The Scene"}}, {"model": "hydrogen.artists", "pk": 31, "fields": {"name": "t.A.T.u."}}, {"model": "hydrogen.artists", "pk": 14, "fields": {"name": "Verdine White"}}, {"model": "hydrogen.artists", "pk": 19, "fields": {"name": "Wynter Gordon"}}, {"model": "hydrogen.artists", "pk": 21, "fields": {"name": "Yael Na\u00efm"}}], "msg": "success", "err_num": 0}
art = sorted(d['list'], key=lambda g: g['fields']['name'])
with open('temp.txt', 'w') as file:
    for arf in art:
        ar=arf['fields']
        file.write(raw.format(ar['name'], 'Group' if '/' in ar['name']else 'Individual'))

art_name[]