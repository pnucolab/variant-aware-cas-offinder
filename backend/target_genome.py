from enum import Enum
class Target_Genome(str, Enum):
     human = "Homo sapiens (GRCh38/hg38) - Human",
     human1 = "Homo sapiens (hg19) - Human",
     pepper = "CM334",
     dempsey = "Dempsey",
     mm10 = "Mus musculus (mm10) - Mouse",
     grcm39 = "Mus musculus (GRCm39) - Mouse",
     bosTau7 = "Bos taurus (bosTau7) - Cow",
     arsd = "Bos taurus (ARS-UCD1.3) - Cow",
     arsd2 = "Bos taurus (ARS-UCD1.2) - Cow",
     canFam3 = "Canis familiaris (canFam3) - Dog",
     dog2 = "Canis lupus familiaris (ROS_Cfam_1.0) - Dog",
     dog3 = "Canis lupus familiaris ( Basenji_breed-1.1) - Dog",
     dog4 = "Canis lupus familiaris ( Dog10K_Boxer_Tasha) - Dog",
     dog5 = "Canis lupus familiaris ( UU_Cfam_GSD_1.0) - Dog",
     dog6 = "Canis lupus familiaris ( UMICH_Zoey_3.1) - Dog",
     rn5 = "Rattus norvegicus (rn5) - Rat",
     Rnor60 = "Rattus norvegicus (Rnor 6.0) - Rat",
     rat3 = "Rattus norvegicus (mRatBN7.2) - Rat",
     rat4 = "Rattus norvegicus (UTH_Rnor_SHR_Utx) - Rat",
     rat5 = "Rattus norvegicus (UTH_Rnor_SHRSP_BbbUtx_1.0) - Rat",
     rat6 = "Rattus norvegicus (UTH_Rnor_WKY_Bbb_1.0) - Rat",
     susScr11 = "Sus scrofa (susScr11) - Pig",
     pig3 = "Cavia aperea( CavAp1.0) - Brazilian guinea pig",
     pig4 = "Sus scrofa (Sscrofa11.1 ) - Pig",
     pig5 = "Sus scrofa (Bamei_pig_v1) - Bamei Pig",
     pig6 = "Sus scrofa (Berkshire_pig_v1) - Pig - Berkshire",
     pig7 = "Sus scrofa (Hampshire_pig_v1) - Pig - Hampshire",
     pig8 = "Sus scrofa (Jinhua_pig_v1) - Pig - Jinhua",
     pig9 = "Sus scrofa (Landrace_pig_v1) - Pig - Landrace",
     pig10 = "Sus scrofa (Meishan_pig_v1) - Pig - Meishan",
     pig11 = "Sus scrofa (Pietrain_pig_v1) - Pig - Pietrain",
     pig12 = "Sus scrofa (Rongchang_pig_v1) - Pig - Rongchang",
     pig13 = "Sus scrofa (Tibetan_Pig_v2) - Pig - Tibetan",
     pig14 = "Sus scrofa (minipig_v1.0) - Pig - Wuzhishan",
     pig15 = "Sus scrofa (USMARCv1.0) - Pig - USMARC",
     danRer7 = "Danio rerio (danRer7) - Zebrafish",
     rheMac3 = "Macaca mulatta(rheMac3) - Monkey",
     monkey4 = "Rhinopithecus bieti (ASM169854v1) - Black snub-nosed monkey",
     monkey5 = "Saimiri boliviensis boliviensis (SaiBol1.0) - Bolivian squirrel monkey",
     monkey6 = "Rhinopithecus roxellana (Rrox_v1) - Golden snub-nosed monkey", 
     monkey7 = "Aotus nancymaae (Anan_2.0) - Ma's night monkey", 
     JGI42 = "Xenopus tropicalis (JGI 4.2/xenTro3) - Western clawed frog",
     JGI71 = "Xenopus tropicalis (JGI 7.1) - Western clawed frog",
     JGI71A = "Xenopus laevis (JGI 7.1) - African clawed frog",
     Cv10 = "Cricetulus griseus (v1.0) - Chinese Hamster",
     JGI90 = "Xenopus_tropicalis_v9.1/xenTro9 - Western clawed frog",
     xentro10 = "Xenopus tropicalis (xenTro10) - Western clawed frog",
     JGI91 = "Xenopus laevis_v10.1 - African clawed frog",
     macaca50 = "Macaca fascicularis (5.0) - Crab-eating macaque",
     EquCab2 = "Equus caballus (EquCab3) - Horse",
     OryCun2 = "Oryctolagus cuniculus (OryCun2) - Rabbit",
     MesAur10 = "Mesocricetus auratus (MesAur1.0) - Golden hamster",
     Felis62 = "Felis catus - Cat",
     AHZW01 = "Microtus ochrogaster - Prairie vole",
     bosTau8 = "Bos taurus (bosTau8) - Cow",
     calJac3 = "Callithrix jacchus (mCalJac1.pat.X) -marmoset",
     SOAPdenovov2 = "Pimephales promelas (SOAPdenovo v. 2) - fathead minnow",
     Oarv31 = "ovis_aries (Oar_v3.1) - sheep",
     AQIB01 = "Chlorocebus_sabeus (ChlSab1.1) - green monkey",
     Galga14 = "Gallus gallus (Galgal4) - Chicken",
     ASM1858804v2 = "Oreochromis niloticus",
     ARS1 = "Capra hircus (ARS1) - goat",
     Pman10 = "Peromyscus maniculatus (Pman_2.1) - North American deer mouse",
     Muml801 = "Macaca mulatta (Mmul_10) - Monkey",
     CriGri10 = "Cricetulus griseus (CriGri_1.0) - Chinese hamster",
     Cavpor30="Cavia porcellus (Cavpor3.0) -guinea pig",
     GRCz11 = "Danio rerio (GRCz11) - zebrafish",   
     BGIduk10 = "Anas platyrhynchos (CAU_duck_1.0) - duck",
     ICSASGv2 = "Salmo salar (Ssal_v3.1) -Atlantic salmon",
     commoncarp = "Cyprinus carpio (Cypcar_WagV4.0)",
     Otshv10 = "Oncorhynchus tshawytscha (Otsh_v1.0) - Chinook salmon",
     Otshv20 = "Oncorhynchus tshawytscha (Otsh_v2.0) - Chinook salmon",
     NC012920 = "Human Mitochondria genome (NC_012920.1)",
     AJ512208 = "BalbC/J mouse Mitochondria genome (AJ512208.1)",
     ARSUCD12 = "Bos taurus (ARS UCD1.3)",
     Flounderrefguidedv10 = "Paralichthys olivaceus (Flounder_ref_guided_V1.0)",
     Myoluc20= "Myotis lucifugus (Myoluc2.0)",
     Raegyp20= "Rousettus aegyptiacus (RouAeg_v1_BIUU)",
     mRouAeg1 = "Rousettus aegyptiacus (mRouAeg1.p)",
     TS20longread= "Tree shrew (TS_20 long-read)",
     ASM291563v2 = "Ambystoma mexicanum (AmbMex60DD) -axolotl",
     GRCg6a = "Gallus gallus (GRCg6a) - chicken",
     IPCoco12 = "Ictalurus punctatus (IpCoco_1.2)",
     Ictalurus= "Ictalurus punctatus (ASM400665v3)",
     Musputfur10 = "Mustela putorius furo (MusPutFur1.0) - Ferret",
     GCF0002967551 = "Erinaceus_europaeus (eriEur1)",
     Mmul10= "Macaca mulatta (Mmul_10)",
     Macacafascicularis50 = "Macaca fascicularis (Macaca_fascicularis_6.0)",
     Pmaj10 = "Pagrus major (Pma_NU_1.0)",
     Petromyzon = "Petromyzon_marinus",
     CHM13T2Tv11= "Homo sapiens (CHM13 T2T v2.0) - Human",
     ARSUIRambv20= "Ovis aries (ARS-UI_Ramb_v2.0) - Sheep",
     EquCab30 = "Equus caballus (EquCab3.0) - horse",
     Epinephelus = "Epinephelus lanceolatus (giant grouper)",
     fAnaTes12= "Anabas testudineus (fAnaTes1.2) - Climbing perch",
     fAnaTes13 = "Anabas testudineus (fAnaTes1.3) - Climbing perch",
     NDDBSH1= "Bubalus bubalis (NDDB_SH_1)",
     Largewhitev1= "Sus scrofa (Large white v1 from ensembl) - pig",
     USDANASsal11= "Salmo salar (USDA_NASsal_1.1) - Atlantic salmon",
     ASM1834538v1= "Vulpes lagopus (VulLag_v1_BIUU) - Arctic fox",
     fTakRub13= "Takifugu rubripes (fTakRub1.3 from ENA)",
     Mnem10= "Macaca nemestrina (Mnem_1.0)",
     EptFus10 = "Eptesicus fuscus (DD_ASM_mEF_20220401) - Big brown bat",
     USDAOmykA11= "Oncorhynchus mykiss (USDA_OmykA_1.1) - rainbow trout",
     ASM32557v1= "Pteropus alecto (ASM32557v1) - Black flying fox",
     Macaca60= "Macaca fascicularis (6.0) - Crab-eating macaque",
     Europeanseabass= "Dicentrarchus labrax - (European seabass)",
     ASM1607732v2= "Equus asinus (ASM1607732v2) - Ass",
     mm9= "Mus musculus (GRCm39) - Mouse", 
     Gallus50 = "Gallus gallus (bGalGal1.mat.broiler.GRCg7b) - Chicken",
     tair101 = "Arabidopsis thaliana (TAIR10.1)-Thale cress",
     Japonica =  "Oryza sativa Japonica Group (Japanese rice)",
     tomato = "Solanum lycopersicum (SL3.1) - Tomato",
     maize = "Zea mays (Zm-B73-REFERENCE-NAM-5.0)-maize",
     chlamydomonas = "Chlamydomonas_reinhardtii_v5.5",
     potato = "Solanum tuberosum (SolTub_3.0) - Potato",
     soybean = "Glycine max(v4.0) - Soybean",
     winegrape = "Vitis vinifera (ASM3070453v1) - wine grape",
     casava = "Manihot esculenta (M.esculenta_v8)-cassava",
     apple = "Malus domestica (ASM211411v1)-apple",
     barley = "Hordeum vulgare subsp. vulgare (MorexV3_pseudomolecules)-domesticated barley",
     nicotiana = "Nicotiana benthamiana(ASM3437652v1)",
     strawberry  = "Fragaria vesca (FraVesHawaii_1.0)-Wild strawberry",
     citrus = "Citrus sinensis (DVS_A1.0) - Sweet orange",
     cacao = "Theobroma cacao (Criollo_cocoa_genome_V2) - Cacao",
     banana = "Musa acuminata AAA Group (Cavendish_Baxijiao_AAA) - Dessert banana",
     peanut = "Arachis ipaensis (Araip1.1) - Wild peanut",
     wildpeanutdura = "Arachis duranensis (aradu.V14167.gnm2.J7QH) - Wild peanut",
     kiwifruit = "Actinidia chinensis (ASM966300v1) - Golden kiwifruit",
     rape = "Brassica napus (Da-Ae)-Rape",
     sorghum = "Sorghum bicolor (Sorghum_bicolor_NCBIv3) - Sorghum",
     switchgrass = "Panicum virgatum (P.virgatum_v5) - Switchgrass",
     canabis = "Cannabis sativa (Cannabis sativa)",
     canabisf = "Cannabis sativa female",
     truncatula = "Medicago truncatula (MtrunA17r5.0-ANR)-Barrel medic",
     turcica = "Exserohilum turcica Et28A (v1.0)",
     capsicum = "Capsicum annuum (UCD10Xv1.1)",
     carrot = "Daucus carota subsp. sativus (DH1 v3.0)- Carrot",
     petunia = "Petunia axillaris",
     reinhardtii = "Chlamydomonas reinhardtii(v5.5)",
     vulgaris = "Phaseolus vulgaris (PhaVulg1_0)",
     tef = "Eragrostis tef (tef)",
     haematobium = "Schistosoma haematobium (UoM_Shae.V3)",
     grandis = "Eucalyptus grandis (rose gum)",
     cajan = "Cajanus cajan (C.cajan_V1.1) - pigeon pea",
     cylindrus = "Fragilariopsis cylindrus CCMP1102 (Fc_falcon_quiver_polished)",
     rapa  = "Brassica rapa (CAAS_Brap_v3.01) - field mustard",
     hirsutum = "Gossypium hirsutum (Gossypium_hirsutum_v2.1) - cotton",
     oleracea = "Brassica oleracea var. oleracea (BOL)",
     tabacum = "Nicotiana tabacum (Ntab-TN90) - common tobacco",
     canephora = "Coffea canephora (robusta coffee)",
     clementina = "Citrus x clementina (Citrus_clementina_v1.0) - clementine",
     betavulgaris = "Beta vulgaris subsp. vulgaris (EL10.2) - sugar beet",
     fedtschenkoi = "Kalanchoe fedtschenkoi (K_fedtschenkoi_M2_v1) - South American air plant",
     indicum = "Sesamum indicum (S_indicum_v1.0)-sesame",
     sativus = "Cucumis sativus (Cucumber_9930_V3) - cucumber",
     lanatus = "Citrullus lanatus (watermelon)",
     melo = "Cucumis melo (USDA_Cmelo_AY_1.0) - muskmelon",
     trichocarpa = "Populus trichocarpa (P.trichocarpa_v4.1) - black cottonwood",
     tremula = "Populus tremula (ddPopTrem1.hap1.1) - European aspen",
     patens = "Physcomitrium patens (Phypa V3)",
     distachyon = "Brachypodium distachyon (v3.0) - stiff brome",
     obtusifolia = "Nicotiana obtusifolia (NIOBT.version3)",
     aestivum = "Triticum aestivum (IWGSC CS RefSeq v2.1)-bread wheat",
     sativa = "Camelina sativa (Cs)-false flax",
     lasativa = "Lactuca sativa (Lsat_Salinas_v11) - garden lettuce",
     annuus = "Helianthus annuus (HanXRQr2.0-SUNRISE) - common sunflower",
     guineensis = "Elaeis guineensis (EG5) - African oil palm",
     polyrhiza = "Spirodela polyrhiza (Salk_sp9512.v2) - great duckweed",
     viridis = "Setaria viridis (Setaria_viridis_v2.0)",
     japonicus = "Lotus japonicus (LjGifu_v1.2)",
     virginianum = "Solanum virginianum (SME_r2.5.1) - eggplant",
     communis = "Ricinus communis (castor bean)",
     deltoides = "Populus deltoides ",
     polymorpha =  "Marchantia polymorpha subsp. ruderalis (MpTak2_v7.1)",
     lupulus = "Humulus lupulus (drHumLupu1.1)-European hop",
     pvulgaris  = "Phaseolus vulgaris (P. vulgaris v2.0 ) - string bean",
     arietinum = "Cicer arietinum (ASM33114v1) - chickpea",
     ginseng = "Panax ginseng (ASM2020560v1) - jinsão",
     guttata = "Erythranthe guttata (Mimgu1_0) - spotted monkey flower",
     longifolia = "Mentha longifolia (Mlong_CMEN585_v3) - horsemint",
     arvense = "Thlaspi arvense (T_arvense_v2)",
     radiata = "Vigna radiata var. radiata (Vradiata_ver6) - mung bean",
     equestris = "Phalaenopsis equestris (ASM126359v1)",
     catenatum = "Dendrobium catenatum (ASM160598v2)",
     avium = "Prunus avium (PAV_r1.0)-sweet cherry",
     spontaneum = "Saccharum spontaneum (ASM2245720v1)-fodder cane",
     persica  = "Prunus persica (Prunus_persica_NCBIv2) - peach",
     juncea = "Brassica juncea (ASM1870372v1)-brown mustard",
     maxima = "Cucurbita maxima (Cmax_1.0) - winter squash",
     moschata = "Cucurbita moschata (Cmos_1.0) - crookneck pumpkin",
     pepo = "Cucurbita pepo subsp. pepo (ASM280686v2) - vegetable marrow",
     glauca = "Nicotiana glauca (ASM2677062v1) - tree tobacco",
     attenuata = "Nicotiana attenuata (NIATTr2)",
     annua = "Artemisia annua (Aran) -sweet wormwood",
     Saccharumhyby = "Saccharum hybrid cultivar R570 (Saccharum officinarum X spontaneum var R570 v2.1)",
     makinoi = "Chrysanthemum makinoi",
     lavandulifolium = "Chrysanthemum lavandulifolium (ASM2254549v1)",
     seticuspe = "Chrysanthemum seticuspe(CsGojo-0_v1)",
     syringae = "Pseudomonas syringae pv. tomato str. DC3000 (ASM780v1)",
     somniferum = "Papaver somniferum (ASM357369v1) -opium poppy",
     pimpinellifolium = "Solanum pimpinellifolium (SDAU_Spim_LA1589_1.0) - currant tomato",
     mollissima = "Castanea mollissima (ASM1418300v1) - Chinese chestnut",
     albax = "Populus alba x Populus glandulosa (84K_subgenomeG)",
     quinoa = "Chenopodium quinoa (ASM168347v1) - quinoa",
     hispida = "Benincasa hispida (ASM972705v1) -wax gourd",
     nil = "Ipomoea nil (Asagao_1.1) - Japanese morning glory",
     chinensis = "Rosa chinensis (RchiOBHm-V2) - China rose",
     roseus = "Catharanthus roseus (ASM2865129v1) - Madagascar periwinkle",
     unguiculata =  "Vigna unguiculata (ASM411807v2 ) - cowpea",
     exilis = "Digitaria exilis (DiExil)",
     sativusradish = "Raphanus sativus (ASM80110v3) - radish",
     lupulushop =  "Humulus lupulus (drHumLupu1.1) European hop",
     japonica = "Lonicera japonica (ASM2146441v1) Japanese honeysuckle",
     tauri = "Ostreococcus tauri (version 140606)",
     chacoense = "Solanum chacoense (chc0917) Chaco potato",
     sinensis = "Camellia sinensis (AHAU_CSS_1) black tea",
     sinensis2 = "Camellia sinensis var. sinensis (AHAU_CSS_2)",
     regia = "Juglans regia (Walnut 2.0) English walnut",
     microcarpa = "Juglans microcarpa (ASM312384v1)",
     comosus = "Ananas comosus (ASM154086v1) pineapple",
     bretschneideri = "Pyrus x bretschneideri (Pyrus_bretschneideri_v1) Chinese white pear",
     sativum = "Pisum sativum (CAAS_Psat_ZW6_1.0) garden pea",
     caryophyllus = "Dianthus caryophyllus (ASM2309106v1) clove pink",
     rubella = "Capsella rubella (Caprub1_0)",
     grandiflora = "Capsella grandiflora (UAZ_Capgrnd_2)",
     corymbosum =  "Vaccinium corymbosum (ASM1450483v1) American blueberry",
     abies = "Picea abies (Pabies01) Norway spruce",
     rebaudiana = "Stevia rebaudiana (ASM993640v2)",
     hypogaea = "Arachis hypogaea (arahy.Tifrunner.gnm1.KYV3) peanut",
     hypogaea5 = "Arachis hypogaea (arahy.Tifrunner.gnm2.J5K5) peanut",
     papaya = "Carica papaya (Papaya1.0) papaya",
     equisetifolia = "Casuarina equisetifolia (ASM2855147v1)",
     camaldulensis = "Eucalyptus camaldulensis (ASM1991518v1) Murray red gum",
     granatum = "Punica granatum (ASM765513v2) pomegranate",
     albus = "Lupinus albus (CNRS_Lalb_1.0) white lupine",
     cepa = "Allium cepa (ASM3076508v1) onion",
     trifoliata = "Citrus trifoliata (ASM1835013v1) hardy orange",
     paleacea = "Marchantia paleacea (ASM1418076v2)",
     notabilis = "Morus notabilis (ASM41409v2)",
     pulcherrima = "Euphorbia pulcherrima (Ep-USBG2016-0302-DRAFT-NextGenCassava-1.0) poinsettia",
     faba = "Vicia faba (Hedin2 genome v1) fava bean",
     umbellata = "Vigna umbellata (ASM1883591v1) rice bean",
     macrophylla = "Hydrangea macrophylla( Hmc_EndlessSummer_p1.0)",
     pastoris = "Capsella bursa-pastoris (ASM3645264v1) shepherd's purse",
     sylvestris = "Olea europaea var. sylvestris (O_europaea_v1) wild olive",
     coracana = "Eleusine coracana subsp. coracana (Eleusine_coracana_v1.0 ) Indian finger millet",
     planifolia = "Vanilla planifolia (ASM2384627v1 ) ASM2384627v1",
     richardii = "Ceratopteris richardii (C.richardii_v2)",
     commersonii = "Solanum commersonii (CGN18024_1v5_2 ) Commerson's wild potato",
     argenteum = "Bryum argenteum (EGI_Barg_1.0)",
     catechu = "Areca catechu (ASM2139784v1 ) areca-nut",
     americanus = "Cenchrus americanus (pearl_millet_23DB_ONT_assembly ) bulrush millet",
     melanogaster = "Drosophila melanogaster ( BDGP6.46) Fruit fly",
     melanogaster632 = "Drosophila melanogaster ( BDGP6.32) Fruit fly",
     mellifera = "Apis mellifera (Amel_HAv3.1) honey bee",
     domestica = "Musca domestica (Musca_domestica.polishedcontigs.V.1.1) house fly",
     castaneum = "Tribolium castaneum (icTriCast1.1) red flour beetle",
     albopictus = "Aedes albopictus (AalbF5) Asian tiger mosquito",
     silkworm = "Bombyx mori (ASM3026992v2) domestic silkworm",
     xylostella = "Plutella xylostella (ilPluXylo3.1) diamondback moth",
     terrestris = "Bombus terrestris (iyBomTerr1.2) buff-tailed bumblebee",
     suzukii = "Drosophila suzukii (Dsuz_RU_1.0)",
     Drosophila = "Drosophila melanogaster (Release 6 plus ISO1 MT) fruit fly",
     gambiae = "Anopheles gambiae (idAnoGambNW_F1_1) African malaria mosquito",
     armigera = "Helicoverpa armigera (ASM3070526v1) cotton bollworm",
     citri = "Diaphorina citri (Diaci psyllid genome assembly version 1.1) Asian citrus psyllid",
     mosquito = "Aedes aegypti (AaegL5.0) yellow fever mosquito",
     quinquefasciatus = "Culex quinquefasciatus (VPISU_Cqui_1.0_pri_paternal) southern house mosquito",
     plexippus = "Danaus plexippus (MEX_DaPlex) monarch butterfly",
     demophoon = "Heliconius erato demophoon (SRR8883904)",
     coenia = "Junonia coenia (SRR10765679) buckeye",
     invicta = "Solenopsis invicta (UNIL_Sinv_3.0) red fire ant",
     stephensi = "Anopheles stephensi (UCI_ANSTEP_V1.0) Asian malaria mosquito",
     floridanus = "Camponotus floridanus (Cflo_v7.5) Florida carpenter ant",
     saltator = "Harpegnathos saltator (Hsal_v8.6) Jerdon's jumping ant",
     axyridis = "Harmonia axyridis (icHarAxyr1.1)",
     rapae = "Pieris rapae (ilPieRapa1.1) cabbage white",
     lectularius = "Cimex lectularius (Clec_2.1) bed bug",
     frugiperda = "Spodoptera frugiperda (AGI-APGP_CSIRO_Sfru_2.0) fall armyworm",
     hookeri = "Clitarchus hookeri (ASM4018264v1) smooth stick-insect",
     tabaci = "Bemisia tabaci (ASM185493v1) sweet potato whitefly",
     anopheles = "Anopheles sinensis (AS2)",
     niger = "Lasius niger (ASM104565v1)",
     brasiliensis = "Nippostrongylus brasiliensis (ASM3055315v1)",
     furnacalis = "Ostrinia furnacalis (ASM419383v2) Asian corn borer",
     virgifera = "Diabrotica virgifera virgifera (PGI_DIABVI_V3a) western corn rootworm",
     longisetosus = "Archegozetes longisetosus (Caltech_Along_2.0)",
     fasciatus = "Oncopeltus fasciatus (Ofas_2.0) milkweed bug",
     septempunctata = "Coccinella septempunctata ( icCocSept1.1) seven-spotted ladybird",
     persicae = "Myzus persicae (MPER_G0061.0) green peach aphid",
     illucens = "Hermetia illucens (iHerIll2.2.curated.20191125 ) black soldier fly",
     punctiferalis = "Conogethes punctiferalis (ASM3116337v1) durian fruit borer",
     simulans = "Drosophila simulans (Prin_Dsim_3.1)",
     arabiensis = "Anopheles arabiensis (AaraD3)",
     gregaria = "Schistocerca gregaria (iqSchGreg1.2) desert locust",
     australis = "Struthio camelus australis (ASM69896v1) - African ostrich",
     spretus = "Mus spretus (SPRET_EiJ_v1) Algerian mouse",
     musculus = "Mus musculus (129S1_SvImJ_v1) Mouse 129S1_SvImJ_v1",
     mouseaj = "Mus musculus (A_J_v1) Mouse A_J_v1",
     mouseakr = "Mus musculus (AKR_J_v1) Mouse AKR_J_v1",
     mousebalb = "Mus musculus (BALB_cJ_v1) Mouse BALB_cJ_v1",
     mousec3h = "Mus musculus (C3H_HeJ_v1) Mouse C3H_HeJ_v1",
     mouseC57BL = "Mus musculus (C57BL_6NJ_v1) Mouse  C57BL_6NJ_v1",
     mouseCAST = "Mus musculus (CAST_EiJ_v1) Mouse CAST/EiJ",
     mousecba = "Mus musculus (CBA_J_v1) Mouse CBA/J",
     mousedba = "Mus musculus (DBA_2J_v1) Mouse DBA/2J",
     mousefvb = "Mus musculus (FVB_NJ_v1) Mouse FVB/NJ",
     mouselp = "Mus musculus (LP_J_v1) Mouse  LP/J",
     mouselemur = "Mus musculus (Mmur_3.0) Mouse Lemur",
     mousenod = "Mus musculus (NOD_ShiLtJ_v1) Mouse NOD/ShiLtJ",
     mousenzo = "Mus musculus (NZO_HlLtJ_v1) Mouse NZO/HlLtJ",
     mousepwk = "Mus musculus (PWK_PhJ_v1) Mouse PWK/PhJ",
     mousewsb = "Mus musculus (WSB_EiJ_v1) Mouse WSB/EiJ",
     mouseryu = "Mus musculus (CAROLI_EIJ_v1.1) Ryukyu mouse",
     mouseshrew = "Mus musculus (PAHARI_EIJ_v1.1) Shrew mouse",
     mousesteppe = "Mus musculus (MUSP714) Steppe mouse",
     pacos = "Vicugna pacos (vicPac1) Alpaca",
     marmota = "Marmota marmota marmota (marMar2.1) Alpine marmot",
     formosa =  "Poecilia formosa (Poecilia_formosa-5.1.2) Amazon molly",
     canadensis = "Castor canadensis (C.can_genome_v1.0) American beaver",
     bison =  "Bison bison bison (Bison_UMD1.0) American bison",
     elegans =" Caenorhabditis elegans 	(WBcel235 )Caenorhabditis elegans (Nematode, N2)",
     aspni = "Aspergillus niger ATCC 1015 (ASPNI v3.0)",
     ecoli = "Escherichia coli K-12 (GCA_004919995)",
     Saccharomycetales = "Saccharomycetales 	(GCA_000027005.1) Komagataella pastoris",
     Komagataella = "Saccharomycetales (ASM170810v1) Komagataella pastoris",
     leishmania = "Leishmania major (ASM272v2)",
     denitrificans = "Paracoccus denitrificans PD1222 (GCA_000203895)",
     anisopliae = "Metarhizium anisopliae BRIP 53293 (ASM42696v1)",
     anisopliae549 = "Metarhizium anisopliae ARSEF 549 (MAN_1.0)",
     anisopliae53284 =" Metarhizium anisopliae BRIP 53284 (ASM42698v1)",
     anisopliaee6 = "Metarhizium anisopliae str. E6 (Metarhizium_anisopliae)",
     jostii = "Rhodococcus jostii RHA1 (GCA_000014565)",
     pneumoniae = "Klebsiella pneumoniae subsp. pneumoniae MGH 78578 (GCA_000016305)",
     falciparum3d7 = "Plasmodium falciparum 3D7",
     falciparum7g8 = "Plasmodium falciparum 7G8 (GCA_000150435.3)",
     falciparumcamp = "Plasmodium falciparum CAMP/Malaysia (GCA_000521115.1)",
     falciparumdd2 = "Plasmodium falciparum Dd2 (GCA_000149795.1)",
     falciparumfch = "Plasmodium falciparum FCH/4 (GCA_000521155.1)",
     falciparumhb3 = "Plasmodium falciparum HB3 (GCA_000149665.2)",
     falciparumigh = "Plasmodium falciparum IGH-CR14 (GCA_000186055.2)",
     falciparummali = "Plasmodium falciparum MaliPS096_E11 (GCA_000521035.1)",
     falciparumnf = "Plasmodium falciparum NF135/5.C10 (GCA_000521075.1)",
     falciparumnf54 = "Plasmodium falciparum NF54 (GCA_000401695.2)",
     falciparum542 = "Plasmodium falciparum NF54 (GCA_002831795.1)",
     falciparumpalo = "Plasmodium falciparum Palo Alto/Uganda (GCA_000521095.1)",
     falciparumraji = "Plasmodium falciparum RAJ116 (GCA_000186025.2)",
     falciparumsanta = "Plasmodium falciparum Santa Lucia (GCA_000150455.3)",
     falciparumtanza = "Plasmodium falciparum Tanzania (2000708) (GCA_000521055.1)",
     falciparumugt = "Plasmodium falciparum UGT5.1 (GCA_000401715.2)",
     falciparumvet = "Plasmodium falciparum Vietnam Oak-Knoll (FVO) (GCA_000521015.1)",
     mucosae = "Limosilactobacillus mucosae LM1 (GCA_000248095)",
     tricornutum = "Phaeodactylum tricornutum (ASM15095v2)",
     glutamicum = "Corynebacterium glutamicum ATCC 13032 (GCA_000011325)",
     tuberculosis = "Mycobacterium tuberculosis variant bovis AF2122/97 (GCA_000195835)",
     africanum = "Mycobacterium tuberculosis variant africanum (GCA_001544855)",
     microti = "Mycobacterium tuberculosis variant microti OV254 (GCA_002865895)",
     pinnipedii = "Mycobacterium tuberculosis variant pinnipedii (GCA_003027895)",
     infantum = "Leishmania infantum (GCA_900500625.1)",
     aureus = "Staphylococcus aureus subsp. aureus str. Newman (GCA_000010465)",
     putida = "Pseudomonas putida KT2440 (GCA_000007565)",
     acetobutylicum = "Clostridium acetobutylicum ATCC 824 (GCA_000008765)",
     sacchari = "Paraburkholderia sacchari str. LMG 19450 (GCA_000785435)",
     cruzi = "Trypanosoma cruzi Dm28c",
     hansenii = "Debaryomyces hansenii CBS767 (GCA_000006445)",
     mansoni = "Schistosoma mansoni (Flatworm)",
     monocytogenes = "Listeria monocytogenes (GCA_006364655)",
     beijerinckii = "Clostridium beijerinckii NCIMB 8052 (GCA_000016965)",
     tyrobutyricum = "Clostridium tyrobutyricum DIVETGP (GCA_000577845)",
     tyrobutyricumbia = "Clostridium tyrobutyricum str. Cirm BIA 2237 (GCA_004924375)",
     acidaminophilum = "Peptoclostridium acidaminophilum DSM 3953 (GCA_000597865)",
     litorale = "Peptoclostridium litorale DSM 5388 str. W6 (GCA_000699585)",
     peptoclostridium = "Peptoclostridium sp. AF21-18 (GCA_003478825)",
     carboxidivorans = "Clostridium carboxidivorans P7 (GCA_000175595)",
     kluyveri = "Clostridium kluyveri DSM 555 (GCA_000016505)",
     lusitaniae = "Clavispora lusitaniae ATCC 42720",
     lusitaniaecbs = "Clavispora lusitaniae str. CBS 6936",
     equiperdum = "Trypanosoma brucei equiperdum str. IVM-t1 (GCA_003543875.1)",
     pseudonana = "Thalassiosira pseudonana",
     cerevisiae131 = "Saccharomyces cerevisiae str. 131",
     cerevisiae2 = "Saccharomyces cerevisiae str. Kagoshima No.2",
     cerevisiae684 = "Saccharomyces cerevisiae str. P-684",
     cerevisiaepf = "Saccharomyces cerevisiae str. Pf-1",
     threadworm = "Strongyloides ratti (Threadworm)",
     versutusd301 = "Thioalkalivibrio versutus str. D301 (GCA_001020955)",
     versutusal2 = "Thioalkalivibrio versutus str. AL 2 (GCA_001999325)",
     toruloides = "Rhodotorula toruloides str. NBRC 0880",
     extorquens = "Methylorubrum extorquens AM1 (GCA_000022685)",
     sinica = "Candidatus Brocadia sinica JPN1 (GCA_000949635)",
     acetobutylicumatcc = "Clostridium acetobutylicum ATCC 824 (GCA_000008765)",
     baumannii = "Acinetobacter baumannii (GCA_006369845)",
     baumanniiatcc = "Acinetobacter baumannii ATCC 19606 = CIP 70.34 = JCM 6841 (GCA_000162295)",
     albicans = "Candida albicans SC5314 (Cand_albi_SC5314_V3) (GCA_000784655)",
     albicansv4  = "Candida albicans SC5314 (Cand_albi_SC5314_V4) (GCA_000784635)",
     glabrata = "Candida glabrata CBS138 (GCA_000002545.2)",
     nucleatum = "Fusobacterium nucleatum subsp. nucleatum ATCC 25586 (GCA_000007325)",
     polymyxa = "Paenibacillus polymyxa (GCA_900454525)",
     pasteurianum = "Clostridium pasteurianum DSM 525 = ATCC 6013 (GCA_000807255)",
     bovis = "Mycobacterium tuberculosis variant bovis BCG (GCA_001544735)",
     knowlesi = "Plasmodium knowlesi",
     knowlesimala = "Plasmodium knowlesi str. Malayan Strain Pk1 (A+) (GCA_002140095.1)",
     knowlesih = "Plasmodium knowlesi strain H (GCA_900004885.2)",
     ambofaciens = "Streptomyces ambofaciens ATCC 23877 str. ATCC23877 (GCA_001267885)",
     biovar = "Vibrio cholerae O1 biovar El Tor str. N16961 (GCA_000006745)",
     putidaf1 = "Pseudomonas putida F1 (GCA_000016865)",
     agglomerans = "Pantoea agglomerans (GCA_004793995)",
     enterica = "Salmonella enterica subsp. enterica serovar Typhimurium str. LT2 (GCA_000006945)",
     hanpo2 = "Ogataea polymorpha str. NCYC 495 leu1.1 (Hanpo2)",
     bacteriovorus = "Bdellovibrio bacteriovorus HD100 (GCA_000196175)",
     leidyi = "Mnemiopsis leidyi (Warty comb jelly)",
     bdellovibrio = "Bdellovibrio bacteriovorus (GCA_001592755)",
     huxleyi = "Emiliania huxleyi",
     commune = "Schizophyllum commune H4-8",
     reesei = "Trichoderma reesei",
     reeseirut = "Trichoderma reesei RUT C-30",
     ari = "Toxoplasma gondii ARI (GCA_000250965.2)",
     cast = "Toxoplasma gondii CAST (GCA_000256705.2)",
     coug = "Toxoplasma gondii COUG (GCA_000338675.2)",
     fou = "Toxoplasma gondii FOU (GCA_000224905.2)",
     gab2 = "Toxoplasma gondii GAB2-2007-GAL-DOM2 (GCA_000325525.2)",
     gti = "Toxoplasma gondii GT1 (GCA_000149715.2)",
     mas = "Toxoplasma gondii MAS (GCA_000224865.2)",
     me49 = "Toxoplasma gondii ME49",
     rub = "Toxoplasma gondii RUB (GCA_000224805.2)",
     tgcat = "Toxoplasma gondii TgCATBr9 (GCA_000224825.2)",
     tgcatprc= "Toxoplasma gondii TgCatPRC2 (GCA_000256725.2)",
     vand = "Toxoplasma gondii VAND (GCA_000224845.2)",
     veg = "Toxoplasma gondii VEG (GCA_000150015.2)",
     p89 = "Toxoplasma gondii p89 (GCA_000224885.2)",
     berghei = "Plasmodium berghei (GCA_900095635.1)",
     yoelii17x = "Plasmodium yoelii str. 17X (GCA_900002385.1)",
     yoeliiym = "Plasmodium yoelii str. YM (GCA_900002395.1)",
     yoelii17xnl = "Plasmodium yoelii yoelii str. 17XNL (GCA_000003085.2)",
     platensisc1 = "Arthrospira platensis C1 (GCA_000307915)",
     platensisnies = "Arthrospira platensis NIES-39 (GCA_000210375)",
     rhaeticus = "Komagataeibacter rhaeticus AF1 (GCA_000700985)",
     komagataeibacter = "Komagataeibacter rhaeticus (GCA_900086575)",
     subtilis = "Bacillus subtilis (GCA_000878265)",
     pectorale = "Gonium pectorale",
     colik12 = "Escherichia coli K-12 (GCA_004919995)",
     harzianum = "Trichoderma harzianum str. T6776",
     harzianum274 = "Trichoderma harzianum str. TR274",
     harzianumTr1 = "Trichoderma harzianum str. Tr1",
     harzianumCBS = "Trichoderma harzianum CBS 226.95",
     albusdsm = "Streptomyces albus str. DSM 41398 (GCA_000827005)",
     albusalbus = "Streptomyces albus subsp. albus (GCA_001541145)",
     fiocruz = "Leptospira interrogans serovar Copenhageni str. Fiocruz L1-130 (GCA_000007685)",
     lT2050 = "Leptospira interrogans serovar Copenhageni str. LT2050 (GCA_000216155)",
     phagocytophilum = "Anaplasma phagocytophilum str. HZ (GCA_000013125)",
     meningitidis = "Neisseria meningitidis (GCA_006334835)",
     pneumoniaes = "Streptococcus pneumoniae (GCA_006376385)",
     mg1655 = "Escherichia coli str. K-12 substr. MG1655 str. K12 (GCA_000005845)",
     w3110 = "Escherichia coli str. K-12 substr. W3110 (GCA_000010245)",
     holarctica = "Francisella tularensis subsp. holarctica str. FTT_1 (GCA_000833235)",
     holarctica08 =" Francisella tularensis subsp. holarctica str. 08T0073 (GCA_001953575)",
     phaffii = "Komagataella phaffii CBS 7435 (PicPas_Mar2011)",
     phaffiicbs = "Komagataella phaffii CBS 7435 (ASM90023503v1)",
     phaffiigs = "Komagataella phaffii GS115",
     phaffiiwt = "Komagataella phaffii str. WT",
     loti = "Mesorhizobium loti str. UFLA 01-765 (GCA_001510895)",
     loti1 = "Mesorhizobium loti str. R7ANS::ICEMlSym2042 (GCA_001671485)",
     loti2 = "Mesorhizobium loti str. NZP2042 (GCA_001672355)",
     loti3 = "Mesorhizobium loti str. NZP2014 (GCA_001672365)",
     loti4 = "Mesorhizobium loti (GCA_002356515)",
     loti5 = "Mesorhizobium loti str. LU (GCA_002858745)",
     loti6 = "Mesorhizobium loti (GCA_003024615)",
     loti7 = "Mesorhizobium loti str. DSM 2626 (GCA_003148495)",
     meliloti = "Sinorhizobium meliloti 1021 (GCA_000006965)",
     butyricum1 = "Clostridium butyricum (GCA_002940805)",
     butyricum2 = "Clostridium butyricum (GCA_003935945)",
     pcc6714 = "Synechocystis sp. PCC 6714 (GCA_000478825)",
     pcc6803 = "Synechocystis sp. PCC 6803 (GCA_000009725)",
     thermotolerans = "Lachancea thermotolerans CBS 6340",
     lactis1 = "Lactococcus lactis str. C2D (GCA_004022375)",
     lactis2 = "Lactococcus lactis str. SRCM103457 (GCA_004194355)",
     lactis3 = "Lactococcus lactis str. gh1 (GCA_004795205)",
     lactis4 = "Lactococcus lactis str. CH_LC01 (GCA_005146285)",
     sinense = "Ganoderma sinense ZZ0214-1",
     xylinus1 = "Komagataeibacter xylinus E25 (GCA_000550765)",
     xylinus2 = "Komagataeibacter xylinus (GCA_002762195)",
     xylinus3 = "Komagataeibacter xylinus (GCA_003207915)",
     xylinus4 = "Komagataeibacter xylinus str. DSM 2325 (GCA_004006375)",
     xylinus5 = "Komagataeibacter xylinus (GCA_900016225)",
     xylinus6 = "Komagataeibacter xylinus NBRC 13693 (GCA_000964505)",
     chrysogenum = "Penicillium chrysogenum str. P2niaD18",
     trachomatis1 = "Chlamydia trachomatis 434/Bu (GCA_000068585)",
     trachomatis2 = "Chlamydia trachomatis A2497 (GCA_000226605)",
     trachomatis3 = "Chlamydia trachomatis A/HAR-13 (GCA_000012125)",
     trachomatis4 = "Chlamydia trachomatis D/UW-3/CX (GCA_000008725)",
     trachomatis5 = "Chlamydia trachomatis (GCA_001213105)",
     trachomatis6 = "Chlamydia trachomatis (GCA_001317725)",
     trachomatis7 = "Chlamydia trachomatis (GCA_001317765)",
     trachomatis8 = "Chlamydia trachomatis (GCA_001398195)",
     gaditana1 = "Nannochloropsis gaditana CCMP526 (GCA_000240725.1)",
     gaditana2 = "Nannochloropsis gaditana str. B-31 (GCA_000569095.1)",
     coelicolor1 = "Streptomyces coelicolor str. O-10.2 (GCA_004368945)",
     coelicolor2 = "Streptomyces coelicolor str. O-10.1 (GCA_004368985)",
     histolytica1 = "Entamoeba histolytica",
     histolytica2 = "Entamoeba histolytica HM-1:IMSS-A (GCA_000365475.1)",
     histolytica3 = "Entamoeba histolytica HM-1:IMSS-B str. HM3:IMSS-B (GCA_000344925.1)",
     histolytica4 = "Entamoeba histolytica HM-3:IMSS (GCA_000346345.1)",
     histolytica5 = "Entamoeba histolytica KU27 (GCA_000338855.1)",
     histolytica6 = "Entamoeba histolytica str. HM1:IMSS clone 6 (GCA_001662325.1)",
     eubayanus = "Saccharomyces eubayanus str. FM1318",
     monophora = "Fonsecaea monophora",
     cellulovorans = "Clostridium cellulovorans 743B (GCA_000145275)",
     plantarum = "Lactobacillus plantarum WCFS1 (GCA_000203855)",
     opacus1 = "Rhodococcus opacus B4 (GCA_000010805)",
     opacus2 = "Rhodococcus opacus str. R7 (GCA_000736435)",
     opacus3 = "Rhodococcus opacus str. 1CP (GCA_001685605)",
     opacus4 = "Rhodococcus opacus str. 04-OD7 (GCA_002968035)",
     opacus5 = "Rhodococcus opacus str. DSM 44186 (GCA_003626495)",
     opacus6 = "Rhodococcus opacus str. ATCC 51882 (GCA_004365075)",
     opacus7 = "Rhodococcus opacus M213 (GCA_000264745)",
     opacus8 = "Rhodococcus opacus PD630 (GCA_000599545)",
     aeruginosa =  "Pseudomonas aeruginosa PAO1 (GCA_000006765)",
     aeruginosa2 = "Pseudomonas aeruginosa UCBPP-PA14 (GCA_000014625)",
     pneumophila = "Legionella pneumophila subsp. pneumophila str. Philadelphia 1 (GCA_000008485)",
     pneumophila2 = "Legionella pneumophila (GCA_006364635)",
     pneumophila3 = "Legionella pneumophila str. Lens (GCA_000048665)",
     pneumophila4 = "Legionella pneumophila subsp. pascullei (GCA_001590695)",
     pneumophila5 = "Legionella pneumophila subsp. pneumophila (GCA_003605955)",
     capsulatus = "Rhodobacter capsulatus SB 1003 str. SB1003 (GCA_000021865)",
     sphaeroides = "Rhodobacter sphaeroides 2.4.1 (GCA_000012905)",
     europaea = "Nitrosomonas europaea ATCC 19718 (GCA_000009145)",
     castellanii = "Acanthamoeba castellanii str. Neff (GCA_000313135.1)",
     suis1 = "Streptococcus suis (GCA_004922915)",
     suis2 = "Streptococcus suis str. NSUI060 (GCA_001572685)",
     suis3 = "Streptococcus suis str. DN13 (GCA_001640765)",
     suis4 = "Streptococcus suis str. CZ130302 (GCA_002803825)",
     suis5 = "Streptococcus suis str. AH681 (GCA_002812525)",
     suis6 = "Streptococcus suis str. HN136 (GCA_002831545)",
     suis7 = "Streptococcus suis str. NJAU-TF-202 (GCA_002896475)",
     suis8 = "Streptococcus suis str. HN105 (GCA_003144175)",
     suis9 =  "Streptococcus suis str. 1081 (GCA_003285245)",
     suis10 = "Streptococcus suis str. HA1003 (GCA_003352205)",
     suis11 = "Streptococcus suis str. WUSS351 (GCA_004843685)",
     suis12 = "Streptococcus suis 05ZYH33 (GCA_000014305)",
     suis13 = "Streptococcus suis 6407 (GCA_000732355)",
     suis14 =" Streptococcus suis BM407 (GCA_000026745)",
     suis15 = "Streptococcus suis D12 (GCA_000231905)",
     suis16 = "Streptococcus suis GZ1 (GCA_000018185)",
     suis17 = "Streptococcus suis T15 (GCA_000494895)",
     difficile = "Clostridioides difficile (GCA_002301955)",
     difficile2 = "Clostridioides difficile 630 (GCA_000009205)",
     difficile3 = "Clostridioides difficile ATCC 9689 = DSM 1296 (GCA_001077535)",
     difficile4 = "Clostridioides difficile CD160 (GCA_000449425)",
     difficile5 = "Clostridioides difficile CD196 (GCA_000085225)",
     difficile6 = "Clostridioides difficile F501 (GCA_000450805)",
     difficile7 = "Clostridioides difficile str. RA09_70 (GCA_001299495)",
     difficile8 = "Clostridioides difficile str. CD-B18-123 (GCA_005502205)",
     difficile9 = "Clostridioides difficile str. WCH065050 (GCA_005786645)",
     difficile10 = "Clostridioides difficile NAP08 (GCA_000164175)",
     difficile11 = "Clostridioides difficile P28 (GCA_000450985)",
     difficile12 = "Clostridioides difficile R20291 (GCA_000027105)",
     difficile13 = "Clostridioides difficile Y384 (GCA_000451045)",
     


