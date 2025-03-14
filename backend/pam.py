
from enum import Enum
from fastapi import Query

class Pam(str, Enum):
  spcas9ngg = "SpCas9 from streptococcus pyogenes: 5'-NGG-3'",
  SPCas9nrg = "SpCas9 from Streptococcus pyogenes: 5'-NRG-3' (R = A or G)",
  TTTN = "AsCpf1 from Acidaminococcus or LbCpf1 from Lachnospiraceae: 5'-TTTN-3'",
  TTTV = "AsCpf1 from Acidaminococcus or LbCpf1 from Lachnospiraceae: 5'-TTTV-3' (V = G or C or A)",
  stcas9 = "StCas9 from Streptococcus thermophilus: 5'-NNAGAAW-3' (W = A or T)",
  NmCas9 = "NmCas9 from Neisseria meningitidis: 5'-NNNNGMTT-3' (M = A or C)",
  NNGRRT = "SaCas9 from Staphylococcus aureus: 5'-NNGRRT-'3 (R=A or G)",
  KYTV = "FnCpf1 from Francisella: 5'-KYTV-3'",
  NNNVRYAC = "CjCas9 from Campylobacter jejuni: 5'-NNNVRYAC-3' (V = G or C or A, R = A or G, Y = C or T)",
  NNGTGA = "SpCas9 from Streptococcus pasteurianus: 5'-NNGTGA-3'",
  TTN ="FnCpf1 from Francisella: 5'-TTN-3'",
  NNNRRT = "SaCas9 from Staphylococcus aureus: 5'-NNNRRT-'3 (R=A or G)",
  NGCG = "VRER SpCas9 from Streptococcus pyogenes: 5'-NGCG-3'",
  NGA = "VQR SpCas9 from Streptococcus pyogenes: 5'-NGA-3'",
  NGT = "XCas9 3.7 (TLIKDIV SpCas9) from Streptococcus pyogenes: 5'-NGT-3'",
  NG = "XCas9 3.7 (TLIKDIV SpCas9) from Streptococcus pyogenes: 5'-NG-3'",
  TTNB = "BhCas12b from Bacillus hisashii: 5'-TTN-3'",
  ATTN = "BhCas12b v4 from Bacillus hisashii: 5'-ATTN-3'",
  DTTN = "BhCas12b v4 from Bacillus hisashii: 5'-DTTN-3'",
  NAAN = "Spy-macCas9 from Streptococcus pyogenes and Streptococcus macacae: 5'-NAAN-3'",
  NNNNCC = "Nme2Cas9 from Neisseria meningitidis: 5'-NNNNCC-3'",
  TYCV = "RR AsCpf1 from Acidaminococcus: 5'-TYCV-3'",
  TATV = "RVR AsCpf1 from Acidaminococcus: 5'-TATV-3'",
  NNNNGNA = "CcCas9 from Clostridium cellulolyticum: 5'-NNNNGNA-3'",
  YTTV = "MAD7 nuclease: 5'-YTTV-3'",
  NCC = "Complementary SpCas9 from Streptococcus pyogenes: 5'-NCC-3'",
  NNNNCNR = "ThermoCas9 from Geobacillus thermodenitrificans T1: 5'-NNNNCNR-3'",
  NNNNCNAA = "ThermoCas9 from Geobacillus thermodenitrificans T1: 5'-NNNNCNAA-3'",
  NNN = "SpRY Cas9 from Streptococcus pyogenes: 5'-NNN-3'",
  NRN = "SpRY Cas9 from Streptococcus pyogenes: 5'-NRN-3'",
  NGC = "SpCas9 Variant from Streptococcus pyogenes: 5'-NGC-3'",
  TTTR = "Cas12f1 from Acidibacillus sulfuroxidans: 5'-TTTR-3'",
  NTTR = "Cas12f1 from Acidibacillus sulfuroxidans: 5'-NTTR-3'",
  TTCN = "DpbCasX (Cas12e) from Deltaproteobacteria: 5'-TTCN-3'",
  NRTH = "SpCas9 Variant (TAT.P5-1) from Streptococcus pyogenes: 5'-NRTH-3' (R=G or A, H=A or C orT)",
  NNGG = "SpCas9 from Staphylococcus Auricularis: 5'-NNGG-3'",
  NGGNG = "St3Cas9 from Streptococcus Thermophilus: 5'-NGGNG-3'",
  NRTA = "Frcas9 from Faecalibaculum rodentium: 5'-NRTA-3' for target (R=A or G)",
  NNNA = "Frcas9 from Faecalibaculum rodentium: 5'-NNNA-3'",

