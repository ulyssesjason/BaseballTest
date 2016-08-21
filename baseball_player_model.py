from sqlalchemy import Column, Integer, String, Float, ForeignKey, ForeignKeyConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.declarative import AbstractConcreteBase
import math
import json

Base = declarative_base()


class AbstractBatter(AbstractConcreteBase, Base):
    playerid = Column(Integer, nullable=False, primary_key=True)

    Year = Column(Integer, nullable=False, primary_key=True)
    G = Column(Integer)
    AB = Column(Integer)
    PA = Column(Integer)
    H = Column(Integer)
    Single_Bat = Column(Integer)
    Double_Bat = Column(Integer)
    Triple_Bat = Column(Integer)
    HR = Column(Integer)
    R = Column(Integer)
    RBI = Column(Integer)
    BB = Column(Integer)
    IBB = Column(Integer)
    SO = Column(Integer)
    HBP = Column(Integer)
    SF = Column(Integer)
    SH = Column(Integer)
    GDP = Column(Integer)
    SB = Column(Integer)
    CS = Column(Integer)
    AVG = Column(Float)
    GB = Column(Integer)
    FB = Column(Integer)
    LD = Column(Integer)
    IFFB = Column(Integer)
    Pitches = Column(Integer)
    Balls = Column(Integer)
    Strikes = Column(Integer)
    IFH = Column(Integer)
    BU = Column(Integer)
    BUH = Column(Integer)
    BB_Percentage = Column(Float)
    K_Percentage = Column(Float)
    BB_Divided_By_K = Column(Float)
    OBP = Column(Float)
    SLG = Column(Float)
    OPS = Column(Float)
    ISO = Column(Float)
    BABIP = Column(Float)
    GB_Divided_By_FB = Column(Float)
    LD_Percentage = Column(Float)
    GB_Percentage = Column(Float)
    FB_Percentage = Column(Float)
    IFFB_Percentage = Column(Float)
    HR_Divided_By_FB = Column(Float)
    IFH_Percentage = Column(Float)
    BUH_Percentage = Column(Float)
    wOBA = Column(Float)
    wRAA = Column(Float)
    wRC = Column(Integer)
    Bat = Column(Float)
    Fld = Column(Float)
    Rep = Column(Float)
    Pos = Column(Float)
    RAR = Column(Float)
    WAR = Column(Float)
    Dol = Column(Float)
    Spd = Column(Float)
    wRC_Plus = Column(Integer)
    WPA = Column(Float)
    Minus_WPA = Column(Float)
    Plus_WPA = Column(Float)
    RE24 = Column(Float)
    REW = Column(Float)
    pLI = Column(Float)
    phLI = Column(Float)
    PH = Column(Integer)
    WPA_Divided_By_LI = Column(Float)
    Clutch = Column(Float)
    FBv = Column(Float)
    SL_Percentage = Column(Float)
    SLv = Column(Float)
    CT_Percentage = Column(Float)
    CTv = Column(Float)
    CB_Percentage = Column(Float)
    CBv = Column(Float)
    CH_Percentage = Column(Float)
    CHv = Column(Float)
    SF_Percentage = Column(Float)
    SFv = Column(Float)
    KN_Percentage = Column(Float)
    KNv = Column(Float)
    XX_Percentage = Column(Float)
    PO_Percentage = Column(Float)
    wFB = Column(Float)
    wSL = Column(Float)
    wCT = Column(Float)
    wCB = Column(Float)
    wCH = Column(Float)
    wSF = Column(Float)
    wKN = Column(Float)
    wFB_Divided_By_C = Column(Float)
    wSL_Divided_By_C = Column(Float)
    wCT_Divided_By_C = Column(Float)
    wCB_Divided_By_C = Column(Float)
    wCH_Divided_By_C = Column(Float)
    wSF_Divided_By_C = Column(Float)
    wKN_Divided_By_C = Column(Float)
    O_Swing_Percentage = Column(Float)
    Z_Swing_Percentage = Column(Float)
    Swing_Percentage = Column(Float)
    O_Contact_Percentage = Column(Float)
    Z_Contact_Percentage = Column(Float)
    Contact_Percentage = Column(Float)
    Zone_Percentage = Column(Float)
    F_Strike_Percentage = Column(Float)
    SwStr_Percentage = Column(Float)
    BsR = Column(Float)
    FA_Percentage_pfx = Column(Float)
    FT_Percentage_pfx = Column(Float)
    FC_Percentage_pfx = Column(Float)
    FS_Percentage_pfx = Column(Float)
    FO_Percentage_pfx = Column(Float)
    SI_Percentage_pfx = Column(Float)
    SL_Percentage_pfx = Column(Float)
    CU_Percentage_pfx = Column(Float)
    KC_Percentage_pfx = Column(Float)
    EP_Percentage_pfx = Column(Float)
    CH_Percentage_pfx = Column(Float)
    SC_Percentage_pfx = Column(Float)
    KN_Percentage_pfx = Column(Float)
    UN_Percentage_pfx = Column(Float)
    vFA_pfx = Column(Float)
    vFT_pfx = Column(Float)
    vFC_pfx = Column(Float)
    vFS_pfx = Column(Float)
    vFO_pfx = Column(Float)
    vSI_pfx = Column(Float)
    vSL_pfx = Column(Float)
    vCU_pfx = Column(Float)
    vKC_pfx = Column(Float)
    vEP_pfx = Column(Float)
    vCH_pfx = Column(Float)
    vSC_pfx = Column(Float)
    vKN_pfx = Column(Float)
    FA_X_pfx = Column(Float)
    FT_X_pfx = Column(Float)
    FC_X_pfx = Column(Float)
    FS_X_pfx = Column(Float)
    FO_X_pfx = Column(Float)
    SI_X_pfx = Column(Float)
    SL_X_pfx = Column(Float)
    CU_X_pfx = Column(Float)
    KC_X_pfx = Column(Float)
    EP_X_pfx = Column(Float)
    CH_X_pfx = Column(Float)
    SC_X_pfx = Column(Float)
    KN_X_pfx = Column(Float)
    FA_Z_pfx = Column(Float)
    FT_Z_pfx = Column(Float)
    FC_Z_pfx = Column(Float)
    FS_Z_pfx = Column(Float)
    FO_Z_pfx = Column(Float)
    SI_Z_pfx = Column(Float)
    SL_Z_pfx = Column(Float)
    CU_Z_pfx = Column(Float)
    KC_Z_pfx = Column(Float)
    EP_Z_pfx = Column(Float)
    CH_Z_pfx = Column(Float)
    SC_Z_pfx = Column(Float)
    KN_Z_pfx = Column(Float)
    wFA_pfx = Column(Float)
    wFT_pfx = Column(Float)
    wFC_pfx = Column(Float)
    wFS_pfx = Column(Float)
    wFO_pfx = Column(Float)
    wSI_pfx = Column(Float)
    wSL_pfx = Column(Float)
    wCU_pfx = Column(Float)
    wKC_pfx = Column(Float)
    wEP_pfx = Column(Float)
    wCH_pfx = Column(Float)
    wSC_pfx = Column(Float)
    wKN_pfx = Column(Float)
    wFA_Divided_By_C_pfx = Column(Float)
    wFT_Divided_By_C_pfx = Column(Float)
    wFC_Divided_By_C_pfx = Column(Float)
    wFS_Divided_By_C_pfx = Column(Float)
    wFO_Divided_By_C_pfx = Column(Float)
    wSI_Divided_By_C_pfx = Column(Float)
    wSL_Divided_By_C_pfx = Column(Float)
    wCU_Divided_By_C_pfx = Column(Float)
    wKC_Divided_By_C_pfx = Column(Float)
    wEP_Divided_By_C_pfx = Column(Float)
    wCH_Divided_By_C_pfx = Column(Float)
    wSC_Divided_By_C_pfx = Column(Float)
    wKN_Divided_By_C_pfx = Column(Float)
    O_Swing_Percentage_pfx = Column(Float)
    Z_Swing_Percentage_pfx = Column(Float)
    Swing_Percentage_pfx = Column(Float)
    O_Contact_Percentage_pfx = Column(Float)
    Z_Contact_Percentage_pfx = Column(Float)
    Contact_Percentage_pfx = Column(Float)
    Zone_Percentage_pfx = Column(Float)
    Pace = Column(Float)
    Def = Column(Float)
    wSB = Column(Float)
    UBR = Column(Float)
    Off = Column(Float)
    Lg = Column(Float)
    wGDP = Column(Float)
    Pull_Percentage = Column(Float)
    Cent_Percentage = Column(Float)
    Oppo_Percentage = Column(Float)
    Soft_Percentage = Column(Float)
    Med_Percentage = Column(Float)
    Hard_Percentage = Column(Float)

    def batted_ball(self):
        batted_ball = {'BABIP': self.BABIP or 0, 'GB/FB': self.GB_Divided_By_FB or 0, 'LD%': self.LD_Percentage or 0,
                       'GB%': self.GB_Percentage or 0, 'FB%': self.FB_Percentage or 0,
                       'IFFB%': self.IFFB_Percentage or 0,
                       'HR/FB': self.HR_Divided_By_FB or 0, 'IFH': self.IFH or 0, 'BUH': self.BUH or 0,
                       'BUH%': self.BUH_Percentage or 0,
                       'Pull%': self.Pull_Percentage or 0, 'Cent%': self.Cent_Percentage or 0,
                       'Oppo%': self.Oppo_Percentage or 0,
                       'Soft%': self.Soft_Percentage or 0, 'Med%': self.Med_Percentage or 0,
                       'Hard%': self.Hard_Percentage or 0}

        return batted_ball

    def plate_discipline(self):
        plate_discipline = {'O-Swing%': self.O_Swing_Percentage or 0, 'Z-Swing%': self.Z_Swing_Percentage or 0,
                            'Swing%': self.Swing_Percentage or 0, 'O-Contact%': self.O_Contact_Percentage or 0,
                            'Z-Contact%': self.Z_Contact_Percentage or 0, 'Contact%': self.Contact_Percentage or 0,
                            'Zone%': self.Zone_Percentage or 0,
                            'F-Strike%': self.F_Strike_Percentage or 0, 'SwStr%': self.SwStr_Percentage or 0}
        return plate_discipline

    def standard(self):
        standard = {'G': self.G, 'AB': self.AB, 'PA': self.PA, 'H': self.H, '1B': self.Single_Bat,
                    '2B': self.Double_Bat, '3B': self.Triple_Bat, 'HR': self.HR, 'R': self.R, 'RBI': self.RBI,
                    'BB': self.BB, 'IBB': self.IBB, 'SO': self.SO, 'HBP': self.HBP, 'SF': self.SF, 'SH': self.SH,
                    'GDP': self.GDP, 'SB': self.SB, 'CS': self.CS, 'AVG': self.AVG}
        return standard

    def advanced(self):
        advanced = {'PA': self.PA, 'BB%': self.BB_Percentage, 'K%': self.K_Percentage, 'BB/K': self.BB_Divided_By_K,
                    'AVG': self.AVG, 'OBP': self.OBP, 'SLG': self.SLG, 'OPS': self.OPS, 'ISO': self.ISO,
                    'Spd': self.Spd, 'BABIP': self.BABIP, 'UBR': self.UBR, 'wGDP': self.wGDP, 'wSB': self.wSB,
                    'wRC': self.wRC, 'wRAA': self.wRAA, 'wOBA': self.wOBA, 'wRC+': self.wRC_Plus}
        return advanced

    def advance_extracted(self):
        advanced = {'BB%': self.BB_Percentage, 'K%': self.K_Percentage,
                    'AVG': self.AVG, 'OBP': self.OBP, 'SLG': self.SLG, 'OPS': self.OPS, 'ISO': self.ISO,
                    'Spd': self.Spd, 'BABIP': self.BABIP, 'UBR': self.UBR, 'wGDP': self.wGDP, 'wSB': self.wSB}

        return advanced

    def woba_related(self):
        woba_related = {'AB': self.AB, 'HBP': self.HBP
            , '1B': self.Single_Bat, '2B': self.Double_Bat, '3B': self.Triple_Bat, 'HR': self.HR, 'IBB': self.IBB,
                        'SF': self.SF}

        return woba_related

    def predictable(self):
        predictable_fields = self.plate_discipline().copy()
        predictable_fields.update(self.batted_ball())
        predictable_fields.pop('BABIP', None)
        return predictable_fields

    def performance(self):
        display_fields = self.standard().copy()
        display_fields.update(self.advanced())

        # derivative fields
        display_fields.pop('BABIP', None)
        display_fields.pop('wOBA', None)
        display_fields.pop('wRC', None)
        display_fields.pop('wRC+', None)
        display_fields.pop('Spd', None)

        display_fields.pop('PA', None)
        display_fields.pop('AB', None)
        display_fields.pop('G', None)

        return display_fields


class Batter(AbstractBatter):
    __tablename__ = 'batter'
    Name = Column(String(30), nullable=False)
    Birth_Year = Column(Integer)
    Team = Column(String(30))
    Age = Column(Integer)
    Age_Rng = Column(String(30))
    __mapper_args__ = {
        'polymorphic_identity': 'batter',
        'concrete': True}

    ommited_fields = ('Name', 'Team', 'Year', 'Age', 'Age_Rng', 'playerid')

    def __repr__(self):
        return "Batter {batter_name} in Year {year}, WRC+ is {wrcplus}".format(batter_name=self.Name, year=self.Year,
                                                                               wrcplus=self.wRC_Plus)


class Normalized_Batter(AbstractBatter):
    __tablename__ = 'normalized_batter'
    __mapper_args__ = {
        'polymorphic_identity': 'normalized_batter',
        'concrete': True}