def ref_paths(Target_Genome):
     if Target_Genome == "CM334":
         return './genome/pepper/pepper_ref/GCA_000512255.2_ASM51225v2_genomic.fa'
     if Target_Genome == "Dempsey":
         return './genome/dempsey/dempsey_ref/Dempsey.v1.0.fasta'
     if Target_Genome == "Homo sapiens (GRCh38/hg38) - Human":
         return './genome/human38/Homo_sapiens.GRCh38.dna.primary_assembly.fa'
     if Target_Genome == "Homo sapiens (hg19) - Human":
         return './genome/human19/hg19.fa'
     if Target_Genome == "Mus musculus (mm10) - Mouse":
         return './genome/mm10/Mus_musculus.GRCm39.dna_sm.primary_assembly.fa'
     if Target_Genome == "Bos taurus (bosTau7) - Cow":
         return './genome/cow/GCF_002263795.3_ARS-UCD2.0_genomic.fna'
     if Target_Genome == "Canis familiaris (canFam3) - Dog":
         return './genome/dog/GCF_011100685.1_UU_Cfam_GSD_1.0_genomic.fna'
     if Target_Genome == "Rattus norvegicus (rn5) - Rat":
         return './genome/rat/GCF_036323735.1_GRCr8_genomic.fna'
     if Target_Genome == "Sus scrofa (susScr11) - Pig":
         return './genome/pig/GCF_000003025.6_Sscrofa11.1_genomic.fna'
     if Target_Genome ==  "Danio rerio (danRer7) - Zebrafish":
         return './genome/zebrafish/GCF_000002035.6_GRCz11_genomic.fna'
     if Target_Genome == "Macaca mulatta(rheMac3) - Monkey":
         return './genome/monkey/GCF_003339765.1_Mmul_10_genomic.fna '
     if Target_Genome == "Xenopus tropicalis (JGI 4.2/xenTro3) - Western clawed frog":
         return './genome/frogJGI42/GCF_000004195.4_UCB_Xtro_10.0_genomic.fna'
     if Target_Genome == "Xenopus tropicalis (JGI 7.1) - Western clawed frog":
         return './genome/frogJGI71/GCF_000004195.4_UCB_Xtro_10.0_genomic.fna '
     if Target_Genome == "Xenopus_laevis_v2 - African clawed frog":
         return './genome/frogv2/GCF_001663975.1.fa'
     if Target_Genome == "Cricetulus griseus (v1.0) - Chinese Hamster":
         return './genome/hamster/GCF_003668045.3_CriGri-PICRH-1.0_genomic.fna'
     if Target_Genome == "Xenopus_tropicalis_v9.1/xenTro9 - Western clawed frog":
         return './genome/frogv9.1/GCF_000004195.4_UCB_Xtro_10.0_genomic.fna'
     if Target_Genome == "Xenopus tropicalis (xenTro10) - Western clawed frog":
         return './genome/frogxen10/GCF_000004195.4_UCB_Xtro_10.0_genomic.fna'
     if Target_Genome == "Xenopus laevis_v10.1 - African clawed frog":
         return './genome/frogv10.1/GCF_017654675.1.fa '
     if Target_Genome == "Macaca fascicularis (5.0) - Crab-eating macaque":
         return './genome/macaque/GCF_037993035.1_T2T-MFA8v1.0_genomic.fna'
     if Target_Genome == "Danio rerio (GRCz11) - Zebrafish":
         return './genome/zebrafishGRCz11/Danio_rerio.GRCz11.dna.toplevel.fa'
     if Target_Genome == "Rattus norvegicus (Rnor 6.0) - Rat":
         return './genome/ratRnor60/GCF_000001895.5.fa'
     if Target_Genome == "Equus caballus (EquCab3.0) - horse":
         return './genome/horse/GCF_002863925.1_EquCab3.0_genomic.fna '
     if Target_Genome == "Oryctolagus cuniculus (OryCun2) - Rabbit":
         return './genome/rabbit/GCF_000003625.3_OryCun2.0_genomic.fna'
     if Target_Genome == "Mesocricetus auratus (MesAur1.0) - Golden hamster":
         return './genome/hamsterMesAur10/GCF_000349665.1.fa'
     if Target_Genome == "Felis catus - Cat":
         return './genome/cat/GCF_018350175.1_F.catus_Fca126_mat1.0_genomic.fna'
     if Target_Genome == "Microtus ochrogaster - Prairie vole":
         return './genome/Prairie/GCF_000317375.1.fa'
     if Target_Genome == "Bos taurus (bosTau8) - Cow":
         return './genome/cowbosTau8/GCF_002263795.3_ARS-UCD2.0_genomic.fna'
     if Target_Genome == "Callithrix jacchus (mCalJac1.pat.X) -marmoset":
         return './genome/marmoset/Callithrix_jacchus.mCalJac1.pat.X.dna.toplevel.fa'
     if Target_Genome == "Pimephales promelas (SOAPdenovo v. 2) - fathead minnow":
         return './genome/minnow/GCF_016745375.1.fa'
     if Target_Genome == "ovis_aries (Oar_v3.1) - sheep":
         return './genonme/sheep/GCF_016772045.2_ARS-UI_Ramb_v3.0_genomic.fna'
     if Target_Genome == "Chlorocebus_sabeus (ChlSab1.1) - green monkey":
         return './genome/greenmonkey/Chlorocebus_sabaeus.ChlSab1.1.dna.toplevel.fa'
     if Target_Genome == "Gallus gallus (Galgal4) - Chicken":
         return './genome/chicken/GCF_016699485.2_bGalGal1.mat.broiler.GRCg7b_genomic.fna'
     if Target_Genome == "Oreochromis niloticus":
         return './genome/niloticus/Oreochromis_niloticus.O_niloticus_UMD_NMBU.dna.toplevel.fa'
     if Target_Genome == "Capra hircus (ARS1) - goat":
         return './genome/goat/Capra_hircus.ARS1.dna.toplevel.fa'
     if Target_Genome == "Peromyscus maniculatus (Pman_2.1) - North American deer mouse":
         return './genome/mousePman21/Peromyscus_maniculatus_bairdii.HU_Pman_2.1.dna.toplevel.fa'
     if Target_Genome == "Macaca mulatta (Mmul_10) - Monkey":
         return './genome/monekyMuml10/Macaca_mulatta.Mmul_10.dna.toplevel.fa'
     if Target_Genome =="Cricetulus griseus (CriGri_1.0) - Chinese hamster":
         return './genome/hamsterCriGri10/Cricetulus_griseus_crigri.CriGri_1.0.dna.toplevel.fa' 
     if Target_Genome == "Cavia porcellus (Cavpor3.0) -guinea pig":
         return './genome/pigCavpor30/Cavia_porcellus.Cavpor3.0.dna.toplevel.fa'
     if Target_Genome == "Anas platyrhynchos (CAU_duck_1.0) - duck":
         return './genome/duck/Anas_platyrhynchos_platyrhynchos.CAU_duck1.0.dna.toplevel.fa'
     if Target_Genome == "Salmo salar (Ssal_v3.1) -Atlantic salmon":
         return './genome/salmon/Salmo_salar.Ssal_v3.1.dna.toplevel.fa'
     if Target_Genome == "Cyprinus carpio (Cypcar_WagV4.0)":
         return './genome/carp/Cyprinus_carpio_carpio.Cypcar_WagV4.0.dna.toplevel.fa'
     if Target_Genome == "Oncorhynchus tshawytscha (Otsh_v2.0) - Chinook salmon":
         return './genome/salmonOtshv20/Oncorhynchus_tshawytscha.Otsh_v2.0.dna.toplevel.fa'
     if Target_Genome == "Oncorhynchus tshawytscha (Otsh_v1.0) - Chinook salmon":
         return './genome/salmonOtshv10/Oncorhynchus_tshawytscha.Otsh_v1.0.dna.toplevel.fa'
     if Target_Genome == "Human Mitochondria genome (NC_012920.1)":
         return './genome/Mitochondria/NC_012920.1.fna'
     if Target_Genome == "BalbC/J mouse Mitochondria genome (AJ512208.1)":
         return './genome/mouseAJ512208/AJ512208.1.fna'
     if Target_Genome == "Bos taurus (ARS UCD1.3)":
         return './genome/taurus/Bos_taurus.ARS-UCD1.3.dna.toplevel.fa'
     if Target_Genome == "Paralichthys olivaceus (Flounder_ref_guided_V1.0)":
         return './genome/olivaceus/GCF_001970005.1_Flounder_ref_guided_V1.0_genomic.fna'
     if Target_Genome == "Myotis lucifugus (Myoluc2.0)":
         return './genome/lucifugus/Myotis_lucifugus.Myoluc2.0.dna.toplevel.fa'
     if Target_Genome == "Rousettus aegyptiacus (RouAeg_v1_BIUU)":
         return './genome/aegyptiacus/GCA_004024865.1_RouAeg_v1_BIUU_genomic.fna'
     if Target_Genome == "Rousettus aegyptiacus (mRouAeg1.p)":
         return './genome/aegyptiacusmRouAeg1/GCF_014176215.1_mRouAeg1.p_genomic.fna'
     if Target_Genome == "Tree shrew (TS_20 long-read)":
         return './genome/shrew/Tupaia_belangeri.TREESHREW.dna.toplevel.fa'
     if Target_Genome == "Ambystoma mexicanum (AmbMex60DD) -axolotl":
         return './genome/Ambystoma/GCA_002915635.3_AmbMex60DD_genomic.fna'
     if Target_Genome == "Gallus gallus (GRCg6a) - chicken":
         return './genome/chickenGRCg6a/Gallus_gallus_gca000002315v5.GRCg6a.dna.toplevel.fa'
     if Target_Genome == "Ictalurus punctatus (IpCoco_1.2)":
         return './genome/punctatus/Ictalurus_punctatus.IpCoco_1.2.dna.toplevel.fa'
     if Target_Genome == "Ictalurus punctatus (ASM400665v3)":
         return './genome/punctatusASM400665v3/Ictalurus_punctatus.ASM400665v3.dna.toplevel.fa'
     if Target_Genome == "Mustela putorius furo (MusPutFur1.0) - Ferret":
         return './genome/ferret/Mustela_putorius_furo.MusPutFur1.0.dna.toplevel.fa'
     if Target_Genome == "Erinaceus europaeus (eriEur1)":
         return './genome/europaeus/Erinaceus_europaeus.HEDGEHOG.dna.toplevel.fa'
     if Target_Genome == "Macaca mulatta (Mmul_10)":
         return './genome/mulatta/Macaca_mulatta.Mmul_10.dna.toplevel.fa'
     if Target_Genome == "Pagrus major (Pma_NU_1.0)":
         return './genome/pagrus/GCA_040436345.1_Pma_NU_1.0_genomic.fna'
     if Target_Genome =="Petromyzon marinus":
         return './genome/Petromyzon/Petromyzon_marinus.Pmarinus_7.0.dna.toplevel.fa'
     if Target_Genome == "Homo sapiens (CHM13 T2T v2.0) - Human":
         return './genome/humanCHM13/GCF_009914755.1_T2T-CHM13v2.0_genomic.fna' 
     if Target_Genome == "Ovis aries (ARS-UI_Ramb_v2.0) - Sheep":
         return './genome/sheepARSUIRambv20/Ovis_aries_rambouillet.ARS-UI_Ramb_v2.0.dna.toplevel.fa'
     if Target_Genome == "Ovis aries (Oar_v3.1) - Sheep(texel)":
         return './genome/sheepOarv31/Ovis_aries.Oar_v3.1.dna.toplevel.fa'
     if Target_Genome == "Equus caballus (EquCab3.0) - horse":
         return './genome/horseEquCab30/Equus_caballus.EquCab3.0.dna.toplevel.fa'
     if Target_Genome == " Epinephelus lanceolatus (giant grouper)":
         return './genome/lanceolatus/GCF_005281545.1_ASM528154v1_genomic.fna'
     if Target_Genome == "Anabas testudineus (fAnaTes1.2) - Climbing perch":
         return './genome/perch12/Anabas_testudineus.fAnaTes1.2.dna.toplevel.fa'
     if Target_Genome == "Anabas testudineus (fAnaTes1.3) - Climbing perch":
         return './genome/perch13/Anabas_testudineus.fAnaTes1.3.dna.toplevel.fa'
     if Target_Genome == "Bubalus bubalis (NDDB_SH_1)":
         return './genome/bubalis/GCF_019923935.1_NDDB_SH_1_genomic.fna'
     if Target_Genome == "Sus scrofa (Large white v1 from ensembl) - pig":
         return './genome/pigLargewhitev1/Sus_scrofa_largewhite.Large_White_v1.dna.toplevel.fa'
     if Target_Genome == "Salmo salar (USDA_NASsal_1.1) - Atlantic salmon":
         return './genome/salmonUSDANASsal11/Salmo_salar_gca021399835v1.USDA_NASsal_1.1.dna.toplevel.fa'
     if Target_Genome == "Vulpes lagopus (VulLag_v1_BIUU) - Arctic fox":
         return './genome/fox/GCA_004023825.1_VulLag_v1_BIUU_genomic.fna'
     if Target_Genome == "Takifugu rubripes (fTakRub1.3 from ENA)":
         return './genome/rubripes/GCA_901000725.3_fTakRub1.3_genomic.fna'
     if Target_Genome == "Macaca nemestrina (Mnem_1.0)":
         return './genome/macacaMnem10/Macaca_nemestrina.Mnem_1.0.dna.toplevel.fa'
     if Target_Genome == "Eptesicus fuscus (DD_ASM_mEF_20220401) - Big brown bat":
         return './genome/fuscus/GCF_027574615.1_DD_ASM_mEF_20220401_genomic.fna'
     if Target_Genome == "Oncorhynchus mykiss (USDA_OmykA_1.1) - rainbow trout":
         return './genome/trout/Oncorhynchus_mykiss.USDA_OmykA_1.1.dna.toplevel.fa'
     if Target_Genome == "Pteropus alecto (ASM32557v1) - Black flying fox":
         return './genome/foxASM32557v1/GCF_000325575.1_ASM32557v1_genomic.fna'
     if Target_Genome == "Macaca fascicularis (6.0) - Crab-eating macaque":
         return './genome/macaca60/Macaca_fascicularis.Macaca_fascicularis_6.0.dna.toplevel.fa'
     if Target_Genome == "Dicentrarchus labrax - (European seabass)":
         return './genome/seabass/Dicentrarchus_labrax.dlabrax2021.dna.toplevel.fa'
     if Target_Genome == "Equus asinus (ASM1607732v2) - Ass":
         return './genome/Equus/Equus_asinus.ASM1607732v2.dna.toplevel.fa'
     if Target_Genome == "Mus musculus (GRCm39) - Mouse":
         return './genome/mousemm9/GCF_000001635.27_GRCm39_genomic.fna'
     if Target_Genome == "Gallus gallus (bGalGal1.mat.broiler.GRCg7b) - Chicken":
         return './genome/chickenGallus7b/Gallus_gallus.bGalGal1.mat.broiler.GRCg7b.dna.toplevel.fa'
     if Target_Genome == "Arabidopsis thaliana (TAIR10.1)-Thale cress":
         return './genome/thaliana/GCF_000001735.4_TAIR10.1_genomic.fna'
     if Target_Genome == "Oryza sativa Japonica Group (Japanese rice)":
         return './genome/Japonica/GCF_034140825.1_ASM3414082v1_genomic.fna'
     if Target_Genome == "Solanum lycopersicum (SL3.1) - Tomato":
         return './genome/tomato/GCF_000188115.5_SL3.1_genomic.fna'
     if Target_Genome == "Zea mays (Zm-B73-REFERENCE-NAM-5.0)-maize":
         return './genome/maize/GCF_902167145.1_Zm-B73-REFERENCE-NAM-5.0_genomic.fna'
     if Target_Genome == "Chlamydomonas_reinhardtii_v5.5":
         return './genome/chlamydomonas/GCF_000002595.2_Chlamydomonas_reinhardtii_v5.5_genomic.fna'
     if Target_Genome == "Solanum tuberosum (SolTub_3.0) - Potato":
         return './genome/potato/GCF_000226075.1_SolTub_3.0_genomic.fna'
     if Target_Genome == "Glycine max(v4.0) - Soybean":
         return './genome/soybean/GCF_000004515.6_Glycine_max_v4.0_genomic.fna'
     if Target_Genome == "Vitis vinifera (ASM3070453v1) - wine grape":
         return './genome/winegrape/GCF_030704535.1_ASM3070453v1_genomic.fna'
     if Target_Genome == "Manihot esculenta (M.esculenta_v8)-cassava":
         return './genome/cassava/GCF_001659605.2_M.esculenta_v8_genomic.fna'
     if Target_Genome == "Malus domestica (ASM211411v1)-apple":
         return './genome/apple/GCF_002114115.1_ASM211411v1_genomic.fna'
     if Target_Genome == "Hordeum vulgare subsp. vulgare (MorexV3_pseudomolecules)-domesticated barley":
         return './genome/barley/GCF_904849725.1_MorexV3_pseudomolecules_assembly_genomic.fna'
     if Target_Genome == "Nicotiana benthamiana(ASM3437652v1)":
         return './genome/nicotiana/GCA_034376525.1_ASM3437652v1_genomic.fna'
     if Target_Genome == "Fragaria vesca (FraVesHawaii_1.0)-Wild strawberry":
         return './genome/strawberry/GCF_000184155.1_FraVesHawaii_1.0_genomic.fna'
     if Target_Genome == "Citrus sinensis (DVS_A1.0) - Sweet orange":
         return './genome/orange/GCF_022201045.2_DVS_A1.0_genomic.fna'
     if Target_Genome == "Theobroma cacao (Criollo_cocoa_genome_V2) - Cacao":
         return './genome/cacao/GCF_000208745.1_Criollo_cocoa_genome_V2_genomic.fna'
     if Target_Genome == "Musa acuminata AAA Group (Cavendish_Baxijiao_AAA) - Dessert banana":
         return './genome/dessertbanana/GCF_036884655.1_Cavendish_Baxijiao_AAA_genomic.fna'
     if Target_Genome == "Arachis ipaensis (Araip1.1) - Wild peanut":
         return './genome/wildpeanut/GCF_000816755.2_Araip1.1_genomic.fna'
     if Target_Genome == "Arachis duranensis (aradu.V14167.gnm2.J7QH) - Wild peanut":
         return './genome/peanutaradu/GCF_000817695.3_aradu.V14167.gnm2.J7QH_genomic.fna'
     if Target_Genome == "Actinidia chinensis (ASM966300v1) - Golden kiwifruit":
         return './genome/kiwifruit/GCA_009663005.1_ASM966300v1_genomic.fna'
     if Target_Genome == "Brassica napus (Da-Ae)-Rape":
         return './genome/rape/GCF_020379485.1_Da-Ae_genomic.fna'
     if Target_Genome == "Sorghum bicolor (Sorghum_bicolor_NCBIv3) - Sorghum":
         return './genome/sorghum/GCF_000003195.3_Sorghum_bicolor_NCBIv3_genomic.fna'
     if Target_Genome == "Panicum virgatum (P.virgatum_v5) - Switchgrass":
         return './genome/switchgrass/GCF_016808335.1_P.virgatum_v5_genomic.fna'
     if Target_Genome == "Cannabis sativa (Cannabis sativa)":
         return './genome/canabis/GCF_029168945.1_ASM2916894v1_genomic.fna'
     if Target_Genome == "Medicago truncatula (MtrunA17r5.0-ANR)-Barrel medic":
         return './genome/truncatula/GCF_003473485.1_MtrunA17r5.0-ANR_genomic.fna'
     if Target_Genome == "Exserohilum turcica Et28A (v1.0)":
         return './genome/turcica/GCF_000359705.1_Setospaeria_trucica_Et28A_v1.0_genomic.fna'
     if Target_Genome == "Capsicum annuum (UCD10Xv1.1)":
         return './genome/annuum/GCF_002878395.1_UCD10Xv1.1_genomic.fna'
     if Target_Genome == "Daucus carota subsp. sativus (DH1 v3.0)- Carrot":
         return './genome/carota/GCF_001625215.2_DH1_v3.0_genomic.fna'
     if Target_Genome == "Petunia axillaris":
         return './genome/Petunia/GCA_029990575.1_ASM2999057v1_genomic.fna'                
     if Target_Genome == "Chlamydomonas reinhardtii(v5.5)":
         return './genome/reinhardtii/GCF_000002595.2_Chlamydomonas_reinhardtii_v5.5_genomic.fna'
     if Target_Genome == "Phaseolus vulgaris (PhaVulg1_0)":
         return './genome/vulgaris/GCF_000499845.1_PhaVulg1_0_genomic.fna'
     if Target_Genome == "Eragrostis tef (tef)":
         return './genome/tef/GCA_000970635.1_ASM97063v1_genomic.fna'
     if Target_Genome == "Schistosoma haematobium (UoM_Shae.V3)":
         return './genome/haematobium/GCF_000699445.3_UoM_Shae.V3_genomic.fna'
     if Target_Genome == "Eucalyptus grandis (rose gum)":
         return './genome/grandis/GCF_016545825.1_ASM1654582v1_genomic.fna'
     if Target_Genome == "Cajanus cajan (C.cajan_V1.1) - pigeon pea":
         return './genome/cajan/GCF_000340665.2_C.cajan_V1.1_genomic.fna'
     if Target_Genome == "Fragilariopsis cylindrus CCMP1102 (Fc_falcon_quiver_polished)":
         return './genome/cylindrus/GCA_900095095.1_Fc_falcon_quiver_polished_genomic.fna'
     if Target_Genome == "Brassica rapa (CAAS_Brap_v3.01) - field mustard":
         return './genome/rapa/GCF_000309985.2_CAAS_Brap_v3.01_genomic.fna'
     if Target_Genome == "Gossypium hirsutum (Gossypium_hirsutum_v2.1) - cotton":
         return './genome/hirsutum/GCF_007990345.1_Gossypium_hirsutum_v2.1_genomic.fna'
     if Target_Genome == "Brassica oleracea var. oleracea (BOL)":
         return './genome/oleracea/GCF_000695525.1_BOL_genomic.fna'
     if Target_Genome == "Nicotiana tabacum (Ntab-TN90) - common tobacco":
         return './genome/tabacum/GCF_000715135.1_Ntab-TN90_genomic.fna'
     if Target_Genome == "Coffea canephora (robusta coffee)":
         return './genome/canephora/GCA_036785865.1_ASM3678586v1_genomic.fna'
     if Target_Genome == "Citrus x clementina (Citrus_clementina_v1.0) - clementine":
         return './genome/clementina/GCF_000493195.1_Citrus_clementina_v1.0_genomic.fna'
     if Target_Genome == "Beta vulgaris subsp. vulgaris (EL10.2) - sugar beet":
         return './genome/betavulgaris/GCF_026745355.1_EL10.2_genomic.fna'
     if Target_Genome == "Kalanchoe fedtschenkoi (K_fedtschenkoi_M2_v1) - South American air plant":
         return './genome/fedtschenkoi/GCA_002312845.1_K_fedtschenkoi_M2_v1_genomic.fna'
     if Target_Genome == "Sesamum indicum (S_indicum_v1.0)-sesame":
         return './genome/indicum/GCF_000512975.1_S_indicum_v1.0_genomic.fna'
     if Target_Genome == "Cucumis sativus (Cucumber_9930_V3) - cucumber":
         return './genome/sativus/GCF_000004075.3_Cucumber_9930_V3_genomic.fna'
     if Target_Genome == "Citrullus lanatus (watermelon)":
         return './genome/lanatus/GCA_039639715.1_ASM3963971v1_genomic.fna'
     if Target_Genome == "Cucumis melo (USDA_Cmelo_AY_1.0) - muskmelon":
         return './genome/melo/GCF_025177605.1_USDA_Cmelo_AY_1.0_genomic.fna'
     if Target_Genome == "Populus trichocarpa (P.trichocarpa_v4.1) - black cottonwood":
         return './genome/trichocarpa/GCF_000002775.5_P.trichocarpa_v4.1_genomic.fna'
     if Target_Genome == "Populus tremula (ddPopTrem1.hap1.1) - European aspen":
         return './genome/tremula/GCA_964106015.1_ddPopTrem1.hap1.1_genomic.fna'
     if Target_Genome == "Physcomitrium patens (Phypa V3)":
         return './genome/patens/GCF_000002425.4_Phypa_V3_genomic.fna'
     if Target_Genome == "Brachypodium distachyon (v3.0) - stiff brome":
         return './genome/distachyon/GCF_000005505.3_Brachypodium_distachyon_v3.0_genomic.fna'
     if Target_Genome == "Nicotiana obtusifolia (NIOBT.version3)":
         return './genome/obtusifolia/GCA_002018475.1_NIOBT.version3_genomic.fna'
     if Target_Genome == "Triticum aestivum (IWGSC CS RefSeq v2.1)-bread wheat":
         return './genome/aestivum/GCF_018294505.1_IWGSC_CS_RefSeq_v2.1_genomic.fna'
     if Target_Genome == "Camelina sativa (Cs)-false flax":
         return './genome/sativa/GCF_000633955.1_Cs_genomic.fna'
     if Target_Genome == "Lactuca sativa (Lsat_Salinas_v11) - garden lettuce":
         return './genome/lasativa/GCF_002870075.4_Lsat_Salinas_v11_genomic.fna'
     if Target_Genome == "Helianthus annuus (HanXRQr2.0-SUNRISE) - common sunflower":
         return './genome/annuus/GCF_002127325.2_HanXRQr2.0-SUNRISE_genomic.fna'
     if Target_Genome == "Elaeis guineensis (EG5) - African oil palm":
         return './genome/guineensis/GCF_000442705.1_EG5_genomic.fna'
     if Target_Genome == "Spirodela polyrhiza (Salk_sp9512.v2) - great duckweed":
         return './genome/polyrhiza/GCA_024713555.1_Salk_sp9512.v2_genomic.fna'
     if Target_Genome == "Setaria viridis (Setaria_viridis_v2.0)":
         return './genome/viridis/GCF_005286985.1_Setaria_viridis_v2.0_genomic.fna'
     if Target_Genome == "Lotus japonicus (LjGifu_v1.2)":
         return './genome/japonicus/GCF_012489685.1_LjGifu_v1.2_genomic.fna'
     if Target_Genome == "Solanum virginianum (SME_r2.5.1) - eggplant":
         return './genome/virginianum/GCA_000787875.1_SME_r2.5.1_genomic.fna'
     if Target_Genome == "Ricinus communis (castor bean)":
         return './genome/communis/GCF_019578655.1_ASM1957865v1_genomic.fna'
     if Target_Genome == "Populus deltoides ":
         return './genome/deltoides/GCA_015852605.2_ASM1585260v2_genomic.fna'
     if Target_Genome == "Marchantia polymorpha subsp. ruderalis (MpTak2_v7.1)":
         return './genome/polymorpha/GCA_037833965.1_MpTak2_v7.1_genomic.fna'
     if Target_Genome == "Humulus lupulus (drHumLupu1.1)-European hop":
         return './genome/lupulus/GCF_963169125.1_drHumLupu1.1_genomic.fna'
     if Target_Genome == "Phaseolus vulgaris (P. vulgaris v2.0 ) - string bean":
         return './genome/pvulgaris/GCA_000499845.2_P._vulgaris_v2.0_genomic.fna'
     if Target_Genome == "Cicer arietinum (ASM33114v1) - chickpea":
         return './genome/arietinum/GCF_000331145.1_ASM33114v1_genomic.fna'
     if Target_Genome == "Panax ginseng (ASM2020560v1) - jinsão":
         return './genome/ginseng/GCA_020205605.1_ASM2020560v1_genomic.fna'
     if Target_Genome == "Erythranthe guttata (Mimgu1_0) - spotted monkey flower":
         return './genome/guttata/GCF_000504015.1_Mimgu1_0_genomic.fna'
     if Target_Genome == "Mentha longifolia (Mlong_CMEN585_v3) - horsemint":
         return './genome/longifolia/GCA_001642375.2_Mlong_CMEN585_v3_genomic.fna'
     if Target_Genome == "Thlaspi arvense (T_arvense_v2)":
         return './genome/arvense/GCA_911865555.2_T_arvense_v2_genomic.fna'
     if Target_Genome == "Vigna radiata var. radiata (Vradiata_ver6) - mung bean":
         return './genome/radiata/GCF_000741045.1_Vradiata_ver6_genomic.fna'
     if Target_Genome == "Phalaenopsis equestris (ASM126359v1)":
         return './genome/equestris/GCF_001263595.1_ASM126359v1_genomic.fna'
     if Target_Genome == "Dendrobium catenatum (ASM160598v2)":
         return './genome/catenatum/GCF_001605985.2_ASM160598v2_genomic.fna'
     if Target_Genome == "Prunus avium (PAV_r1.0)-sweet cherry":
         return './genome/avium/GCF_002207925.1_PAV_r1.0_genomic.fna'
     if Target_Genome == "Saccharum spontaneum (ASM2245720v1)-fodder cane":
         return './genome/spontaneum/GCA_022457205.1_ASM2245720v1_genomic.fna'
     if Target_Genome == "Prunus persica (Prunus_persica_NCBIv2) - peach":
         return './genome/persica/GCA_022457205.1_ASM2245720v1_genomic.fna'
     if Target_Genome == "Brassica juncea (ASM1870372v1)-brown mustard":
         return './genome/juncea/GCA_018703725.1_ASM1870372v1_genomic.fna'
     if Target_Genome == "Cucurbita maxima (Cmax_1.0) - winter squash":
         return './genome/maxima/GCF_002738345.1_Cmax_1.0_genomic.fna'
     if Target_Genome == "Cucurbita moschata (Cmos_1.0) - crookneck pumpkin":
         return './genome/moschata/GCF_002738365.1_Cmos_1.0_genomic.fna'
     if Target_Genome == "Cucurbita pepo subsp. pepo (ASM280686v2) - vegetable marrow":
         return './genome/pepo/GCF_002806865.2_ASM280686v2_genomic.fna'
     if Target_Genome == "Nicotiana glauca (ASM2677062v1) - tree tobacco":
         return './genome/glauca/GCA_026770625.1_ASM2677062v1_genomic.fna'
     if Target_Genome == "Nicotiana attenuata (NIATTr2)":
         return './genome/attenuata/GCF_001879085.1_NIATTr2_genomic.fna'
     if Target_Genome == "Artemisia annua (Aran) -sweet wormwood":
         return './genome/annua/GCA_014162995.1_Aran_genomic.fna'
     if Target_Genome == "Saccharum hybrid cultivar R570 (Saccharum officinarum X spontaneum var R570 v2.1)":
         return './genome/Saccharumhyb/GCA_038087645.1_Saccharum_officinarum_X_spontaneum_var_R570_v2.1_genomic.fna'
     if Target_Genome == "Chrysanthemum makinoi":
         return './genome/makinoi/GCA_910596185.1_chrysanthemum_makinoi_genome_sequence_genomic.fna'
     if Target_Genome == "Chrysanthemum lavandulifolium (ASM2254549v1)":
         return './genome/lavandulifolium/GCA_022545495.1_ASM2254549v1_genomic.fna'
     if Target_Genome == "Chrysanthemum seticuspe(CsGojo-0_v1)":
         return './genome/seticuspe/GCA_019973895.1_CsGojo-0_v1_genomic.fna'
     if Target_Genome == "Pseudomonas syringae pv. tomato str. DC3000 (ASM780v1)":
         return './genome/syringae/GCF_000007805.1_ASM780v1_genomic.fna'
     if Target_Genome == "Papaver somniferum (ASM357369v1) -opium poppy":
         return './genome/somniferum/GCF_003573695.1_ASM357369v1_genomic.fna'
     if Target_Genome == "Solanum pimpinellifolium (SDAU_Spim_LA1589_1.0) - currant tomato":
         return './genome/pimpinellifolium/GCA_034621305.1_SDAU_Spim_LA1589_1.0_genomic.fna'
     if Target_Genome == "Castanea mollissima (ASM1418300v1) - Chinese chestnut":
         return './genome/mollissima/GCA_014183005.1_ASM1418300v1_genomic.fna'
     if Target_Genome == "Populus alba x Populus glandulosa (84K_subgenomeG)":
         return './genome/albax/GCA_033617975.1_84K_subgenomeG_genomic.fna'
     if Target_Genome == "Chenopodium quinoa (ASM168347v1) - quinoa":
         return './genome/quinoa/GCF_001683475.1_ASM168347v1_genomic.fna'
     if Target_Genome == "Benincasa hispida (ASM972705v1) -wax gourd":
         return './genome/hispida/GCF_009727055.1_ASM972705v1_genomic.fna'
     if Target_Genome == "Ipomoea nil (Asagao_1.1) - Japanese morning glory":
         return './genome/nil/GCF_001879475.1_Asagao_1.1_genomic.fna'
     if Target_Genome == "Rosa chinensis (RchiOBHm-V2) - China rose":
         return './genome/chinensis/GCF_002994745.2_RchiOBHm-V2_genomic.fna'
     if Target_Genome == "Catharanthus roseus (ASM2865129v1) - Madagascar periwinkle":
         return './genome/roseus/GCA_028651295.1_ASM2865129v1_genomic.fna'
     if Target_Genome == "Vigna unguiculata (ASM411807v2 ) - cowpea":
         return './genome/unguiculata/GCF_004118075.2_ASM411807v2_genomic.fna'
     if Target_Genome == "Digitaria exilis (DiExil)":
         return './genome/exilis/GCA_015342445.1_DiExil_genomic.fna'
     if Target_Genome == "Raphanus sativus (ASM80110v3) - radish":
         return './genome/rapsativus/GCF_000801105.2_ASM80110v3_genomic.fna'
     if Target_Genome == "Humulus lupulus (drHumLupu1.1) European hop":
         return './genome/hulupulus/GCF_963169125.1_drHumLupu1.1_genomic.fna'
     if Target_Genome == "Cannabis sativa female":
         return './genome/cannabisf/Cannabis_sativa_female.cs10.dna.toplevel.fa'
     if Target_Genome == "Lonicera japonica (ASM2146441v1) Japanese honeysuckle":
         return './genome/japonica/GCA_021464415.1_ASM2146441v1_genomic.fna'
     if Target_Genome == "Ostreococcus tauri (version 140606)":
         return './genome/tauri/GCF_000214015.3_version_140606_genomic.fna'
     if Target_Genome == "Solanum chacoense (chc0917) Chaco potato":
         return './genome/chacoense/GCA_029582705.1_chc0917_genomic.fna'
     if Target_Genome == "Camellia sinensis (AHAU_CSS_1) black tea":
         return './genome/sinensis/GCF_004153795.1_AHAU_CSS_1_genomic.fna'
     if Target_Genome == "Camellia sinensis var. sinensis (AHAU_CSS_2)":
         return './genome/sinensis2/GCA_004153795.2_AHAU_CSS_2_genomic.fna'
     if Target_Genome == "Juglans regia (Walnut 2.0) English walnut":
         return './genome/regia/GCF_001411555.2_Walnut_2.0_genomic.fna'
     if Target_Genome == "Juglans microcarpa (ASM312384v1)":
         return './genome/microcarpa/GCA_003123845.1_ASM312384v1_genomic.fna'
     if Target_Genome == "Ananas comosus (ASM154086v1) pineapple":
         return './genome/comosus/GCF_001540865.1_ASM154086v1_genomic.fna'
     if Target_Genome == "Pyrus x bretschneideri (Pyrus_bretschneideri_v1) Chinese white pear":
         return './genome/bretschneideri/GCF_019419815.1_Pyrus_bretschneideri_v1_genomic.fna'
     if Target_Genome == "Pisum sativum (CAAS_Psat_ZW6_1.0) garden pea":
         return './genome/sativum/GCF_024323335.1_CAAS_Psat_ZW6_1.0_genomic.fna'
     if Target_Genome == "Dianthus caryophyllus (ASM2309106v1) clove pink":
         return './genome/caryophyllus/GCA_023091065.1_ASM2309106v1_genomic.fna'
     if Target_Genome == "Capsella rubella (Caprub1_0)":
         return './genome/rubella/GCF_000375325.1_Caprub1_0_genomic.fna'
     if Target_Genome == "Capsella grandiflora (UAZ_Capgrnd_2)":
         return './genome/grandiflora/GCA_040086895.1_UAZ_Capgrnd_2_genomic.fna'
     if Target_Genome == "Vaccinium corymbosum (ASM1450483v1) American blueberry":
         return './genome/corymbosum/GCA_014504835.1_ASM1450483v1_genomic.fna'
     if Target_Genome == "Picea abies (Pabies01) Norway spruce":
         return './genome/abies/GCA_900067695.1_Pabies01_genomic.fna'
     if Target_Genome == "Stevia rebaudiana (ASM993640v2)":
         return './genome/rebaudiana/GCA_009936405.2_ASM993640v2_genomic.fna'
     if Target_Genome == "Arachis hypogaea (arahy.Tifrunner.gnm1.KYV3) peanut":
         return './genome/hypogaea/GCF_003086295.2_arahy.Tifrunner.gnm1.KYV3_genomic.fna'
     if Target_Genome == "Arachis hypogaea (arahy.Tifrunner.gnm2.J5K5) peanut":
         return './genome/hypogaea5/GCA_003086295.3_arahy.Tifrunner.gnm2.J5K5_genomic.fna'
     if Target_Genome == "Carica papaya (Papaya1.0) papaya":
         return './genome/papaya/GCF_000150535.2_Papaya1.0_genomic.fna'
     if Target_Genome == "Casuarina equisetifolia (ASM2855147v1)":
         return './genome/equisetifolia/GCA_028551475.1_ASM2855147v1_genomic.fna'
     if Target_Genome == "Eucalyptus camaldulensis (ASM1991518v1) Murray red gum":
         return './genome/camaldulensis/GCA_019915185.1_ASM1991518v1_genomic.fna'
     if Target_Genome == "Punica granatum (ASM765513v2) pomegranate":
         return './genome/granatum/GCF_007655135.1_ASM765513v2_genomic.fna'
     if Target_Genome == "Lupinus albus (CNRS_Lalb_1.0) white lupine":
         return './genome/albus/GCA_009771035.1_CNRS_Lalb_1.0_genomic.fna'
     if Target_Genome == "Allium cepa (ASM3076508v1) onion":
         return './genome/cepa/GCA_030765085.1_ASM3076508v1_genomic.fna'
     if Target_Genome == "Citrus trifoliata (ASM1835013v1) hardy orange":
         return './genome/trifoliata/GCA_018350135.1_ASM1835013v1_genomic.fna'
     if Target_Genome == "Marchantia paleacea (ASM1418076v2)":
         return './genome/paleacea/GCA_014180765.2_ASM1418076v2_genomic.fna'
     if Target_Genome == "Morus notabilis (ASM41409v2)":
         return './genome/notabilis/GCF_000414095.1_ASM41409v2_genomic.fna'
     if Target_Genome == "Euphorbia pulcherrima (Ep-USBG2016-0302-DRAFT-NextGenCassava-1.0) poinsettia":
         return './genome/pulcherrima/GCA_947683365.1_Ep-USBG2016-0302-DRAFT-NextGenCassava-1.0_genomic.fna'
     if Target_Genome == "Vicia faba (Hedin2 genome v1) fava bean":
         return './genome/faba/GCA_948472305.1_Hedin2_genome_v1_genomic.fna'
     if Target_Genome == "Vigna umbellata (ASM1883591v1) rice bean":
         return './genome/umbellata/GCF_018835915.1_ASM1883591v1_genomic.fna'
     if Target_Genome == "Hydrangea macrophylla( Hmc_EndlessSummer_p1.0)":
         return './genome/macrophylla/GCA_033977485.1_Hmc_EndlessSummer_p1.0_genomic.fna'
     if Target_Genome == "Capsella bursa-pastoris (ASM3645264v1) shepherd's purse":
         return './genome/pastoris/GCA_036452645.1_ASM3645264v1_genomic.fna'
     if Target_Genome == "Olea europaea var. sylvestris (O_europaea_v1) wild olive":
         return './genome/sylvestris/GCF_002742605.1_O_europaea_v1_genomic.fna'
     if Target_Genome == "Eleusine coracana subsp. coracana (Eleusine_coracana_v1.0 ) Indian finger millet":
         return './genome/coracana/GCA_032690845.1_Eleusine_coracana_v1.0_genomic.fna'
     if Target_Genome == "Vanilla planifolia (ASM2384627v1 ) ASM2384627v1":
         return './genome/planifolia/GCA_023846275.1_ASM2384627v1_genomic.fna'
     if Target_Genome == "Ceratopteris richardii (C.richardii_v2)":
         return './genome/richardii/GCA_020310875.1_C.richardii_v2_genomic.fna'
     if Target_Genome == "Solanum commersonii (CGN18024_1v5_2 ) Commerson's wild potato":
         return './genome/commersonii/GCA_029007595.1_CGN18024_1v5_2_genomic.fna'
     if Target_Genome == "Bryum argenteum (EGI_Barg_1.0)":
         return './genome/argenteum/GCA_037043015.1_EGI_Barg_1.0_genomic.fna'
     if Target_Genome == "Areca catechu (ASM2139784v1 ) areca-nut":
         return './genome/catechu/GCA_021397845.1_ASM2139784v1_genomic.fna'
     if Target_Genome == "Cenchrus americanus (pearl_millet_23DB_ONT_assembly ) bulrush millet":
         return './genome/americanus/GCA_947561735.1_pearl_millet_23DB_ONT_assembly_genomic.fna'
     if Target_Genome == "Drosophila melanogaster ( BDGP6.46) Fruit fly":
         return './genome/melanogaster/Drosophila_melanogaster.BDGP6.46.dna.toplevel.fa'
     if Target_Genome == "Drosophila melanogaster ( BDGP6.32) Fruit fly":
         return './genome/melanogaster632/Drosophila_melanogaster.BDGP6.32.dna.toplevel.fa'
     if Target_Genome == "Apis mellifera (Amel_HAv3.1) honey bee":
         return './genome/mellifera/GCF_003254395.2_Amel_HAv3.1_genomic.fna'
     if Target_Genome == "Musca domestica (Musca_domestica.polishedcontigs.V.1.1) house fly":
         return './genome/domesticamusca/GCF_030504385.1_Musca_domestica.polishedcontigs.V.1.1_genomic.fna'
     if Target_Genome == "Tribolium castaneum (icTriCast1.1) red flour beetle":
         return './genome/castaneum/GCF_031307605.1_icTriCast1.1_genomic.fna'
     if Target_Genome == "Aedes albopictus (AalbF5) Asian tiger mosquito":
         return './genome/albopictus/GCF_035046485.1_AalbF5_genomic.fna'
     if Target_Genome == "Bombyx mori (ASM3026992v2) domestic silkworm":
         return './genome/silkworm/GCF_030269925.1_ASM3026992v2_genomic.fna'
     if Target_Genome == "Plutella xylostella (ilPluXylo3.1) diamondback moth":
         return './genome/xylostella/GCF_932276165.1_ilPluXylo3.1_genomic.fna'
     if Target_Genome == "Bombus terrestris (iyBomTerr1.2) buff-tailed bumblebee":
         return './genome/terrestris/GCF_910591885.1_iyBomTerr1.2_genomic.fna'
     if Target_Genome == "Drosophila suzukii (Dsuz_RU_1.0)":
         return './genome/suzukii/GCF_037355615.1_Dsuz_RU_1.0_genomic.fna'
     if Target_Genome == "Drosophila melanogaster (Release 6 plus ISO1 MT) fruit fly":
         return './genome/drosophila/GCF_000001215.4_Release_6_plus_ISO1_MT_genomic.fna'
     if Target_Genome == "Anopheles gambiae (idAnoGambNW_F1_1) African malaria mosquito":
         return './genome/gambiae/GCF_943734735.2_idAnoGambNW_F1_1_genomic.fna'
     if Target_Genome == "Helicoverpa armigera (ASM3070526v1) cotton bollworm":
         return './genome/armigera/GCF_030705265.1_ASM3070526v1_genomic.fna'
     if Target_Genome == "Diaphorina citri (Diaci psyllid genome assembly version 1.1) Asian citrus psyllid":
         return './genome/citri/GCF_000475195.1_Diaci_psyllid_genome_assembly_version_1.1_genomic.fna'
     if Target_Genome == "Aedes aegypti (AaegL5.0) yellow fever mosquito":
         return './genome/mosquito/GCF_002204515.2_AaegL5.0_genomic.fna'
     if Target_Genome == "Culex quinquefasciatus (VPISU_Cqui_1.0_pri_paternal) southern house mosquito":
         return './genome/quinquefasciatus/GCF_015732765.1_VPISU_Cqui_1.0_pri_paternal_genomic.fna'
     if Target_Genome == "Danaus plexippus (MEX_DaPlex) monarch butterfly":
         return './genome/plexippus/GCF_018135715.1_MEX_DaPlex_genomic.fna'
     if Target_Genome == "Heliconius erato demophoon (SRR8883904)":
         return './genome/demophoon/GCA_018249695.1_SRR8883904_genomic.fna'
     if Target_Genome == "Junonia coenia (SRR10765679) buckeye":
         return './genome/coenia/GCA_018235105.1_SRR10765679_genomic.fna'
     if Target_Genome == "Solenopsis invicta (UNIL_Sinv_3.0) red fire ant":
         return './genome/invicta/GCF_016802725.1_UNIL_Sinv_3.0_genomic.fna'
     if Target_Genome == "Anopheles stephensi (UCI_ANSTEP_V1.0) Asian malaria mosquito":
         return './genome/stephensi/GCF_013141755.1_UCI_ANSTEP_V1.0_genomic.fna'
     if Target_Genome == "Camponotus floridanus (Cflo_v7.5) Florida carpenter ant":
         return './genome/floridanus/GCF_003227725.1_Cflo_v7.5_genomic.fna'
     if Target_Genome == "Harpegnathos saltator (Hsal_v8.6) Jerdon's jumping ant":
         return './genome/saltator/GCF_003227715.2_Hsal_v8.6_genomic.fna'
     if Target_Genome == "Harmonia axyridis (icHarAxyr1.1)":
         return './genome/axyridis/GCF_914767665.1_icHarAxyr1.1_genomic.fna'
     if Target_Genome == "Pieris rapae (ilPieRapa1.1) cabbage white":
         return './genome/rapae/GCF_905147795.1_ilPieRapa1.1_genomic.fna'
     if Target_Genome == "Cimex lectularius (Clec_2.1) bed bug":
         return './genome/lectularius/GCF_000648675.2_Clec_2.1_genomic.fna'
     if Target_Genome == "Spodoptera frugiperda (AGI-APGP_CSIRO_Sfru_2.0) fall armyworm":
         return './genome/frugiperda/GCF_023101765.2_AGI-APGP_CSIRO_Sfru_2.0_genomic.fna'
     if Target_Genome == "Clitarchus hookeri (ASM4018264v1) smooth stick-insect":
         return './genome/hookeri/GCA_040182645.1_ASM4018264v1_genomic.fna'
     if Target_Genome == "Bemisia tabaci (ASM185493v1) sweet potato whitefly":
         return './genome/tabaci/GCF_001854935.1_ASM185493v1_genomic.fna'
     if Target_Genome == "Anopheles sinensis (AS2)":
         return './genome/anopheles/GCA_000441895.2_AS2_genomic.fna'
     if Target_Genome == "Lasius niger (ASM104565v1)":
         return './genome/niger/GCA_001045655.1_ASM104565v1_genomic.fna'
     if Target_Genome == "Nippostrongylus brasiliensis (ASM3055315v1)":
         return './genome/brasiliensis/GCA_030553155.1_ASM3055315v1_genomic.fna'
     if Target_Genome == "Ostrinia furnacalis (ASM419383v2) Asian corn borer":
         return './genome/furnacalis/GCF_004193835.3_ASM419383v2_genomic.fna'
     if Target_Genome == "Diabrotica virgifera virgifera (PGI_DIABVI_V3a) western corn rootworm":
         return './genome/virgifera/GCF_917563875.1_PGI_DIABVI_V3a_genomic.fna'
     if Target_Genome == "Archegozetes longisetosus (Caltech_Along_2.0)":
         return './genome/longisetosus/GCA_018873245.2_Caltech_Along_2.0_genomic.fna'
     if Target_Genome == "Oncopeltus fasciatus (Ofas_2.0) milkweed bug":
         return './genome/fasciatus/GCA_000696205.2_Ofas_2.0_genomic.fna'
     if Target_Genome == "Coccinella septempunctata ( icCocSept1.1) seven-spotted ladybird":
         return './genome/septempunctata/GCF_907165205.1_icCocSept1.1_genomic.fna'
     if Target_Genome == "Myzus persicae (MPER_G0061.0) green peach aphid":
         return './genome/persicae/GCF_001856785.1_MPER_G0061.0_genomic.fna'
     if Target_Genome == "Hermetia illucens (iHerIll2.2.curated.20191125 ) black soldier fly":
         return './genome/illucens/GCF_905115235.1_iHerIll2.2.curated.20191125_genomic.fna'
     if Target_Genome == "Conogethes punctiferalis (ASM3116337v1) durian fruit borer":
         return './genome/punctiferalis/GCA_031163375.1_ASM3116337v1_genomic.fna'
     if Target_Genome == "Drosophila simulans (Prin_Dsim_3.1)":
         return './genome/simulans/GCF_016746395.2_Prin_Dsim_3.1_genomic.fna'
     if Target_Genome == "Anopheles arabiensis (AaraD3)":
         return './genome/arabiensis/GCF_016920715.1_AaraD3_genomic.fna'
     if Target_Genome == "Schistocerca gregaria (iqSchGreg1.2) desert locust":
         return './genome/gregaria/GCF_023897955.1_iqSchGreg1.2_genomic.fna'
     if Target_Genome == "Struthio camelus australis (ASM69896v1) - African ostrichAfrican ostrich":
         return './genome/australis/Struthio_camelus_australis.ASM69896v1.dna.toplevel.fa'
     if Target_Genome == "Mus spretus (SPRET_EiJ_v1) Algerian mouse":
         return './genome/spretus/Mus_spretus.SPRET_EiJ_v1.dna.toplevel.fa'
     if Target_Genome == "Mus musculus (129S1_SvImJ_v1) Mouse 129S1_SvImJ_v1":
         return './genome/mousesvimj/Mus_musculus_129s1svimj.129S1_SvImJ_v1.dna.toplevel.fa'
     if Target_Genome == "Mus musculus (A_J_v1) Mouse A_J_v1":
         return './genome/mouseajv/Mus_musculus_aj.A_J_v1.dna.toplevel.fa'
     if Target_Genome == "Mus musculus (AKR_J_v1) Mouse 	AKR_J_v1":
         return './genome/mouseakr/Mus_musculus_akrj.AKR_J_v1.dna.toplevel.fa'
     if Target_Genome == "Mus musculus (BALB_cJ_v1) Mouse BALB_cJ_v1":
         return './genome/mousebalb/Mus_musculus_balbcj.BALB_cJ_v1.dna.toplevel.fa'
     if Target_Genome == "Mus musculus (C3H_HeJ_v1) Mouse C3H_HeJ_v1":
         return './genome/mousec3h/Mus_musculus_c3hhej.C3H_HeJ_v1.dna.toplevel.fa'
     if Target_Genome == "Mus musculus (C57BL_6NJ_v1) Mouse  C57BL_6NJ_v1":
         return './genome/mousec57/Mus_musculus_c57bl6nj.C57BL_6NJ_v1.dna.toplevel.fa'
     if Target_Genome == "Mus musculus (CAST_EiJ_v1) Mouse CAST/EiJ":
         return './genome/mousecast/Mus_musculus_casteij.CAST_EiJ_v1.dna.toplevel.fa'
     if Target_Genome == "Mus musculus (CBA_J_v1) Mouse CBA/J":
         return './genome/mousecba/Mus_musculus_cbaj.CBA_J_v1.dna.toplevel.fa'
     if Target_Genome == "Mus musculus (DBA_2J_v1) Mouse DBA/2J":
         return './genome/mousedba/Mus_musculus_dba2j.DBA_2J_v1.dna.toplevel.fa'
     if Target_Genome == "Mus musculus (FVB_NJ_v1) Mouse FVB/NJ":
         return './genome/mousefvb/Mus_musculus_fvbnj.FVB_NJ_v1.dna.toplevel.fa'
     if Target_Genome == "Mus musculus (LP_J_v1) Mouse  LP/J":
         return './genome/mouselp/Mus_musculus_lpj.LP_J_v1.dna.toplevel.fa'
     if Target_Genome == "Mus musculus (Mmur_3.0) Mouse Lemur":
         return './genome/mouselemur/Microcebus_murinus.Mmur_3.0.dna.toplevel.fa'
     if Target_Genome == "Mus musculus (NOD_ShiLtJ_v1) Mouse NOD/ShiLtJ":
         return './genome/mousenod/Mus_musculus_nodshiltj.NOD_ShiLtJ_v1.dna.toplevel.fa'
     if Target_Genome == "Mus musculus (NZO_HlLtJ_v1) Mouse NZO/HlLtJ":
         return './genome/mousenzo/Mus_musculus_nzohlltj.NZO_HlLtJ_v1.dna.toplevel.fa'
     if Target_Genome == "Mus musculus (PWK_PhJ_v1) Mouse PWK/PhJ":
         return './genome/mousepwk/Mus_musculus_pwkphj.PWK_PhJ_v1.dna.toplevel.fa'
     if Target_Genome == "Mus musculus (WSB_EiJ_v1) Mouse WSB/EiJ":
         return './genome/mousewsb/Mus_musculus_wsbeij.WSB_EiJ_v1.dna.toplevel.fa'
     if Target_Genome == "Mus musculus (CAROLI_EIJ_v1.1) Ryukyu mouse":
         return './genome/mouseryu/Mus_caroli.CAROLI_EIJ_v1.1.dna.toplevel.fa'
     if Target_Genome == "Mus musculus (PAHARI_EIJ_v1.1) Shrew mouse":
         return './genome/mouseshre/Mus_pahari.PAHARI_EIJ_v1.1.dna.toplevel.fa'
     if Target_Genome == "Mus musculus (MUSP714) Steppe mouse":
         return './genome/mousestep/Mus_spicilegus.MUSP714.dna.toplevel.fa'
     if Target_Genome == "Vicugna pacos (vicPac1) Alpaca":
         return './genome/pacos/Vicugna_pacos.vicPac1.dna.toplevel.fa'
     if Target_Genome == "Marmota marmota marmota (marMar2.1) Alpine marmot":
         return './genome/marmota/Marmota_marmota_marmota.marMar2.1.dna.toplevel.fa'
     if Target_Genome == "Poecilia formosa (Poecilia_formosa-5.1.2) Amazon molly":
         return './genome/formosa/Poecilia_formosa.PoeFor_5.1.2.dna.toplevel.fa'
     if Target_Genome == "Castor canadensis (C.can_genome_v1.0) American beaver":
         return './genome/canadensis/Castor_canadensis.C.can_genome_v1.0.dna.toplevel.fa'
     if Target_Genome == "Bison bison bison (Bison_UMD1.0) American bison":
         return './genome/bison/Bison_bison_bison.Bison_UMD1.0.dna.toplevel.fa'
     if Target_Genome == " Caenorhabditis elegans 	(WBcel235 )Caenorhabditis elegans (Nematode, N2)":
         return './genome/elegans/Caenorhabditis_elegans.WBcel235.dna.toplevel.fa'
     if Target_Genome == "Aspergillus niger ATCC 1015 (ASPNI v3.0)":
         return './genome/aspni/GCA_000230395.2_ASPNI_v3.0_genomic.fna'
     if Target_Genome == "Escherichia coli K-12 (GCA_004919995)":
         return './genome/ecoli/Escherichia_coli_k_12_gca_004919995.ASM491999v1_.dna.toplevel.fa'
     if Target_Genome == "Saccharomycetales 	(GCA_000027005.1) Komagataella pastoris":
         return './genome/Saccharomycetales/Komagataella_pastoris.GCA_000027005.1.dna.toplevel.fa'
     if Target_Genome == "Saccharomycetales (ASM170810v1) Komagataella pastoris":
         return './genome/Komagataella/Komagataella_pastoris_gca_001708105.ASM170810v1.dna.toplevel.fa'
     if Target_Genome == "Leishmania major (ASM272v2)":
         return './genome/leishmania/Leishmania_major.ASM272v2.dna.toplevel.fa'
     if Target_Genome == "Paracoccus denitrificans PD1222":
         return './genome/denitrificans/Paracoccus_denitrificans_pd1222_gca_000203895.ASM20389v1.dna.toplevel.fa'
     if Target_Genome == "Metarhizium anisopliae BRIP 53293 (ASM42696v1)":
         return './genome/anisopliae/Metarhizium_anisopliae_brip_53293_gca_000426965.ASM42696v1.dna.toplevel.fa'
     if Target_Genome == "Metarhizium anisopliae ARSEF 549 (MAN_1.0)":
         return './genome/anisopliae549/Metarhizium_anisopliae_arsef_549_gca_000814975.MAN_1.0.dna.toplevel.fa'
     if Target_Genome == "Metarhizium anisopliae BRIP 53284 (ASM42698v1)":
         return './genome/anisopliae53284/Metarhizium_anisopliae_brip_53284_gca_000426985.ASM42698v1.dna.toplevel.fa'
     if Target_Genome == "Metarhizium anisopliae str. E6 (Metarhizium_anisopliae)":
         return './genome/anisopliaee6/Metarhizium_anisopliae_gca_000739145.Metarhizium_anisopliae.dna.toplevel.fa'
     if Target_Genome == "Rhodococcus jostii RHA1 (GCA_000014565)":
         return './genome/jostii/Rhodococcus_jostii_rha1_gca_000014565.ASM1456v1_.dna.toplevel.fa'
     if Target_Genome == "Klebsiella pneumoniae subsp. pneumoniae MGH 78578 (GCA_000016305)":
         return './genome/pneumoniae/Klebsiella_pneumoniae_subsp_pneumoniae_mgh_78578_gca_000016305.ASM1630v1.dna.toplevel.fa'
     if Target_Genome == "Plasmodium falciparum 3D7":
         return './genome/falciparum3d7/Plasmodium_falciparum.ASM276v2.dna.toplevel.fa'
     if Target_Genome == "Plasmodium falciparum 7G8 (GCA_000150435.3)":
         return './genome/falciparum7g8/Plasmodium_falciparum_7g8_gca_000150435.Plas_falc_7G8_V1.dna.toplevel.fa'
     if Target_Genome == "Plasmodium falciparum CAMP/Malaysia (GCA_000521115.1)":
         return './genome/falciparumcamp/Plasmodium_falciparum_camp_malaysia_gca_000521115.Plas_falc_Malayan_Camp_V1.dna.toplevel.fa'
     if Target_Genome == "Plasmodium falciparum Dd2 (GCA_000149795.1)":
         return './genome/falciparumdd2/Plasmodium_falciparum_dd2_gca_000149795.ASM14979v1.dna.toplevel.fa'
     if Target_Genome == "Plasmodium falciparum FCH/4 (GCA_000521155.1)":
         return './genome/falciparumfch/Plasmodium_falciparum_fch_4_gca_000521155.Plas_falc_FCH_4_V2.dna.toplevel.fa'
     if Target_Genome == "Plasmodium falciparum HB3 (GCA_000149665.2)":
         return './genome/falciparumhb3/Plasmodium_falciparum_hb3_gca_000149665.ASM14966v2.dna.toplevel.fa'
     if Target_Genome == "Plasmodium falciparum IGH-CR14 (GCA_000186055.2)":
         return './genome/falciparumigh/Plasmodium_falciparum_igh_cr14_gca_000186055.ASM18605v2.dna.toplevel.fa'
     if Target_Genome == "Plasmodium falciparum MaliPS096_E11 (GCA_000521035.1)":
         return './genome/falciparummali/Plasmodium_falciparum_malips096_e11_gca_000521035.Plas_falc_MaliPS096_E11_V1.dna.toplevel.fa'
     if Target_Genome == "Plasmodium falciparum NF135/5.C10 (GCA_000521075.1)":
         return './genome/falciparumnf/Plasmodium_falciparum_nf135_5_c10_gca_000521075.Plas_falc_NF135_5_C10_V1.dna.toplevel.fa'
     if Target_Genome == "Plasmodium falciparum NF54 (GCA_000401695.2)":
         return './genome/falciparumnf54/Plasmodium_falciparum_nf54_gca_000401695.Plas_falc_NF4_V1.dna.toplevel.fa'
     if Target_Genome == "Plasmodium falciparum NF54 (GCA_002831795.1)":
         return './genome/falciparum542/Plasmodium_falciparum_nf54_gca_002831795.ASM283179v1.dna.toplevel.fa'
     if Target_Genome == "Plasmodium falciparum Palo Alto/Uganda (GCA_000521095.1)":
         return './genome/falciparumpalo/Plasmodium_falciparum_palo_alto_uganda_gca_000521095.Plas_falc_Uganda_Palo-Alto_FUP_H_V1.dna.toplevel.fa'
     if Target_Genome == "Plasmodium falciparum RAJ116 (GCA_000186025.2)":
         return './genome/falciparumraji/Plasmodium_falciparum_raj116_gca_000186025.ASM18602v2.dna.toplevel.fa'
     if Target_Genome == "Plasmodium falciparum Santa Lucia (GCA_000150455.3)":
         return './genome/falciparumsanta/Plasmodium_falciparum_santa_lucia_gca_000150455.Plas_falc_Santa_Lucia_Salvador_I_V1.dna.toplevel.fa'
     if Target_Genome == "Plasmodium falciparum Tanzania (2000708) (GCA_000521055.1)":
         return './genome/falciparumtanza/Plasmodium_falciparum_tanzania_2000708__gca_000521055.Plas_falc_02000708_V1.dna.toplevel.fa'
     if Target_Genome == "Plasmodium falciparum UGT5.1 (GCA_000401715.2)":
         return './genome/falciparumugt/Plasmodium_falciparum_ugt5_1_gca_000401715.Plas_falc_5_1_V1.dna.toplevel.fa'
     if Target_Genome == "Plasmodium falciparum Vietnam Oak-Knoll (FVO) (GCA_000521015.1)":
         return './genome/falciparumvet/Plasmodium_falciparum_vietnam_oak_knoll_fvo__gca_000521015.Plas_falc_Vietnam_Oak-Knoll_FVO_V1.dna.toplevel.fa'
     if Target_Genome == "Limosilactobacillus mucosae LM1 (GCA_000248095)":
         return './genome/mucosae/Limosilactobacillus_mucosae_lm1_gca_000248095.ASM24809v3_.dna.toplevel.fa'
     if Target_Genome == "Phaeodactylum tricornutum (ASM15095v2)":
         return './genome/tricornutum/Phaeodactylum_tricornutum.ASM15095v2.dna.toplevel.fa'
     if Target_Genome == "Corynebacterium glutamicum ATCC 13032 (GCA_000011325)":
         return './genome/glutamicum/Corynebacterium_glutamicum_atcc_13032_gca_000011325.ASM1132v1_.dna.toplevel.fa'
     if Target_Genome == "Mycobacterium tuberculosis variant bovis AF2122/97 (GCA_000195835)":
         return './genome/tuberculosis/Mycobacterium_bovis_af2122_97_gca_000195835.ASM19583v2_.dna.toplevel.fa'
     if Target_Genome == "Mycobacterium tuberculosis variant africanum (GCA_001544855)":
         return './genome/africanum/Mycobacterium_tuberculosis_variant_africanum_gca_001544855.ASM154485v1_.dna.toplevel.fa'
     if Target_Genome == "Mycobacterium tuberculosis variant microti OV254 (GCA_002865895)":
         return './genome/microti/Mycobacterium_tuberculosis_variant_microti_ov254_gca_002865895.ASM286589v1_.dna.toplevel.fa'
     if Target_Genome == "Mycobacterium tuberculosis variant pinnipedii (GCA_003027895)":
         return './genome/pinnipedii/Mycobacterium_tuberculosis_variant_pinnipedii_gca_003027895.ASM302789v2_.dna.toplevel.fa'
     if Target_Genome == "Leishmania infantum (GCA_900500625.1)":
         return './genome/infantum/Leishmania_infantum_gca_900500625.LINF.dna.toplevel.fa'
     if Target_Genome == "Staphylococcus aureus subsp. aureus str. Newman (GCA_000010465)":
         return './genome/aureus/Staphylococcus_aureus_subsp_aureus_str_newman_gca_000010465.ASM1046v1_.dna.toplevel.fa'
     if Target_Genome == "Pseudomonas putida KT2440 (GCA_000007565)":
         return './genome/putida/Pseudomonas_putida_kt2440_gca_000007565.ASM756v2_.dna.toplevel.fa'
     if Target_Genome == "Clostridium acetobutylicum ATCC 824 (GCA_000008765)":
         return './genome/acetobutylicum/Clostridium_acetobutylicum_atcc_824_gca_000008765.ASM876v1_.dna.toplevel.fa'
     if Target_Genome == "Paraburkholderia sacchari str. LMG 19450 (GCA_000785435)":
         return './genome/sacchari/Paraburkholderia_sacchari_gca_000785435.ASM78543v1_.dna.toplevel.fa'
     if Target_Genome == "Trypanosoma cruzi Dm28c":
         return './genome/cruzi/Trypanosoma_cruzi_dm28c_gca_000496795.T.cruzi.Dm28c_v01.dna.toplevel.fa'
     if Target_Genome == "Debaryomyces hansenii CBS767 (GCA_000006445)":
         return './genome/hansenii/Debaryomyces_hansenii_cbs767_gca_000006445.ASM644v2.dna.toplevel.fa'
     if Target_Genome == "Schistosoma mansoni (Flatworm)":
         return './genome/mansoni/Schistosoma_mansoni.Smansoni_v7.dna.toplevel.fa'
     if Target_Genome == "Listeria monocytogenes (GCA_006364655)":
         return './genome/monocytogenes/Listeria_monocytogenes_gca_006364655.ASM636465v1_.dna.toplevel.fa'
     if Target_Genome == "Clostridium beijerinckii NCIMB 8052 (GCA_000016965)":
         return './genome/beijerinckii/Clostridium_beijerinckii_ncimb_8052_gca_000016965.ASM1696v1_.dna.toplevel.fa'
     if Target_Genome == "Clostridium tyrobutyricum DIVETGP (GCA_000577845)":
         return './genome/tyrobutyricum/Clostridium_tyrobutyricum_divetgp_gca_000577845.CTDIVETGP_.dna.toplevel.fa'
     if Target_Genome == "Clostridium tyrobutyricum str. Cirm BIA 2237 (GCA_004924375)":
         return './genome/tyrobutyricumbia/Clostridium_tyrobutyricum_gca_004924375.ASM492437v1_.dna.toplevel.fa'
     if Target_Genome == "Peptoclostridium acidaminophilum DSM 3953 (GCA_000597865)":
         return './genome/acidaminophilum/Peptoclostridium_acidaminophilum_dsm_3953_gca_000597865.ASM59786v1_.dna.toplevel.fa'
     if Target_Genome == "Peptoclostridium litorale DSM 5388 str. W6 (GCA_000699585)":
         return './genome/litorale/Peptoclostridium_litorale_dsm_5388_gca_000699585.CLIT1_.dna.toplevel.fa'
     if Target_Genome == "Peptoclostridium sp. AF21-18 (GCA_003478825)":
         return './genome/peptoclostridium/Peptoclostridium_sp_af21_18_gca_003478825.ASM347882v1_.dna.toplevel.fa'
     if Target_Genome == "Clostridium carboxidivorans P7 (GCA_000175595)":
         return './genome/carboxidivorans/Clostridium_carboxidivorans_p7_gca_000175595.ASM17559v1_.dna.toplevel.fa'
     if Target_Genome == "Clostridium kluyveri DSM 555 (GCA_000016505)":
         return './genome/kluyveri/Clostridium_kluyveri_dsm_555_gca_000016505.ASM1650v1_.dna.toplevel.fa'
     if Target_Genome == "Clavispora lusitaniae ATCC 42720":
         return './genome/lusitaniae/Clavispora_lusitaniae_atcc_42720_gca_000003835.ASM383v1.dna.toplevel.fa'
     if Target_Genome == "Clavispora lusitaniae str. CBS 6936":
         return './genome/lusitaniaecbs/Clavispora_lusitaniae_gca_001673695.ASM167369v2.dna.toplevel.fa'
     if Target_Genome == "Trypanosoma brucei equiperdum str. IVM-t1 (GCA_003543875.1)":
         return './genome/equiperdum/Trypanosoma_brucei_equiperdum_gca_003543875.ASM354387v1.dna.toplevel.fa'
     if Target_Genome == "Thalassiosira pseudonana":
         return './genome/pseudonana/Thalassiosira_pseudonana.ASM14940v2.dna.toplevel.fa'
     if Target_Genome == "Saccharomyces cerevisiae str. 131":
         return './genome/cerevisiae131/Saccharomyces_cerevisiae_gca_001983315.ASM198331v1.dna.toplevel.fa'
     if Target_Genome == "Saccharomyces cerevisiae str. Kagoshima No.2":
         return './genome/cerevisiae2/Saccharomyces_cerevisiae_gca_002335645.ScerevisiaeKagoshima_assembly01.dna.toplevel.fa'
     if Target_Genome == "Saccharomyces cerevisiae str. P-684":
         return './genome/cerevisiae684/Saccharomyces_cerevisiae_gca_014132395.Scer_P-684_01.dna.toplevel.fa'
     if Target_Genome == "Saccharomyces cerevisiae str. Pf-1":
         return './genome/cerevisiaepf/Saccharomyces_cerevisiae_gca_009014655.Scer_Pf_1_01.dna.toplevel.fa'
     if Target_Genome == "Strongyloides ratti (Threadworm)":
         return './genome/threadworm/Strongyloides_ratti.S_ratti_ED321_v5_0_4.dna.toplevel.fa'
     if Target_Genome == "Thioalkalivibrio versutus str. D301 (GCA_001020955)":
         return './genome/versutusd301/Thioalkalivibrio_versutus_gca_001020955.ASM102095v1_.dna.toplevel.fa'
     if Target_Genome == "Thioalkalivibrio versutus str. AL 2 (GCA_001999325)":
         return './genome/versutusal2/Thioalkalivibrio_versutus_gca_001999325.ASM199932v1_.dna.toplevel.fa'
     if Target_Genome == "Rhodotorula toruloides str. NBRC 0880":
         return './genome/toruloides/Rhodotorula_toruloides_gca_000988875.ASM98887v2.dna.toplevel.fa'
     if Target_Genome == "Methylorubrum extorquens AM1 (GCA_000022685)":
         return './genome/extorquens/Methylorubrum_extorquens_am1_gca_000022685.ASM2268v1_.dna.toplevel.fa'
     if Target_Genome == "Candidatus Brocadia sinica JPN1 (GCA_000949635)":
         return './genome/sinica/Candidatus_brocadia_sinica_jpn1_gca_000949635.ASM94963v1_.dna.toplevel.fa'
     if Target_Genome == "Clostridium acetobutylicum ATCC 824 (GCA_000008765)":
         return './genome/acetobutylicumatcc/Clostridium_acetobutylicum_atcc_824_gca_000008765.ASM876v1_.dna.toplevel.fa'
     if Target_Genome == "Acinetobacter baumannii (GCA_006369845)":
         return './genome/baumannii/Acinetobacter_baumannii_gca_006369845.ASM636984v1_.dna.toplevel.fa'
     if Target_Genome == "Acinetobacter baumannii ATCC 19606 = CIP 70.34 = JCM 6841 (GCA_000162295)":
         return './genome/baumanniiatcc/Acinetobacter_baumannii_atcc_19606_cip_70_34_jcm_6841_gca_000162295.ASM16229v1_.dna.toplevel.fa'
     if Target_Genome == "Candida albicans SC5314 (Cand_albi_SC5314_V3) (GCA_000784655)":
         return './genome/albicans/Candida_albicans_sc5314_gca_000784655.Cand_albi_SC5314_V3.dna.toplevel.fa'
     if Target_Genome == "Candida albicans SC5314 (Cand_albi_SC5314_V4) (GCA_000784635)":
         return './genome/albicansv4/Candida_albicans_sc5314_gca_000784635.Cand_albi_SC5314_V4.dna.toplevel.fa'
     if Target_Genome == "Candida glabrata CBS138 (GCA_000002545.2)":
         return './genome/glabrata/Candida_glabrata.GCA000002545v2.dna.toplevel.fa'
     if Target_Genome == "Fusobacterium nucleatum subsp. nucleatum ATCC 25586 (GCA_000007325)":
         return './genome/nucleatum/Fusobacterium_nucleatum_subsp_nucleatum_atcc_25586_gca_000007325.ASM732v1.dna.toplevel.fa'
     if Target_Genome == "Paenibacillus polymyxa (GCA_900454525)":
         return './genome/polymyxa/Paenibacillus_polymyxa_gca_900454525.49508_G02_.dna.toplevel.fa'
     if Target_Genome == "Clostridium pasteurianum DSM 525 = ATCC 6013 (GCA_000807255)":
         return './genome/pasteurianum/Clostridium_pasteurianum_dsm_525_atcc_6013_gca_000807255.ASM80725v1_.dna.toplevel.fa'
     if Target_Genome == "Mycobacterium tuberculosis variant bovis BCG (GCA_001544735)":
         return './genome/bovis/Mycobacterium_tuberculosis_variant_bovis_bcg_gca_001544735.ASM154473v1_.dna.toplevel.fa'
     if Target_Genome == "Plasmodium knowlesi":
         return './genome/knowlesi/Plasmodium_knowlesi.ASM635v1.dna.toplevel.fa'
     if Target_Genome == "Plasmodium knowlesi str. Malayan Strain Pk1 (A+) (GCA_002140095.1)":
         return './genome/knowlesimala/Plasmodium_knowlesi_gca_002140095.PKNOHv1.dna.toplevel.fa'
     if Target_Genome == "Plasmodium knowlesi strain H (GCA_900004885.2)":
         return './genome/knowlesih/Plasmodium_knowlesi_strain_h_gca_900004885.PKNA1-C.2.dna.toplevel.fa'
     if Target_Genome == "Streptomyces ambofaciens ATCC 23877 str. ATCC23877 (GCA_001267885)":
         return './genome/ambofaciens/Streptomyces_ambofaciens_atcc_23877_gca_001267885.ASM126788v1_.dna.toplevel.fa'
     if Target_Genome == "Vibrio cholerae O1 biovar El Tor str. N16961 (GCA_000006745)":
         return './genome/biovar/Vibrio_cholerae_o1_biovar_el_tor_str_n16961_gca_000006745.ASM674v1.dna.toplevel.fa'
     if Target_Genome == "Pseudomonas putida F1 (GCA_000016865)":
         return './genome/putidaf1/Pseudomonas_putida_f1_gca_000016865.ASM1686v1_.dna.toplevel.fa'
     if Target_Genome == "Pantoea agglomerans (GCA_004793995)":
         return './genome/agglomerans/Pantoea_agglomerans_gca_004793995.ASM479399v1_.dna.toplevel.fa'
     if Target_Genome == "Salmonella enterica subsp. enterica serovar Typhimurium str. LT2 (GCA_000006945)":
         return './genome/enterica/Salmonella_enterica_subsp_enterica_serovar_typhimurium_str_lt2_gca_000006945.ASM694v2_.dna.toplevel.fa'
     if Target_Genome == "Ogataea polymorpha str. NCYC 495 leu1.1 (Hanpo2)":
         return './genome/hanpo2/Ogataea_polymorpha_gca_001664045.Hanpo2.dna.toplevel.fa'
     if Target_Genome == "Bdellovibrio bacteriovorus HD100 (GCA_000196175)":
         return './genome/bacteriovorus/Bdellovibrio_bacteriovorus_hd100_gca_000196175.ASM19617v1_.dna.toplevel.fa'
     if Target_Genome == "Mnemiopsis leidyi (Warty comb jelly)":
         return './genome/leidyi/Mnemiopsis_leidyi.MneLei_Aug2011.dna.toplevel.fa'
     if Target_Genome == "Bdellovibrio bacteriovorus (GCA_001592755)":
         return './genome/bdellovibrio/Bdellovibrio_bacteriovorus_gca_001592755.ASM159275v1_.dna.toplevel.fa'
     if Target_Genome == "Emiliania huxleyi":
         return './genome/huxleyi/Emiliania_huxleyi.Emiliana_huxleyi_CCMP1516_main_genome_assembly_v1.0.dna.toplevel.fa'
     if Target_Genome == "Schizophyllum commune H4-8":
         return './genome/commune/Schizophyllum_commune_h4_8_gca_000143185.v1.0.dna.toplevel.fa'
     if Target_Genome == "Trichoderma reesei":
         return './genome/reesei/Trichoderma_reesei.GCA_000167675.2.dna.toplevel.fa'
     if Target_Genome == "Trichoderma reesei RUT C-30":
         return './genome/reeseirut/Trichoderma_reesei_rut_c_30_gca_000513815.TrireRUTC30_1.dna.toplevel.fa'
     if Target_Genome == "Toxoplasma gondii ARI (GCA_000250965.2)":
         return './genome/ari/Toxoplasma_gondii_ari_gca_000250965.TGARI_v2.dna.toplevel.fa'
     if Target_Genome == "Toxoplasma gondii CAST (GCA_000256705.2)":
         return './genome/cast/Toxoplasma_gondii_gca_000256705.TGCAST_v2.dna.toplevel.fa'
     if Target_Genome == "Toxoplasma gondii COUG (GCA_000338675.2)":
         return './genome/coug/Toxoplasma_gondii_coug_gca_000338675.TGCOUG_v2.dna.toplevel.fa'
     if Target_Genome == "Toxoplasma gondii FOU (GCA_000224905.2)":
         return './genome/fou/Toxoplasma_gondii_fou_gca_000224905.TGFOU1v02.dna.toplevel.fa'
     if Target_Genome == "Toxoplasma gondii GAB2-2007-GAL-DOM2 (GCA_000325525.2)":
         return './genome/gab2/Toxoplasma_gondii_gab2_2007_gal_dom2_gca_000325525.TGGABGALDOM2_v2.1.dna.toplevel.fa'
     if Target_Genome == "Toxoplasma gondii GT1 (GCA_000149715.2)":
         return './genome/gt1/Toxoplasma_gondii_gt1_gca_000149715.TGGT1.dna.toplevel.fa'
     if Target_Genome == "Toxoplasma gondii MAS (GCA_000224865.2)":
         return './genome/mas/Toxoplasma_gondii_mas_gca_000224865.TGMAS1_v2.dna.toplevel.fa'
     if Target_Genome == "Toxoplasma gondii ME49":
         return './genome/me49/Toxoplasma_gondii.TGA4.dna.toplevel.fa'
     if Target_Genome == "Toxoplasma gondii RUB (GCA_000224805.2)":
         return './genome/rub/Toxoplasma_gondii_rub_gca_000224805.TGRUB_v2.dna.toplevel.fa'
     if Target_Genome == "Toxoplasma gondii TgCATBr9 (GCA_000224825.2)":
         return './genome/tgcat/Toxoplasma_gondii_tgcatbr9_gca_000224825.TGCATBR9_v2.dna.toplevel.fa'
     if Target_Genome == "Toxoplasma gondii TgCatPRC2 (GCA_000256725.2)":
         return './genome/tgcatprc/Toxoplasma_gondii_tgcatprc2_gca_000256725.TGCATPRC2_v2.dna.toplevel.fa'
     if Target_Genome == "Toxoplasma gondii VAND (GCA_000224845.2)":
         return './genome/vand/Toxoplasma_gondii_vand_gca_000224845.TGVAND_v2.dna.toplevel.fa'
     if Target_Genome == "Toxoplasma gondii VEG (GCA_000150015.2)":
         return './genome/veg/Toxoplasma_gondii_veg_gca_000150015.TGVEG.dna.toplevel.fa'
     if Target_Genome == "Toxoplasma gondii p89 (GCA_000224885.2)":
         return './genome/p89/Toxoplasma_gondii_p89_gca_000224885.TGP89A_v02.dna.toplevel.fa'
     if Target_Genome == "Plasmodium berghei (GCA_900095635.1)":
         return './genome/berghei/Plasmodium_berghei_gca_900095635.PbSP11A.dna.toplevel.fa'
     if Target_Genome == "Plasmodium yoelii str. 17X (GCA_900002385.1)":
         return './genome/yoelii17x/Plasmodium_yoelii_gca_900002385.PY17X01.dna.toplevel.fa'
     if Target_Genome == "Plasmodium yoelii str. YM (GCA_900002395.1)":
         return './genome/yoeliiym/Plasmodium_yoelii_gca_900002395.PYYM01.dna.toplevel.fa'
     if Target_Genome == "Plasmodium yoelii yoelii str. 17XNL (GCA_000003085.2)":
         return './genome/yoelii17xnl/Plasmodium_yoelii_yoelii_gca_000003085.ASM308v2.dna.toplevel.fa'
     if Target_Genome == "Arthrospira platensis C1 (GCA_000307915)":
         return './genome/platensisc1/Arthrospira_platensis_c1_gca_000307915.ASM30791v1_.dna.toplevel.fa'
     if Target_Genome == "Arthrospira platensis NIES-39 (GCA_000210375)":
         return './genome/platensisnies/Arthrospira_platensis_nies_39_gca_000210375.ASM21037v1_.dna.toplevel.fa'
     if Target_Genome == "Komagataeibacter rhaeticus AF1 (GCA_000700985)":
         return './genome/rhaeticus/Komagataeibacter_rhaeticus_af1_gca_000700985.GLUCORHAEAF1_v1_.dna.toplevel.fa'
     if Target_Genome == "Komagataeibacter rhaeticus (GCA_900086575)":
         return './genome/komagataeibacter/Komagataeibacter_rhaeticus_gca_900086575.K.rhaeticus_iGEM_genome_.dna.toplevel.fa'
     if Target_Genome == "Bacillus subtilis (GCA_000878265)":
         return './genome/subtilis/Bacillus_subtilis_gca_000878265.ASM87826v1_.dna.toplevel.fa'
     if Target_Genome == "Gonium pectorale":
         return './genome/pectorale/GCA_001584585.1_ASM158458v1_genomic.fna'
     if Target_Genome == "Escherichia coli K-12 (GCA_004919995)":
         return './genome/colik12/Escherichia_coli_k_12_gca_004919995.ASM491999v1_.dna.toplevel.fa'
     if Target_Genome == "Trichoderma harzianum str. T6776":
         return './genome/harzianum/Trichoderma_harzianum_gca_000988865.ASM98886v1.dna.toplevel.fa'
     if Target_Genome == "Trichoderma harzianum str. TR274":
         return './genome/harzianum274/Trichoderma_harzianum_gca_002838845.ASM283884v1.dna.toplevel.fa'
     if Target_Genome == "Trichoderma harzianum str. Tr1":
         return './genome/harzianumTr1/Trichoderma_harzianum_gca_002894145.Tr1.dna.toplevel.fa'
     if Target_Genome == "Trichoderma harzianum CBS 226.95":
         return './genome/harzianumCBS/Trichoderma_harzianum_cbs_226_95_gca_003025095.Triha_v1.0.dna.toplevel.fa'
     if Target_Genome == "Streptomyces albus str. DSM 41398 (GCA_000827005)":
         return './genome/albusdsm/Streptomyces_albus_gca_000827005.ASM82700v1_.dna.toplevel.fa'
     if Target_Genome == "Streptomyces albus subsp. albus (GCA_001541145)":
         return './genome/albusalbus/Streptomyces_albus_subsp_albus_gca_001541145.ASM154114v1_.dna.toplevel.fa'
     if Target_Genome == "Leptospira interrogans serovar Copenhageni str. Fiocruz L1-130 (GCA_000007685)":
         return './genome/fiocruz/Leptospira_interrogans_serovar_copenhageni_str_fiocruz_l1_130_gca_000007685.ASM768v1_.dna.toplevel.fa'
     if Target_Genome == "Leptospira interrogans serovar Copenhageni str. LT2050 (GCA_000216155)":
         return './genome/lT2050/Leptospira_interrogans_serovar_copenhageni_str_lt2050_gca_000216155.gls454150v02_.dna.toplevel.fa'
     if Target_Genome == "Anaplasma phagocytophilum str. HZ (GCA_000013125)":
         return './genome/phagocytophilum/Anaplasma_phagocytophilum_str_hz_gca_000013125.ASM1312v1.dna.toplevel.fa'
     if Target_Genome == "Neisseria meningitidis (GCA_006334835)":
         return './genome/meningitidis/Neisseria_meningitidis_gca_006334835.ASM633483v1_.dna.toplevel.fa'
     if Target_Genome == "Streptococcus pneumoniae (GCA_006376385)":
         return './genome/pneumoniaes/Streptococcus_pneumoniae_gca_006376385.ASM637638v1_.dna.toplevel.fa'
     if Target_Genome == "Escherichia coli str. K-12 substr. MG1655 str. K12 (GCA_000005845)":
         return './genome/mg1655/Escherichia_coli_str_k_12_substr_mg1655_gca_000005845.ASM584v2.dna.toplevel.fa'
     if Target_Genome == "Escherichia coli str. K-12 substr. W3110 (GCA_000010245)":
         return './genome/w3110/Escherichia_coli_str_k_12_substr_w3110_gca_000010245.ASM1024v1_.dna.toplevel.fa'
     if Target_Genome == "Francisella tularensis subsp. holarctica str. FTT_1 (GCA_000833235)":
         return './genome/holarctica/Francisella_tularensis_subsp_holarctica_gca_000833235.ASM83323v1_.dna.toplevel.fa'
     if Target_Genome == "Francisella tularensis subsp. holarctica str. 08T0073 (GCA_001953575)":
         return './genome/holarctica08/Francisella_tularensis_subsp_holarctica_gca_001953575.ASM195357v1_.dna.toplevel.fa'
     if Target_Genome == "Komagataella phaffii CBS 7435 (PicPas_Mar2011)":
         return './genome/phaffii/Komagataella_phaffii_cbs_7435_gca_000223565.PicPas_Mar2011.dna.toplevel.fa'
     if Target_Genome == "Komagataella phaffii CBS 7435 (ASM90023503v1)":
         return './genome/phaffiicbs/Komagataella_phaffii_cbs_7435_gca_900235035.ASM90023503v1.dna.toplevel.fa'
     if Target_Genome == "Komagataella phaffii GS115":
         return './genome/phaffiigs/Komagataella_phaffii_gs115_gca_001746955.ASM174695v1.dna.toplevel.fa'
     if Target_Genome == "Komagataella phaffii str. WT":
         return './genome/phaffiiwt/Komagataella_phaffii_gca_001708085.ASM170808v1.dna.toplevel.fa'
     if Target_Genome == "Mesorhizobium loti str. UFLA 01-765 (GCA_001510895)":
         return './genome/loti/Mesorhizobium_loti_gca_001510895.ASM151089v1_.dna.toplevel.fa'
     if Target_Genome == "Mesorhizobium loti str. R7ANS::ICEMlSym2042 (GCA_001671485)":
         return './genome/loti1/Mesorhizobium_loti_gca_001671485.ASM167148v1_.dna.toplevel.fa'
     if Target_Genome == "Mesorhizobium loti str. NZP2042 (GCA_001672355)":
         return './genome/loti2/Mesorhizobium_loti_gca_001672355.NZP2042_.dna.toplevel.fa'
     if Target_Genome == "Mesorhizobium loti str. NZP2014 (GCA_001672365)":
         return './genome/loti3/Mesorhizobium_loti_gca_001672365.ASM167236v1_.dna.toplevel.fa'
     if Target_Genome == "Mesorhizobium loti (GCA_002356515)":
         return './genome/loti4/Mesorhizobium_loti_gca_002356515.MlotiTONO_1.0_.dna.toplevel.fa'
     if Target_Genome == "Mesorhizobium loti str. LU (GCA_002858745)":
         return './genome/loti5/Mesorhizobium_loti_gca_002858745.ASM285874v1_.dna.toplevel.fa'
     if Target_Genome == "Mesorhizobium loti (GCA_003024615)":
         return './genome/loti6/Mesorhizobium_loti_gca_003024615.ASM302461v1_.dna.toplevel.fa'
     if Target_Genome == "Mesorhizobium loti str. DSM 2626 (GCA_003148495)":
         return './genome/loti7/Mesorhizobium_loti_gca_003148495.ASM314849v1_.dna.toplevel.fa'
     if Target_Genome == "Sinorhizobium meliloti 1021 (GCA_000006965)":
         return './genome/meliloti/Sinorhizobium_meliloti_1021_gca_000006965.ASM696v1.dna.toplevel.fa'
     if Target_Genome == "Clostridium butyricum (GCA_002940805)":
         return './genome/butyricum1/Clostridium_butyricum_gca_002940805.ASM294080v1_.dna.toplevel.fa'
     if Target_Genome == "Clostridium butyricum (GCA_003935945)":
         return './genome/butyricum2/Clostridium_butyricum_gca_003935945.ASM393594v1_.dna.toplevel.fa'
     if Target_Genome == "Synechocystis sp. PCC 6714 (GCA_000478825)":
         return './genome/pcc6714/Synechocystis_sp_pcc_6714_gca_000478825.ASM47882v2_.dna.toplevel.fa'
     if Target_Genome == "Synechocystis sp. PCC 6803 (GCA_000009725)":
         return './genome/pcc6803/Synechocystis_sp_pcc_6803_gca_000009725.ASM972v1.dna.toplevel.fa'
     if Target_Genome == "Lachancea thermotolerans CBS 6340":
         return './genome/thermotolerans/Lachancea_thermotolerans_cbs_6340_gca_000142805.ASM14280v1.dna.toplevel.fa'
     if Target_Genome == "Lactococcus lactis str. C2D (GCA_004022375)":
         return './genome/lactis1/Lactococcus_lactis_gca_004022375.ASM402237v1_.dna.toplevel.fa'
     if Target_Genome == "Lactococcus lactis str. SRCM103457 (GCA_004194355)":
         return './genome/lactis2/Lactococcus_lactis_gca_004194355.ASM419435v1_.dna.toplevel.fa'
     if Target_Genome == "Lactococcus lactis str. gh1 (GCA_004795205)":
         return './genome/lactis3/Lactococcus_lactis_gca_004795205.ASM479520v1_.dna.toplevel.fa'
     if Target_Genome == "Lactococcus lactis str. CH_LC01 (GCA_005146285)":
         return './genome/lactis4/Lactococcus_lactis_gca_005146285.ASM514628v1_.dna.toplevel.fa'
     if Target_Genome == "Ganoderma sinense ZZ0214-1":
         return './genome/sinense/Ganoderma_sinense_zz0214_1_gca_002760635.GanSi1.6.dna.toplevel.fa'
     if Target_Genome == "Komagataeibacter xylinus E25 (GCA_000550765)":
         return './genome/xylinus1/Komagataeibacter_xylinus_e25_gca_000550765.ASM55076v1_.dna.toplevel.fa'
     if Target_Genome == "Komagataeibacter xylinus (GCA_002762195)":
         return './genome/xylinus2/Komagataeibacter_xylinus_gca_002762195.ASM276219v1_.dna.toplevel.fa'
     if Target_Genome == "Komagataeibacter xylinus (GCA_003207915)":
         return './genome/xylinus3/Komagataeibacter_xylinus_gca_003207915.ASM320791v1_.dna.toplevel.fa'
     if Target_Genome == "Komagataeibacter xylinus str. DSM 2325 (GCA_004006375)":
         return './genome/xylinus4/Komagataeibacter_xylinus_gca_004006375.ASM400637v1_.dna.toplevel.fa'
     if Target_Genome == "Komagataeibacter xylinus (GCA_900016225)":
         return './genome/xylinus5/Komagataeibacter_xylinus_gca_900016225.ATCC53582.1_.dna.toplevel.fa'
     if Target_Genome == "Komagataeibacter xylinus NBRC 13693 (GCA_000964505)":
         return './genome/xylinus6/Komagataeibacter_xylinus_nbrc_13693_gca_000964505.ASM96450v1_.dna.toplevel.fa'
     if Target_Genome == "Penicillium chrysogenum str. P2niaD18":
         return './genome/chrysogenum/Penicillium_chrysogenum_gca_000710275.ASM71027v1.dna.toplevel.fa'
     if Target_Genome == "Chlamydia trachomatis 434/Bu (GCA_000068585)":
         return './genome/trachomatis1/Chlamydia_trachomatis_434_bu_gca_000068585.ASM6858v1_.dna.toplevel.fa'
     if Target_Genome == "Chlamydia trachomatis A2497 (GCA_000226605)":
         return './genome/trachomatis2/Chlamydia_trachomatis_a2497_gca_000226605.ASM22660v1_.dna.toplevel.fa'
     if Target_Genome == "Chlamydia trachomatis A/HAR-13 (GCA_000012125)":
         return './genome/trachomatis3/Chlamydia_trachomatis_a_har_13_gca_000012125.ASM1212v1_.dna.toplevel.fa'
     if Target_Genome == "Chlamydia trachomatis D/UW-3/CX (GCA_000008725)":
         return './genome/trachomatis4/Chlamydia_trachomatis_d_uw_3_cx_gca_000008725.ASM872v1.dna.toplevel.fa'
     if Target_Genome == "Chlamydia trachomatis (GCA_001213105)":
         return './genome/trachomatis5/Chlamydia_trachomatis_gca_001213105.5833_5_5_.dna.toplevel.fa'
     if Target_Genome == "Chlamydia trachomatis (GCA_001317725)":
         return './genome/trachomatis6/Chlamydia_trachomatis_gca_001317725.7054_3_86_.dna.toplevel.fa'
     if Target_Genome == "Chlamydia trachomatis (GCA_001317765)":
         return './genome/trachomatis7/Chlamydia_trachomatis_gca_001317765.7396_3_18_.dna.toplevel.fa'
     if Target_Genome == "Chlamydia trachomatis (GCA_001398195)":
         return './genome/trachomatis8/Chlamydia_trachomatis_gca_001398195.7794_5_16_.dna.toplevel.fa'
     if Target_Genome == "Nannochloropsis gaditana CCMP526 (GCA_000240725.1)":
         return './genome/gaditana1/Nannochloropsis_gaditana_ccmp526_gca_000240725.ASM24072v1.dna.toplevel.fa'
     if Target_Genome == "Nannochloropsis gaditana str. B-31 (GCA_000569095.1)":
         return './genome/gaditana2/Nannochloropsis_gaditana_gca_000569095.NagaB31_1.0.dna.toplevel.fa'
     if Target_Genome == "Streptomyces coelicolor str. O-10.2 (GCA_004368945)":
         return './genome/coelicolor1/Streptomyces_coelicolor_gca_004368945.ASM436894v1_.dna.toplevel.fa'
     if Target_Genome == "Streptomyces coelicolor str. O-10.1 (GCA_004368985)":
         return './genome/coelicolor2/Streptomyces_coelicolor_gca_004368985.ASM436898v1_.dna.toplevel.fa'
     if Target_Genome == "Entamoeba histolytica":
         return './genome/histolytica1/Entamoeba_histolytica.JCVI-ESG2-1.0.dna.toplevel.fa'
     if Target_Genome == "Entamoeba histolytica HM-1:IMSS-A (GCA_000365475.1)":
         return './genome/histolytica2/Entamoeba_histolytica_hm_1_imss_a_gca_000365475.EHA_CA_v1.dna.toplevel.fa'
     if Target_Genome == "Entamoeba histolytica HM-1:IMSS-B str. HM3:IMSS-B (GCA_000344925.1)":
         return './genome/histolytica3/Entamoeba_histolytica_hm_1_imss_b_gca_000344925.EHA_CB_v1.dna.toplevel.fa'
     if Target_Genome == "Entamoeba histolytica HM-3:IMSS (GCA_000346345.1)":
         return './genome/histolytica4/Entamoeba_histolytica_hm_3_imss_gca_000346345.EHA.strHM3_v1.dna.toplevel.fa'
     if Target_Genome == "Entamoeba histolytica KU27 (GCA_000338855.1)":
         return './genome/histolytica5/Entamoeba_histolytica_ku27_gca_000338855.EHA_ku27_v1.dna.toplevel.fa'
     if Target_Genome == "Entamoeba histolytica str. HM1:IMSS clone 6 (GCA_001662325.1)":
         return './genome/histolytica6/Entamoeba_histolytica_gca_001662325.Ehistolytica_2016.dna.toplevel.fa'
     if Target_Genome == "Saccharomyces eubayanus str. FM1318":
         return './genome/eubayanus/Saccharomyces_eubayanus_gca_001298625.SEUB3.0.dna.toplevel.fa'
     if Target_Genome == "Fonsecaea monophora":
         return './genome/monophora/Fonsecaea_monophora_gca_001642475.ASM164247v1.dna.toplevel.fa'
     if Target_Genome == "Clostridium cellulovorans 743B (GCA_000145275)":
         return './genome/cellulovorans/Clostridium_cellulovorans_743b_gca_000145275.ASM14527v1_.dna.toplevel.fa'
     if Target_Genome == "Lactobacillus plantarum WCFS1 (GCA_000203855)":
         return './genome/plantarum/Lactobacillus_plantarum_wcfs1_gca_000203855.ASM20385v3.dna.toplevel.fa'
     if Target_Genome == "Rhodococcus opacus B4 (GCA_000010805)":
         return './genome/opacus1/Rhodococcus_opacus_b4_gca_000010805.ASM1080v1_.dna.toplevel.fa'
     if Target_Genome == "Rhodococcus opacus str. R7 (GCA_000736435)":
         return './genome/opacus2/Rhodococcus_opacus_gca_000736435.ASM73643v1_.dna.toplevel.fa'
     if Target_Genome == "Rhodococcus opacus str. 1CP (GCA_001685605)":
         return './genome/opacus3/Rhodococcus_opacus_gca_001685605.ASM168560v1_.dna.toplevel.fa'
     if Target_Genome == "Rhodococcus opacus str. 04-OD7 (GCA_002968035)":
         return './genome/opacus4/Rhodococcus_opacus_gca_002968035.ASM296803v1_.dna.toplevel.fa'
     if Target_Genome == "Rhodococcus opacus str. DSM 44186 (GCA_003626495)":
         return './genome/opacus5/Rhodococcus_opacus_gca_003626495.ASM362649v1_.dna.toplevel.fa'
     if Target_Genome == "Rhodococcus opacus str. ATCC 51882 (GCA_004365075)":
         return './genome/opacus6/Rhodococcus_opacus_gca_004365075.ASM436507v1_.dna.toplevel.fa'
     if Target_Genome == "Rhodococcus opacus M213 (GCA_000264745)":
         return './genome/opacus7/Rhodococcus_opacus_m213_gca_000264745.ASM26474v2_.dna.toplevel.fa'
     if Target_Genome == "Rhodococcus opacus PD630 (GCA_000599545)":
         return './genome/opacus8/Rhodococcus_opacus_pd630_gca_000599545.ASM59954v1_.dna.toplevel.fa'
     if Target_Genome == "Pseudomonas aeruginosa PAO1 (GCA_000006765)":
         return './genome/aeruginosa/Pseudomonas_aeruginosa_pao1_gca_000006765.ASM676v1_.dna.toplevel.fa'
     if Target_Genome == "Pseudomonas aeruginosa UCBPP-PA14 (GCA_000014625)":
         return './genome/aeruginosa2/Pseudomonas_aeruginosa_ucbpp_pa14_gca_000014625.ASM1462v1_.dna.toplevel.fa'
     if Target_Genome == "Legionella pneumophila subsp. pneumophila str. Philadelphia 1 (GCA_000008485)":
         return './genome/pneumophila/Legionella_pneumophila_subsp_pneumophila_str_philadelphia_1_gca_000008485.ASM848v1_.dna.toplevel.fa'
     if Target_Genome == "Legionella pneumophila (GCA_006364635)":
         return './genome/pneumophila2/Legionella_pneumophila_gca_006364635.ASM636463v1_.dna.toplevel.fa'
     if Target_Genome == "Legionella pneumophila str. Lens (GCA_000048665)":
         return './genome/pneumophila3/Legionella_pneumophila_str_lens_gca_000048665.ASM4866v1_.dna.toplevel.fa'
     if Target_Genome == "Legionella pneumophila subsp. pascullei (GCA_001590695)":
         return './genome/pneumophila4/Legionella_pneumophila_subsp_pascullei_gca_001590695.ASM159069v1_.dna.toplevel.fa'
     if Target_Genome == "Legionella pneumophila subsp. pneumophila (GCA_003605955)":
         return './genome/pneumophila5/Legionella_pneumophila_subsp_pneumophila_gca_003605955.L01C.1_n_l_OLDA_.dna.toplevel.fa'
     if Target_Genome == "Rhodobacter capsulatus SB 1003 str. SB1003 (GCA_000021865)":
         return './genome/capsulatus/Rhodobacter_capsulatus_sb_1003_gca_000021865.ASM2186v1_.dna.toplevel.fa'
     if Target_Genome == "Rhodobacter sphaeroides 2.4.1 (GCA_000012905)":
         return './genome/sphaeroides/Rhodobacter_sphaeroides_2_4_1_gca_000012905.ASM1290v2.dna.toplevel.fa'
     if Target_Genome == "Nitrosomonas europaea ATCC 19718 (GCA_000009145)":
         return './genome/europaea/Nitrosomonas_europaea_atcc_19718_gca_000009145.ASM914v1_.dna.toplevel.fa'
     if Target_Genome == "Acanthamoeba castellanii str. Neff (GCA_000313135.1)":
         return './genome/castellanii/Acanthamoeba_castellanii_str_neff_gca_000313135.Acastellanii.strNEFF_v1.dna.toplevel.fa'
     if Target_Genome == "Streptococcus suis (GCA_004922915)":
         return './genome/suis1/Streptococcus_suis_gca_004922915.ASM492291v1_.dna.toplevel.fa'
     if Target_Genome == "Streptococcus suis str. NSUI060 (GCA_001572685)":
         return './genome/suis2/Streptococcus_suis_gca_001572685.ASM157268v1_.dna.toplevel.fa'
     if Target_Genome == "Streptococcus suis str. DN13 (GCA_001640765)":
         return './genome/suis3/Streptococcus_suis_gca_001640765.ASM164076v1_.dna.toplevel.fa'
     if Target_Genome == "Streptococcus suis str. CZ130302 (GCA_002803825)":
         return './genome/suis4/Streptococcus_suis_gca_002803825.ASM280382v1_.dna.toplevel.fa'
     if Target_Genome == "Streptococcus suis str. AH681 (GCA_002812525)":
         return './genome/suis5/Streptococcus_suis_gca_002812525.ASM281252v1_.dna.toplevel.fa'
     if Target_Genome == "Streptococcus suis str. HN136 (GCA_002831545)":
         return './genome/suis6/Streptococcus_suis_gca_002831545.ASM283154v1_.dna.toplevel.fa'
     if Target_Genome == "Streptococcus suis str. NJAU-TF-202 (GCA_002896475)":
         return './genome/suis7/Streptococcus_suis_gca_002896475.ASM289647v1_.dna.toplevel.fa'
     if Target_Genome == "Streptococcus suis str. HN105 (GCA_003144175)":
         return './genome/suis8/Streptococcus_suis_gca_003144175.ASM314417v1_.dna.toplevel.fa'
     if Target_Genome == "Streptococcus suis str. 1081 (GCA_003285245)":
         return './genome/suis9/Streptococcus_suis_gca_003285245.ASM328524v1_.dna.toplevel.fa'
     if Target_Genome == "Streptococcus suis str. HA1003 (GCA_003352205)":
         return './genome/suis10/Streptococcus_suis_gca_003352205.ASM335220v1_.dna.toplevel.fa'
     if Target_Genome == "Streptococcus suis str. WUSS351 (GCA_004843685)":
         return './genome/suis11/Streptococcus_suis_gca_004843685.ASM484368v1_.dna.toplevel.fa'
     if Target_Genome == "Streptococcus suis 05ZYH33 (GCA_000014305)":
         return './genome/suis12/Streptococcus_suis_05zyh33_gca_000014305.ASM1430v1_.dna.toplevel.fa'
     if Target_Genome == "Streptococcus suis 6407 (GCA_000732355)":
         return './genome/suis13/Streptococcus_suis_6407_gca_000732355.ASM73235v1_.dna.toplevel.fa'
     if Target_Genome == "Streptococcus suis BM407 (GCA_000026745)":
         return './genome/suis14/Streptococcus_suis_bm407_gca_000026745.ASM2674v1_.dna.toplevel.fa'
     if Target_Genome == "Streptococcus suis D12 (GCA_000231905)":
         return './genome/suis15/Streptococcus_suis_d12_gca_000231905.ASM23190v1_.dna.toplevel.fa'
     if Target_Genome == "Streptococcus suis GZ1 (GCA_000018185)":
         return './genome/suis16/Streptococcus_suis_gz1_gca_000018185.ASM1818v1_.dna.toplevel.fa'
     if Target_Genome == "Streptococcus suis T15 (GCA_000494895)":
         return './genome/suis17/Streptococcus_suis_t15_gca_000494895.ASM49489v1_.dna.toplevel.fa'
     if Target_Genome == "Clostridioides difficile (GCA_002301955)":
         return './genome/difficile/Clostridioides_difficile_gca_002301955.ASM230195v1_.dna.toplevel.fa'
     if Target_Genome == "Clostridioides difficile 630 (GCA_000009205)":
         return './genome/difficile2/Clostridioides_difficile_630_gca_000009205.ASM920v2.dna.toplevel.fa'
     if Target_Genome == "Clostridioides difficile ATCC 9689 = DSM 1296 (GCA_001077535)":
         return './genome/difficile3/Clostridioides_difficile_atcc_9689_dsm_1296_gca_001077535.ASM107753v2_.dna.toplevel.fa'
     if Target_Genome == "Clostridioides difficile CD160 (GCA_000449425)":
         return './genome/difficile4/Clostridioides_difficile_cd160_gca_000449425.ASM44942v2_.dna.toplevel.fa'
     if Target_Genome == "Clostridioides difficile CD196 (GCA_000085225)":
         return './genome/difficile5/Clostridioides_difficile_cd196_gca_000085225.ASM8522v1_.dna.toplevel.fa'
     if Target_Genome == "Clostridioides difficile F501 (GCA_000450805)":
         return './genome/difficile6/Clostridioides_difficile_f501_gca_000450805.ASM45080v2_.dna.toplevel.fa'
     if Target_Genome == "Clostridioides difficile str. RA09_70 (GCA_001299495)":
         return './genome/difficile7/Clostridioides_difficile_gca_001299495.ASM129949v1_.dna.toplevel.fa'
     if Target_Genome == "Clostridioides difficile str. CD-B18-123 (GCA_005502205)":
         return './genome/difficile8/Clostridioides_difficile_gca_005502205.ASM550220v1_.dna.toplevel.fa'
     if Target_Genome == "Clostridioides difficile str. WCH065050 (GCA_005786645)":
         return './genome/difficile9/Clostridioides_difficile_gca_005786645.ASM578664v1_.dna.toplevel.fa'
     if Target_Genome == "Clostridioides difficile NAP08 (GCA_000164175)":
         return './genome/difficile10/Clostridioides_difficile_nap08_gca_000164175.ASM16417v1_.dna.toplevel.fa'
     if Target_Genome == "Clostridioides difficile P28 (GCA_000450985)":
         return './genome/difficile11/Clostridioides_difficile_p28_gca_000450985.ASM45098v2_.dna.toplevel.fa'
     if Target_Genome == "Clostridioides difficile R20291 (GCA_000027105)":
         return './genome/difficile12/Clostridioides_difficile_r20291_gca_000027105.ASM2710v1_.dna.toplevel.fa'
     if Target_Genome == "Clostridioides difficile Y384 (GCA_000451045)":
         return './genome/difficile13/Clostridioides_difficile_y384_gca_000451045.ASM45104v2_.dna.toplevel.fa'
     if Target_Genome == "Mus musculus (GRCm39) - Mouse":
         return './genome/grcm39/Mus_musculus.GRCm39.dna.toplevel.fa'
     if Target_Genome == "Bos taurus (ARS-UCD1.3) - Cow":
         return './genome/arsd/Bos_taurus.ARS-UCD1.3.dna.toplevel.fa'
     if Target_Genome == "Bos taurus (ARS-UCD1.2) - Cow":
         return './genome/arsd2/Bos_taurus.ARS-UCD1.2.dna.toplevel.fa'
     if Target_Genome == "Canis lupus familiaris (ROS_Cfam_1.0) - Dog":
         return './genome/dog2/Canis_lupus_familiaris.ROS_Cfam_1.0.dna.toplevel.fa'
     if Target_Genome == "Canis lupus familiaris ( Basenji_breed-1.1) - Dog":
         return './genome/dog3/Canis_lupus_familiarisbasenji.Basenji_breed-1.1.dna.toplevel.fa'
     if Target_Genome == "Canis lupus familiaris ( Dog10K_Boxer_Tasha) - Dog":
         return './genome/dog4/Canis_lupus_familiarisboxer.Dog10K_Boxer_Tasha.dna.toplevel.fa'
     if Target_Genome == "Canis lupus familiaris ( UU_Cfam_GSD_1.0) - Dog":
         return './genome/dog5/Canis_lupus_familiarisgsd.UU_Cfam_GSD_1.0.dna.toplevel.fa'
     if Target_Genome == "Canis lupus familiaris ( UMICH_Zoey_3.1) - Dog":
         return './genome/dog6/Canis_lupus_familiarisgreatdane.UMICH_Zoey_3.1.dna.toplevel.fa'
     if Target_Genome == "Rattus norvegicus (mRatBN7.2) - Rat":
         return './genome/rat3/Rattus_norvegicus.mRatBN7.2.dna.toplevel.fa'
     if Target_Genome == "Rattus norvegicus (UTH_Rnor_SHR_Utx) - Rat":
         return './genome/rat4/Rattus_norvegicus_shrutx.UTH_Rnor_SHR_Utx.dna.toplevel.fa'
     if Target_Genome == "Rattus norvegicus (UTH_Rnor_SHRSP_BbbUtx_1.0) - Rat":
         return './genome/rat5/Rattus_norvegicus_shrspbbbutx.UTH_Rnor_SHRSP_BbbUtx_1.0.dna.toplevel.fa'
     if Target_Genome == "Rattus norvegicus (UTH_Rnor_WKY_Bbb_1.0) - Rat":
         return './genome/rat6/Rattus_norvegicus_wkybbb.UTH_Rnor_WKY_Bbb_1.0.dna.toplevel.fa'
     if Target_Genome == "Cavia aperea( CavAp1.0) - Brazilian guinea pig":
         return './genome/pig3/Cavia_aperea.CavAp1.0.dna.toplevel.fa'
     if Target_Genome == "Sus scrofa (Sscrofa11.1 ) - Pig":
         return './genome/pig4/Sus_scrofa.Sscrofa11.1.dna.toplevel.fa'
     if Target_Genome == "Sus scrofa (Bamei_pig_v1) - Bamei Pig":
         return './genome/pig5/Sus_scrofa_bamei.Bamei_pig_v1.dna.toplevel.fa'
     if Target_Genome == "Sus scrofa (Berkshire_pig_v1) - Pig - Berkshire":
         return './genome/pig6/Sus_scrofa_berkshire.Berkshire_pig_v1.dna.toplevel.fa'
     if Target_Genome == "Sus scrofa (Hampshire_pig_v1) - Pig - Hampshire":
         return './genome/pig7/Sus_scrofa_hampshire.Hampshire_pig_v1.dna.toplevel.fa'
     if Target_Genome == "Sus scrofa (Jinhua_pig_v1) - Pig - Jinhua":
         return './genome/pig8/Sus_scrofa_jinhua.Jinhua_pig_v1.dna.toplevel.fa'
     if Target_Genome == "Sus scrofa (Landrace_pig_v1) - Pig - Landrace":
         return './genome/pig9/Sus_scrofa_landrace.Landrace_pig_v1.dna.toplevel.fa'
     if Target_Genome == "Sus scrofa (Meishan_pig_v1) - Pig - Meishan":
         return './genome/pig10/Sus_scrofa_meishan.Meishan_pig_v1.dna.toplevel.fa'
     if Target_Genome == "Sus scrofa (Pietrain_pig_v1) - Pig - Pietrain":
         return './genome/pig11/Sus_scrofa_pietrain.Pietrain_pig_v1.dna.toplevel.fa'
     if Target_Genome == "Sus scrofa (Rongchang_pig_v1) - Pig - Rongchang":
         return './genome/pig12/Sus_scrofa_rongchang.Rongchang_pig_v1.dna.toplevel.fa'
     if Target_Genome == "Sus scrofa (Tibetan_Pig_v2) - Pig - Tibetan":
         return './genome/pig13/Sus_scrofa_tibetan.Tibetan_Pig_v2.dna.toplevel.fa'
     if Target_Genome == "Sus scrofa (minipig_v1.0) - Pig - Wuzhishan":
         return './genome/pig14/Sus_scrofa_wuzhishan.minipig_v1.0.dna.toplevel.fa'
     if Target_Genome == "Sus scrofa (USMARCv1.0) - Pig - USMARC":
         return './genome/pig15/Sus_scrofa_usmarc.USMARCv1.0.dna.toplevel.fa'
     if Target_Genome == "Rhinopithecus bieti (ASM169854v1) - Black snub-nosed monkey":
         return './genome/monkey4/Rhinopithecus_bieti.ASM169854v1.dna.toplevel.fa'
     if Target_Genome == "Saimiri boliviensis boliviensis (SaiBol1.0) - Bolivian squirrel monkey":
         return './genome/monkey5/Saimiri_boliviensis_boliviensis.SaiBol1.0.dna.toplevel.fa'
     if Target_Genome == "Rhinopithecus roxellana (Rrox_v1) - Golden snub-nosed monkey":
         return './genome/monkey6/Rhinopithecus_roxellana.Rrox_v1.dna.toplevel.fa'
     if Target_Genome == "Aotus nancymaae (Anan_2.0) - Ma's night monkey":
         return './genome/monkey7/Aotus_nancymaae.Anan_2.0.dna.toplevel.fa' 
     

ref_paths(Target_Genome)   

     
     
