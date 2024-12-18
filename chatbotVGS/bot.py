from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Substitua 'YOUR_TOKEN' pelo token que você obteve com o BotFather
TOKEN = '7812663073:AAFc3g8WfVM7vgztaNkhiKaZG_i82ayEHr4'

# Função de comando para iniciar o bot
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text('Olá! Eu sou um bot. Como posso te ajudar?')

# Função para responder a qualquer mensagem de texto
async def echo(update: Update, context: CallbackContext):
    # Responde com a mesma mensagem que o usuário enviou
    await update.message.reply_text(update.message.text)

# Função principal para configurar e iniciar o bot
def main():
    # Cria o "application" e passa o TOKEN
    application = Application.builder().token(TOKEN).build()

    # Adiciona o handler para o comando "/start"
    application.add_handler(CommandHandler("start", start))

    # Adiciona o handler para responder todas as mensagens de texto
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Inicia o bot
    application.run_polling()

if __name__ == '__main__':
    main()
