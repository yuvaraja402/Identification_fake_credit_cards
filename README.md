# Identification of Fake Credit card :credit_card: combinations and payment networks during Payment Gateway
<b>Motivation</b> :thought_balloon: : During product :package: checkouts in <b>E-commerce websites</b> I have noticed as I type just 4 to 5 digits of my credit card :credit_card:, the website's payment system automatically validates the card I have and identifies its payment network. But to my surprise at the time of this project, the E-commerce websites did not recognise all payment networks, websites implicitly requests user to specify card details.

<b>Objective</b> :dart: : Develop a program that will identify fake credit card combinations by calculating card digits over Luhn formula. Also, successfully recognize credit card’s payment network provider such as <b><i>Mastercard, Visa, American Express, Discover and RuPay(India's newly government introduced payment network).</i></b>

### Disclaimer :
User data is not collected by this program. This project intention is to show how payment systems work to operate and functionalities that can be improvised. <b>For educational purposes only.</b>

### Quick links :link::
[Python source code](https://github.com/yuvaraja402/Identification_fake_credit_cards/blob/master/card_validation.py)

[Python Notebook with output](https://github.com/yuvaraja402/Identification_fake_credit_cards/blob/master/card_validation.ipynb)

[Executable program](https://github.com/yuvaraja402/Identification_fake_credit_cards/blob/master/dist/card_validation/card_validation.exe) - Enables the user to interact with the program and run card validation (<i><b>'Run as Administrator</i></b>).

### Understanding Card prefix's :
<i>Payment networks</i> stand for financial system that provides <b>payments</b> and <b>transaction services</b> to a customer from a merchant.

Payment Network | Logo on card | Card Prefix's :credit_card:
----------------|---------------|-------------------
American Express|<img src="https://img.icons8.com/cotton/48/000000/amex.png">|3
Discover|<img src="https://img.icons8.com/plasticine/48/000000/discover.png">|65, 644, 645, etc
MasterCard|<img src="https://img.icons8.com/color/48/000000/mastercard.png">|5
Rupay|<img src='https://uxwing.com/wp-content/themes/uxwing/download/10-brands-and-social-media/rupay-logo.png' width=48 height=48>|6
Visa|<img src="https://img.icons8.com/dusk/48/000000/visa.png">|4

For <b>RuPay</b> card : The combinations that do not validate as Discover card fall under RuPay card combination.

### Verdict :pushpin:: 
This program serves the purpose in the prevention of payment frauds. <i><b>Source code can be integrated</i></b> with any E-commerce website and existing payment networks to validate the cards :credit_card: and identify their payment networks.

### Implementation Snapshots :camera::
<b>Snapshots are from [Executable program](https://github.com/yuvaraja402/Identification_fake_credit_cards/blob/master/dist/card_validation/card_validation.exe)</b>

<img src = 'https://github.com/yuvaraja402/Identification_fake_credit_cards/blob/master/output%20snapshots/discover.jpg' width=600>

<img src = 'https://github.com/yuvaraja402/Identification_fake_credit_cards/blob/master/output%20snapshots/mastercard.PNG' width=600>

<img src = 'https://github.com/yuvaraja402/Identification_fake_credit_cards/blob/master/output%20snapshots/rupay.PNG' width=600>

<img src = 'https://github.com/yuvaraja402/Identification_fake_credit_cards/blob/master/output%20snapshots/visa.PNG' width=600>
