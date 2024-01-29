'''from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, CallbackQueryHandler, Application, CommandHandler, ContextTypes, MessageHandler, filters, CallbackContext
from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials

# Замените 'path_to_your_credentials.json' на путь к вашему credentials.json файлу
creds = Credentials.from_service_account_file('key.json')
service = build('docs', 'v1', credentials=creds)

def start(update: Update, context: CallbackContext) -> None:
    doc_id = '1ep_ceQOtAluRBlJYmUOglqkpuozqtieCj9BmAhEa8Qw'  # Замените 'your_document_id' на ID вашего документа
    doc = service.documents().get(documentId=doc_id).execute()
    chapters = doc.get('body').get('content')
    keyboard = [[InlineKeyboardButton(chapter.get('paragraph').get('elements')[0].get('textRun').get('content'), callback_data=chapter.get('startIndex'))] for chapter in chapters if chapter is not None]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(doc)

def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    doc_id = '1ep_ceQOtAluRBlJYmUOglqkpuozqtieCj9BmAhEa8Qw'  # Замените 'your_document_id' на ID вашего документа
    doc = service.documents().get(documentId=doc_id).execute()
    chapters = doc.get('body').get('content')
    chapter = next(chapter for chapter in chapters if chapter.get('startIndex') == int(query.data))
    text = chapter.get('paragraph').get('elements')[0].get('textRun').get('content')
    query.edit_message_text(text=text)

def main():
    
    application = Application.builder().token("6487668550:AAEJgZv7kUP-IJD-eghYfoVAJEpEc6G72Ok").build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))
    application.run_polling()



if __name__ == '__main__':
    main()'''

from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, Application
from googleapiclient.discovery import build
from google.oauth2 import service_account
from queue import Queue

SCOPES = ['https://www.googleapis.com/auth/documents.readonly']
SERVICE_ACCOUNT_FILE = 'key.json'
creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('docs', 'v1', credentials=creds)
DOCUMENT_ID = '1ep_ceQOtAluRBlJYmUOglqkpuozqtieCj9BmAhEa8Qw'

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Hello! Send /chapters to get the chapters of the document.')

async def chapters(update: Update, context: CallbackContext) -> None:
    document = service.documents().get(documentId=DOCUMENT_ID).execute()
    document_content = ''
    for element in document.get('body').get('content'):
        if 'paragraph' in element:
            for paragraph_element in element.get('paragraph').get('elements'):
                if 'textRun' in paragraph_element:
                    document_content += paragraph_element.get('textRun').get('content')
    if len(document_content) >= 4096:
        document_content = document_content.split('\n')
        print(document_content)
    for i in document_content :
        await update.message.reply_text(i)

def main() -> None:

    application = Application.builder().token("6487668550:AAEJgZv7kUP-IJD-eghYfoVAJEpEc6G72Ok").build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("chapters", chapters))
    application.run_polling()

if __name__ == '__main__':
    main()