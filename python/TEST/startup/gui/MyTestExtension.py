import GafferUI
import MyTestExtension
import MyTestExtensionUI

nodeMenu = GafferUI.NodeMenu.acquire( application )

nodeMenu.append( "/MyTestExtension/Box", MyTestExtension.Box )

