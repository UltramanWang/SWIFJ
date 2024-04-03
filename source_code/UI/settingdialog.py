import os
import sys
import json
from loguru import logger
from PyQt5.QtWidgets import QDialog
from PyQt5.QtSerialPort import QSerialPort ,QSerialPortInfo
from ui.ui_settingdialog import Ui_Dialog
from source_code.script.utils import utils

class Settings():
    def __init__(self):
        self.name = ""
        self.baud_rate = 0
        self.string_baud_rate = ""
        self.data_bits = QSerialPort.Data8
        self.string_data_bits = ""
        self.parity = QSerialPort.NoParity
        self.string_parity = ""
        self.stop_bits =  QSerialPort.OneStop
        self.string_stop_bits = ""
        self.flow_control = QSerialPort.SoftwareControl
        self.string_flow_control = ""
        self.local_echo_enabled = False

class Settingtest():
    def __init__(self):
        self.name = ""
        self.baud_rate = 0
        self.data_bits = QSerialPort.Data8
        self.parity = QSerialPort.NoParity
        self.stop_bits =  QSerialPort.OneStop
        self.flow_control = QSerialPort.SoftwareControl


class SettingDialog(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.m_ui = Ui_Dialog()
        self.m_ui.setupUi(self) 
        self.m_currentSettings = Settings() #m_currentSettings初始化
        self.m_currentSet = Settingtest() #m_currentSet初始化,主页点击打开串口的配置
        print("hello World")
        self.checkParameter()#检查本地是否有串口的配置文件

        self.m_ui.applyButton.clicked.connect(self.apply)#点击保存串口配置按钮

        # self.fill_ports_parameters()#串口配置参数
        self.full_port_info()#获取端口号


    def apply(self):
        self.update_settings()   #更新m_currentSettings值
        self.to_dict()           #将配置写成字典
        self.save_to_json()
        self.hide() 

    def setting(self):
        self.update_setting()
        return self.m_currentSet

    def full_port_info(self):
        self.m_ui.serialPortInfoListBox.clear()
        for info in QSerialPortInfo.availablePorts():
            self.m_ui.serialPortInfoListBox.addItem(info.portName())

    def fill_ports_parameters(self):
        self.m_ui.baudRateBox.addItem("9600", QSerialPort.Baud9600)
        self.m_ui.baudRateBox.addItem("19200", QSerialPort.Baud19200)
        self.m_ui.baudRateBox.addItem("38400", QSerialPort.Baud38400)
        self.m_ui.baudRateBox.addItem("115200", QSerialPort.Baud115200)
        self.m_ui.baudRateBox.addItem("Custom")
        self.m_ui.baudRateBox.setCurrentIndex(1)
 
        self.m_ui.dataBitsBox.addItem("5", QSerialPort.Data5)
        self.m_ui.dataBitsBox.addItem("6", QSerialPort.Data6)
        self.m_ui.dataBitsBox.addItem("7", QSerialPort.Data7)
        self.m_ui.dataBitsBox.addItem("8", QSerialPort.Data8)
        self.m_ui.dataBitsBox.setCurrentIndex(3)
 
        self.m_ui.parityBox.addItem("None", QSerialPort.NoParity)
        self.m_ui.parityBox.addItem("Even", QSerialPort.EvenParity)
        self.m_ui.parityBox.addItem("Odd", QSerialPort.OddParity)
        self.m_ui.parityBox.addItem("Mark", QSerialPort.MarkParity)
        self.m_ui.parityBox.addItem("Space", QSerialPort.SpaceParity)
 
        self.m_ui.stopBitsBox.addItem("1", QSerialPort.OneStop)
        if sys.platform == "win32":
            self.m_ui.stopBitsBox.addItem("1.5", QSerialPort.OneAndHalfStop)
 
        self.m_ui.stopBitsBox.addItem("2", QSerialPort.TwoStop)
 
        self.m_ui.flowControlBox.addItem("None", QSerialPort.NoFlowControl)
        self.m_ui.flowControlBox.addItem("RTS/CTS", QSerialPort.HardwareControl)
        self.m_ui.flowControlBox.addItem("XON/XOFF", QSerialPort.SoftwareControl)


    def update_settings(self):
        self.m_currentSettings.name = self.m_ui.serialPortInfoListBox.currentText()
 
        self.m_currentSettings.baud_rate = self.m_ui.baudRateBox.currentData()
        self.m_currentSettings.string_baud_rate = f"{self.m_currentSettings.baud_rate}"
 
        self.m_currentSettings.data_bits = self.m_ui.dataBitsBox.currentData()
        self.m_currentSettings.string_data_bits = self.m_ui.dataBitsBox.currentText()
 
        self.m_currentSettings.parity = self.m_ui.parityBox.currentData()
        self.m_currentSettings.string_parity = self.m_ui.parityBox.currentText()
 
        self.m_currentSettings.stop_bits = self.m_ui.stopBitsBox.currentData()
        self.m_currentSettings.string_stop_bits = self.m_ui.stopBitsBox.currentText()
 
        self.m_currentSettings.flow_control = self.m_ui.flowControlBox.currentData()
        self.m_currentSettings.string_flow_control = self.m_ui.flowControlBox.currentText()    
         
    def update_setting(self):
        self.m_currentSet.name = self.m_ui.serialPortInfoListBox.currentText()
        self.m_currentSet.baud_rate = self.m_ui.baudRateBox.currentData()
        self.m_currentSet.data_bits = self.m_ui.dataBitsBox.currentData()
        self.m_currentSet.parity = self.m_ui.parityBox.currentData()
        self.m_currentSet.stop_bits = self.m_ui.stopBitsBox.currentData()
        self.m_currentSet.flow_control = self.m_ui.flowControlBox.currentData()
    
    def to_dict(self):
        return {
           'baud_rate': self.m_currentSettings.baud_rate,
           'dataBits':self.m_currentSettings.data_bits,
           'Parity':self.m_currentSettings.parity,
           'stopBits':self.m_currentSettings.stop_bits,
           'flowControl':self.m_currentSet.flow_control
        }
    
    def save_to_json(self, file_path='D:\\Project\\Demo\\SWIFJ\\config'):
        file_path=utils.get_config_path()
        file_path=os.path.join(file_path,'uart.json')
        data = self.to_dict()
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)
        crc32_value = utils.calculate_crc32(file_path)

    def checkParameter(self):
        uart_file=utils.get_config_path()
        file_uart=os.path.join(uart_file,'uart.json')
        if os.path.exists(file_uart):
            print("文件存在")
            crc32_value = utils.calculate_crc32(file_uart)
            if not crc32_value:
               self.fill_ports_parameters() 
            else:
                with open(file_uart, 'r') as file:
                    data = json.load(file)  
                print('-----------',data['baud_rate'])
                self.m_ui.baudRateBox.addItem(str(data['baud_rate']))
                self.m_ui.dataBitsBox.addItem(str(data['dataBits']))
                self.m_ui.parityBox.addItem(str(data['Parity']))
                self.m_ui.stopBitsBox.addItem(str(data['stopBits']))
                self.m_ui.flowControlBox.addItem(str(data['flowControl']))
        else:
            print("文件不存在")
            self.fill_ports_parameters()


         