from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
import csv
import io
import baseball_player_model

if __name__ == '__main__':
    engine = create_engine('')

    session = sessionmaker()
    session.configure(bind=engine)
    baseball_player_model.Batter.metadata.drop_all(engine)
    baseball_player_model.Batter.metadata.create_all(engine)

    operation_session = Session(engine)


    with io.open('test.csv', 'r', encoding='utf-8-sig') as f:
        batter_2015_csv = csv.DictReader(f)

        for row in batter_2015_csv:
            batter = baseball_player_model.Batter(playerid=row['playerid'].strip(),
                                                  Year=2015,
                                                  Name=row['Name'].strip(),
                                                  Team=row['Team'].strip() or None,
                                                  Age=row['Age'].strip() or None,
                                                  G=row['G'].strip() or None,
                                                  AB=row['AB'].strip() or None,
                                                  PA=row['PA'].strip() or None,
                                                  H=row['H'].strip() or None,
                                                  Single_Bat=row['1B'].strip() or None,
                                                  Double_Bat=row['2B'].strip() or None,
                                                  Triple_Bat=row['3B'].strip() or None,
                                                  HR=row['HR'].strip() or None,
                                                  R=row['R'].strip() or None,
                                                  RBI=row['RBI'].strip() or None,
                                                  BB=row['BB'].strip() or None,
                                                  IBB=row['IBB'].strip() or None,
                                                  SO=row['SO'].strip() or None,
                                                  HBP=row['HBP'].strip() or None,
                                                  SF=row['SF'].strip() or None,
                                                  SH=row['SH'].strip() or None,
                                                  GDP=row['GDP'].strip() or None,
                                                  SB=row['SB'].strip() or None,
                                                  CS=row['CS'].strip() or None,
                                                  AVG=row['AVG'].strip() or None,
                                                  GB=row['GB'].strip() or None,
                                                  FB=row['FB'].strip() or None,
                                                  LD=row['LD'].strip() or None,
                                                  IFFB=row['IFFB'].strip() or None,
                                                  Pitches=row['Pitches'].strip() or None,
                                                  Balls=row['Balls'].strip() or None,
                                                  Strikes=row['Strikes'].strip() or None,
                                                  IFH=row['IFH'].strip() or None,
                                                  BU=row['BU'].strip() or None,
                                                  BUH=row['BUH'].strip() or None,
                                                  BB_Percentage=row['BB%'].rstrip('%').strip() or None,
                                                  K_Percentage=row['K%'].rstrip('%').strip() or None,
                                                  BB_Divided_By_K=row['BB/K'].strip() or None,
                                                  OBP=row['OBP'].strip() or None,
                                                  SLG=row['SLG'].strip() or None,
                                                  OPS=row['OPS'].strip() or None,
                                                  ISO=row['ISO'].strip() or None,
                                                  BABIP=row['BABIP'].strip() or None,
                                                  GB_Divided_By_FB=row['GB/FB'].strip() or None,
                                                  LD_Percentage=row['LD%'].rstrip('%').strip() or None,
                                                  GB_Percentage=row['GB%'].rstrip('%').strip() or None,
                                                  FB_Percentage=row['FB%'].rstrip('%').strip() or None,
                                                  IFFB_Percentage=row['IFFB%'].rstrip('%').strip() or None,
                                                  HR_Divided_By_FB=row['HR/FB'].rstrip('%').strip() or None,
                                                  IFH_Percentage=row['IFH%'].rstrip('%').strip() or None,
                                                  BUH_Percentage=row['BUH%'].rstrip('%').strip() or None,
                                                  wOBA=row['wOBA'].strip() or None,
                                                  wRAA=row['wRAA'].strip() or None,
                                                  wRC=row['wRC'].strip() or None,
                                                  Bat=row['Bat'].strip() or None,
                                                  Fld=row['Fld'].strip() or None,
                                                  Rep=row['Rep'].strip() or None,
                                                  Pos=row['Pos'].strip() or None,
                                                  RAR=row['RAR'].strip() or None,
                                                  WAR=row['WAR'].strip() or None,
                                                  Dol=row['Dol'].lstrip('($').rstrip(')').strip() or None,
                                                  Spd=row['Spd'].strip() or None,
                                                  wRC_Plus=row['wRC+'].strip() or None,
                                                  WPA=row['WPA'].strip() or None,
                                                  Minus_WPA=row['-WPA'].strip() or None,
                                                  Plus_WPA=row['+WPA'].strip() or None,
                                                  RE24=row['RE24'].strip() or None,
                                                  REW=row['REW'].strip() or None,
                                                  pLI=row['-WPA'].strip() or None,
                                                  phLI=row['phLI'].strip() or None,
                                                  PH=row['PH'].strip() or None,
                                                  WPA_Divided_By_LI=row['WPA/LI'].strip() or None,
                                                  Clutch=row['Clutch'].strip() or None,
                                                  FBv=row['FBv'].strip() or None,
                                                  SL_Percentage=row['SL%'].rstrip('%').strip() or None,
                                                  SLv=row['SLv'].strip() or None,
                                                  CT_Percentage=row['CT%'].rstrip('%').strip() or None,
                                                  CTv=row['CTv'].strip() or None,
                                                  CB_Percentage=row['CB%'].rstrip('%').strip() or None,
                                                  CBv=row['CBv'].strip() or None,
                                                  CH_Percentage=row['CH%'].rstrip('%').strip() or None,
                                                  CHv=row['CHv'].strip() or None,
                                                  SF_Percentage=row['SF%'].rstrip('%').strip() or None,
                                                  SFv=row['SFv'].strip() or None,
                                                  KN_Percentage=row['KN%'].rstrip('%').strip() or None,
                                                  KNv=row['KNv'].strip() or None,
                                                  XX_Percentage=row['XX%'].rstrip('%').strip() or None,
                                                  PO_Percentage=row['PO%'].rstrip('%').strip() or None,
                                                  wFB=row['wFB'].strip() or None,
                                                  wSL=row['wSL'].strip() or None,
                                                  wCT=row['wCT'].strip() or None,
                                                  wCB=row['wCB'].strip() or None,
                                                  wCH=row['wCH'].strip() or None,
                                                  wSF=row['wSF'].strip() or None,
                                                  wKN=row['wKN'].strip() or None,
                                                  wFB_Divided_By_C=row['wFB/C'].strip() or None,
                                                  wSL_Divided_By_C=row['wSL/C'].strip() or None,
                                                  wCT_Divided_By_C=row['wCT/C'].strip() or None,
                                                  wCB_Divided_By_C=row['wCB/C'].strip() or None,
                                                  wCH_Divided_By_C=row['wCH/C'].strip() or None,
                                                  wSF_Divided_By_C=row['wSF/C'].strip() or None,
                                                  wKN_Divided_By_C=row['wKN/C'].strip() or None,
                                                  O_Swing_Percentage=row['O-Swing%'].rstrip('%').strip() or None,
                                                  Z_Swing_Percentage=row['Z-Swing%'].rstrip('%').strip() or None,
                                                  Swing_Percentage=row['Swing%'].rstrip('%').strip() or None,
                                                  O_Contact_Percentage=row['O-Contact%'].rstrip('%').strip() or None,
                                                  Z_Contact_Percentage=row['Z-Contact%'].rstrip('%').strip() or None,
                                                  Contact_Percentage=row['Contact%'].rstrip('%').strip() or None,
                                                  Zone_Percentage=row['Zone%'].rstrip('%').strip() or None,
                                                  F_Strike_Percentage=row['F-Strike%'].rstrip('%').strip() or None,
                                                  SwStr_Percentage=row['SwStr%'].rstrip('%').strip() or None,
                                                  BsR=row['BsR'].strip() or None,
                                                  FA_Percentage_pfx=row['FA% (pfx)'].rstrip('%').strip() or None,
                                                  FT_Percentage_pfx=row['FT% (pfx)'].rstrip('%').strip() or None,
                                                  FC_Percentage_pfx=row['FC% (pfx)'].rstrip('%').strip() or None,
                                                  FS_Percentage_pfx=row['FS% (pfx)'].rstrip('%').strip() or None,
                                                  FO_Percentage_pfx=row['FO% (pfx)'].rstrip('%').strip() or None,
                                                  SI_Percentage_pfx=row['SI% (pfx)'].rstrip('%').strip() or None,
                                                  SL_Percentage_pfx=row['SL% (pfx)'].rstrip('%').strip() or None,
                                                  CU_Percentage_pfx=row['CU% (pfx)'].rstrip('%').strip() or None,
                                                  KC_Percentage_pfx=row['KC% (pfx)'].rstrip('%').strip() or None,
                                                  EP_Percentage_pfx=row['EP% (pfx)'].rstrip('%').strip() or None,
                                                  CH_Percentage_pfx=row['CH% (pfx)'].rstrip('%').strip() or None,
                                                  SC_Percentage_pfx=row['SC% (pfx)'].rstrip('%').strip() or None,
                                                  KN_Percentage_pfx=row['KN% (pfx)'].rstrip('%').strip() or None,
                                                  UN_Percentage_pfx=row['UN% (pfx)'].rstrip('%').strip() or None,
                                                  vFA_pfx=row['vFA (pfx)'].strip() or None,
                                                  vFT_pfx=row['vFT (pfx)'].strip() or None,
                                                  vFC_pfx=row['vFC (pfx)'].strip() or None,
                                                  vFS_pfx=row['vFS (pfx)'].strip() or None,
                                                  vFO_pfx=row['vFO (pfx)'].strip() or None,
                                                  vSI_pfx=row['vSI (pfx)'].strip() or None,
                                                  vSL_pfx=row['vSL (pfx)'].strip() or None,
                                                  vCU_pfx=row['vCU (pfx)'].strip() or None,
                                                  vKC_pfx=row['vKC (pfx)'].strip() or None,
                                                  vEP_pfx=row['vEP (pfx)'].strip() or None,
                                                  vCH_pfx=row['vCH (pfx)'].strip() or None,
                                                  vSC_pfx=row['vSC (pfx)'].strip() or None,
                                                  vKN_pfx=row['vKN (pfx)'].strip() or None,
                                                  FA_X_pfx=row['FA-X (pfx)'].strip() or None,
                                                  FT_X_pfx=row['FT-X (pfx)'].strip() or None,
                                                  FC_X_pfx=row['FC-X (pfx)'].strip() or None,
                                                  FS_X_pfx=row['FS-X (pfx)'].strip() or None,
                                                  FO_X_pfx=row['FO-X (pfx)'].strip() or None,
                                                  SI_X_pfx=row['SI-X (pfx)'].strip() or None,
                                                  SL_X_pfx=row['SL-X (pfx)'].strip() or None,
                                                  CU_X_pfx=row['CU-X (pfx)'].strip() or None,
                                                  KC_X_pfx=row['KC-X (pfx)'].strip() or None,
                                                  EP_X_pfx=row['EP-X (pfx)'].strip() or None,
                                                  CH_X_pfx=row['CH-X (pfx)'].strip() or None,
                                                  SC_X_pfx=row['SC-X (pfx)'].strip() or None,
                                                  KN_X_pfx=row['KN-X (pfx)'].strip() or None,
                                                  FA_Z_pfx=row['FA-Z (pfx)'].strip() or None,
                                                  FT_Z_pfx=row['FT-Z (pfx)'].strip() or None,
                                                  FC_Z_pfx=row['FC-Z (pfx)'].strip() or None,
                                                  FS_Z_pfx=row['FS-Z (pfx)'].strip() or None,
                                                  FO_Z_pfx=row['FO-Z (pfx)'].strip() or None,
                                                  SI_Z_pfx=row['SI-Z (pfx)'].strip() or None,
                                                  SL_Z_pfx=row['SL-Z (pfx)'].strip() or None,
                                                  CU_Z_pfx=row['CU-Z (pfx)'].strip() or None,
                                                  KC_Z_pfx=row['KC-Z (pfx)'].strip() or None,
                                                  EP_Z_pfx=row['EP-Z (pfx)'].strip() or None,
                                                  CH_Z_pfx=row['CH-Z (pfx)'].strip() or None,
                                                  SC_Z_pfx=row['SC-Z (pfx)'].strip() or None,
                                                  KN_Z_pfx=row['KN-Z (pfx)'].strip() or None,
                                                  wFA_pfx=row['wFA (pfx)'].strip() or None,
                                                  wFT_pfx=row['wFT (pfx)'].strip() or None,
                                                  wFC_pfx=row['wFC (pfx)'].strip() or None,
                                                  wFS_pfx=row['wFS (pfx)'].strip() or None,
                                                  wFO_pfx=row['wFO (pfx)'].strip() or None,
                                                  wSI_pfx=row['wSI (pfx)'].strip() or None,
                                                  wSL_pfx=row['wSL (pfx)'].strip() or None,
                                                  wCU_pfx=row['wCU (pfx)'].strip() or None,
                                                  wKC_pfx=row['wKC (pfx)'].strip() or None,
                                                  wEP_pfx=row['wEP (pfx)'].strip() or None,
                                                  wCH_pfx=row['wCH (pfx)'].strip() or None,
                                                  wSC_pfx=row['wSC (pfx)'].strip() or None,
                                                  wKN_pfx=row['wKN (pfx)'].strip() or None,
                                                  wFA_Divided_By_C_pfx=row['wFA/C (pfx)'].strip() or None,
                                                  wFT_Divided_By_C_pfx=row['wFT/C (pfx)'].strip() or None,
                                                  wFC_Divided_By_C_pfx=row['wFC/C (pfx)'].strip() or None,
                                                  wFS_Divided_By_C_pfx=row['wFS/C (pfx)'].strip() or None,
                                                  wFO_Divided_By_C_pfx=row['wFO/C (pfx)'].strip() or None,
                                                  wSI_Divided_By_C_pfx=row['wSI/C (pfx)'].strip() or None,
                                                  wSL_Divided_By_C_pfx=row['wSL/C (pfx)'].strip() or None,
                                                  wCU_Divided_By_C_pfx=row['wCU/C (pfx)'].strip() or None,
                                                  wKC_Divided_By_C_pfx=row['wKC/C (pfx)'].strip() or None,
                                                  wEP_Divided_By_C_pfx=row['wEP/C (pfx)'].strip() or None,
                                                  wCH_Divided_By_C_pfx=row['wCH/C (pfx)'].strip() or None,
                                                  wSC_Divided_By_C_pfx=row['wSC/C (pfx)'].strip() or None,
                                                  wKN_Divided_By_C_pfx=row['wKN/C (pfx)'].strip() or None,
                                                  O_Swing_Percentage_pfx=row['O-Swing% (pfx)'].rstrip(
                                                      '%').strip() or None,
                                                  Z_Swing_Percentage_pfx=row['Z-Swing% (pfx)'].rstrip(
                                                      '%').strip() or None,
                                                  Swing_Percentage_pfx=row['Swing% (pfx)'].rstrip('%').strip() or None,
                                                  O_Contact_Percentage_pfx=row['O-Contact% (pfx)'].rstrip(
                                                      '%').strip() or None,
                                                  Z_Contact_Percentage_pfx=row['Z-Contact% (pfx)'].rstrip(
                                                      '%').strip() or None,
                                                  Contact_Percentage_pfx=row['Contact% (pfx)'].rstrip(
                                                      '%').strip() or None,
                                                  Zone_Percentage_pfx=row['Zone% (pfx)'].rstrip('%').strip() or None,
                                                  Pace=row['Pace'].strip() or None,
                                                  Def=row['Def'].strip() or None,
                                                  wSB=row['wSB'].strip() or None,
                                                  UBR=row['UBR'].strip() or None,
                                                  Age_Rng=row['Age Rng'].strip() or None,
                                                  Off=row['Off'].strip() or None,
                                                  Lg=row['Lg'].strip() or None,
                                                  wGDP=row['wGDP'].strip() or None,
                                                  Pull_Percentage=row['Pull%'].rstrip('%').strip() or None,
                                                  Cent_Percentage=row['Cent%'].rstrip('%').strip() or None,
                                                  Oppo_Percentage=row['Oppo%'].rstrip('%').strip() or None,
                                                  Soft_Percentage=row['Soft%'].rstrip('%').strip() or None,
                                                  Med_Percentage=row['Med%'].rstrip('%').strip() or None,
                                                  Hard_Percentage=row['Hard%'].rstrip('%').strip() or None)
            operation_session.add(batter)

    operation_session.commit()
    operation_session.close()