def pam_type(Pam):
  if Pam == "SpCas9 from streptococcus pyogenes: 5'-NGG-3'":
     return 'NGG'
  if Pam == "SpCas9 from Streptococcus pyogenes: 5'-NRG-3' (R = A or G)":
    return 'NRG'
  if Pam == "StCas9 from Streptococcus thermophilus: 5'-NNAGAAW-3' (W = A or T)":
    return 'NNAGAAW'
  if Pam == "NmCas9 from Neisseria meningitidis: 5'-NNNNGMTT-3' (M = A or C)":
    return 'NNNNGMTT'
  if Pam == "SaCas9 from Staphylococcus aureus: 5'-NNGRRT-'3 (R=A or G)":
    return 'NNGRRT'
  if Pam == "FnCpf1 from Francisella: 5'-KYTV-3'":
    return 'KYTV'
  if Pam ==  "CjCas9 from Campylobacter jejuni: 5'-NNNVRYAC-3' (V = G or C or A, R = A or G, Y = C or T)":
    return 'NNNVRYAC'
  if Pam == "AsCpf1 from Acidaminococcus or LbCpf1 from Lachnospiraceae: 5'-TTTN-3'":
    return 'TTTN'
  if Pam == "AsCpf1 from Acidaminococcus or LbCpf1 from Lachnospiraceae: 5'-TTTV-3' (V = G or C or A)":
    return 'TTTV'
  if Pam == "SpCas9 from Streptococcus pasteurianus: 5'-NNGTGA-3'":
    return 'NNGTGA'
  if Pam == "FnCpf1 from Francisella: 5'-TTN-3'":
    return 'TTN'
  if Pam == "SaCas9 from Staphylococcus aureus: 5'-NNNRRT-'3 (R=A or G)":
    return 'NNNRRT'
  if Pam == "VRER SpCas9 from Streptococcus pyogenes: 5'-NGCG-3'":
    return 'NGCG'
  if Pam == "VQR SpCas9 from Streptococcus pyogenes: 5'-NGA-3'":
    return 'NGA'
  if Pam == "XCas9 3.7 (TLIKDIV SpCas9) from Streptococcus pyogenes: 5'-NGT-3'":
    return 'NGT'
  if Pam == "XCas9 3.7 (TLIKDIV SpCas9) from Streptococcus pyogenes: 5'-NG-3'":
    return 'NG'
  if Pam == "BhCas12b from Bacillus hisashii: 5'-TTN-3'":
    return 'TTN'
  if Pam == "BhCas12b v4 from Bacillus hisashii: 5'-ATTN-3'":
    return 'ATTN'
  if Pam == "BhCas12b v4 from Bacillus hisashii: 5'-DTTN-3'":
    return 'DTTN'
  if Pam == "Spy-macCas9 from Streptococcus pyogenes and Streptococcus macacae: 5'-NAAN-3'":
    return 'NAAN'
  if Pam ==  "Nme2Cas9 from Neisseria meningitidis: 5'-NNNNCC-3'":
    return 'NNNNCC'
  if Pam == "RR AsCpf1 from Acidaminococcus: 5'-TYCV-3'":
    return 'TYCV'
  if Pam == "RVR AsCpf1 from Acidaminococcus: 5'-TATV-3'":
    return 'TATV'
  if Pam == "CcCas9 from Clostridium cellulolyticum: 5'-NNNNGNA-3'":
    return 'NNNNGNA'
  if Pam == "MAD7 nuclease: 5'-YTTV-3'":
    return 'YTTV'
  if Pam == "Complementary SpCas9 from Streptococcus pyogenes: 5'-NCC-3'":
    return 'NCC'
  if Pam == "ThermoCas9 from Geobacillus thermodenitrificans T1: 5'-NNNNCNR-3'":
    return 'NNNNCNR'
  if Pam == "ThermoCas9 from Geobacillus thermodenitrificans T1: 5'-NNNNCNAA-3'":
    return 'NNNNCNAA'
  if Pam == "SpRY Cas9 from Streptococcus pyogenes: 5'-NNN-3'":
    return 'NNN'
  if Pam == "SpRY Cas9 from Streptococcus pyogenes: 5'-NRN-3'":
    return 'NRN'
  if Pam == "SpCas9 Variant from Streptococcus pyogenes: 5'-NGC-3'":
    return 'NGC'
  if Pam ==  "Cas12f1 from Acidibacillus sulfuroxidans: 5'-TTTR-3'":
    return 'TTTR'
  if Pam == "Cas12f1 from Acidibacillus sulfuroxidans: 5'-NTTR-3'":
    return 'NTTR'
  if Pam == "DpbCasX (Cas12e) from Deltaproteobacteria: 5'-TTCN-3'":
    return 'TTCN'
  if Pam == "SpCas9 Variant (TAT.P5-1) from Streptococcus pyogenes: 5'-NRTH-3' (R=G or A, H=A or C orT)":
    return 'NRTH'
  if Pam == "SpCas9 from Staphylococcus Auricularis: 5'-NNGG-3'":
    return 'NNGG'
  if Pam == "St3Cas9 from Streptococcus Thermophilus: 5'-NGGNG-3'":
    return 'NGGNG'
  if Pam == "Frcas9 from Faecalibaculum rodentium: 5'-NRTA-3' for target (R=A or G)":
    return 'NRTA'
  if Pam == "Frcas9 from Faecalibaculum rodentium: 5'-NNNA-3'":
    return 'NNNA'
  
pam_type(Pam)



