# Identification of Fake Credit and Debit card :credit_card: combinations during Payment Gateways
<b>Motivation</b> :thought_balloon: : During product checkouts in E-commerce websites I have noticed as I type just 4 to 5 digits of my debit card :credit_card:, the checkout system automatically identifies the type of card and payment network. But to my surprise at the time of this project, the E-commerce website did not support or recognise all payment networks. So, I decided to develop a program that will identify all payment networks.

<b>Objective</b> :dart: : Develop a script to identify fake credit card combinations at time of payments by calculating card numbers over Luhn formula. Also, successfully recognize credit card’s payment network provider such as <b><i>Mastercard, Visa, American Express, Discover and RuPay(India's newly government introduced payment network).</i></b>

### Disclaimer :
User data is not collected by this program. This project intention is to show how payment systems work to operate and functionalities that can be improvised. <b>For educational purposes only.</b>

### Quick links :link::
[Python code]()

[Executable program]() - Enables the user to interact with the program and run card validation. 

### Understanding Card and prefix's :
<i>Type of card</i> stands for <b>Debit and Credit </b>cards.

<i>Payment networks</i> stand for financial system that provides <b>payments</b> and <b>transaction services</b> to a customer from a merchant.

Payment Network | Logo on card | Card Prefix's :credit_card:
----------------|---------------|-------------------
American Express|<img src="https://img.icons8.com/cotton/48/000000/amex.png">|3
Discover|<img src="https://img.icons8.com/plasticine/48/000000/discover.png">|65, 644, 645, etc
MasterCard|<img src="https://img.icons8.com/color/48/000000/mastercard.png">|5
Rupay|<img src='https://uxwing.com/wp-content/themes/uxwing/download/10-brands-and-social-media/rupay-logo.png' width=48 height=48>|6
Visa|<img src="https://img.icons8.com/dusk/48/000000/visa.png">|4

For <b>RuPay</b> card : The combinations that do not validate as Discover card fall under RuPay card combination.

### Verdict : 
This program serves the purpose in the prevention of payment frauds. <i><b>Source code can be integrated</i></b> with any E-commerce website and existing payment networks to recognise the type of cards :credit_card: and their payment networks.
