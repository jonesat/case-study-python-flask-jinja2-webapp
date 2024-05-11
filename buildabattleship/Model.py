class Order:
    def __init__(self,orderID,customerName,customerEmail,chassisID,engineID,systemID,weaponID):
        self.orderID = orderID
        self.customerName = customerName
        self.customerEmail = customerEmail
        self.chassisID = chassisID
        # self.slot_ID = slot_ID
        # self.module_ID = module_ID
        self.engineID = engineID
        self.systemID  = systemID
        self.weaponID = weaponID

    def get_order_details(self):
        return(str(self))

    def __repr__(self):
        # str = "OrderID: {} Customer Name: {}, Customer Email: {},chassis_ID: {}, slot_ID: {}, module_ID: {} \n"
        str = "OrderID: {} Customer Name: {}, Customer Email: {},chassis_ID: {}, engineID: {}, systemID: {}, weaponID: {} \n"
        # str = str.format(self.orderID,self.customerName,self.customerEmail,self.chassis_ID,self.slot_ID,self.module_ID)
        str = str.format(self.orderID,self.customerName,self.customerEmail,self.chassisID,self.engineID,self.systemID,self.weaponID)
        return(str)

class Slot:
    def __init__(self,slotID,quality,slotType):
        self.slotID = slotID
        self.quality = quality
        self.type = type

    def view_Slot(self):
        return(str(self))

    def __repr__(self):
        str = "slotID: {}, quality: {}, type: {}"
        str = str.format(self.slotID,self.quality,self.type)
        return(str)

class Chassis:
    def __init__(self,chassisID,chassisName,description,price,shipClass,armourRating,manoeuvrabilityRating,cargoSpaceRating,recommendation,keyFeature,engineSlotQuality,systemSlotQuality,weaponSlotQuality):
        self.chassisID = chassisID
        self.chassisName = chassisName
        self.description=description
        self.price = price
        self.shipClass = shipClass
        self.armourRating = armourRating
        self.manoeuvrabilityRating = manoeuvrabilityRating
        self.cargoSpaceRating = cargoSpaceRating
        self.recommendation = recommendation
        self.keyFeature = keyFeature
        self.engineSlotQuality = engineSlotQuality
        self.systemSlotQuality = systemSlotQuality
        self.weaponSlotQuality = weaponSlotQuality

    def view_Chassis(self):
        return(str(self))

    def __repr__(self):
        str = "chassisID: {}, chassisName: {}, description: {}, price: {}, shipClass: {}, armourRating: {}, manoeuvrabilityRating: {}, cargoSpaceRating: {}, recommendation: {}, keyFeature: {}, engineSlotQuality: {}, systemSlotQuality: {}, weaponSlotQuality: {}"
        str = str.format(self.chassisID,self.chassisName,self.description,self.price,self.shipClass,self.armourRating,self.manoeuvrabilityRating,self.cargoSpaceRating,self.recommendation,self.keyFeature,self.engineSlotQuality,self.systemSlotQuality,self.weaponSlotQuality)
        return(str)

class Module:
    def __init__(self,moduleID,moduleName,description,price,quality,moduleType):
        self.moduleID = moduleID
        self.moduleName = moduleName
        self.description= description
        self.price = price
        self.quality = quality
        self.moduleType = moduleType

    def view_Module(self):
        return(str(self))

    def __repr__(self):
        str = "moduleID: {}, moduleName: {}, description: {}, price: {}, quality: {}, moduleType: {}"
        str = str.format(self.moduleID,self.moduleName,self.description,self.price,self.quality,self.moduleType)
        return(str)

class Weapon(Module):
    def __init__ (self,moduleID,moduleName,description,price,quality,moduleType,weaponID,armamentType,hullDamage,shieldDamage,range,keyFeature):
        super().__init__(moduleID,moduleName,description,price,quality,moduleType)
        self.weaponID = weaponID
        self.armamentType=armamentType
        self.hullDamage = hullDamage
        self.shieldDamage=shieldDamage
        self.range = range
        self.keyFeature = keyFeature

    def view_Weapon(self):
        return(str(self))

    def __repr__(self):
        str = "moduleID: {}, moduleName: {}, description: {}, price: {}, quality: {}, moduleType: {}, weaponID: {}, armamentType: {}, hullDamage: {}, shieldDamage: {}, range: {}, keyFeature: {}"
        str = str.format(self.moduleID,self.moduleName,self.description,self.price,self.quality,self.moduleType,self.weaponID,self.armamentType,self.hullDamage,self.shieldDamage,self.range,self.keyFeature)
        return(str)

class Engine(Module):
    def __init__ (self,moduleID,moduleName,description,price,quality,moduleType,engineID,engineType,speed,acceleration,fuelEfficiency,keyFeature):
        super().__init__(moduleID,moduleName,description,price,quality,moduleType)
        self.engineID = engineID
        self.engineType=engineType
        self.speed = speed
        self.acceleration=acceleration
        self.fuelEfficiency=fuelEfficiency
        self.keyFeature = keyFeature

    def view_Engine(self):
        return(str(self))

    def __repr__(self):
        str = "moduleID: {}, moduleName: {}, description: {}, price: {}, quality: {}, moduletype: {}, engineID: {},engineType: {}, speed: {}, acceleration: {}, fuelEfficiency: {}, keyFeature: {}"
        str = str.format(self.moduleID,self.moduleName,self.description,self.price,self.quality,self.moduleType,self.engineID,self.engineType,self.speed,self.acceleration,self.fuelEfficiency,self.keyFeature)
        return(str)

class System(Module):
    def __init__ (self,moduleID,moduleName,description,price,quality,moduleType,systemID,systemType,weight,maintenance,powerDraw,keyFeature):
        super().__init__(moduleID,moduleName,description,price,quality,moduleType)
        self.systemID =  systemID
        self.systemType=systemType
        self.weight = weight
        self.maintenance = maintenance
        self.powerDraw = powerDraw
        self.keyFeature = keyFeature

    def view_System(self):
        return(str(self))

    def __repr__(self):
        str = "moduleID: {}, moduleName: {}, description: {}, price: {}, quality: {}, moduletype: {},systemID: {},systemType: {}, weight: {}, maintenance: {}, powerDraw: {}, keyFeature: {}"
        str = str.format(self.moduleID,self.moduleName,self.description,self.price,self.quality,self.moduleType,self.systemID,self.systemType,self.weight,self.maintenance,self.powerDraw,self.keyFeature)
        return(str)
