from time import sleep
str1 = """Bless 'em and there ain't no stress
And this one is straight for di girldem
Enrique Iglesias 'longside Gente de Zona (Deceme)
Get di girl them in a di zone
And there's a Big Bone
Sean a-Paul a me deh ya what me tell 'em 'pon the throne
Lockin' it just like that
Di girldem dem move 'pon track
Sean a-P aul a me deh ya
Enrique, sing to dem, do it"""
str2 = str1.splitlines()

for i in str2:
    print(i)
    sleep(1)