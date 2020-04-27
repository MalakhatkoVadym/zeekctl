# This plugin sets necessary environment variables to run Zeek with
# testimony load balancing.

import ZeekControl.plugin

class LBTestimony(ZeekControl.plugin.Plugin):
    def __init__(self):
        super(LBTestimony, self).__init__(apiversion=1)

    def name(self):
        return "lb_testimony"

    def pluginVersion(self):
        return 1

    def init(self):
        useplugin = False

        for nn in self.nodes():
            if nn.type != "worker" or nn.lb_method != "testimony":
                continue

            useplugin = True

            # runnning zeek worker with testimony::pathToSocket as interfaces.
            nn.interface = "%s::%s" % ("testimony", nn.interface)

        return useplugin
