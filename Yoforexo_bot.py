from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Initialize ChatterBot
chatbot = ChatBot('TelegramBot')
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot with the English corpus
trainer.train("chatterbot.corpus.english")

# Start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("""
Hello and welcome to Yoforex! 🌟

Thank you for reaching out to us. We’re thrilled to introduce you to our cutting-edge trading bots and expert signals, designed to enhance your trading journey.

Feel free to explore the options below, or ask us any questions you might have. Our mission is to empower you with the knowledge and tools needed to make confident, informed decisions and reach your trading goals.
""", parse_mode="Markdown")

# /courses command handler
async def courses_info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    courses_text = """
*YoForex VIP (Trading Course)*

We Target Basic to Advance Knowledge:
1. No Indicators Used
2. SMC
3. ICT
4. FVG
5. Entry on H4 & M15 
6. SL/TP Using ATR 
7. Money/Risk Management
8. Trade Entry Layering
9. Advanced Fibonacci Graphing
10. News Trading
11. Live Trading Classes (Friday Only)

- *Purchase YoForex VIP Course*
    - 1500$ Lifetime Access

- *Join Super-VIP*
    The Course is free for Super-VIP Members and live trading sessions.

- *To buy this course, Contact us on* [@yoforexpremium](https://t.me/YoForexPremium?text=Hi%20%40YoForexPremium%2C%20I%20am%20here%20for%20a%20query%20regarding%20the%20YoForex%20VIP%20%28Trading%20Course%29%20plan.%20Can%20you%20please%20elaborate%20on%20this%3F)

*Note: Online Support time is from 10 AM to 7 PM IST, Monday to Saturday.*
*Please Mention Your Detailed Requirements, and one of our executives will assist you.*
    """
    await update.message.reply_text(courses_text, parse_mode="Markdown")

# /trading command handler
async def trading_course(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    trading_course = """
*Trading Course*
    - *Explore all the courses by Yoforex family*
        - [YoForex.org Courses](https://www.yoforex.org/product-category/course/)
        - [YoForexEA.com Courses](https://yoforexea.com/product-category/course/)
        - [FXCracked.org Courses](https://www.fxcracked.org/product-category/course/)
        - [ForexFactory.cc Courses](https://www.forexfactory.cc/product-category/course/)
        - [MQL5.software Courses](https://www.mql5.software/product-category/course/)
        - [BankNifty.online Courses](https://banknifty.online/course-list/)
        - [AITRadingBot.org Courses](http://aitradingbot.org/product-category/course/)
        - [TradingView.services Courses](https://tradingview.services/product-category/course/)

    - Customer Support (Sales)
        - Contact [@yoforexpremium](https://t.me/yoforexpremium?text=Hi%20%40yoforexpremium%2C%20I%20want%20to%20know%20more%20about%20Trading%20Courses%2C%20can%20you%20please%20help%20me%20with%20that%3F) for inquiries
            
        - Custom Course Request
            
            [Click here to fill the form](https://t.me/yoforexpremium?text=Hi%20%40yoforexpremium%2C%20I%20am%20interested%20in%20the%20Custom%20Trading%20course%2C%20below%20are%20my%20details%3A%0A%0AName%20of%20Course%3A%0ALink%20of%20Original%20Course%3A%0AOriginal%20Price%3A)
    """
    await update.message.reply_text(trading_course, parse_mode="Markdown")

# Other existing command handlers
async def send_link(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("""
*Thanks for Choosing Yoforex, you can explore our other services and products.*
                                    
*Below are the links:*
                                    
[YoForex Website](https://www.yoforex.org/)

[YoForex EA](https://yoforexea.com/)

[FXCracked](https://fxcracked.org/)

[Forex Factory](https://www.forexfactory.cc/)

[MQL5 Software](https://www.mql5.software/)

[AI Trading Bot](http://aitradingbot.org/)

[TradingView Services](https://tradingview.services/)
                                    
For more info, *Contact us on* [@yoforexpremium](https://t.me/YoForexPremium?text=Hi%20%40YoForexPremium%2C%20I%20am%20here%20for%20a%20query%20regarding%20the%20YoForex%20services%20%28and%20course%29%20plans.%20Can%20you%20please%20elaborate%20on%20this%3F)
""", parse_mode="Markdown")

# /propFirm command handler
async def propFirm(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("""
*PropFirm Passing Services*
*Manual Passing*
    - A dedicated trader will be assigned to you
    - Trader will enter and exit manually
    - IP Address can't be detected; we will use Premium Proxy cost $5 Each
    - Contact [@yoforexpremium](https://t.me/YoForexPremium?text=Hi%20%40YoForexPremium%2C%20I%20want%20to%20know%20more%20about%20Manual%20Passing%20in%20PropFirm%20Passing%20Services.%20Here%20is%20my%20account%20details%3A) with your account details
        
        *Price*
            
            Passing Fees:
            
            $6K = $50 per phase, both phases $80
            $10K = $60 per phase, both phases $100
            $15K = $70 per phase, both phases $120
            $25k = $85 per phase, both phases $140
            $50k = $100 per phase, both phases $170
            $100k = $200 per phase, both phases $300
            $200k = $300 per phase, both phases $500

    *HFT Passing*
        - The broker can restrict your account and put a hold on the prop account you purchased
        It is better to go for Manual Passing
""", parse_mode="Markdown")

# /ea command handler
async def ea_info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("""
*Expert Advisor AI Robot Trading*

[Custom EA Unlock Trading Bot Request](https://t.me/YoForexPremium?text=Please%20Fill%20the%20below%20blanks%3A%0A%0AName%20of%20EA%3A%20%0ALink%20of%20Original%20Seller%3A%20%0AMT4%2FMT5%3A%20%0AOriginal%20Price%3A%20%0AWhy%20do%20you%20need%20this%3A%20)

*Purchased From Website*
- Error details with a screenshot and video (if needed)
- Explain in detail and send it to @yoforexpremium

*Note*: Online support is available from 10 AM to 7 PM IST, Monday to Saturday.  
Please mention your detailed requirements, and one of our executives will assist you.

*Purchased From Telegram Executive*
- Error details with a screenshot and video (if needed)
- Explain in detail and send it to @yoforexpremium

*Note*: Online support is available from 10 AM to 7 PM IST, Monday to Saturday.  
Please mention your detailed requirements, and one of our executives will assist you.
""", parse_mode="Markdown")

# /payment command handler
async def payment_details(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Payment details: Please send $100 to our PayPal account at payments@example.com.')

# /amount command handler
async def amount_info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('The amount is: $100')

# /real_account command handler
async def ram_text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    ram_text = """
- *Real Account Management*
    
    ✔️ Min Deposit: 300$
    ✔️ Recommended: 500$ or More
    
    *We are using highly trained AI Software which can manage all the accounts together & tokens, auto Trail SL, profit will be hunted.*
    🔸 Trade will be placed manually
    🔸 No Loss (Tight SL 1:2)
    🔸 3-5 Trades/Day
    
    🔻 You Have to Join through our IB Link
    🔻 50-50% Profit Share
    🔻 Weekly 100% profit
    🔻 Low Latency Premium Server
    🔻 Dedicated Proxy $5 Each
    
    🌐 Go to [@yoforexpremium](https://t.me/YoForexPremium?text=Hi%20%40YoForexPremium%2C%20I%27m%20interested%20in%20Real%20Account%20Management.%20Could%20you%20please%20provide%20me%20with%20more%20details%20about%20this%20service%3F) for more info.
    """
    await update.message.reply_text(ram_text, parse_mode="Markdown")

# IB Link (Must) - Best Broker
async def iblink(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    iblink = """
- IB Link (Must) - Best Broker
    
    [Link 1](https://mygtcportal.com/getview?view=register&token=8zKowwww7owwwwww) OR [Link 2](https://my.dooprime.com/links/go/42522)
    
    Once Joined Send us the Registered Email and Account ID.
    Click here to send → [@yoforexpremium](https://t.me/yoforexpremium?text=Hi%20%40yoforexpremium%2C%20I%20have%20created%20an%20account%20using%20the%20IB%20link.%0A%0AHere%20are%20my%20Details%3A%0AEmail%3A%0AAccount%20ID%3A)
    
    We are sub-broker
    any problem withdrawing / depositing
    contact us , we can solve every broker-related issue in no-time
    *Applicable for only GTCFX & Doo Prime*
    """
    await update.message.reply_text(iblink, parse_mode="Markdown")

# VIP Plan
async def vipplan(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.message.chat_id

    # Path to your image file
    image_path = 'images/supervip.jpg'  # Use forward slashes or escape backslashes

    # Text to accompany the image
    caption = """
*Join VIP*

- *Features*
    
    Signals: 3-5 Premium Signal’s / Day
    Joining: Directly through YoForex IB link
    Promotion to Super VIP: Subscribe to VIP and purchase any subscription pack (monthly/yearly/lifetime)
    Forums: No access to forums
    Educational Content: Not included
    News Trading: Not included
    Support: 12/7 chat support

- *How To Join*
    
    Join through our IB link and deposit a minimum of $100 to start receiving premium signals!
    
    📺*Create Account* : [Link 1](https://mygtcportal.com/getview?view=register&token=8zKowwww7owwwwww) [Link 2](https://my.dooprime.com/links/go/42522)
    🟣MT5 STD
    🟣1:500 Leverage

    For more info → [@yoforexpremium](https://t.me/yoforexpremium?text=Hi%20%40yoforexpremium%2C%20I%20want%20to%20upgrade%20to%20the%20VIP%20plan%2C%20guide%20me%20to%20buy%20this%20plan.)
"""

    # Send the image with caption
    await context.bot.send_photo(chat_id=chat_id, photo=open(image_path, 'rb'), caption=caption, parse_mode="Markdown")

# Super VIP Plan
async def supervip(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.message.chat_id

    # Path to your image file
    image_path = 'images/supervip.jpg'  # Use forward slashes or escape backslashes

    # Text to accompany the image
    caption = """
*Join Super-VIP*

- *Features*
    
    Signals: 4-8 Premium Signal’s / Day
    Joining: Subscribe VIP then you can join Super-VIP
    Trading Strategy: Included
    Trading Course: Included
    Live Trading Classes: Included
    News Trading: Included
    Support: 24/7 priority chat support
    Special Tags: For Super VIP clients
    Group Chat: Available

- *How To Join*
    
    Join VIP → Then Our VIP Group → Choose Plan → Pay 120$/Month or more → Welcome to Super-VIP

    Click here to proceed → [@yoforexpremium](https://t.me/yoforexpremium?text=Hi%20%40yoforexpremium%2C%20I%20want%20to%20upgrade%20to%20Super%20VIP%20plan%2C%20guide%20me%20to%20buy%20this%20plan.)
"""

    # Send the image with caption
    await context.bot.send_photo(chat_id=chat_id, photo=open(image_path, 'rb'), caption=caption, parse_mode="Markdown")    

# Handle unknown messages using ChatterBot and trigger /start if "hello" is found
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_message = update.message.text.lower()

    # Check if the message contains "hello"
    if 'hello' in user_message:
        await start(update, context)  # Trigger the /start command
    else:
        response = chatbot.get_response(user_message)
        await update.message.reply_text(str(response))

# Main function to set up the bot
def main():
    application = Application.builder().token("7046808243:AAGo73Hr-AtZXbShdXzgk8OkUjYEnsO3g00").build()  # Replace with your bot token

    # Registering the command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("link", send_link))
    application.add_handler(CommandHandler("propFirm", propFirm))
    application.add_handler(CommandHandler("ea", ea_info))
    application.add_handler(CommandHandler("payment", payment_details))
    application.add_handler(CommandHandler("trading", trading_course))
    application.add_handler(CommandHandler("courses", courses_info))
    application.add_handler(CommandHandler("real_account", ram_text))
    application.add_handler(CommandHandler("vipplan", vipplan))
    application.add_handler(CommandHandler("supervip", supervip))
    application.add_handler(CommandHandler("iblink", iblink))

    # Handling text messages that are not commands
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Start the bot
    application.run_polling()

if __name__ == '__main__':
    main()
