class Deck ():

    def __init__(self, index=None):
        self.deckindex = index
        self.PlateList = []
        self.PipetteList = []
        


    def __repr__(self):
        return 'D{}'.format(self.deckindex)

    def __str__(self):
        return 'Deck {}'.format(self.deckindex)

    def __len__(self):
        return len(self.PlateList)

    def __getitem__(self, position):
        if type(position) == int:
            return self.PlateList[position]
        elif type(position) == str:
            for i in range(len(self.PlateList)):
                if (self.PlateList[i].plateName == position) or (self.PlateList[i].plateTypeName == position):
                    return self.PlateList[i]
        print("'"+str(position)+"' not found")
    
    def nextfreeplate(self):
        # freeplates = []
        # for plate in self.PlateList:
        #     if plate.isempty():
        #         freeplates.append(plate.plateIndex)
        # if len(freeplates)>=1:
        #     nextfreeplate= int(freeplates[0])
        # else:
        #     nextfreeplate = "no free wells"
        nextfreeplateindex = len(self.PlateList)+1
        #nextfreeplateindex = 1
        return nextfreeplateindex

    def add(self, Type, location, numwells=None, platewellVolume=None, platename = ""):
        DeckObject(self, Type, index=self.nextfreeplate(), numwells=numwells,platewellVolume=platewellVolume, platename=platename)
        return self.PlateList[-1]

    def findPippets (self, volume):
        releventracks = []
        for plate in self.PlateList:
            if plate.platetype == "TipRack":
                if int(plate.tipVolume) == int(volume):
                    releventracks.append(plate.plateName)
        return releventracks

    def findTipRacks (self, volume):
        releventracks = []
        for plate in self.PlateList:
            if plate.platetype == "TipRack":
                if int(plate.tipVolume) == int(volume):
                    releventracks.append(plate.plateName)
        return releventracks

    def addPipette (self, name, model, mount, volume):
        #self.PipetteList.append(self, pipette(len(self.PipetteList), name, model, mount, volume))
        self.PipetteList.append(Pipette(self, len(self.PipetteList), name, model, mount, volume))
                    


class DeckObject ():
    def __init__(self, Deck, Type, index=None, numwells=None, platewellVolume=None, platename="", numTips=None, tipVolume=None):
        if Type == "Plate":
            Deck.PlateList.append(Plate(Deck, index, numwells, platewellVolume, platename))
        elif Type == "TipRack":
            Deck.PlateList.append(TipRack(Deck, index, numTips=numwells, tipVolume=platewellVolume, platename=platename))

class Plate ():

    def __init__(self, Deck, index=None, numwells=None, platewellVolume=None, platename=""):
        self.platetype = "Plate"
        self.deck = Deck
        self.plateIndex = index
        self.numwells = numwells
        self.platewellVolume = platewellVolume
        self.WellList = None
        self.setupwells()
        self.plateTypeName= "plate_"+str(numwells)
        self.plateName = platename
        self.activeWell = self.nextfreewell()

    def __repr__(self):
        return 'D{}P{}'.format(self.deck.deckindex, self.plateIndex)

    def __str__(self):
        return 'Deck {}, Plate number {}'.format(self.deck.deckindex, self.plateIndex)

    def __len__(self):
        return len(self.WellList)

    def __getitem__(self, position):
        return self.WellList[position]

    def printplate(self):
        for well in self.WellList:
            print(str(well.StartSmiles) + " " + str(well.GoalSmiles) + " " + str(well.VolumeUsed)+ "/" + str(well.Volume))

    def setupwells(self):
        self.WellList = []
        for well in range(self.numwells):
            self.WellList.append(Well(self, wellindex=well, Volume=self.platewellVolume, VolumeUsed=0, StartSmiles="", GoalSmiles=""))
        return self.WellList

    def addplacehoder(self):
        pass
        #self.WelList(self.nextfreewell()) = ""
        


    def nextfreewell(self):
        freewells = []
        for well in self.WellList:
            if well.isempty():
                freewells.append(well.wellindex)
        if len(freewells)>=1:
            nextfreewell = int(freewells[0])
        else:
            nextfreewell = "no free wells"
        return nextfreewell

    def isempty(self):
        isempty = True
        for well in self.WellList:
            if not well.isempty():
                isempty = False
        return isempty

    def smilesearch(self, smiles, start_smiles=None, goal_smiles=None):
        if (start_smiles == None) & (goal_smiles == None):
            start_smiles = True
            goal_smiles = True
        startinstances = []
        goalinstances = []
        for well in self.WellList:
            if start_smiles == True:
                if well.StartSmiles == smiles:
                    startinstances.append(well.wellindex)
            if goal_smiles == True:
                if well.StartSmiles == smiles:
                    startinstances.append(well.wellindex)
        return[startinstances, goalinstances]


    
