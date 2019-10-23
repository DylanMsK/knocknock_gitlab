import csv

from stores.models import Category, Option, Store

def run():
    with open('/Users/dylan/Desktop/github/s1p1151009/data/강남구_한식_상세.csv', 'r', encoding='utf8') as f:
        reader = csv.DictReader(f)
        fields = ['id', 'name', 'businessCategory', 'category', 'desc', 'x', 'y', 'imageSrc', 'phone',
                  'roadAddr', 'commonAddr', 'addr', 'tags', 'options', 'totalReviewCount', 'priceCategory']
        category = Category.objects.get(sub_category='한식')
        for row in reader:
            # print(row)
            origin_id = row['id']
            name = row['name']
            description = row['desc']
            lon = row['x']
            lat = row['y']
            thumbnail = row['imageSrc']
            contact = row['phone']
            road_addr = row['roadAddr']
            common_addr = row['commonAddr']
            addr = row['addr']
            if row['priceCategory']:
                price_avg = int(row['priceCategory'].split('만원 대')[0] + '0000')
            else:
                price_avg = 0

            if row['totalReviewCount']:
                review_cnt = int(''.join(row['totalReviewCount'].split(',')))
            else:
                review_cnt = 0
            if row['tags']:
                tags = ','.join([tag for tag in eval(row['tags'])])
            else:
                tags = ''
            store = Store.objects.create(origin_id=origin_id, name=name, category=category, description=description, lon=lon, lat=lat,
                          thumbnail=thumbnail, contact=contact, road_addr=road_addr, common_addr=common_addr,
                          addr=addr, tags=tags, price_avg=price_avg, review_cnt=review_cnt)
            for option in row['options'].split(','):
                if option in ['예약', '단체석', '주차', '포장', '배달']:
                    opt = Option.objects.get(name=option)
                    store.options.add(opt)
            store.save()
        