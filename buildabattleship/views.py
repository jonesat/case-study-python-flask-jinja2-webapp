from flask import Blueprint, render_template, request, session,flash,redirect
import sys
from .Model import Order
from .modelsNew  import Chassis, Module, Engine,System,Weapon
from . import db
from sqlalchemy import and_

# MiniGonne = Weapon(1,"MiniGonne","A big gun","$555","C","Weapon",1,"MachinGonne",3,4,1,"Shield Damage")
# Pike = Weapon(9,"Pike","Entry-Level beam weapon","$888","C","Weapon",2,"Beam",4,1,3,"Hull Damage")
# Laser = Weapon(12,"Laser","Entry level laser weapon","$444","C","Weapon",3,"Laser",1,3,4,"Range")
#
# HeavyGonne = Weapon(10,"Heavy Gonne","A really really big gun","$7777","B","Weapon",4,"MachinGonne",5,7,2,"Shield Damage")
# Halberd = Weapon(8,"Halberd","Melts ship hulls like butter","$9988","B","Weapon",5,"Beam",7,2,5,"Hull Damage")
# DualLaser = Weapon(13,"Dual Laser","An upgraded laser weapon","$6682","B","Weapon",6,"Laser",2,5,7,"Range")
#
# VulkanLaser = Weapon(11,"Vulkan Laser","Rapidfiring laser weapon","$28720","A","Weapon",7,"Laser",6,7,7,"Range")
# HeavyLaser = Weapon(14,"Heavy Laser","A weapon that discharges large laser bursts","$32270","A","Weapon",8,"Laser",3,7,10,"Range")
# GatlingGonne = Weapon(10,"Gatling Gonne","A withering hail of big gonnefire","$24000","A","Weapon",9,"MachinGonne",7,10,3,"Shield Damage")
# Glaive = Weapon(7,"Glaive","A terrifying beam weapon","$40000","A","Weapon",10,"Beam",10,3,7,"Hull Damage")

# BubbleShield = System(2,"Bubble Shield","Basic Energy Bubble","$777","C","System",1,"Shield",1,3,4,"Weight")
# SensorSuite = System(6,"Sensor Suite","A rudimentary set of sensors","$1212","C","System",2,"Sensor",1,4,3,"Weight")
# ArmourPlating = System(15,"Armour Plating","Heavy armour plates","$950","C","System",3,"Armour",4,2,1,"Power Draw")
#
# PrismShield = System(16,"Prism Shield","Minor capacity increase but greater recharge rate","$7777","B","System",4,"Shield",2,5,7,"Weight")
# LRScanner = System(17,"LRScanner","A suite of sensors suitable for exploration","$12120","B","System",5,"Sensor",2,7,5,"Weight")
# ReinforcedPlating = System(18,"Reinforced Plating","Layered armour plates fused together","$9250","B","System",6,"Armour",7,5,2,"Power Draw")
#
# ForceShield = System(19,"Force Shield","Hardened Energy Barriers","$87778","A","System",7,"Shield",3,7,10,"Weight")
# Surveillance = System(20,"Surveillance","A cutting edge sensor suite used by the galaxies spys","$121212","A","System",8,"Sensor",3,10,7,"Weight")
# ReactivePlating = System(21,"Armour Plating","Advanced armour plates that readjust and disperse damage","$95000","A","System",9,"Armour",10,7,3,"Power Draw")
#
# hotbox = Engine(3,"Hotbox","Primitive combustion engine","$333","C","Engine",1,"Combustion","3","4","1","Acceleration")
# FTLDrive = Engine(4,"FTLDrive","Cutting Edge Technology","$251231","A","Engine",2,"FTL","8","3","4","Speed")
# HyperDrive = Engine(5,"HyperDrive","The peoples choice for interstellar travel","$35123","B","Engine",3,"Jump","6","2","7","Speed")

# Kestrel = Chassis(1,"Kestrel","Workhorse of the People","$7777","Frigate",3,4,1,"All-Rounder","Manoeuvrability","B","C","C")
# Blackbird = Chassis(2,"Blackbird","Stealth vessel used by the galactic fedaration","$420000","Cruiser",4,7,3,"Stealth","Manoeuvrability","A","B","B")
# ChassisList = [Kestrel,Blackbird]

