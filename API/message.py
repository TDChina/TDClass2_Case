import maya.OpenMaya as OpenMaya

callback_array = OpenMaya.MCallbackIdArray()


def call_back(time_s, time_e, *args):
    '''
    '''
    print time_s, time_e



callback_array.append(OpenMaya.MTimerMessage.addTimerCallback(2, call_back))

OpenMaya.MMessage.removeCallbacks(callback_array)
