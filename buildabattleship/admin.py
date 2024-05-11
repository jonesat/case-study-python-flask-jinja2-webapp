from flask import Blueprint
from . import db
from .modelsNew import *
import datetime

bp = Blueprint('admin', __name__, url_prefix='/admin/')

# function to put some seed data in the database
@bp.route('/dbseed/')
def dbseed():
    Kestrel = Chassis(
    chassisID =1,
    chassisName="Kestrel",
    description="Workhorse of the People",
    price=7777,
    shipClass="Frigate",
    armourRating=3,
    manoeuvrabilityRating=4,
    cargoSpaceRating=1,
    recommendation="All-Rounder",
    keyFeature="Manoeuvrability",
    engineSlotQuality="B",
    systemSlotQuality="C",
    weaponSlotQuality="C"
    )
    Blackbird = Chassis(
    chassisID =2,
    chassisName="Blackbird",
    description="Stealth vessel used by the galactic fedaration",
    price=420000,
    shipClass="Cruiser",
    armourRating=4,
    manoeuvrabilityRating=7,
    cargoSpaceRating=2,
    recommendation="Stealth",
    keyFeature="Manoeuvrability",
    engineSlotQuality="A",
    systemSlotQuality="B",
    weaponSlotQuality="B"
    )
    Lanius = Chassis(
    chassisID =3,
    chassisName="Lanius",
    description="An alien ship that fights indirectly with strange technology",
    price=157777,
    shipClass="Cruiser",
    armourRating=4,
    manoeuvrabilityRating=5,
    cargoSpaceRating=4,
    recommendation="Exploration",
    keyFeature="Manoeuvrability",
    engineSlotQuality="B",
    systemSlotQuality="A",
    weaponSlotQuality="C"
    )
    Zoltan = Chassis(
    chassisID =4,
    chassisName="Zoltan",
    description="A famous alien designed frigate with support for powerful shields",
    price=67000,
    shipClass="Frigate",
    armourRating=5,
    manoeuvrabilityRating=4,
    cargoSpaceRating=2,
    recommendation="Combat",
    keyFeature="Armour",
    engineSlotQuality="C",
    systemSlotQuality="B",
    weaponSlotQuality="B"
    )
    Slug = Chassis(
    chassisID =5,
    chassisName="Slug",
    description="Extremely Sturdy design from the slug empire",
    price=780000,
    shipClass="Capital",
    armourRating=10,
    manoeuvrabilityRating=7,
    cargoSpaceRating=4,
    recommendation="Flagship",
    keyFeature="Armour",
    engineSlotQuality="B",
    systemSlotQuality="A",
    weaponSlotQuality="A"
    )

    try:
        db.session.add(Kestrel)
        db.session.add(Blackbird)
        db.session.add(Lanius)
        db.session.add(Zoltan)
        db.session.add(Slug)
        db.session.commit()
    except:
        return 'There was an issue adding the chassis in dbseed function'

    # Weapons Quality C
    MiniGonne = Module(
    moduleID =1,
    moduleName="MiniGonne",
    description="A big gun",
    price=555,
    quality="C",
    moduleType="Weapon"
    )
    MiniGonneD = Weapon(
    weaponID =1,
    armamentType="MachinGonne",
    hullDamage = 3,
    shieldDamage =4,
    range = 1,
    keyFeature="Shield Damage",
    moduleID = 1
    )
    Pike = Module(
    moduleID =2,
    moduleName="Pike",
    description="Entry-Level beam weapon",
    price=888,
    quality="C",
    moduleType="Weapon"
    )
    PikeD = Weapon(
    weaponID =2,
    armamentType="Beam",
    hullDamage = 4,
    shieldDamage =1,
    range = 3,
    keyFeature="Hull Damage",
    moduleID = 2
    )
    Laser = Module(
    moduleID =3,
    moduleName="Laser",
    description="Entry-Level laser weapon",
    price=444,
    quality="C",
    moduleType="Weapon"
    )
    LaserD = Weapon(
    weaponID =3,
    armamentType="Laser",
    hullDamage = 1,
    shieldDamage =3,
    range = 4,
    keyFeature="Range",
    moduleID = 3
    )
    # Weapons Quality B
    HeavyGonne = Module(
    moduleID =4,
    moduleName="HeavyGonne",
    description="A really really big gun",
    price=7777,
    quality="B",
    moduleType="Weapon"
    )
    HeavyGonneD = Weapon(
    weaponID =4,
    armamentType="MachinGonne",
    hullDamage = 5,
    shieldDamage =7,
    range = 2,
    keyFeature="Shield Damage",
    moduleID = 4
    )
    Halberd = Module(
    moduleID =5,
    moduleName="Halberd",
    description="Melts ship hulls like butter",
    price=9988,
    quality="B",
    moduleType="Weapon"
    )
    HalberdD = Weapon(
    weaponID =5,
    armamentType="Beam",
    hullDamage = 7,
    shieldDamage =2,
    range = 5,
    keyFeature="Hull Damage",
    moduleID = 5
    )
    DualLaser = Module(
    moduleID =6,
    moduleName="Dual Laser",
    description="A pair of upgraded laser weapons",
    price=6682,
    quality="B",
    moduleType="Weapon"
    )
    DualLaserD = Weapon(
    weaponID =6,
    armamentType="Laser",
    hullDamage = 2,
    shieldDamage =5,
    range = 7,
    keyFeature="Range",
    moduleID = 6
    )
    # Weapons Quality A
    GatlingGonne = Module(
    moduleID =7,
    moduleName="Gatling Gonne",
    description="A withering hail of big gonnefire",
    price=24000,
    quality="A",
    moduleType="Weapon"
    )
    GatlingGonneD = Weapon(
    weaponID =7,
    armamentType="MachinGonne",
    hullDamage = 7,
    shieldDamage =10,
    range = 3,
    keyFeature="Shield Damage",
    moduleID = 7
    )
    Glaive = Module(
    moduleID =8,
    moduleName="Glaive",
    description="A terrifying beam weapon",
    price=40000,
    quality="A",
    moduleType="Weapon"
    )
    GlaiveD = Weapon(
    weaponID =8,
    armamentType="Beam",
    hullDamage = 10,
    shieldDamage =3,
    range = 7,
    keyFeature="Hull Damage",
    moduleID = 8
    )
    HeavyLaser = Module(
    moduleID =9,
    moduleName="Heavy Laser",
    description="A weapon that discharges large laser bursts",
    price=32270,
    quality="A",
    moduleType="Weapon"
    )
    HeavyLaserD = Weapon(
    weaponID =9,
    armamentType="Laser",
    hullDamage = 3,
    shieldDamage =7,
    range = 10,
    keyFeature="Range",
    moduleID = 9
    )

    # Systems Quality C
    BubbleShield = Module(
    moduleID =10,
    moduleName="Bubble Shield",
    description="Basic Energy Bubble",
    price=777,
    quality="C",
    moduleType="System"
    )
    BubbleShieldD = System(
    systemID =1,
    systemType="Shield",
    weight = 1,
    maintenance = 3,
    powerDraw = 4,
    keyFeature="Weight",
    moduleID = 10
    )
    SensorSuite = Module(
    moduleID =11,
    moduleName="Sensor Suite",
    description="A rudimentary set of sensors",
    price=1212,
    quality="C",
    moduleType="System"
    )
    SensorSuiteD = System(
    systemID =2,
    systemType="Sensor",
    weight = 1,
    maintenance = 4,
    powerDraw = 3,
    keyFeature="Weight",
    moduleID = 11
    )
    ArmourPlating = Module(
    moduleID =12,
    moduleName="Armour Plating",
    description="Heavy armour plates",
    price=950,
    quality="C",
    moduleType="System"
    )
    ArmourPlatingD = System(
    systemID =3,
    systemType="Armour",
    weight = 4,
    maintenance = 2,
    powerDraw = 1,
    keyFeature="Power Draw",
    moduleID = 12
    )

    #Systems Quality B
    PrismShield = Module(
    moduleID =13,
    moduleName="Prism Shield",
    description="Minor capacity increase but greater recharge rate",
    price=7777,
    quality="B",
    moduleType="System"
    )
    PrismShieldD = System(
    systemID =4,
    systemType="Shield",
    weight = 2,
    maintenance = 5,
    powerDraw = 7,
    keyFeature="Weight",
    moduleID = 13
    )
    LRScanner = Module(
    moduleID =14,
    moduleName="LR Scanner",
    description="A suite of sensors suitable for exploration",
    price=12120,
    quality="B",
    moduleType="System"
    )
    LRScannerD = System(
    systemID =5,
    systemType="Sensor",
    weight = 2,
    maintenance = 7,
    powerDraw = 5,
    keyFeature="Weight",
    moduleID = 14
    )
    ReinforcedPlating = Module(
    moduleID =15,
    moduleName="Reinforced Plating",
    description="Layered armour plates fused together",
    price=9250,
    quality="B",
    moduleType="System"
    )
    ReinforcedPlatingD = System(
    systemID =6,
    systemType="Armour",
    weight = 7,
    maintenance = 5,
    powerDraw = 2,
    keyFeature="Power Draw",
    moduleID = 15
    )

    #Systems Quality A
    ForceShield = Module(
    moduleID =16,
    moduleName="Force Shield",
    description="Hardened Energy Barriers",
    price=58777,
    quality="A",
    moduleType="System"
    )
    ForceShieldD = System(
    systemID =7,
    systemType="Shield",
    weight = 3,
    maintenance = 7,
    powerDraw = 10,
    keyFeature="Weight",
    moduleID = 16
    )
    Surveillance = Module(
    moduleID =17,
    moduleName="Surveillance",
    description="A cutting edge sensor suite used by the galaxies spys",
    price=85777,
    quality="A",
    moduleType="System"
    )
    SurveillanceD = System(
    systemID =8,
    systemType="Sensor",
    weight = 3,
    maintenance = 10,
    powerDraw = 7,
    keyFeature="Weight",
    moduleID = 17
    )
    ReactivePlating = Module(
    moduleID =18,
    moduleName="Reactive Plating",
    description="Advanced armour plates that readjust and disperse damage",
    price=65000,
    quality="A",
    moduleType="System"
    )
    ReactivePlatingD = System(
    systemID =9,
    systemType="Armour",
    weight = 10,
    maintenance = 7,
    powerDraw = 3,
    keyFeature="Power Draw",
    moduleID = 18
    )

    #Engines
    Hotbox = Module(
    moduleID =19,
    moduleName="Hotbox",
    description="Primitive combustion engine",
    price=333,
    quality="C",
    moduleType="Engine"
    )
    HotboxD = Engine(
    engineID =1,
    engineType="Combustion",
    speed = 3,
    acceleration=4,
    fuelEfficiency=1,
    keyFeature="Acceleration",
    moduleID = 19
    )
    HyperDrive = Module(
    moduleID =20,
    moduleName="Hyper Drive",
    description="The peoples choice for interstellar travel",
    price=11000,
    quality="B",
    moduleType="Engine"
    )
    HyperDriveD = Engine(
    engineID =2,
    engineType="Jump",
    speed = 6,
    acceleration=2,
    fuelEfficiency=7,
    keyFeature="Fuel Efficiency",
    moduleID = 20
    )

    FTLDrive = Module(
    moduleID =21,
    moduleName="FTL Drive",
    description="The rules of physics no longer apply",
    price=200000,
    quality="A",
    moduleType="Engine"
    )
    FTLDriveD = Engine(
    engineID =3,
    engineType="FTL",
    speed = 10,
    acceleration=3,
    fuelEfficiency=7,
    keyFeature="Speed",
    moduleID = 21
    )

    try:
        db.session.add(MiniGonne)
        db.session.add(MiniGonneD)
        db.session.add(Pike)
        db.session.add(PikeD)
        db.session.add(Laser)
        db.session.add(LaserD)
        db.session.add(HeavyGonne)
        db.session.add(HeavyGonneD)
        db.session.add(Halberd)
        db.session.add(HalberdD)
        db.session.add(DualLaser)
        db.session.add(DualLaser)
        db.session.add(GatlingGonne)
        db.session.add(GatlingGonneD)
        db.session.add(Glaive)
        db.session.add(GlaiveD)
        db.session.add(HeavyLaser)
        db.session.add(HeavyLaserD)
        db.session.add(BubbleShield)
        db.session.add(BubbleShieldD)
        db.session.add(SensorSuite)
        db.session.add(SensorSuiteD)
        db.session.add(ArmourPlating)
        db.session.add(ArmourPlatingD)
        db.session.add(PrismShield)
        db.session.add(PrismShieldD)
        db.session.add(LRScanner)
        db.session.add(LRScannerD)
        db.session.add(ReinforcedPlating)
        db.session.add(ReinforcedPlatingD)
        db.session.add(ForceShield)
        db.session.add(ForceShieldD)
        db.session.add(Surveillance)
        db.session.add(SurveillanceD)
        db.session.add(ReactivePlating)
        db.session.add(ReactivePlatingD)
        db.session.add(Hotbox)
        db.session.add(HotboxD)
        db.session.add(HyperDrive)
        db.session.add(HyperDriveD)
        db.session.add(FTLDrive)
        db.session.add(FTLDriveD)
        db.session.commit()
    except:
        return 'There was an issue adding the module in dbseed function'

    return 'DATA LOADED'
