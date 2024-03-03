end = ""
while(end != "nein"):
    einwohner = {"berlin" : 3_677_472, 
    "hamburg" : 1_853_935, 
    "münchen" : 1_487_708,
    "köln" : 1_073_096,
    "frankfurt" : 759_224,
    "stuttgart" : 626_275,
    "düsseldorf" : 619_477,
    "leipzig" : 601_866,
    "dortmund" : 586_852,
    "essen" : 579_432,
    "bremen" : 563_290,
    "dresden" : 555_351,
    "hannover" : 535_932,
    "nürnberg" : 510_632,
    "duisburg" : 495_152,
    "bochum" : 363_441,
    "wuppertal" : 354_572,
    "bielefeld" : 334_002,
    "bonn" : 331_885,
    "münster" : 317_713,
    "mannheim" : 311_831,
    "karlsruhe" : 306_502,
    "augsburg" : 296_478,
    "wiesbaden" : 278_950,
    "mönchengladbach" : 261_001,
    "muenchen": 1_487_708,
    "koeln": 1_073_096,
    "duesseldorf": 619_477,
    "nuernberg": 510_632,
    "moenchengladbach": 261_001}
    city = input("Welche Stadt? ")
    city = city.lower()
    if einwohner.get(city) == None:
        print("Diese Stadt gehört nicht zu den 25 einwohnerreichsten.")
    else:
        print(f"{city.title()} hat {einwohner[city]} Einwohner.")
    end = input("Möchtest du noch eine Stadt abfragen? (ja/nein) ")
print("Danke fürs Benutzen!")