class TipRack ():
    
    def __init__(self, Deck, index=None, numTips=None, tipVolume=None, platename=""):
        self.platetype = "TipRack"
        self.deck = Deck
        self.plateIndex = index
        self.numTips = numTips
        self.tipVolume = tipVolume
        self.TipList = []
        self.setupTips()
        self.plateTypeName= platename
        self.plateName = "tips_"+str(numTips)+"_"+str(tipVolume)

    def __repr__(self):
        return 'D{}T{}'.format(self.deckindex, self.plateIndex)

    def __str__(self):
        return 'Deck {} TipRack {}'.format(self.deckindex, self.plateIndex)

    def __len__(self):
        return len(self.TipList)

    def __getitem__(self, position):
        return self.TipList[position]
    
    def setupTips (self):
        for i in range(self.numTips):
            self.TipList.append(True)
        return self.TipList

    def nextFreeTip (self):
        for i in range(len(self.TipList)):
            if self.TipList[i] == True:
                return i
        return False

    def useTip (self, index):
        self.TipList[index] = False

class Well ():
    
    def __init__(self, Plate, wellindex=None, Volume=None, VolumeUsed=0, StartSmiles=None, GoalSmiles=None):
        self.plate = Plate
        self.wellindex = wellindex
        self.Volume = float(Volume)
        self.VolumeUsed = float(VolumeUsed)
        self.StartSmiles = StartSmiles
        self.GoalSmiles = GoalSmiles
        
    def __repr__(self):
        return 'D{}P{}W{}'.format(self.plate.deck.deckindex, self.plate.plateIndex, self.wellindex)

    def __str__(self):
        return 'Deck {}, Plate {}, Well {}'.format(self.plate.deck.deckindex, self.plate.plateIndex, self.wellindex)
    
    def add(self, Ammount, smiles=""):
        SafetyMargin = 5 # percentage of the well's volume to be keept empty to prevent overvlow
        WorkingVolumeused = self.VolumeUsed+Ammount
        if WorkingVolumeused >= float(self.Volume)*(1-(SafetyMargin/100)):
            raise NameError("the resultant value of adding "+str(Ammount)+"ul  to "+str(self.VolumeUsed)+"ul would be "+str(WorkingVolumeused)+"ul exceeding the well's volume of "+str(self.Volume)+"ul (with a saftey margin of "+str(SafetyMargin)+"%)")
            self.VolumeUsed = False
        elif WorkingVolumeused < 0:
            raise NameError("the resultant value of adding "+str(Ammount)+"ul to "+str(self.VolumeUsed)+"ul would be "+str(WorkingVolumeused)+"ul")
            self.VolumeUsed = False
        else:
            self.VolumeUsed = WorkingVolumeused
            if smiles != "":
                self.changesmiles(start_smiles=smiles)
        return self.VolumeUsed
    
    def isempty(self):
        if self.VolumeUsed <= 0:
            isempty = True
        else:
            isempty = False
        return isempty


    def changesmiles(self, start_smiles=None, goal_smiles=None):
        if type(start_smiles) != None:
            if type(start_smiles) == str:
                self.StartSmiles = start_smiles
        if type(goal_smiles) != None:
            if type(goal_smiles) == str:
                self.GoalSmiles = goal_smiles
        return [self.StartSmiles, self.GoalSmiles]

class Pipette():
    def __init__(self, deck, pipetteIndex, name, model, mount, volume):
        self.deck = deck
        self.pipetteIndex = pipetteIndex
        self.name = name
        self.model = model
        self.mount = mount
        self.volume = volume
        self.tipRacks = self.deck.findTipRacks(self.volume)
