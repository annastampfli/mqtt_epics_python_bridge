import variables as var
from pcaspy import Driver

class myDriver(Driver):
    def __init__(self):
        super(myDriver, self).__init__()
    def read(self, reason):

	#DATAV
	if reason == 'V1': value = var.V1;
	elif reason == 'V2': value = var.V2;
	elif reason == 'V3': value = var.V3;
        elif reason == 'V4': value = var.V4;
	elif reason == 'V5': value = var.V5;
        elif reason == 'V6': value = var.V6;
        elif reason == 'V7': value = var.V7;
        elif reason == 'V8': value = var.V8;

	#DATAP
        elif reason == 'PPC': value = var.ppc;
        elif reason == 'PPV': value = var.ppv;

	#DATAC
	elif reason == 'IC': value = var.ic;
        elif reason == 'GAS1': value = var.gas1;
        elif reason == 'GAS2': value = var.gas2;
        elif reason == 'PGAS1': value = var.pgas1;
        elif reason == 'PGAS2': value = var.pgas2;
        elif reason == 'CYCLE': value = var.cycle;
        elif reason == 'ACTCYCLE': value = var.actcycle;
        elif reason == 'STATUS': value = var.status;
	elif reason == 'SETPOINT': value = var.setpoint;

	else: value = self.getParam(reason)
	return value

    def write(self, reason, value):
        status = True
        #if reason == 'DATA': global msgData; msgData = value; publish.single(MQTT_TOPIC_01, msgData, hostname=MQTT_SERVER);
	#elif reason == 'TEST': global msgTest; msgTest = value; publish.single(MQTT_TOPIC_02, msgTest, hostname=MQTT_SERVER);
	#elif reason == 'FILL': global msgFill; msgFill = value; publish.single(MQTT_TOPIC_03, msgFill, hostname=MQTT_SERVER);
	#elif reason == 'RECEIPT':
#		global receipt, msgGas1, msgGas2, msgPGas1, msgPGas2, energy, coresponding; 
#		receipt = value; 
#		temp = Json(msgDataC); 
#		msgGas1 = str(temp.dataC.pcGM[receipt].gas1); 
#		msgGas2 = str(temp.dataC.pcGM[receipt].gas2);
#		msgPGas1 = int(temp.dataC.pcGM[receipt].pgas1)
#		msgPGas2 = int(temp.dataC.pcGM[receipt].pgas2)
#		energy = str(temp.dataC.pcGM[receipt].Energy)
#		coresponding = str(temp.dataC.pcGM[receipt].Coresponding)

        if status:
           self.setParam(reason, value)
        return status