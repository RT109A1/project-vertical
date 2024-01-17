import pickle
## Обозначения переменных
VAR_RES_workers = 0
VAR_RES_dependents = 0
VAR_RES_security = 0
VAR_RES_steel = 0
VAR_RES_wood = 0
VAR_RES_concrete = 0
VAR_RES_special_metals = 0
VAR_RES_civilian_goods = 0
VAR_RES_food = 0
VAR_RES_alcohol = 0
VAR_RES_lightweapons = 0
VAR_RES_advweapons = 0
VAR_RES_happiness = 75
VAR_RES_loyalty = 95
VAR_RES_steel_change = 1
VAR_RES_wood_change = 3
VAR_RES_concrete_change = 4
VAR_RES_special_metals_change = 3
VAR_RES_civilian_goods_change = 5
VAR_RES_food_change = 6
VAR_RES_alcohol_change = 2
VAR_RES_cycle = 7
LIST_events = []
for i in range(20):
    LIST_events.append(0)
LIST_resources = [1111111, VAR_RES_workers, VAR_RES_dependents, VAR_RES_security, VAR_RES_steel, VAR_RES_wood, VAR_RES_concrete, VAR_RES_special_metals,
                  VAR_RES_civilian_goods, VAR_RES_food, VAR_RES_alcohol, VAR_RES_lightweapons, VAR_RES_advweapons, VAR_RES_cycle, VAR_RES_happiness, VAR_RES_loyalty,
                  VAR_RES_steel_change, VAR_RES_wood_change, VAR_RES_concrete_change, VAR_RES_special_metals_change, VAR_RES_civilian_goods_change,
                  VAR_RES_food_change, VAR_RES_alcohol_change, LIST_events]
LIST_all_saves = [LIST_resources]
with open('saves.sfh', 'wb') as file:
    pickle.dump(LIST_all_saves, file)