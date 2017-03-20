from area import area
import random

obj = {"type": "Polygon", "coordinates": [
    [[30.51547659158315, 50.4505846849063], [30.515427327291547, 50.4505924341209],
     [30.515506240521276, 50.45079480303311], [30.515555408404854, 50.450787016749615],
     [30.515660994072732, 50.45105835881416], [30.516236566716373, 50.450967477707636],
     [30.51619565591572, 50.45086473822111], [30.516118066466213, 50.450877079921874],
     [30.51608420925188, 50.45079036988093], [30.516174495156765, 50.45077621849175],
     [30.516156155832334, 50.45072897908463], [30.516277477517022, 50.45070984907763],
     [30.516322620469463, 50.45066366817274], [30.516315566883147, 50.45064567165426],
     [30.516335316924838, 50.45064248943147], [30.51625067388901, 50.4504263901954],
     [30.516230923847317, 50.4504296338088], [30.516218227391942, 50.45039649358176],
     [30.516037655582174, 50.45042498895356], [30.5160249591268, 50.4503916157973],
     [30.51589940529032, 50.45041136647007], [30.515864137358722, 50.450321705421224],
     [30.5158260479926, 50.45022368629927], [30.5156934405698, 50.450244796497714],
     [30.51536429599658, 50.45029668755051], [30.51547659158315, 50.4505846849063]],
    [[30.51580065508185, 50.4507481853734], [30.515854262337875, 50.450883708317804],
     [30.515751279977618, 50.450899887620245], [30.515699083438857, 50.45076430208944],
     [30.51580065508185, 50.4507481853734]],
    [[30.515561461214947, 50.450411069468174], [30.51566381550726, 50.45039488964269],
     [30.51572306563234, 50.450545853131494], [30.515620328401827, 50.45056197024613],
     [30.515561461214947, 50.450411069468174]]]}

obj1 = {'type': 'Polygon',
        'coordinates': [[[30.515347369976766, 50.45619438968216], [30.51523672689217, 50.45613371931523],
                         [30.51508331169045, 50.45607707229428], [30.51494567779895, 50.456043315568365],
                         [30.514745312986207, 50.456023895118726], [30.514568376152457, 50.456027740934225],
                         [30.51447763268961, 50.45604620634238], [30.51440495890472, 50.45606091676711],
                         [30.514267417495834, 50.456106482858246], [30.514170430248615, 50.45615317008443],
                         [30.51403560244305, 50.456199751264464], [30.51389463554477, 50.4562054862527],
                         [30.513724308015533, 50.456178476693196], [30.51355830206563, 50.45615074521304],
                         [30.5134067311604, 50.45613566295133], [30.51326734502298, 50.456139663234495],
                         [30.51309632766566, 50.45615298953356], [30.51293636266572, 50.456182649632254],
                         [30.51281483086917, 50.45621525581116], [30.512689664649873, 50.45626775331907],
                         [30.512536661419354, 50.456333898578734], [30.512394727574478, 50.456380014597315],
                         [30.5122375606421, 50.45641086062588], [30.51211804460242, 50.45640566577617],
                         [30.512007389944564, 50.456375116291625], [30.511747805653123, 50.456298739420625],
                         [30.511592473911886, 50.45626683726583], [30.511436237108065, 50.456262818825884],
                         [30.511288041381498, 50.4562699441002], [30.51114969101841, 50.456296728788985],
                         [30.511053220733412, 50.456305497700804], [30.51097992262328, 50.4562935001653],
                         [30.51091894501023, 50.45625189691516], [30.510899145565556, 50.45618633548316],
                         [30.510866318779982, 50.45605555085569], [30.51083667827033, 50.4559842869076],
                         [30.510768026047487, 50.455933865149845], [30.510697628865845, 50.45589879436232],
                         [30.51059412329022, 50.455858969955905], [30.510447098622866, 50.455818518585666],
                         [30.51026153277265, 50.4557789951161], [30.510141749998144, 50.45576337661215],
                         [30.509890183669107, 50.455730287273084], [30.509597438529124, 50.45571766794003],
                         [30.50945991285236, 50.455726867844234], [30.50936165073085, 50.45571867401289],
                         [30.509299055737056, 50.45566613741485], [30.509272595547596, 50.45561942471103],
                         [30.509197551521904, 50.45561038934027], [30.50919492475297, 50.45565736999645],
                         [30.509182178697834, 50.45565707695745], [30.509176489806414, 50.455760739866555],
                         [30.508905592124123, 50.45575460971265], [30.508744746900614, 50.455751008764544],
                         [30.508675991465903, 50.45574942519344], [30.508653685409435, 50.45574889270005],
                         [30.50865738609851, 50.45580192104204], [30.50836498423966, 50.45591631081912],
                         [30.50841071805287, 50.455975481320934], [30.508459929109815, 50.45602645562108],
                         [30.508322718939855, 50.456080092524175], [30.508366068598345, 50.45615041629709],
                         [30.508435618934723, 50.456462813642375], [30.50835497732439, 50.45655181034985],
                         [30.507372999289757, 50.456828511052315], [30.50713580098862, 50.45694081409273],
                         [30.50716140928792, 50.456986628172224], [30.507174965691977, 50.45700998436961],
                         [30.507185274217623, 50.45700818773904], [30.507325172404766, 50.457277682324275],
                         [30.507368567116018, 50.45732888629547], [30.50736911177773, 50.45750315946059],
                         [30.50713566146043, 50.45744207402127], [30.507036188896418, 50.45737290374439],
                         [30.50660151189686, 50.45750136283002], [30.506531024750263, 50.45751573587457],
                         [30.506620185561633, 50.45765138148247], [30.515347369976766, 50.45619438968216]]]}

print(area(obj1))

north = [30.50562143325806, 50.45781822317228]
east = [30.519477725028995, 50.45550434421866]
south = [30.515277385711673, 50.44530143532968]
west = [30.501423776149753, 50.44761581331231]

mapsquare = {'type': 'Polygon', 'coordinates': [[north, west, south, east]]}
print(mapsquare)
print(area(mapsquare))

total_area = 1192034.29215 - 47050.347984
total_area = 1144983.94417



