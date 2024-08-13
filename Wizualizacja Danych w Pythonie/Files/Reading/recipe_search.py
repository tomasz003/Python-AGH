def search_by_name(filename: str, word: str):
    f=open(filename, 'r')
    all_names=[]

    with open(filename) as f:
        temp=f.read()
        temp=temp.replace('\n',';')
        #temp - string separated with ";", 2 enters=";;"
        big_list=temp.split(';;')
        #big_list - list of strings (one string = one dish)
        for i in big_list:
            one_recipe=i.split(';')
            #one_recipe - list for one dish
            if word.lower() in one_recipe[0].lower():
                 all_names.append(one_recipe[0])

    return all_names

def search_by_time(filename: str, prep_time: int):
    f=open(filename, 'r')
    meal_and_time={}

    with open(filename) as f:
        temp=f.read()
        temp=temp.replace('\n',';')
        big_list=temp.split(';;')
        for i in big_list:
            one_recipe=i.split(';')
            if int(one_recipe[1])<=prep_time:
                meal_and_time[one_recipe[0]]=one_recipe[1]

    return [f'{x}, preparation time {meal_and_time[x]} min' for x in meal_and_time.keys()]

def search_by_ingredient(filename: str, ingredient: str):
    f=open(filename, 'r')
    meals_with_ingr={}

    with open(filename) as f:
        temp=f.read()
        temp=temp.replace('\n',';')
        big_list=temp.split(';;')
        for i in big_list:
            one_recipe=i.split(';')
            if ingredient in one_recipe:
                meals_with_ingr[one_recipe[0]]=one_recipe[1]
    return [f'{x}, preparation time {meals_with_ingr[x]} min' for x in meals_with_ingr.keys()]