# Order1 = Order(1,"Bob","bob@warspace.cospace",1,4,2,1)
Order1 = Order(2,"Mel","mel@seriousspy.secret",2,21,14,1)
# EngineList = [hotbox,FTLDrive,HyperDrive]
# SystemList = [BubbleShield,SensorSuite,ArmourPlating,PrismShield,LRScanner,ReinforcedPlating,ForceShield,Surveillance,ReactivePlating]
# WeaponList = [MiniGonne,Pike,Laser,HeavyGonne,Halberd,DualLaser,VulkanLaser,HeavyLaser,GatlingGonne,Glaive]
# ModuleList = EngineList+SystemList+WeaponList
#
#
# def generateOrder():
#     chassisID = request.values.get("chassisID")
#     moduleID = request.values.get("moduleID")
#     print(chassisID)
#     print("Found")
#     print()





def orderContent(order):
        # dummy = 1;
        # return [0]*10
    keyList = ["ID","Name","price"]
    suffixList1 = ["chassis","engine","system","weapon"]
    suffixList2 = ["chassis","module","module","module"]
    ChassisList1  = Chassis.query.order_by(Chassis.chassisID).all()
    ModuleList1 = Module.query.order_by(Module.moduleID).all()
    # EnginesList = Engine.query.order_by(Engine.ModuleID).all)()
    # SystemsList = System.query.order_by(System.ModuleID).all)()
    # WeaponList = Weapon.query.order_by(Weapon.ModuleID).all)()
    metaList = [ChassisList1,ModuleList1]
    outputVal = [0]*10
    totalPrice = 0.0
    for val in range(len(suffixList1)):
        if(val==0):
            x = 0
        elif(val!=0):
            x = 1
        for object in metaList[x]:
            if getattr(order,suffixList1[val]+keyList[0]) == getattr(object,suffixList2[val]+keyList[0]):
                outputVal[val*2]=getattr(object,suffixList2[val]+keyList[1])
                outputVal[val*2+1]=getattr(object,keyList[2])

                # totalPrice += outputVal[val*2+1];
    # outputVal[8]=totalPrice;
    outputVal[8]=0;
    outputVal[9]=order.orderID
    return outputVal;



# def CartContent(order):
#     if x not in session:
#         session['x'] = "x-number-1"
#     for item in orders:
#         if int(item.id) == int(session['x']):
#             order = item
#
#     return order

bp = Blueprint('main',__name__)

@bp.route('/ProductsChassis/<string:chassisName>',methods=['POST','GET'])
# @bp.route('/Products/<string:moduleType>/',methods=['POST','GET'])
def ProductsChassis(chassisName="All"):
    x = request.values.get("chassisID")
    # chassisID = 2
    #
    # if 'order_id'in session.keys():
    #     order = Order.query.get(session['order_id'])
    #     # order will be None if order_id stale
    # else:
    #     # there is no order
    #     order = None
    #
    # # create new order if needed
    # if order is None:
    #     order = Order(orderID=0,customerName="",customerEmail="",chassisID="",engineID=0,systemID=0,weaponID=0)
    #     try:
    #         db.session.add(order)
    #         db.session.commit()
    #         session['order_id'] = order.id
    #     except:
    #         print('failed at creating a new order')
    #         order = None
    # if chassisID is not None and order is not None:
    #         item = Chassis.query.get(chassisID)
    #         if item not in order.chassisID:
    #             try:
    #                 order.chassisID.append(item)
    #                 db.session.commit()
    #             except:
    #                 return 'We could not add this ship to  cart'
    #             return redirect(url_for('main.ProductsChassis',chassisName='All'))
    #         else:
    #             flash('item already in basket')
    #             return redirect(url_for('main.ProductsChassis',chassisName='All'))
    #
    # print(f"The chassis1 ID is {x}, ok?")
    # if(x !="None"):
    #     flash(f"Thank you for adding ship {x} to cart  on page {chassisName}")


    ChassisListOut=[]
    if(chassisName=="All"):
        # ChassisListOut = ChassisList
        ChassisListOut  = Chassis.query.order_by(Chassis.chassisID).all()

    elif(chassisName!="All"):
        # for item in ChassisList:
        #     if(chassisName == item.chassisName):
        #         ChassisListOut = [item]
        ChassisListOut =  Chassis.query.filter(Chassis.chassisName==chassisName)

    return render_template('ProductsChassis.html',Chassis=ChassisListOut,orderContent= orderContent(Order1));

