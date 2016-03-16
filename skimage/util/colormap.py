from matplotlib.colors import LinearSegmentedColormap
from matplotlib import cm

viridis_data = [[ 0.26700401,  0.00487433,  0.32941519],
       [ 0.26851048,  0.00960483,  0.33542652],
       [ 0.26994384,  0.01462494,  0.34137895],
       [ 0.27130489,  0.01994186,  0.34726862],
       [ 0.27259384,  0.02556309,  0.35309303],
       [ 0.27380934,  0.03149748,  0.35885256],
       [ 0.27495242,  0.03775181,  0.36454323],
       [ 0.27602238,  0.04416723,  0.37016418],
       [ 0.2770184 ,  0.05034437,  0.37571452],
       [ 0.27794143,  0.05632444,  0.38119074],
       [ 0.27879067,  0.06214536,  0.38659204],
       [ 0.2795655 ,  0.06783587,  0.39191723],
       [ 0.28026658,  0.07341724,  0.39716349],
       [ 0.28089358,  0.07890703,  0.40232944],
       [ 0.28144581,  0.0843197 ,  0.40741404],
       [ 0.28192358,  0.08966622,  0.41241521],
       [ 0.28232739,  0.09495545,  0.41733086],
       [ 0.28265633,  0.10019576,  0.42216032],
       [ 0.28291049,  0.10539345,  0.42690202],
       [ 0.28309095,  0.11055307,  0.43155375],
       [ 0.28319704,  0.11567966,  0.43611482],
       [ 0.28322882,  0.12077701,  0.44058404],
       [ 0.28318684,  0.12584799,  0.44496   ],
       [ 0.283072  ,  0.13089477,  0.44924127],
       [ 0.28288389,  0.13592005,  0.45342734],
       [ 0.28262297,  0.14092556,  0.45751726],
       [ 0.28229037,  0.14591233,  0.46150995],
       [ 0.28188676,  0.15088147,  0.46540474],
       [ 0.28141228,  0.15583425,  0.46920128],
       [ 0.28086773,  0.16077132,  0.47289909],
       [ 0.28025468,  0.16569272,  0.47649762],
       [ 0.27957399,  0.17059884,  0.47999675],
       [ 0.27882618,  0.1754902 ,  0.48339654],
       [ 0.27801236,  0.18036684,  0.48669702],
       [ 0.27713437,  0.18522836,  0.48989831],
       [ 0.27619376,  0.19007447,  0.49300074],
       [ 0.27519116,  0.1949054 ,  0.49600488],
       [ 0.27412802,  0.19972086,  0.49891131],
       [ 0.27300596,  0.20452049,  0.50172076],
       [ 0.27182812,  0.20930306,  0.50443413],
       [ 0.27059473,  0.21406899,  0.50705243],
       [ 0.26930756,  0.21881782,  0.50957678],
       [ 0.26796846,  0.22354911,  0.5120084 ],
       [ 0.26657984,  0.2282621 ,  0.5143487 ],
       [ 0.2651445 ,  0.23295593,  0.5165993 ],
       [ 0.2636632 ,  0.23763078,  0.51876163],
       [ 0.26213801,  0.24228619,  0.52083736],
       [ 0.26057103,  0.2469217 ,  0.52282822],
       [ 0.25896451,  0.25153685,  0.52473609],
       [ 0.25732244,  0.2561304 ,  0.52656332],
       [ 0.25564519,  0.26070284,  0.52831152],
       [ 0.25393498,  0.26525384,  0.52998273],
       [ 0.25219404,  0.26978306,  0.53157905],
       [ 0.25042462,  0.27429024,  0.53310261],
       [ 0.24862899,  0.27877509,  0.53455561],
       [ 0.2468114 ,  0.28323662,  0.53594093],
       [ 0.24497208,  0.28767547,  0.53726018],
       [ 0.24311324,  0.29209154,  0.53851561],
       [ 0.24123708,  0.29648471,  0.53970946],
       [ 0.23934575,  0.30085494,  0.54084398],
       [ 0.23744138,  0.30520222,  0.5419214 ],
       [ 0.23552606,  0.30952657,  0.54294396],
       [ 0.23360277,  0.31382773,  0.54391424],
       [ 0.2316735 ,  0.3181058 ,  0.54483444],
       [ 0.22973926,  0.32236127,  0.54570633],
       [ 0.22780192,  0.32659432,  0.546532  ],
       [ 0.2258633 ,  0.33080515,  0.54731353],
       [ 0.22392515,  0.334994  ,  0.54805291],
       [ 0.22198915,  0.33916114,  0.54875211],
       [ 0.22005691,  0.34330688,  0.54941304],
       [ 0.21812995,  0.34743154,  0.55003755],
       [ 0.21620971,  0.35153548,  0.55062743],
       [ 0.21429757,  0.35561907,  0.5511844 ],
       [ 0.21239477,  0.35968273,  0.55171011],
       [ 0.2105031 ,  0.36372671,  0.55220646],
       [ 0.20862342,  0.36775151,  0.55267486],
       [ 0.20675628,  0.37175775,  0.55311653],
       [ 0.20490257,  0.37574589,  0.55353282],
       [ 0.20306309,  0.37971644,  0.55392505],
       [ 0.20123854,  0.38366989,  0.55429441],
       [ 0.1994295 ,  0.38760678,  0.55464205],
       [ 0.1976365 ,  0.39152762,  0.55496905],
       [ 0.19585993,  0.39543297,  0.55527637],
       [ 0.19410009,  0.39932336,  0.55556494],
       [ 0.19235719,  0.40319934,  0.55583559],
       [ 0.19063135,  0.40706148,  0.55608907],
       [ 0.18892259,  0.41091033,  0.55632606],
       [ 0.18723083,  0.41474645,  0.55654717],
       [ 0.18555593,  0.4185704 ,  0.55675292],
       [ 0.18389763,  0.42238275,  0.55694377],
       [ 0.18225561,  0.42618405,  0.5571201 ],
       [ 0.18062949,  0.42997486,  0.55728221],
       [ 0.17901879,  0.43375572,  0.55743035],
       [ 0.17742298,  0.4375272 ,  0.55756466],
       [ 0.17584148,  0.44128981,  0.55768526],
       [ 0.17427363,  0.4450441 ,  0.55779216],
       [ 0.17271876,  0.4487906 ,  0.55788532],
       [ 0.17117615,  0.4525298 ,  0.55796464],
       [ 0.16964573,  0.45626209,  0.55803034],
       [ 0.16812641,  0.45998802,  0.55808199],
       [ 0.1666171 ,  0.46370813,  0.55811913],
       [ 0.16511703,  0.4674229 ,  0.55814141],
       [ 0.16362543,  0.47113278,  0.55814842],
       [ 0.16214155,  0.47483821,  0.55813967],
       [ 0.16066467,  0.47853961,  0.55811466],
       [ 0.15919413,  0.4822374 ,  0.5580728 ],
       [ 0.15772933,  0.48593197,  0.55801347],
       [ 0.15626973,  0.4896237 ,  0.557936  ],
       [ 0.15481488,  0.49331293,  0.55783967],
       [ 0.15336445,  0.49700003,  0.55772371],
       [ 0.1519182 ,  0.50068529,  0.55758733],
       [ 0.15047605,  0.50436904,  0.55742968],
       [ 0.14903918,  0.50805136,  0.5572505 ],
       [ 0.14760731,  0.51173263,  0.55704861],
       [ 0.14618026,  0.51541316,  0.55682271],
       [ 0.14475863,  0.51909319,  0.55657181],
       [ 0.14334327,  0.52277292,  0.55629491],
       [ 0.14193527,  0.52645254,  0.55599097],
       [ 0.14053599,  0.53013219,  0.55565893],
       [ 0.13914708,  0.53381201,  0.55529773],
       [ 0.13777048,  0.53749213,  0.55490625],
       [ 0.1364085 ,  0.54117264,  0.55448339],
       [ 0.13506561,  0.54485335,  0.55402906],
       [ 0.13374299,  0.54853458,  0.55354108],
       [ 0.13244401,  0.55221637,  0.55301828],
       [ 0.13117249,  0.55589872,  0.55245948],
       [ 0.1299327 ,  0.55958162,  0.55186354],
       [ 0.12872938,  0.56326503,  0.55122927],
       [ 0.12756771,  0.56694891,  0.55055551],
       [ 0.12645338,  0.57063316,  0.5498411 ],
       [ 0.12539383,  0.57431754,  0.54908564],
       [ 0.12439474,  0.57800205,  0.5482874 ],
       [ 0.12346281,  0.58168661,  0.54744498],
       [ 0.12260562,  0.58537105,  0.54655722],
       [ 0.12183122,  0.58905521,  0.54562298],
       [ 0.12114807,  0.59273889,  0.54464114],
       [ 0.12056501,  0.59642187,  0.54361058],
       [ 0.12009154,  0.60010387,  0.54253043],
       [ 0.11973756,  0.60378459,  0.54139999],
       [ 0.11951163,  0.60746388,  0.54021751],
       [ 0.11942341,  0.61114146,  0.53898192],
       [ 0.11948255,  0.61481702,  0.53769219],
       [ 0.11969858,  0.61849025,  0.53634733],
       [ 0.12008079,  0.62216081,  0.53494633],
       [ 0.12063824,  0.62582833,  0.53348834],
       [ 0.12137972,  0.62949242,  0.53197275],
       [ 0.12231244,  0.63315277,  0.53039808],
       [ 0.12344358,  0.63680899,  0.52876343],
       [ 0.12477953,  0.64046069,  0.52706792],
       [ 0.12632581,  0.64410744,  0.52531069],
       [ 0.12808703,  0.64774881,  0.52349092],
       [ 0.13006688,  0.65138436,  0.52160791],
       [ 0.13226797,  0.65501363,  0.51966086],
       [ 0.13469183,  0.65863619,  0.5176488 ],
       [ 0.13733921,  0.66225157,  0.51557101],
       [ 0.14020991,  0.66585927,  0.5134268 ],
       [ 0.14330291,  0.66945881,  0.51121549],
       [ 0.1466164 ,  0.67304968,  0.50893644],
       [ 0.15014782,  0.67663139,  0.5065889 ],
       [ 0.15389405,  0.68020343,  0.50417217],
       [ 0.15785146,  0.68376525,  0.50168574],
       [ 0.16201598,  0.68731632,  0.49912906],
       [ 0.1663832 ,  0.69085611,  0.49650163],
       [ 0.1709484 ,  0.69438405,  0.49380294],
       [ 0.17570671,  0.6978996 ,  0.49103252],
       [ 0.18065314,  0.70140222,  0.48818938],
       [ 0.18578266,  0.70489133,  0.48527326],
       [ 0.19109018,  0.70836635,  0.48228395],
       [ 0.19657063,  0.71182668,  0.47922108],
       [ 0.20221902,  0.71527175,  0.47608431],
       [ 0.20803045,  0.71870095,  0.4728733 ],
       [ 0.21400015,  0.72211371,  0.46958774],
       [ 0.22012381,  0.72550945,  0.46622638],
       [ 0.2263969 ,  0.72888753,  0.46278934],
       [ 0.23281498,  0.73224735,  0.45927675],
       [ 0.2393739 ,  0.73558828,  0.45568838],
       [ 0.24606968,  0.73890972,  0.45202405],
       [ 0.25289851,  0.74221104,  0.44828355],
       [ 0.25985676,  0.74549162,  0.44446673],
       [ 0.26694127,  0.74875084,  0.44057284],
       [ 0.27414922,  0.75198807,  0.4366009 ],
       [ 0.28147681,  0.75520266,  0.43255207],
       [ 0.28892102,  0.75839399,  0.42842626],
       [ 0.29647899,  0.76156142,  0.42422341],
       [ 0.30414796,  0.76470433,  0.41994346],
       [ 0.31192534,  0.76782207,  0.41558638],
       [ 0.3198086 ,  0.77091403,  0.41115215],
       [ 0.3277958 ,  0.77397953,  0.40664011],
       [ 0.33588539,  0.7770179 ,  0.40204917],
       [ 0.34407411,  0.78002855,  0.39738103],
       [ 0.35235985,  0.78301086,  0.39263579],
       [ 0.36074053,  0.78596419,  0.38781353],
       [ 0.3692142 ,  0.78888793,  0.38291438],
       [ 0.37777892,  0.79178146,  0.3779385 ],
       [ 0.38643282,  0.79464415,  0.37288606],
       [ 0.39517408,  0.79747541,  0.36775726],
       [ 0.40400101,  0.80027461,  0.36255223],
       [ 0.4129135 ,  0.80304099,  0.35726893],
       [ 0.42190813,  0.80577412,  0.35191009],
       [ 0.43098317,  0.80847343,  0.34647607],
       [ 0.44013691,  0.81113836,  0.3409673 ],
       [ 0.44936763,  0.81376835,  0.33538426],
       [ 0.45867362,  0.81636288,  0.32972749],
       [ 0.46805314,  0.81892143,  0.32399761],
       [ 0.47750446,  0.82144351,  0.31819529],
       [ 0.4870258 ,  0.82392862,  0.31232133],
       [ 0.49661536,  0.82637633,  0.30637661],
       [ 0.5062713 ,  0.82878621,  0.30036211],
       [ 0.51599182,  0.83115784,  0.29427888],
       [ 0.52577622,  0.83349064,  0.2881265 ],
       [ 0.5356211 ,  0.83578452,  0.28190832],
       [ 0.5455244 ,  0.83803918,  0.27562602],
       [ 0.55548397,  0.84025437,  0.26928147],
       [ 0.5654976 ,  0.8424299 ,  0.26287683],
       [ 0.57556297,  0.84456561,  0.25641457],
       [ 0.58567772,  0.84666139,  0.24989748],
       [ 0.59583934,  0.84871722,  0.24332878],
       [ 0.60604528,  0.8507331 ,  0.23671214],
       [ 0.61629283,  0.85270912,  0.23005179],
       [ 0.62657923,  0.85464543,  0.22335258],
       [ 0.63690157,  0.85654226,  0.21662012],
       [ 0.64725685,  0.85839991,  0.20986086],
       [ 0.65764197,  0.86021878,  0.20308229],
       [ 0.66805369,  0.86199932,  0.19629307],
       [ 0.67848868,  0.86374211,  0.18950326],
       [ 0.68894351,  0.86544779,  0.18272455],
       [ 0.69941463,  0.86711711,  0.17597055],
       [ 0.70989842,  0.86875092,  0.16925712],
       [ 0.72039115,  0.87035015,  0.16260273],
       [ 0.73088902,  0.87191584,  0.15602894],
       [ 0.74138803,  0.87344918,  0.14956101],
       [ 0.75188414,  0.87495143,  0.14322828],
       [ 0.76237342,  0.87642392,  0.13706449],
       [ 0.77285183,  0.87786808,  0.13110864],
       [ 0.78331535,  0.87928545,  0.12540538],
       [ 0.79375994,  0.88067763,  0.12000532],
       [ 0.80418159,  0.88204632,  0.11496505],
       [ 0.81457634,  0.88339329,  0.11034678],
       [ 0.82494028,  0.88472036,  0.10621724],
       [ 0.83526959,  0.88602943,  0.1026459 ],
       [ 0.84556056,  0.88732243,  0.09970219],
       [ 0.8558096 ,  0.88860134,  0.09745186],
       [ 0.86601325,  0.88986815,  0.09595277],
       [ 0.87616824,  0.89112487,  0.09525046],
       [ 0.88627146,  0.89237353,  0.09537439],
       [ 0.89632002,  0.89361614,  0.09633538],
       [ 0.90631121,  0.89485467,  0.09812496],
       [ 0.91624212,  0.89609127,  0.1007168 ],
       [ 0.92610579,  0.89732977,  0.10407067],
       [ 0.93590444,  0.8985704 ,  0.10813094],
       [ 0.94563626,  0.899815  ,  0.11283773],
       [ 0.95529972,  0.90106534,  0.11812832],
       [ 0.96489353,  0.90232311,  0.12394051],
       [ 0.97441665,  0.90358991,  0.13021494],
       [ 0.98386829,  0.90486726,  0.13689671],
       [ 0.99324789,  0.90615657,  0.1439362 ]]


