import unittest, os
from workflow.gpt.summary import request_gpt


class MyTestCase(unittest.TestCase):
    def test_something(self):
        os.environ["https_proxy"] = "http://127.0.0.1:465"
        os.environ["http_proxy"] = "http://127.0.0.1:465"
        os.environ["all_proxy"] = "http://127.0.0.1:465"

        res = request_gpt(
            """
Several of Apple's display suppliers have proposed their prices for supplying
OLED displays for the fourth-generation iPhone SE, The Elec reports.
Samsung Display, BOE, and Tianma are all said to have entered their proposed\nprices for OLED panels for the iPhone SE 4, which is expected to launch next\nyear. Previous iPhone SE models have all used LCD displays.  \n  \nThe report's sources said Samsung offered the lowest unit price of $30, BOE
offered $35, and Tianma $40\\. Apple is reportedly haggling for $20, and\nnegotiations are ongoing. Display manufacturers are believed to have been\nbidding to supply the panels since at least last August.  \n  \nThe panel prices are said to be a lot lower than suppliers charge for the OLED\ndisplays used in the iPhone 15, because the panels for the SE will use legacy\nparts identical to those used in the iPhone 13 and iPhone 14, so the suppliers
won't need to make new investments in R&D.  \n  \nIn that respect, Samsung is said to have an advantage over its rivals since
the Korean company can use its existing iPhone 14 OLED inventory.  \n  \nAccording to Apple analyst Ming-Chi Kuo, the fourth-generation \u200ciPhone SE\u200c\nwill feature a 6.1-inch OLED display with a design similar to the iPhone 14.\nThe \u200ciPhone SE\u200c 4 is also expected to use the exact same battery found in the
base model iPhone 14.  \n  \nIn addition, the new model is likely to be equipped with an Action button and\nUSB-C port, which we've covered extensively in previous reports. As things\nstand, it could be one of the first devices to feature an Apple-designed modem\nchip, too.\n\nRelated Roundup: iPhone SE\n\nBuyer's Guide: iPhone SE (Caution)\n\nRelated Forum: iPhone\n\n  \nThis article, \"Apple Negotiating With OLED Suppliers for Next Year's iPhone SE\n4\" first appeared on MacRumors.com",
"""
        )
        print(res)


if __name__ == '__main__':
    unittest.main()
