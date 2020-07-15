def get_gemstone(date):
    gemstone = {
        '01': {'stone': 'Garnet', 'img': '', 'desc': 'The name “garnet” comes from the Latin word “Garanatus,” meaning “seedlike,” in reference to a pomegranate. This reference makes sense as small garnets look like the bright red seeds you find inside in a pomegranate.'},
        '02': {'stone': 'Amethyst', 'img': '', 'desc': ''},
        '03': {'stone': 'Aquamarine', 'img': '', 'desc': ''},
        '04': {'stone': 'Diamond', 'img': '', 'desc': ''},
        '05': {'stone': 'Emerald', 'img': '', 'desc': ''},
        '06':  {'stone': 'Pearl', 'img': '', 'desc': ''},
        '07': {'stone': 'Ruby', 'img': '', 'desc': ''},
        '08': {'stone': 'Peridot', 'img': '', 'desc': ''},
        '09': {'stone': 'Sapphire', 'img': 'https://www.gemselect.com/photos/sapphire/sapphire-gem-512881a.jpg', 'desc': 'Sapphire is a precious gemstone, a variety of the mineral corundum, consisting of aluminum oxide (α-Al2O3) with trace amounts of elements such as iron, titanium, chromium, vanadium, or magnesium.'},
        '10': {'stone': 'Opal', 'img': 'https://cfbrandtjewelers.com/wp-content/uploads/2017/10/OPAL.jpg', 'desc': 'Opal is a hydrated amorphous form of silica (SiO2·nH2O); its water content may range from 3 to 21% by weight, but is usually between 6 and 10%. Because of its amorphous character, it is classed as a mineraloid, unlike crystalline forms of silica, which are classed as minerals. It is deposited at a relatively low temperature and may occur in the fissures of almost any kind of rock, being most commonly found with limonite, sandstone, rhyolite, marl, and basalt.'},
        '11': {'stone': 'Citrine', 'img': 'https://www.angara.com/blog/wp-content/uploads/2013/11/Historical-Timeline-of-Citrine.jpg', 'desc': 'Citrine is a variety of quartz whose color ranges from a pale yellow to brown due to ferric impurities. Natural citrines are rare; most commercial citrines are heat-treated amethysts or smoky quartzes.'},
        '12': {'stone': 'Topaz', 'img': "https://df2sm3urulav.cloudfront.net/tenants/gr/uploads/images/895000-899999/896154/5c85a0f5887da.jpg", 'desc': "Topaz is a silicate mineral of aluminium and fluorine with the chemical formula Al2SiO4(F, OH)2. Topaz crystallizes in the orthorhombic system, and its crystals are mostly prismatic terminated by pyramidal and other faces. It is one of the hardest naturally occurring minerals (Mohs hardness of 8) and is the hardest of any silicate mineral. This hardness combined with its usual transparency and variety of colors means that it has acquired wide use in jewellery as a cut gemstone as well as for intaglios and other gemstone carvings."}
    }

    gem = gemstone[date[5:7]]

    info = {
        'stone': gem['stone'],
        'img': gem['img'],
        'desc': gem['desc']
    }

    return info
