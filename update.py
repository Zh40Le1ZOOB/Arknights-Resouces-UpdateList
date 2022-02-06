import oss2, json
with open('H:/RhodeIslandRT/oss_res_table.json', 'r', encoding='utf-8') as f1, open('H:/RhodeIslandRT/activity_table.json', 'r', encoding='utf-8') as f2:
    oss_res_table: dict = json.load(f1)
    activity_table: dict = json.load(f2)
bucket = oss2.Bucket(oss2.AnonymousAuth(), 'http://{}'.format(oss_res_table['ossServerEndPoint']), oss_res_table['ossServerBucket'])
for activity in oss_res_table['activities'].keys():
    name = activity_table['basicInfo'][activity]['name'] if activity in activity_table['basicInfo'].keys() else None
    oss_res_table['activities'][activity]['name'] = name
    official_exist = bucket.object_exists('assetbundle/official/Android/assets/{}/hot_update_list.json'.format(oss_res_table['activities'][activity]['resVersion']))
    oss_res_table['activities'][activity]['officialExist'] = official_exist
    bilibili_exist = bucket.object_exists('assetbundle/bilibili/Android/assets/{}/hot_update_list.json'.format(oss_res_table['activities'][activity]['resVersion']))
    oss_res_table['activities'][activity]['bilibiliExist'] = bilibili_exist
    print('{:<16}{:<5}{:<5}{}'.format(activity, official_exist, bilibili_exist, name))
with open('H:/RhodeIslandRT/oss_res_table.json', 'w', encoding='utf-8') as f:
    json.dump(oss_res_table, f, indent=4, ensure_ascii=False)
