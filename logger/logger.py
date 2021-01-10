from datetime import datetime
class Log:
    def __init__(self):
        pass

    def write_log(self, sessionID, log_message):
        self.file_obejct open("conversationLogs/"+sessionID+".txt", 'a+')
        self.now = datetime.now()
        seld.date = self.now.date()
        self.curret_time = self.now.strftime("%H:%M:%S")
        self.file_object.write(
            str(self.date) + "/" + str(self.curret_time) + "\t\t" + log_message + "\n")
        )
        self.file_obejct.close()