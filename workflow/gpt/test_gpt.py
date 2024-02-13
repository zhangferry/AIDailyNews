import unittest, os
from workflow.gpt.summary import request_gpt


class MyTestCase(unittest.TestCase):
    def test_something(self):
        os.environ["https_proxy"] = "http://127.0.0.1:465"
        os.environ["http_proxy"] = "http://127.0.0.1:465"
        os.environ["all_proxy"] = "http://127.0.0.1:465"

        res = request_gpt(
            """
            Apple Cash is a pre-paid virtual card that allows users to send Apple Pay payments to friends and family, transfer cash to their bank accounts, make Apple Card payments, and pay online via Apple Pay.

The new Apple Card virtual card feature will allow Apple Cash users to spend their balance online, even in online stores where Apple Pay is not supported.

iOS 17.4 beta users report they’ve seen a new pop-up inviting them to set up a virtual card number, which Apple says will “keep your card information safe with a new security code for every transaction.”

Once generated, the card number can be accessed using Safari AutoFill, and used to shop online “where Apple Pay is not available.” Users can also view the card number in Wallet, as well as generate new card numbers and CVC codes.

9to5Mac reports the feature may not have rolled out to every iOS 17.4 beta tester. If you’re running the iOS 17.4 beta, you can check to see if the new feature is available to you by opening the Wallet app, tapping your Apple Cash card, and checking for the option to “Set Up Virtual Card Number.”

iOS 17.4 will be released to the public sometime in March."""
        )
        print(res)


if __name__ == '__main__':
    unittest.main()