@bp.route('/ProductsModules/<string:moduleType>/<int:item>/<string:moduleName>',methods=['POST','GET'])
@bp.route('/ProductsModules/<string:moduleType>/<string:quality>',methods=['POST','GET'])
def ProductsModules(moduleType="",quality="",item="",moduleName=""):
    x = request.values.get("moduleID")
    print(f"The module1 ID is {x}, ok?")
    if(x !="None"):
        flash(f"Thank you for adding module {x} to cart on page products modules")
    ModuleListOut = []
    ModuleDListOut = []
    z = []
    mlist=["moduleID","moduleName","description","price","quality","moduleType"]
    elist=["engineID","engineType","speed","acceleration","fuelEfficiency","keyFeature"]
    slist=["systemID","systemType","weight","maintenance","powerDraw","keyFeature"]
    wlist=["weaponID","armamentType","hullDamage","shieldDamage","range","keyFeature"]

    if quality=="All":
        print("Quality is all")
        zz=[]
        labelList = {"Engine":mlist+elist,"System":mlist+slist,"Weapon":mlist+wlist}
        ModuleListOut = Module.query.filter(Module.moduleType==moduleType)
        if moduleType=="Engine":
            ModuleDListOut =  Engine.query.filter(and_(Module.moduleType==moduleType,Engine.moduleID==Module.moduleID))
            print(ModuleDListOut)
            for obj1,obj2 in zip(ModuleListOut,ModuleDListOut):
                for item in mlist:
                    z.append(getattr(obj1,item))
                for item in elist:
                    z.append(getattr(obj2,item))
                zz.append(dict(zip(labelList[moduleType],z)))
            ModuleListOut = zz
        if moduleType=="System":
            ModuleDListOut =  System.query.filter(and_(Module.moduleType==moduleType,System.moduleID==Module.moduleID))
            for obj1,obj2 in zip(ModuleListOut,ModuleDListOut):
                for item in mlist:
                    z.append(getattr(obj1,item))
                for item in slist:
                    z.append(getattr(obj2,item))
                zz.append(dict(zip(labelList[moduleType],z)))
            ModuleListOut = zz
        if moduleType=="Weapon":
            ModuleDListOut =  Weapon.query.filter(and_(Module.moduleType==moduleType,Weapon.moduleID==Module.moduleID))
            for obj1,obj2 in zip(ModuleListOut,ModuleDListOut):
                for item in mlist:
                    z.append(getattr(obj1,item))
                for item in wlist:
                    z.append(getattr(obj2,item))
                zz.append(dict(zip(labelList[moduleType],z)))
            ModuleListOut = zz

    if moduleName!='':
        # for module in ModuleList:
        #     if(moduleName==module.moduleName):
        #         ModuleListOut = [module]
        ModuleListOut =  Module.query.filter(Module.moduleName==moduleName)
        if moduleType == "Engine":
            nList = mlist+elist
            ModuleDListOut = Engine.query.filter(Engine.moduleID == ModuleListOut[0].moduleID)
            for item in mlist:
                z.append(getattr(ModuleListOut[0],item))
            for item in elist:
                z.append(getattr(ModuleDListOut[0],item))
            ModuleListOut = dict(zip(nList,z))
        if moduleType == "System":
            nList = mlist+slist
            ModuleDListOut = System.query.filter(System.moduleID == ModuleListOut[0].moduleID)
            for item in mlist:
                z.append(getattr(ModuleListOut[0],item))
            for item in slist:
                z.append(getattr(ModuleDListOut[0],item))
            ModuleListOut = dict(zip(nList,z))
        if moduleType == "Weapon":
            nList = mlist+wlist
            ModuleDListOut = Weapon.query.filter(Weapon.moduleID == ModuleListOut[0].moduleID)
            for item in mlist:
                z.append(getattr(ModuleListOut[0],item))
            for item in wlist:
                z.append(getattr(ModuleDListOut[0],item))
            ModuleListOut = [dict(zip(nList,z))]

    else:
        ModuleListOut =  Module.query.filter(and_(Module.moduleType==moduleType,Module.quality==quality))
        Weights={"A":3,"B":2,"C":1}
        zz=[]

        labelList = {"Engine":mlist+elist,"System":mlist+slist,"Weapon":mlist+wlist}

        if moduleType=="Engine":
            ModuleDListOut =  Engine.query.filter(and_(Module.moduleType==moduleType,Module.quality==quality,Engine.moduleID==Module.moduleID))
            for obj1,obj2 in zip(ModuleListOut,ModuleDListOut):
                z=[]
                for item in mlist:
                    z.append(getattr(obj1,item))
                for item in elist:
                    z.append(getattr(obj2,item))
                zz.append(dict(zip(labelList[moduleType],z)))
            ModuleListOut = zz
        if moduleType=="System":
            ModuleDListOut =  System.query.filter(and_(Module.moduleType==moduleType,Module.quality==quality,System.moduleID==Module.moduleID))
            for obj1,obj2 in zip(ModuleListOut,ModuleDListOut):
                z=[]
                for item in mlist:
                    z.append(getattr(obj1,item))
                for item in slist:
                    z.append(getattr(obj2,item))
                zz.append(dict(zip(labelList[moduleType],z)))
            ModuleListOut = zz
        if moduleType=="Weapon":
            ModuleDListOut =  Weapon.query.filter(and_(Module.moduleType==moduleType,Module.quality==quality,Weapon.moduleID==Module.moduleID))
            for obj1,obj2 in zip(ModuleListOut,ModuleDListOut):
                z = []
                for item in mlist:
                    z.append(getattr(obj1,item))
                for item in wlist:
                    z.append(getattr(obj2,item))
                zz.append(dict(zip(labelList[moduleType],z)))
            ModuleListOut = zz

    # for item in ModuleListOut:
    #     print(item)
    #     for keys,values in item.items():
    #         print(keys,values)






        #
        # if moduleType=="Engine":
        #     # if(moduleName==""):
        #         for module in EngineList:
        #             if(Weights[module.quality]<=Weights[quality]):
        #                 ModuleListOut.append(module)
        #
        # elif moduleType=="System":
        #     # if(moduleName==""):
        #         for module in SystemList:
        #             if(Weights[module.quality]<=Weights[quality]):
        #                 ModuleListOut.append(module)
        #
        # elif moduleType=="Weapon":
        #     # if(moduleName==""):
        #         for module in WeaponList:
        #             if(Weights[module.quality]<=Weights[quality]):
        #                 ModuleListOut.append(module)


    print(ModuleListOut)
    return render_template('ProductsModules.html',Module=ModuleListOut, orderContent = orderContent(Order1));



