from fake_useragent import UserAgent
import requests
import json

ua = UserAgent()

#brand=17%2C2986
def collect_data(max_price, cfg_brand):
    offset = 0
    batch_size = 72
    result = []
    while True:
        for item in range(offset, offset+batch_size, 72):
            url = f"https://www.asos.com/api/product/search/v2/?attribute_1047=8606&" \
                  f"brand={cfg_brand}&channel=desktop-web&country=RU&currency=RUB&" \
                  f"floor=1000%2C1001&keyStoreDataversion=hgk0y12-29&lang=ru-RU&" \
                  f"limit=72&offset={item}&priceMax={max_price}&priceMin=3000&" \
                  f"q=%D0%BA%D1%80%D0%BE%D1%81%D1%81%D0%BE%D0%B2%D0%BA%D0%B8&rowlength=4&store=RU"
            res = requests.get(
                url=url,
                headers={"user-agent": f"ua.random"}
            )

            offset += batch_size

            data = res.json()
            items = data.get("products")
            for i in items:
                if i.get("price").get("rrp").get("value") is not None \
                        and i.get("price").get("previous").get("value") is not None:
                    item_full_name = i.get("name")
                    item_brand = i.get("brandName")
                    item_url = i.get("url")
                    item_curr_price = int(i.get("price").get("current").get("value"))
                    item_previous_price = int(i.get("price").get("rrp").get("value"))
                    item_sale = round(((item_previous_price - item_curr_price) / item_previous_price) * 100)

                    result.append(
                        {
                            "full_name": item_full_name,
                            "brand": item_brand,
                            "url": "https://www.asos.com/ru/" + item_url,
                            "current_price": item_curr_price,
                            "privious_price": item_previous_price,
                            "sale": item_sale
                        }
                    )
        if len(items) < 71:
            break
    # print(f"Записано {len(result)} вещь/вещей")
    with open("result.json", "w", encoding="utf-8") as file:
        json.dump(result, file, indent=4, ensure_ascii=False)



def main():
    collect_data()


if __name__ == "__main__":
    main()
