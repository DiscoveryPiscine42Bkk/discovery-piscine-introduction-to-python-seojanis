def jennieboat(family):
    return list(filter(lambda name: family[name] == "boat", family.keys()))
    
    dupont_family = {
        "boat": "boat",
        "jennie": "jennie",
        "mairu": "tem",
        "nakharin": "boat",
        "jenjira": "jennie"
    }

    print(jennieboat(dupont_family))