@bp.route('/DetailChassis/<string:chassisName>',methods=['POST','GET'])
def DetailChassis(chassisName):

    # x = request.values.get("chassisID")
    ChassisListOut =  Chassis.query.filter(Chassis.chassisName==chassisName)
    print()
    print(chassisName)
    print(ChassisListOut)
    print()
    return render_template('DetailChassis.html',Chassis=ChassisListOut,orderContent= orderContent(Order1));

@bp.route('/DetailModule/<string:moduleType>/<string:moduleName>/',methods=['POST','GET'])
def DetailModule(moduleType,moduleName):

    x = request.values.get("moduleID")
    print(x)
    ModuleListOut = []
    ModuleDListOut = []
    z = []
    mlist=["moduleID","moduleName","description","price","quality","moduleType"]
    elist=["engineID","engineType","speed","acceleration","fuelEfficiency","keyFeature"]
    slist=["systemID","systemID","weight","maintenance","powerDraw","keyFeature"]
    wlist=["weaponID","armamentType","hullDamage","shieldDamage","range","keyFeature"]
    ModuleListOut =  Module.query.filter(Module.moduleName==moduleName)
    if moduleType == "Engine":
        nList = mlist+elist
        ModuleDListOut = Engine.query.filter(Engine.moduleID == ModuleListOut[0].moduleID)
        for item in mlist:
            z.append(getattr(ModuleListOut[0],item))
        for item in elist:
            z.append(getattr(ModuleDListOut[0],item))
        ModuleListOut = dict(zip(nList,z))
    if moduleType == "System":
        nList = mlist+slist
        ModuleDListOut = System.query.filter(System.moduleID == ModuleListOut[0].moduleID)
        for item in mlist:
            z.append(getattr(ModuleListOut[0],item))
        for item in slist:
            z.append(getattr(ModuleDListOut[0],item))
        ModuleListOut = dict(zip(nList,z))
    if moduleType == "Weapon":
        nList = mlist+wlist
        ModuleDListOut = Weapon.query.filter(Weapon.moduleID == ModuleListOut[0].moduleID)
        for item in mlist:
            z.append(getattr(ModuleListOut[0],item))
        for item in wlist:
            z.append(getattr(ModuleDListOut[0],item))
        ModuleListOut = [dict(zip(nList,z))]
    # if moduleType == "Engine":
    #         for item in EngineList :
    #             if(moduleName == item.moduleName):
    #                 moduleOut=item
    #
    # elif moduleType == "System":
    #         for item in SystemList :
    #             if(moduleName == item.moduleName):
    #                 moduleOut=item
    #
    # elif moduleType == "Weapon":
    #         for item in WeaponList:
    #             if(moduleName == item.moduleName):
    #                 moduleOut=item

    return render_template('DetailModule.html',Module = ModuleListOut,orderContent= orderContent(Order1));

@bp.route('/Products/')
def search():
	search = request.args.get('search')
	search = '%{}%'.format(search) # substrings will match
	ChassisListOut = Chassis.query.filter(Chassis.chassisName.like(search)).all()
	return render_template('ProductsChassis.html', Chassis=ChassisListOut,orderContent= orderContent(Order1))


@bp.route('/secret')
@bp.route('/secret2')
def secret():
    return '<h3 style="color:green;"> Hello secremt! <h3>'
