#测试程序
import ak47
import awp

ak = ak47.Ak47("Ak47",30,0,0.4,3)    #示例化Ak47对象
ak.reload()         #填弹
ak.fire()           #开火
ak.fire()           #开火
print("--------------")
aw = awp.Awp("Awp",10,0,1.0,1)      #实例化Awp对象
aw.reload()
aw.openTelescope()
aw.fire()
aw.closeTelescope()

















