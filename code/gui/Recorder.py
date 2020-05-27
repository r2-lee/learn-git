import os
import sys

import PyQt5.QtWidgets as QtWidgets
from PyQt5.QtCore import QUrl, pyqtSlot
from PyQt5.QtMultimedia import (
    QAudioRecorder, QAudioProbe, QMultimedia, QMediaRecorder, QAudioEncoderSettings, QAudioFormat)
from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow, QMessageBox

from Ui_Recorder import Ui_Form


class Recorder(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.recorder = QAudioRecorder(self)
        self.recorder.stateChanged.connect(self.do_stateChanged)
        self.recorder.durationChanged.connect(self.do_durationChanged)

        self.probe = QAudioProbe(self)
        self.probe.setSource(self.recorder)
        self.probe.audioBufferProbed.connect(self.do_processBuffer)

        if self.recorder.defaultAudioInput() == "":  # str类型
            return  # 无音频录入设备

        for device in self.recorder.audioInputs():
            self.ui.comboDevices.addItem(device)  # 音频录入设备列表

        for codecName in self.recorder.supportedAudioCodecs():
            self.ui.comboCodec.addItem(codecName)  # 支持的音频编码

        sampleList, isContinuous = self.recorder.supportedAudioSampleRates()
        # isContinuous 是否支持连续的采样率，与C++不一样

        for i in range(len(sampleList)):
            self.ui.comboSampleRate.addItem("%d" % sampleList[i])  # 支持的采样率

# channels
        self.ui.comboChannels.addItem("1")
        self.ui.comboChannels.addItem("2")
        self.ui.comboChannels.addItem("4")

# quality
        self.ui.sliderQuality.setRange(0, QMultimedia.VeryHighQuality)
        self.ui.sliderQuality.setValue(QMultimedia.NormalQuality)

# bitrates
        self.ui.comboBitrate.addItem("32000")
        self.ui.comboBitrate.addItem("64000")
        self.ui.comboBitrate.addItem("96000")
        self.ui.comboBitrate.addItem("128000")

        self.__addToolbar()

    def __addToolbar(self):
        layout = QtWidgets.QVBoxLayout()

        Astart = QtWidgets.QToolButton()
        Astart.setText("开始")
        Astart.setDefaultAction(self.ui.actRecordStart)
        Apause = QtWidgets.QToolButton()
        Apause.setText("暂停")
        Apause.setDefaultAction(self.ui.actRecordPause)
        Astop = QtWidgets.QToolButton()
        Astop.setText("停止")
        Astop.setDefaultAction(self.ui.actRecordStop)

        self.toolbar = QtWidgets.QToolBar()
        self.toolbar.addWidget(Astart)
        self.toolbar.addWidget(Apause)
        self.toolbar.addWidget(Astop)

        layout.addWidget(self.toolbar)
        layout.addWidget(self.ui.widget)

        self.setLayout(layout)

    def __setRecordParams(self):
        selectedFile=self.ui.editOutputFile.text().strip()
        if (selectedFile ==""):
            QMessageBox.critical(self,"错误","请先设置录音输出文件")
            return False
        
        if os.path.exists(selectedFile):
            os.remove(selectedFile)#删除已有文件
                 
        recordFile=QUrl.fromLocalFile(selectedFile)
        self.recorder.setOutputLocation(recordFile)  #设置输出文件

        recordDevice=self.ui.comboDevices.currentText()
        self.recorder.setAudioInput(recordDevice)    #设置录入设备

        settings=QAudioEncoderSettings()    #音频编码设置
        settings.setCodec(self.ui.comboCodec.currentText())   #编码

        sampRate=int(self.ui.comboSampleRate.currentText())
        settings.setSampleRate(sampRate)    #采样率

        bitRate=int(self.ui.comboBitrate.currentText())
        settings.setBitRate(bitRate)  #比特率

        channelCount=int(self.ui.comboChannels.currentText())
        settings.setChannelCount(channelCount)    #通道数

        quality=QMultimedia.EncodingQuality(self.ui.sliderQuality.value())
        settings.setQuality(quality)     #品质

        if self.ui.radioQuality.isChecked():  #编码模式为固定品质,自动决定采样率，采样点大小
            settings.setEncodingMode(QMultimedia.ConstantQualityEncoding)
        else:
            settings.setEncodingMode(QMultimedia.ConstantBitRateEncoding)  #固定比特率
        
        self.recorder.setAudioSettings(settings) #音频设置
        return True

##  ==========由connectSlotsByName() 自动连接的槽函数==================    
    @pyqtSlot()
    def on_btnGetFile_clicked(self):    ##"录音输出文件"按钮
        curPath=os.getcwd()        #获取系统当前目录
        dlgTitle="选择输出文件"   
        filt="wav文件(*.wav)"     
        fileName,flt,=QFileDialog.getSaveFileName(self, dlgTitle, curPath, filt)
        if (fileName !=""):
            self.ui.editOutputFile.setText(fileName)
    
    @pyqtSlot()    ##开始录音
    def on_actRecordStart_triggered(self): 
        success=True
        if (self.recorder.state() == QMediaRecorder.StoppedState):  #已停止，重新设置
            success=self.__setRecordParams()  #设置录音参数
        if success:   
            self.recorder.record()

    @pyqtSlot()    ##暂停
    def on_actRecordPause_triggered(self): 
        self.recorder.pause()
    
    @pyqtSlot()
    def on_actRecordStop_triggered(self): 
        self.recorder.stop()

##  =============自定义槽函数===============================       
    def do_stateChanged(self,state):  ##状态变化
        isRecording=(state==QMediaRecorder.RecordingState)  #正在录制
        self.ui.actRecordStart.setEnabled(not isRecording)
        self.ui.actRecordPause.setEnabled(isRecording)
        self.ui.actRecordStop.setEnabled(isRecording)

        isStoped=(state==QMediaRecorder.StoppedState)    #已停止
        self.ui.btnGetFile.setEnabled(isStoped)
        self.ui.editOutputFile.setEnabled(isStoped)

    def do_durationChanged(self,duration):  ##持续时间长度变化
        self.ui.LabPassTime.setText("已录制 %d 秒"%(duration/1000))
    
    def do_processBuffer(self,buffer):     ##解析缓冲区数据
        self.ui.spin_byteCount.setValue(buffer.byteCount())      #缓冲区字节数
        self.ui.spin_duration.setValue(buffer.duration()/1000)   #缓冲区时长
        self.ui.spin_frameCount.setValue(buffer.frameCount())    #缓冲区帧数
        self.ui.spin_sampleCount.setValue(buffer.sampleCount())  #缓冲区采样数
  
        audioFormat=buffer.format()      #缓冲区格式,QAudioBuffer
        self.ui.spin_channelCount.setValue(audioFormat.channelCount()) #通道数
        self.ui.spin_sampleSize.setValue(audioFormat.sampleSize())     #采样大小
        self.ui.spin_sampleRate.setValue(audioFormat.sampleRate())     #采样率
        self.ui.spin_bytesPerFrame.setValue(audioFormat.bytesPerFrame()) #每帧字节数
  
        if (audioFormat.byteOrder()==QAudioFormat.LittleEndian):
           self.ui.edit_byteOrder.setText("LittleEndian")   #字节序
        else:
           self.ui.edit_byteOrder.setText("BigEndian")
  
        self.ui.edit_codec.setText(audioFormat.codec()) #编码格式
  
        if (audioFormat.sampleType()==QAudioFormat.SignedInt): #采样点类型
           self.ui.edit_sampleType.setText("SignedInt")
        elif(audioFormat.sampleType()==QAudioFormat.UnSignedInt):
           self.ui.edit_sampleType.setText("UnSignedInt")
        elif(audioFormat.sampleType()==QAudioFormat.Float):
           self.ui.edit_sampleType.setText("Float")
        else:
           self.ui.edit_sampleType.setText("Unknown")

if __name__ == "__main__":
    import sys
    qapp = QtWidgets.QApplication(sys.argv)
    app = Recorder()
    app.show()
    sys.exit(qapp.exec_())