magma_data = [[0.001462, 0.000466, 0.013866],
              [0.002258, 0.001295, 0.018331],
              [0.003279, 0.002305, 0.023708],
              [0.004512, 0.003490, 0.029965],
              [0.005950, 0.004843, 0.037130],
              [0.007588, 0.006356, 0.044973],
              [0.009426, 0.008022, 0.052844],
              [0.011465, 0.009828, 0.060750],
              [0.013708, 0.011771, 0.068667],
              [0.016156, 0.013840, 0.076603],
              [0.018815, 0.016026, 0.084584],
              [0.021692, 0.018320, 0.092610],
              [0.024792, 0.020715, 0.100676],
              [0.028123, 0.023201, 0.108787],
              [0.031696, 0.025765, 0.116965],
              [0.035520, 0.028397, 0.125209],
              [0.039608, 0.031090, 0.133515],
              [0.043830, 0.033830, 0.141886],
              [0.048062, 0.036607, 0.150327],
              [0.052320, 0.039407, 0.158841],
              [0.056615, 0.042160, 0.167446],
              [0.060949, 0.044794, 0.176129],
              [0.065330, 0.047318, 0.184892],
              [0.069764, 0.049726, 0.193735],
              [0.074257, 0.052017, 0.202660],
              [0.078815, 0.054184, 0.211667],
              [0.083446, 0.056225, 0.220755],
              [0.088155, 0.058133, 0.229922],
              [0.092949, 0.059904, 0.239164],
              [0.097833, 0.061531, 0.248477],
              [0.102815, 0.063010, 0.257854],
              [0.107899, 0.064335, 0.267289],
              [0.113094, 0.065492, 0.276784],
              [0.118405, 0.066479, 0.286321],
              [0.123833, 0.067295, 0.295879],
              [0.129380, 0.067935, 0.305443],
              [0.135053, 0.068391, 0.315000],
              [0.140858, 0.068654, 0.324538],
              [0.146785, 0.068738, 0.334011],
              [0.152839, 0.068637, 0.343404],
              [0.159018, 0.068354, 0.352688],
              [0.165308, 0.067911, 0.361816],
              [0.171713, 0.067305, 0.370771],
              [0.178212, 0.066576, 0.379497],
              [0.184801, 0.065732, 0.387973],
              [0.191460, 0.064818, 0.396152],
              [0.198177, 0.063862, 0.404009],
              [0.204935, 0.062907, 0.411514],
              [0.211718, 0.061992, 0.418647],
              [0.218512, 0.061158, 0.425392],
              [0.225302, 0.060445, 0.431742],
              [0.232077, 0.059889, 0.437695],
              [0.238826, 0.059517, 0.443256],
              [0.245543, 0.059352, 0.448436],
              [0.252220, 0.059415, 0.453248],
              [0.258857, 0.059706, 0.457710],
              [0.265447, 0.060237, 0.461840],
              [0.271994, 0.060994, 0.465660],
              [0.278493, 0.061978, 0.469190],
              [0.284951, 0.063168, 0.472451],
              [0.291366, 0.064553, 0.475462],
              [0.297740, 0.066117, 0.478243],
              [0.304081, 0.067835, 0.480812],
              [0.310382, 0.069702, 0.483186],
              [0.316654, 0.071690, 0.485380],
              [0.322899, 0.073782, 0.487408],
              [0.329114, 0.075972, 0.489287],
              [0.335308, 0.078236, 0.491024],
              [0.341482, 0.080564, 0.492631],
              [0.347636, 0.082946, 0.494121],
              [0.353773, 0.085373, 0.495501],
              [0.359898, 0.087831, 0.496778],
              [0.366012, 0.090314, 0.497960],
              [0.372116, 0.092816, 0.499053],
              [0.378211, 0.095332, 0.500067],
              [0.384299, 0.097855, 0.501002],
              [0.390384, 0.100379, 0.501864],
              [0.396467, 0.102902, 0.502658],
              [0.402548, 0.105420, 0.503386],
              [0.408629, 0.107930, 0.504052],
              [0.414709, 0.110431, 0.504662],
              [0.420791, 0.112920, 0.505215],
              [0.426877, 0.115395, 0.505714],
              [0.432967, 0.117855, 0.506160],
              [0.439062, 0.120298, 0.506555],
              [0.445163, 0.122724, 0.506901],
              [0.451271, 0.125132, 0.507198],
              [0.457386, 0.127522, 0.507448],
              [0.463508, 0.129893, 0.507652],
              [0.469640, 0.132245, 0.507809],
              [0.475780, 0.134577, 0.507921],
              [0.481929, 0.136891, 0.507989],
              [0.488088, 0.139186, 0.508011],
              [0.494258, 0.141462, 0.507988],
              [0.500438, 0.143719, 0.507920],
              [0.506629, 0.145958, 0.507806],
              [0.512831, 0.148179, 0.507648],
              [0.519045, 0.150383, 0.507443],
              [0.525270, 0.152569, 0.507192],
              [0.531507, 0.154739, 0.506895],
              [0.537755, 0.156894, 0.506551],
              [0.544015, 0.159033, 0.506159],
              [0.550287, 0.161158, 0.505719],
              [0.556571, 0.163269, 0.505230],
              [0.562866, 0.165368, 0.504692],
              [0.569172, 0.167454, 0.504105],
              [0.575490, 0.169530, 0.503466],
              [0.581819, 0.171596, 0.502777],
              [0.588158, 0.173652, 0.502035],
              [0.594508, 0.175701, 0.501241],
              [0.600868, 0.177743, 0.500394],
              [0.607238, 0.179779, 0.499492],
              [0.613617, 0.181811, 0.498536],
              [0.620005, 0.183840, 0.497524],
              [0.626401, 0.185867, 0.496456],
              [0.632805, 0.187893, 0.495332],
              [0.639216, 0.189921, 0.494150],
              [0.645633, 0.191952, 0.492910],
              [0.652056, 0.193986, 0.491611],
              [0.658483, 0.196027, 0.490253],
              [0.664915, 0.198075, 0.488836],
              [0.671349, 0.200133, 0.487358],
              [0.677786, 0.202203, 0.485819],
              [0.684224, 0.204286, 0.484219],
              [0.690661, 0.206384, 0.482558],
              [0.697098, 0.208501, 0.480835],
              [0.703532, 0.210638, 0.479049],
              [0.709962, 0.212797, 0.477201],
              [0.716387, 0.214982, 0.475290],
              [0.722805, 0.217194, 0.473316],
              [0.729216, 0.219437, 0.471279],
              [0.735616, 0.221713, 0.469180],
              [0.742004, 0.224025, 0.467018],
              [0.748378, 0.226377, 0.464794],
              [0.754737, 0.228772, 0.462509],
              [0.761077, 0.231214, 0.460162],
              [0.767398, 0.233705, 0.457755],
              [0.773695, 0.236249, 0.455289],
              [0.779968, 0.238851, 0.452765],
              [0.786212, 0.241514, 0.450184],
              [0.792427, 0.244242, 0.447543],
              [0.798608, 0.247040, 0.444848],
              [0.804752, 0.249911, 0.442102],
              [0.810855, 0.252861, 0.439305],
              [0.816914, 0.255895, 0.436461],
              [0.822926, 0.259016, 0.433573],
              [0.828886, 0.262229, 0.430644],
              [0.834791, 0.265540, 0.427671],
              [0.840636, 0.268953, 0.424666],
              [0.846416, 0.272473, 0.421631],
              [0.852126, 0.276106, 0.418573],
              [0.857763, 0.279857, 0.415496],
              [0.863320, 0.283729, 0.412403],
              [0.868793, 0.287728, 0.409303],
              [0.874176, 0.291859, 0.406205],
              [0.879464, 0.296125, 0.403118],
              [0.884651, 0.300530, 0.400047],
              [0.889731, 0.305079, 0.397002],
              [0.894700, 0.309773, 0.393995],
              [0.899552, 0.314616, 0.391037],
              [0.904281, 0.319610, 0.388137],
              [0.908884, 0.324755, 0.385308],
              [0.913354, 0.330052, 0.382563],
              [0.917689, 0.335500, 0.379915],
              [0.921884, 0.341098, 0.377376],
              [0.925937, 0.346844, 0.374959],
              [0.929845, 0.352734, 0.372677],
              [0.933606, 0.358764, 0.370541],
              [0.937221, 0.364929, 0.368567],
              [0.940687, 0.371224, 0.366762],
              [0.944006, 0.377643, 0.365136],
              [0.947180, 0.384178, 0.363701],
              [0.950210, 0.390820, 0.362468],
              [0.953099, 0.397563, 0.361438],
              [0.955849, 0.404400, 0.360619],
              [0.958464, 0.411324, 0.360014],
              [0.960949, 0.418323, 0.359630],
              [0.963310, 0.425390, 0.359469],
              [0.965549, 0.432519, 0.359529],
              [0.967671, 0.439703, 0.359810],
              [0.969680, 0.446936, 0.360311],
              [0.971582, 0.454210, 0.361030],
              [0.973381, 0.461520, 0.361965],
              [0.975082, 0.468861, 0.363111],
              [0.976690, 0.476226, 0.364466],
              [0.978210, 0.483612, 0.366025],
              [0.979645, 0.491014, 0.367783],
              [0.981000, 0.498428, 0.369734],
              [0.982279, 0.505851, 0.371874],
              [0.983485, 0.513280, 0.374198],
              [0.984622, 0.520713, 0.376698],
              [0.985693, 0.528148, 0.379371],
              [0.986700, 0.535582, 0.382210],
              [0.987646, 0.543015, 0.385210],
              [0.988533, 0.550446, 0.388365],
              [0.989363, 0.557873, 0.391671],
              [0.990138, 0.565296, 0.395122],
              [0.990871, 0.572706, 0.398714],
              [0.991558, 0.580107, 0.402441],
              [0.992196, 0.587502, 0.406299],
              [0.992785, 0.594891, 0.410283],
              [0.993326, 0.602275, 0.414390],
              [0.993834, 0.609644, 0.418613],
              [0.994309, 0.616999, 0.422950],
              [0.994738, 0.624350, 0.427397],
              [0.995122, 0.631696, 0.431951],
              [0.995480, 0.639027, 0.436607],
              [0.995810, 0.646344, 0.441361],
              [0.996096, 0.653659, 0.446213],
              [0.996341, 0.660969, 0.451160],
              [0.996580, 0.668256, 0.456192],
              [0.996775, 0.675541, 0.461314],
              [0.996925, 0.682828, 0.466526],
              [0.997077, 0.690088, 0.471811],
              [0.997186, 0.697349, 0.477182],
              [0.997254, 0.704611, 0.482635],
              [0.997325, 0.711848, 0.488154],
              [0.997351, 0.719089, 0.493755],
              [0.997351, 0.726324, 0.499428],
              [0.997341, 0.733545, 0.505167],
              [0.997285, 0.740772, 0.510983],
              [0.997228, 0.747981, 0.516859],
              [0.997138, 0.755190, 0.522806],
              [0.997019, 0.762398, 0.528821],
              [0.996898, 0.769591, 0.534892],
              [0.996727, 0.776795, 0.541039],
              [0.996571, 0.783977, 0.547233],
              [0.996369, 0.791167, 0.553499],
              [0.996162, 0.798348, 0.559820],
              [0.995932, 0.805527, 0.566202],
              [0.995680, 0.812706, 0.572645],
              [0.995424, 0.819875, 0.579140],
              [0.995131, 0.827052, 0.585701],
              [0.994851, 0.834213, 0.592307],
              [0.994524, 0.841387, 0.598983],
              [0.994222, 0.848540, 0.605696],
              [0.993866, 0.855711, 0.612482],
              [0.993545, 0.862859, 0.619299],
              [0.993170, 0.870024, 0.626189],
              [0.992831, 0.877168, 0.633109],
              [0.992440, 0.884330, 0.640099],
              [0.992089, 0.891470, 0.647116],
              [0.991688, 0.898627, 0.654202],
              [0.991332, 0.905763, 0.661309],
              [0.990930, 0.912915, 0.668481],
              [0.990570, 0.920049, 0.675675],
              [0.990175, 0.927196, 0.682926],
              [0.989815, 0.934329, 0.690198],
              [0.989434, 0.941470, 0.697519],
              [0.989077, 0.948604, 0.704863],
              [0.988717, 0.955742, 0.712242],
              [0.988367, 0.962878, 0.719649],
              [0.988033, 0.970012, 0.727077],
              [0.987691, 0.977154, 0.734536],
              [0.987387, 0.984288, 0.742002],
              [0.987053, 0.991438, 0.749504]]


viridis = LinearSegmentedColormap.from_list('viridis', viridis_data)
cm.register_cmap('viridis', viridis)

magma = LinearSegmentedColormap.from_list('magma', magma_data)
cm.register_cmap('magma', magma)
