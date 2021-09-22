#alwin Wezenbeek 99060433

#in bezit van mbo4 diploma ondernemen

#in bezit van geldig rijbewijs

#in bezit van een hoge hoed

#langer dan 150cm

#is zwaarder dan 90kg

#heeft certificaat ''overleven met gevaarlijk personeel''

#is man EN heeft snor breder dan 10cm OF is vrouw EN draagt rood krulhaar langer dan 20cm


print('''        -------------------------------------------------------------
        |       Sollicitatie formulier ''circusdirecteur''          |
        -------------------------------------------------------------
        |er wordt u een aantal relevante vragen gesteld...          |
        |Gelieve die naar eer en geweten in te vullen.`             |
        |Als blijkt dat u aan de criteria voldoet dan               |
        |komt u in aanmerking voor een serieus sollicitatiegesprek! |
        |ontspan maar blijf wakker, hier komen de vragen.           |
        |------------------------------------------------------------
    ''')
naam = input('wat is uw naam?:')
geslacht = input('wat is uw geslacht?[M/V]')
if geslacht == 'M' or geslacht == 'm':
    snor = input('heeft u een snor die breder is dan 20cm?[Y/N]: ')
else:
    krulhaar = input('draagt u rood krulhaar dat langer is dan 20cm?[Y/N]: ')
nietaangenomen = ('beste'' ' + naam +','' ''helaas komt u niet in aanmerking tot een sollicitatiegesprek')
aangenomen = ('beste'' ' + naam +','' ''u komt in aanmerking tot een sollicitatiegesprek!')
ervaring_dieren = input('hoeveel jaar ervaring heeft u met dieren-dressuur?: ')
ervaring_jongleren = input('hoeveel jaar ervaring heeft u met jongleren?: ')
ervaring_acrobatiek = input('hoeveel jaar praktijkervaring heeft u in acrobatiek?: ')
diploma = input('bent u in bezit van een MBO4 diploma ondernemen?[Y/N]: ')
rijbewijs = input('bent u in bezit van een geldig vrachtwagen rijbewijs?[Y/N]: ')
hoed = input('bent u in bezit van een hoge hoed?[Y/N]: ')
lengte = input('hoelang bent u in cm: ')
gewicht = input('hoeveel weegt u in kg: ')
certificaat = input('''heeft u de certificaat ''overleven met gevaarlijk personeel''?[Y/N]: ''')

if (ervaring_dieren <= '4' or ervaring_jongleren <= '5' or ervaring_acrobatiek <= '3') and (diploma == 'Y' and rijbewijs == 'Y' and lengte <= '150' and gewicht <= '90' and hoed == 'Y'):
    print(aangenomen)
else:
    print(nietaangenomen)