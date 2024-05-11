from . import db
class Order(db.Model):
    __tablename__='order'
    orderID = db.Column(db.Integer, primary_key=True)
    customerName = db.Column(db.String(64))
    customerEmail =  db.Column(db.String(128))
    chassisID = db.Column('chassisID', db.Integer,db.ForeignKey('chassis.chassisID'), nullable=False)
    # slot_ID = slot_ID
    # module_ID = module_ID
    engineID =db.Column(db.Integer,db.ForeignKey('module.moduleID'), nullable=False)
    systemID = db.Column(db.Integer,db.ForeignKey('module.moduleID'), nullable=False)
    weaponID = db.Column(db.Integer,db.ForeignKey('module.moduleID'), nullable=False)


    def __repr__(self):
        # str = "OrderID: {} Customer Name: {}, Customer Email: {},chassis_ID: {}, slot_ID: {}, module_ID: {} \n"
        str = "OrderID: {} Customer Name: {}, Customer Email: {},chassis_ID: {}, engineID: {}, systemID: {}, weaponID: {} \n"
        # str = str.format(self.orderID,self.customerName,self.customerEmail,self.chassis_ID,self.slot_ID,self.module_ID)
        str = str.format(self.orderID,self.customerName,self.customerEmail,self.chassisID,self.engineID,self.systemID,self.weaponID)
        return(str)

class Chassis(db.Model):
    __tablename__='chassis'
    chassisID = db.Column(db.Integer, primary_key=True)
    chassisName = db.Column(db.String(64), unique=True)
    description=db.Column(db.String(500), nullable=False)
    price = db.Column(db.Float, nullable=False)
    shipClass = db.Column(db.String(64), unique=False)
    armourRating = db.Column(db.Integer, unique=False)
    manoeuvrabilityRating =  db.Column(db.Integer, unique=False)
    cargoSpaceRating =  db.Column(db.Integer, unique=False)
    recommendation = db.Column(db.String(64), unique=False)
    keyFeature = db.Column(db.String(64), unique=False)
    engineSlotQuality = db.Column(db.String(64), unique=False)
    systemSlotQuality =db.Column(db.String(64), unique=False)
    weaponSlotQuality = db.Column(db.String(64), unique=False)

    def view_Chassis(self):
        return(str(self))

    def __repr__(self):
        str = "chassisID: {}, chassisName: {}, description: {}, price: {}, shipClass: {}, armourRating: {}, manoeuvrabilityRating: {}, cargoSpaceRating: {}, recommendation: {}, keyFeature: {}, engineSlotQuality: {}, systemSlotQuality: {}, weaponSlotQuality: {}"
        str = str.format(self.chassisID,self.chassisName,self.description,self.price,self.shipClass,self.armourRating,self.manoeuvrabilityRating,self.cargoSpaceRating,self.recommendation,self.keyFeature,self.engineSlotQuality,self.systemSlotQuality,self.weaponSlotQuality)
        return(str)

class Module(db.Model):
    __tablename__='module'
    moduleID =  db.Column(db.Integer, primary_key=True)
    moduleName = db.Column(db.String(64), unique=True)
    description= db.Column(db.String(500), nullable=False)
    price = db.Column(db.Float, nullable=False)
    quality = db.Column(db.String(64), unique=False)
    moduleType = db.Column(db.String(64), unique=False)

    def view_Module(self):
        return(str(self))

    def __repr__(self):
        str = "moduleID: {}, moduleName: {}, description: {}, price: {}, quality: {}, moduleType: {}"
        str = str.format(self.moduleID,self.moduleName,self.description,self.price,self.quality,self.moduleType)
        return(str)

class Weapon(db.Model):
    __tablename__='weapon'
    weaponID = db.Column(db.Integer, primary_key=True)
    armamentType=db.Column(db.String(64), unique=False)
    hullDamage = db.Column(db.Integer, unique=False)
    shieldDamage=db.Column(db.Integer, unique=False)
    range = db.Column(db.Integer, unique=False)
    keyFeature = db.Column(db.String(64), unique=False)
    moduleID = db.Column(db.Integer,db.ForeignKey('module.moduleID'))

    def view_Weapon(self):
        return(str(self))

    def __repr__(self):
        str = "moduleID: {}, weaponID: {}, armamentType: {}, hullDamage: {}, shieldDamage: {}, range: {}, keyFeature: {}"
        str = str.format(self.moduleID,self.weaponID,self.armamentType,self.hullDamage,self.shieldDamage,self.range,self.keyFeature)
        return(str)

class Engine(db.Model):
    __tablename__='engine'
    engineID = db.Column(db.Integer, primary_key=True)
    engineType=db.Column(db.String(64), unique=False)
    speed = db.Column(db.Integer, unique=False)
    acceleration=db.Column(db.Integer, unique=False)
    fuelEfficiency=db.Column(db.Integer, unique=False)
    keyFeature = db.Column(db.String(64), unique=False)
    moduleID = db.Column(db.Integer,db.ForeignKey('module.moduleID'))

    def __repr__(self):
        str = "moduleID: {}, engineID: {},engineType: {}, speed: {}, acceleration: {}, fuelEfficiency: {}, keyFeature: {}"
        str = str.format(self.moduleID,self.engineID,self.engineType,self.speed,self.acceleration,self.fuelEfficiency,self.keyFeature)
        return(str)

class System(db.Model):
    __tablename__='system'
    systemID =  db.Column(db.Integer, primary_key=True)
    systemType=db.Column(db.String(64), unique=False)
    weight = db.Column(db.Integer, unique=False)
    maintenance = db.Column(db.Integer, unique=False)
    powerDraw = db.Column(db.Integer, unique=False)
    keyFeature = db.Column(db.String(64), unique=False)
    moduleID = db.Column(db.Integer,db.ForeignKey('module.moduleID'))

    def __repr__(self):
        str = "moduleID: {},systemID: {},systemType: {}, weight: {}, maintenance: {}, powerDraw: {}, keyFeature: {}"
        str = str.format(self.moduleID,self.systemID,self.systemType,self.weight,self.maintenance,self.powerDraw,self.keyFeature)
        return(str)
